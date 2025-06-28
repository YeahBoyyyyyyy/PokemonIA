from pokemon import pokemon
import random 

class Fight():
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        
        ####### Effets de combats : Terrain, Météo, Murs #######

        ## Météo ##
        self.weather = {"current" : None, "previous" : None}  # Météo actuelle (par exemple : "Ensoleillé", "Pluvieux", etc.) sera un dictionnaire 
        # contenant la météo actuelle et la météo du tour précédent pour savoir si la météo est la même que la précédente
        self.weather_turn_left = None  # Nombre de tours restants pour la météo actuelle, si elle est active
        # Peut juste être un entier puisqu'il n'y a qu'une seule météo active à la fois

        ## Terrain ##
        self.field_effects = []  # Effets de terrain actifs (par exemple : "Gravité", "Champ Herbu", etc.)
        self.field_turn_left = {}  # Nombre de tours restants pour le terrain actuel, si il est actif
        # Sera un dictionnaire contenant en clé les terrains et en valeur le nombre de tours restants pour chaque terrain actif

        ## Murs de protection ##
        self.screen = []  # Écran de protection actif (par exemple : "Mur Lumière", "Mur de Fer", etc.)
        self.screen_turn_left = {}  # Nombre de tours restants pour l'écran de protection actif, si il est actif

        self.turn = 0  # Compteur de tours pour suivre le nombre de tours écoulés dans le combat
    
    ###### Méthodes pour gérer les effets de la météo #######
    def set_weather(self, weather):
        previous_weather = self.weather['current']
        self.weather['previous'] = previous_weather
        self.weather['current'] = weather

    def apply_weather_effects(self):
        """
        Applique les effets de la météo actuelle sur les Pokémon.
        Et notamment les degats infligés par la tempete de sable et la neige aux Pokémon non-Roche/Acier/Sol et non-Glace.
        """
        match self.weather['current']:
            case "Sandstorm":
                for pokemon in [self.pokemon1, self.pokemon2]:
                    if not any(t in pokemon.types for t in ["Rock", "Steel", "Ground"]):
                        damage = int(pokemon.max_hp * 0.0625)
                        self.damage_method(pokemon, damage)
            case "Snow":
                for pokemon in [self.pokemon1, self.pokemon2]:
                    if "Ice" not in pokemon.types:
                        damage = int(pokemon.max_hp * 0.0625)
                        self.damage_method(pokemon, damage)
            case "Rainy":
                for pokemon in [self.pokemon1, self.pokemon2]:
                    # Si l'un des Pokémons a le talent "Rain Dish", il regagne des PV
                    if pokemon.talent == "Rain Dish":
                        heal_amount = int(pokemon.max_hp * 0.0625) # Régénération de 1/16 des PV max
                        self.damage_method(pokemon, -heal_amount)
                    # Si l'un des Pokémons a le talent "Dry Skin", il perd des PV
                    if talent == "Dry Skin":
                        heal_amount = int(pokemon.max_hp * 0.125)
                        self.damage_method(pokemon, -heal_amount)  # Régénération de 1/8 des PV max
            case "Sunny":
                for pokemon in [self.pokemon1, self.pokemon2]:
                    # Si l'un des Pokémons a le talent "Dry Skin", il perd des PV
                    if pokemon.talent == "Dry Skin":
                        damage = int(pokemon.max_hp * 0.125)
                        self.damage_method(pokemon, damage)
                    


    def weather_boost_modifier(self, pokemon):
        """
        Applique les changements de stats en fonction de la météo
        """
        if self.weather["current"] == "Snow" and self.weather["previous"] != "Snow" and "Ice" in pokemon.types:
            pokemon.stats_modifier[3] += 1
        elif self.weather["previous"] == "Snow" and self.weather["current"] != "Snow" and "Ice" in pokemon.types:
            pokemon.stats_modifier[3] -= 1
        elif self.weather["current"] == "Sandstorm" and self.weather["previous"] and "Rock" in pokemon.types:
            pokemon.stats_modifier[1] += 1
        elif self.weather["previous"] == "Sandstorm" and self.weather["current"] != "Sandstorm" and "Rock" in pokemon.types:
            pokemon.stats_modifier[1] -= 1
    
    ###### Méthodes pour gérer les effets de terrain #######
    def add_field_effect(self, effect):
        self.field_effects.append(effect)
        self.field_turn_left[effect] = 5  # Classiquement les effets de terrain durent 5 tours, on ignore la Light Clay pour l'instant
    
    def remove_field_effect(self, effect):
        if effect in self.field_effects:
            self.field_effects.remove(effect)
            del self.field_turn_left[effect]  # Supprimer l'effet de terrain et son compteur de tours

    def actualize_field_effects(self):
        """
        Met à jour les effets de terrain actifs en décrémentant le nombre de tours restants.
        Supprime les effets de terrain qui ont expiré.
        """
        for effect in list(self.field_turn_left.keys()):
            self.field_turn_left[effect] -= 1
            if self.field_turn_left[effect] <= 0:
                self.remove_field_effect(effect)
    
    def apply_field_effects(self):
        """
        Applique les effets de terrain actifs sur les Pokémon.
        Par exemple, si le terrain est herbeux, tous les Pokémons sur le terrain regagnent des PV à chaque tour.
        """
        if "Grassy Terrain" in self.field_effects:
            # Regénérer des PV pour les Pokémon de type Plante
            for pokemon in [self.pokemon1, self.pokemon2]:
                damage = -int(pokemon.max_hp * 0.0625)  # Régénération de 1/16 des PV max
                self.damage_method(pokemon, damage)  # Utiliser la méthode de dégâts pour régénérer les PV (dégâts "négatifs")









    def damage_method(self, pokemon : pokemon, damage : int):
        """
        Applique les dégâts à un Pokémon.
        :param pokemon: Instance de la classe Pokemon qui subit les dégâts.
        :param damage: Dégâts à infliger.
        """
        pokemon.current_hp -= damage
        if pokemon.current_hp < 0:
            pokemon.current_hp = 0
        elif pokemon.current_hp > pokemon.max_hp:
            pokemon.current_hp = pokemon.max_hp

    ## Printing methods pour debugger
    def print_fight_status(self):
        print(f"Pokémon 1: {self.pokemon1.name} (HP: {self.pokemon1.current_hp}/{self.pokemon1.max_hp})")
        print(f"Pokémon 2: {self.pokemon2.name} (HP: {self.pokemon2.current_hp}/{self.pokemon2.max_hp})")
        print(f"Météo actuelle: {self.weather['current']}")
        print(f"Effets de terrain actifs: {', '.join(self.field_effects) if self.field_effects else 'Aucun'}")
        print(f"Écran de protection actif: {self.screen if self.screen else 'Aucun'}")

    def fight(self):
        print(f"Le combat oppose {self.pokemon1.name} à {self.pokemon2.name} !")

    def next_turn(self):
        """
        Passe au tour suivant du combat.
        Incrémente le compteur de tours et applique les effets de terrain et de météo.
        """
        self.turn += 1
        print(f"Tour {self.turn}:")
        self.print_fight_status()
        
        # Appliquer les effets de terrain et de météo
        self.apply_weather_effects()

        if self.weather['current'] == "Sunny":
            print("Le soleil brille ! Les attaques de type Feu sont boostées.")
        elif self.weather['current'] == "Rainy":
            print("Il pleut ! Les attaques de type Eau sont boostées.")
        elif self.weather['current'] == "Sandstorm":
            print("Une tempête de sable souffle ! Les Pokémon du mauvais type subissent des dégâts.")
        elif self.weather['current'] == "Snow":
            print("Il neige ! Les Pokémon du mauvais type subissent des dégâts.")
        
        # Gérer les effets de terrain
        self.apply_field_effects()

        if "Grassy Terrain" in self.field_effects:
            print("Le terrain est herbeux ! Tous les Pokémon regagnent des PV.")


    
