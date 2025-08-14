from pokemon import pokemon
from fight import Fight
from Materials.pokemon_attacks import Attack
from Materials.pokemon_items import trigger_item
from Materials.pokemon_talents import trigger_talent
import utilities

def damage_calc(attacker, attack, defender, fight):
    if attack.category == "Status":
        return [None, None, None, None]  # Pas de dégâts pour les attaques de statut

    if hasattr(attack, 'apply_before_damage'):
            attack.apply_before_damage(attacker, defender, fight)

    on_defense_ability_multiplier = trigger_talent(defender, "on_defense", attack, attacker, fight)
    on_attack_ability_multiplier = trigger_talent(attacker, "on_attack", attack, fight)
    on_attack_item_multiplier = trigger_item(attacker, "on_attack", attack, fight)
    on_defense_item_multiplier = trigger_item(defender, "on_defense", attack, fight)
    
    # Valeurs par défaut si on_attack_mod est None
    if on_attack_ability_multiplier is None:
        on_attack_ability_multiplier = {"attack": 1.0, "power": 1.0, "accuracy": 1.0, "type": None}
    
    if on_attack_item_multiplier is None:
        on_attack_item_multiplier = {"attack": 1.0, "power": 1.0, "accuracy" : 1.0}
   
    if on_defense_item_multiplier is None:
        on_defense_item_multiplier = {"attack": 1.0, "power": 1.0, "accuracy": 1.0}

    if attacker.talent == "Mold Breaker":
            if defender.talent == "Fur Coat":
                on_attack_ability_multiplier["attack"] = 2.0 # contre-balance de x2 de fur coat

    # S'assurer que multiplier est un nombre
    if on_defense_ability_multiplier is None or not isinstance(on_defense_ability_multiplier, (int, float)):
        on_defense_ability_multiplier = 1.0

    damage, chances_of_ko, min_roll, max_roll = attack_carac(fight, attacker, attack, defender, on_defense_ability_multiplier, on_attack_ability_multiplier, on_attack_item_multiplier, on_defense_item_multiplier)

    return [int(damage), chances_of_ko, int(min_roll), int(max_roll)]