def attack(pokemon : pokemon, attack : dict, target : pokemon, fight : Fight):
    """
    Effectue une attaque d'un Pokémon sur une cible.

    :param pokemon: Instance de la classe Pokemon qui attaque.
    :param attack: Dictionnaire contenant les détails de l'attaque.
    :param target: Instance de la classe Pokemon qui est la cible de l'attaque.
    :return: Dégâts infligés à la cible.

    formule de calcul des dégâts :
    damage = ((22 * base_power * (attack_stat / defense_stat)) / 50 + 2) * burn * screen * weather * FF * critical * item * stab * random * Type1 * Type2 * Berry
    """
    critical = 2.0 if is_critical_hit(pokemon, attack, target) else 1.0  # Si c'est un coup critique, les dégâts sont doublés
    # Le coup critique est déterminé avant car s'il y a un coup critique, on ne prend pas en compte les modificateurs de stats
    base_power = attack['basePower']
    attack_stat = pokemon.current_stats()['Attack'] if attack['category'] == 'Physical' else pokemon.current_stats()['Sp. Atk']
    defense_stat = target.current_stats()['Defense'] if attack['category'] == 'Physical' else target.current_stats()['Sp. Def']
    terrain_boost = attack_terrain_boost(attack, fight)  # Modificateur de puissance des attaques en fonction du terrain
    weather_boost = attack_weather_boost(attack, fight)  # Modificateur de puissance des attaques en fonction de la météo
    berry = berry_boost(pokemon, attack)  # Placeholder pour l'effet de la baie, si applicable
    burn = 0.5 if is_burned(pokemon) else 1.0  # Si le Pokémon est brûlé, les dégâts sont réduits de moitié
    random = random.uniform(0.85, 1.0)  # Valeur aléatoire entre 0.85 et 1.0
    stab = is_stab(pokemon, attack)
    screen = screen_effect(attack, fight)  # Effet de l'écran de protection actif

    
    damage = ((22 * base_power * (attack_stat / defense_stat)) / 50 + 2) * burn * screen * terrain_boost * weather_boost * critical * stab * random * berry
        
    return damage

def is_stab(pokemon : pokemon, attack : dict):
    if attack['type'] in pokemon.types:
        return 1.5

def is_critical_hit(pokemon, attack, target):
    """Détermine si une attaque est un coup critique.
    :param pokemon: Instance de la classe Pokemon qui attaque. Pour connaitre son item, son talent
    :param attack: Dictionnaire contenant les détails de l'attaque. Si elle a un effet de coup critique, on le prend en compte
    :param target: Instance de la classe Pokemon qui est la cible de l'attaque. Si son talent annule les coups critiques
    :return: True si c'est un coup critique, False sinon.
    Implémentation de Air Veinard après (une attauqe qui empeche les crits)
    """
    nb_of_boost = 1

    if 'critical' in attack['effect']:
        if attack['effect']['critical']['chance'] == 100:
            nb_of_boost += 100
        elif attack['effect']['critical']['chance'] > 0:
            nb_of_boost += 1
    if pokemon.item == "Scope Lens" or pokemon.item == "Razor Claw":
        nb_of_boost += 1  # 12.5% de chance d'avoir un coup critique avec la lentille de visée
    if pokemon.talent == "Super Luck":
        nb_of_boost += 1  # 12.5% de chance d'avoir un coup critique avec le talent Super Luck
    if target.status == "poisoned" and pokemon.talent == "Poison Touch":
        nb_of_boost += 1
    if pokemon.power:
        nb_of_boost += 2
    if target.talent == "Battle Armor" or target.talent == "Shell Armor":
        nb_of_boost = 1  # Si la cible a le talent Battle Armor ou Shell Armor, elle ne subit pas de coups critiques
    
    return random.random() < 0.0625*nb_of_boost  # retourne True si le coup est critique, False sinon. 0.0625 est la probabilité de coup critique de base (1/16)

def attack_terrain_boost(attack, fight : Fight):
    """
    Applique les mdoficateurs de puissance des attaques en fonction du terrein.
    :param attack: Dictionnaire contenant les détails de l'attaque.
    :param fight: Instance de la classe Fight contenant toutes les informations sur le combat, y compris le terrain actuel.
    :return: Modificateur de puissance des attaques en fonction du terrain.
    """
    match fight.field_effects, attack['type']:
        case (["Grassy Terrain"], "Grass"):
            return 1.3
        case (["Electric Terrain"], "Electric"):
            return 1.3
        case (["Psychic Terrain"], "Psychic"):
            return 1.3
        case (["Misty Terrain"], "Dragon"):
            return 0.5
        
def berry_boost(pokemon, attack):
    """
    Placeholder pour l'effet de la baie, si applicable.
    :param pokemon: Instance de la classe Pokemon qui attaque.
    :param attack: Dictionnaire contenant les détails de l'attaque.
    :return: Modificateur de puissance des attaques en fonction de la baie.
    """

    item = pokemon.item
    berry = str.split(item, "_")
    if berry[1] != "berry":
        return 1.0
    else:
        return 1.0    # sera implémenté plus tard

def attack_weather_boost(attack, fight):
    """
    Applique les modificateurs de puissance des attaques en fonction de la météo.

    :param attack: Dictionnaire contenant les détails de l'attaque.
    :param fight: Instance de la classe Fight contenant toutes les informations sur le combat, y compris la météo actuelle.
    :return: Modificateur de puissance des attaques en fonction de la météo.
    """
    match fight.weather["current"], attack['type']:
        case ("Sunny", "Fire"):
            return 1.5
        case ("Rainy", "Water"):
            return 1.5
        case ("Sunny", "Water"):
            return 0.5
        case ("Rainy", "Fire"):
            return 0.5
        case _:
            return 1.0  # Pas de boost si la météo ne correspond pas à l'attaque

    
def is_burned(pokemon):
    if pokemon.status != "burn":
        return False
    else:
        return True

def screen_effect(attack, fight : Fight):
    """
    Applique l'effet de l'écran de protection actif.
    
    :param attack: Dictionnaire contenant les détails de l'attaque.
    :param screen: Écran de protection actif (par exemple : "Mur Lumière", "reflect", "aurora veil").
    :return: Facteur de réduction des dégâts.
    """
    if fight.screen == "light_screen" and attack['category'] == "Special":
        return 0.5
    elif fight.screen == "reflect" and attack['category'] == "Physical":
        return 0.5
    elif fight.screen == "aurora veil":
        return 0.5
    else:
        return 1.0