def attack_carac(fight, user_pokemon : pokemon, attack : Attack, target_pokemon : pokemon, def_ab_mod, atk_ab_mod, atk_item_mod, def_item_mod):
    """
    Effectue une attaque d'un Pokémon sur une cible.

    :param pokemon: Instance de la classe Pokemon qui attaque.
    :param attack: Dictionnaire contenant les détails de l'attaque.
    :param target: Instance de la classe Pokemon qui est la cible de l'attaque.
    :return: Dégâts infligés à la cible.

    formule de calcul des dégâts :
    damage = ((22 * base_power * (attack_stat / defense_stat)) / 50 + 2) * burn * screen * weather * FF * critical * item * stab * random * Type1 * Type2 * Berry
    """

    attack_boost = attack.boosted_attack(user_pokemon, target_pokemon, fight) if hasattr(attack, 'boosted_attack') else 1.0

    if not isinstance(attack_boost, (int, float)):
        attack_boost = 1.0

    # Vérifier si l'attaque a une méthode get_power pour calculer la puissance dynamiquement
    if hasattr(attack, 'get_power'):
        base_power = attack.get_power(user_pokemon, target_pokemon, fight) * atk_ab_mod["power"] * atk_item_mod["power"]
    else:
        base_power = attack.base_power * atk_ab_mod["power"] * atk_item_mod["power"]

    terrain_boost = attack_terrain_boost(attack, fight)  # Modificateur de puissance des attaques en fonction du terrain
    weather_boost = attack_weather_boost(attack, fight)  # Modificateur de puissance des attaques en fonction de la météo
    berry = berry_boost(target_pokemon, attack)  # Placeholder pour l'effet de la baie, si applicable
    burn = burn_effect(user_pokemon, attack)  # Si le Pokémon est brûlé, les dégâts sont réduits de moitié
    defender_team_id = fight.get_team_id(target_pokemon)
    screen = screen_effect(user_pokemon, attack, fight, defender_team_id)  # Effet de l'écran de protection actif pour l'équipe du défenseur
    if atk_ab_mod["type"] != None:
        type_eff = type_effectiveness(atk_ab_mod["type"], target_pokemon)
        attack_copy = attack.copy()
        attack_copy.type = atk_ab_mod["type"]  # Changer le type de l'attaque si un talent modifie le type
        stab = is_stab(user_pokemon, attack_copy)  # Vérifier si l'attaque est STAB
    else:
        if attack.name == "Struggle":
            type_eff = 1.0  # Struggle est de type Normal, pas besoin de calculer l'efficacité touche même les types spectre et jamais de stab
            stab = 1.0
        else:
            type_eff = type_effectiveness(attack.type, target_pokemon)  # Calcul de l'efficacité du type
            stab = is_stab(user_pokemon, attack)

    if hasattr(target_pokemon, 'glaive_rush') and target_pokemon.glaive_rush:
        glaive_rush = 2.0
    else: 
        glaive_rush = 1.0

    multiplier = def_ab_mod * atk_ab_mod["attack"] * def_item_mod["attack"] * atk_item_mod["attack"]  # Modificateur de dégâts basé sur les talents et les objets

    rdm = [0.85 + 0.01 * i for i in range(16)]  # Liste des valeurs aléatoires entre 0.85 et 1.0

    user_current_stats = user_pokemon.current_stats()
    target_current_stats = target_pokemon.current_stats()

    if is_critical_hit(user_pokemon, attack, target_pokemon):
        print(f"{user_pokemon.name} porte un coup critique avec {attack.name} !")
        critical = 1.5  # Coup critique inflige 1.5x les dégâts
        if attack.category == 'Physical' or attack.name == "Psychoc":
            if target_pokemon.stats_modifier[1] > 0:
                defense_stat = int(target_pokemon.calculate_stat(target_pokemon.base_stats['Defense'], target_pokemon.ivs['Defense'], target_pokemon.evs['Defense'], target_pokemon.nature_modifier[1], 0) * target_pokemon.hidden_modifier["Defense"])
            else:
                defense_stat = target_current_stats['Defense']
            if user_pokemon.stats_modifier[0] < 0:
                attack_stat = int(user_pokemon.calculate_stat(user_pokemon.base_stats['Attack'], user_pokemon.ivs['Attack'], user_pokemon.evs['Attack'], user_pokemon.nature_modifier[0], 0) * user_pokemon.hidden_modifier["Attack"])
            else:
                attack_stat = user_current_stats['Attack']
        else:
            if target_pokemon.stats_modifier[3] > 0:
                defense_stat = int(target_pokemon.calculate_stat(target_pokemon.base_stats['Sp. Def'], target_pokemon.ivs['Sp. Def'], target_pokemon.evs['Sp. Def'], target_pokemon.nature_modifier[3], 0) * target_pokemon.hidden_modifier["Sp. Def"])
            else:
                defense_stat = target_current_stats['Sp. Def']
            if user_pokemon.stats_modifier[2] < 0:
                attack_stat = int(user_pokemon.calculate_stat(user_pokemon.base_stats['Sp. Atk'], user_pokemon.ivs['Sp. Atk'], user_pokemon.evs['Sp. Atk'], user_pokemon.nature_modifier[2], 0) * user_pokemon.hidden_modifier["Sp. Atk"])
            else:
                attack_stat = user_current_stats['Sp. Atk']
        damage = ((22 * base_power * (attack_stat / defense_stat)) / 50 + 2) * burn * screen * type_eff * terrain_boost * weather_boost * critical * stab * berry * attack_boost * multiplier * glaive_rush
        # A changer car les crits ne prennent pas en compte les modificateurs de stats
    else:
        critical = 1.0
        defense_stat = target_current_stats['Defense'] if attack.category == 'Physical' else target_current_stats['Sp. Def']
        attack_stat = user_current_stats['Attack'] if attack.category == 'Physical' else user_current_stats['Sp. Atk']
        damage = ((22 * base_power * (attack_stat / defense_stat)) / 50 + 2) * burn * screen * type_eff * terrain_boost * weather_boost * critical * stab * berry * attack_boost * multiplier * glaive_rush

    possible_damages = [damage * r for r in rdm]

    target_health = target_pokemon.current_hp

    cases_of_ko = [d for d in possible_damages if d >= target_health]

    chances_of_ko = len(cases_of_ko) / len(possible_damages) if possible_damages else 0
    min_roll = possible_damages[0] if possible_damages else 0
    max_roll = possible_damages[-1] if possible_damages else 0

    damage *= random.choice(rdm)

    return damage, chances_of_ko, min_roll, max_roll

def type_effectiveness(attack_type, target):
    """
    Calcule l'efficacité du type en tenant compte de la Téracristalisation.
    
    :param attack_type: Type de l'attaque
    :param target: Pokémon cible (instance, pas liste de types)
    :return: Multiplicateur d'efficacité
    """
    target_types = target.types
        
    modifier = 1.0
    for t in target_types:
        modifier *= utilities.type_chart[utilities.POKEMON_TYPES_ID[attack_type]][utilities.POKEMON_TYPES_ID[t]]
    return modifier

#### Gerer le STAB ####
def is_stab(pokemon : pokemon, attack : Attack):
    """
    Calcule le STAB (Same Type Attack Bonus) en tenant compte de la Téracristalisation.
    """
    return pokemon.is_tera_stab(attack.type)

#### Regarder si c'est un coup critique ####
import random

def is_critical_hit(pokemon, attack : Attack, target):
    """
    Détermine si une attaque est un coup critique.
    
    :param pokemon: Attaquant (instance de Pokemon)
    :param attack: Instance d'une classe Attack
    :param target: Défenseur (instance de Pokemon)
    :return: True si coup critique, False sinon
    """
    
    # 1. Cas d'un crit garanti (ex: Flower Trick)
    if attack.guaranteed_critical:
        return True

    # 2. Cas où le talent de la cible bloque les coups critiques
    if target.talent in {"Shell Armor", "Battle Armor"}:
        return False

    # 3. Calcul du niveau de taux critique (crit stage)
    crit_stage = 1  # par défaut

    # Bonus d'attaque : taux critique augmenté
    if hasattr(attack, "critical_chance_up") and attack.critical_chance_up:
        crit_stage += 1

    # Objet augmentant le taux de crit
    if pokemon.item in {"Scope Lens", "Razor Claw"}:
        crit_stage += 1

    # Talent Super Luck
    if pokemon.talent == "Super Luck":
        crit_stage += 1

    # Bonus personnalisé (ex: Laser Focus, effets custom)
    if hasattr(pokemon, "power") and pokemon.power:
        crit_stage += 2

    # 4. Table officielle des chances critiques
    CRIT_RATES = {
        0: 0.0,
        1: 0.0417,  # 1/24
        2: 0.125,   # 1/8
        3: 0.5,    # 1/2
        4: 1.0,   # Always crit
        5: 1.0,  # Always crit
        6: 1.0
    }

    chance = CRIT_RATES.get(min(crit_stage, 6), 1.0)
    return random.random() < chance

#### Regarder si le terrain booste l'attaque ####
def attack_terrain_boost(attack : Attack, fight : Fight):
    """
    Applique les modificateurs de puissance des attaques en fonction du terrain.

    :param attack: Instance de la classe Attack.
    :param fight: Instance de la classe Fight contenant toutes les informations sur le combat, y compris le terrain actuel.
    :return: Modificateur de puissance des attaques en fonction du terrain.
    """
    match fight.field, attack.type:
        case ("Grassy Terrain", "Grass"):
            return 1.3
        case ("Electric Terrain", "Electric"):
            return 1.3
        case ("Psychic Terrain", "Psychic"):
            return 1.3
        case ("Misty Terrain", "Dragon"):
            return 0.5
        
    if fight.field == "Grassy Terrain" and "ground" in attack.flags:
        return 0.5
    else:
        return 1.0
    
        
#### Regarder si le Pokémon en face tient une baie qui le fait resister à l'attaque ####
def berry_boost(pokemon, attack : Attack):
    """
    Placeholder pour l'effet de la baie, si applicable, si le pokémon tient une baie qui réduit les dégâts de l'attaque si celle-ci est super efficace.
    :param pokemon: Instance de la classe Pokemon qui attaque.
    :param attack: Instance de la classe Attack.
    :return: Modificateur de puissance des attaques en fonction de la baie.
    """

    item = pokemon.item
    if item is None:
        return 1.0
    berry = str.split(item, "_")
    if len(berry) > 1 and berry[1] != "berry":
        return 1.0
    else:
        return 1.0    # sera implémenté plus tard

#### Regarder si la météo booste l'attaque ####
def attack_weather_boost(attack : Attack, fight):
    """
    Applique les modificateurs de puissance des attaques en fonction de la météo.

    :param attack: Instance de la classe Attack.
    :param fight: Instance de la classe Fight contenant toutes les informations sur le combat, y compris la météo actuelle.
    :return: Modificateur de puissance des attaques en fonction de la météo.
    """
    match fight.weather["current"], attack.type:
        case ("Sunny", "Fire"):
            return 1.5
        case ("Rain", "Water"):
            return 1.5
        case ("Sunny", "Water"):
            return 0.5
        case ("Rain", "Fire"):
            return 0.5
        case _:
            return 1.0  # Pas de boost si la météo ne correspond pas à l'attaque

#### Regarder si le Pokémon est brûlé ####
def is_burned(pokemon):
    if pokemon.status != "burn":
        return False
    else:
        return True
    
def burn_effect(pokemon : pokemon, attack : Attack):
    """
    Renvoie le multiplicateur de dégâts en fonction de l'attaque
    
    :param pokemon: Instance de la classe Pokemon qui attaque.
    :param attack: Instance de la classe Attack.
    :return: Multiplicateur de dégâts en fonction de l'attaque.
    """
    if attack.category == "Physical" and is_burned(pokemon) and pokemon.talent != "Guts":
        return 0.5
    else:
        return 1.0
    
#### Attaque de confusion ####
def confusion_attack(pokemon : pokemon):
    """
    Gère l'attaque subit lorsqu'un pokémon est confus, il s'agit d'une attaque de type Normal (qui n'est pas affecté par les types ni le stab)
    et qui a 40 de puissance de base. La formule de calcul est donc la suivante :
    ((base_power * (attack_stat / defense_stat)) + 1) 
    """
    damage = int(((40 * (pokemon.current_stats()['Attack'] / pokemon.current_stats()['Defense'])) + 1))
    return damage

def screen_effect(attacker : pokemon, attack : Attack, fight : Fight, defender_team_id):
    """
    Applique l'effet de l'écran de protection actif pour l'équipe du défenseur.
    
    :param attack: Instance de la classe Attack.
    :param fight: Instance de la classe Fight contenant les informations sur les écrans actifs.
    :param defender_team_id: ID de l'équipe du défenseur (1 ou 2).
    :return: Facteur de réduction des dégâts.
    """ 
    screens = fight.screen_team1 if defender_team_id == 1 else fight.screen_team2
    if attacker.talent == "Infiltrator":
        return 1.0
    if 'light_screen' in screens and attack.category == "Special":
        return 0.5
    elif 'reflect' in screens and attack.category == "Physical":
        return 0.5
    elif 'aurora veil' in screens:
        return 0.5
    else:
        return 1.0
    
def protect_update(pokemon : pokemon, attack : Attack):
    """
    Met à jour l'état de protection d'un Pokémon. Sert uniquement le tour après une protection pour annuler le protect si le pokémon attaque.

    :param pokemon: Instance de la classe Pokemon qui utilise la protection.
    :param attack: Instance de la classe Attack qui est utilisée.
    """
    if not "protection" in attack.flags:
        pokemon.protect = False
        pokemon.protect_turns = 0
