POKEMON_TYPES = ["Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel",
              "Fire", "Water", "Grass", "Electric", "Psychic", "Ice", "Dragon", "Dark", "Fairy", "Null"]

POKEMON_TYPES_ID = {"Normal":0, "Fighting":1, "Flying":2, "Poison":3, "Ground":4, "Rock":5, "Bug":6, 
                    "Ghost":7, "Steel":8, "Fire":9, "Water":10, "Grass":11, "Electric":12, "Psychic":13, 
                    "Ice":14, "Dragon":15, "Dark":16, "Fairy":17, "Null":18}

TERRAIN = ["Grassy Terrain", "Electric Terrain", "Psychic Terrain", "Misty Terrain", "None"]

WEATHER = ["Sunny", "Rainy", "Snow", "Sandstorm", "None"]

PRINTING_METHOD = False

# Talents ignorés par Mold Breaker (liste interne en anglais correspondant aux talents présents dans le code)
MOLD_BREAKER_IGNORED_ABILITIES = {
    "Water Absorb",
    "Clear Body",
    "Contrary",
    "Dry Skin",
    "Flash Fire",
    "Thick Fat",
    "Sturdy",
    "Light Metal",
    "Magic Bounce",
    "Multiscale",
    "Sand Veil",
    "Snow Cloak",
    "Levitate",
    "Ice Scales"
    "Inner Focus",
    "Wonder Skin",
    "Sap Sipper",
    "Ice Face",
}

NON_DIRECT_PHYSICAL_ATTACK = {
    "Pay Day",             
    "Poison Sting",          
    "Twineedle",           
    "Pin Missile",          
    "Razor Leaf",
    "Rock Throw",
    "Earthquake",
    "Fissure",
    "Self-Destruct",
    "Egg Bomb",
    "Bone Club",
    "Spike Cannon",
    "Barrage",
    "Sky Attack",
    "Explosion",
    "Bonemerang",
    "Rock Slide",
    "Bone Rush",
    "Present",
    "Sacred Fire",
    "Magnitude",
    "Hidden Power",
    "Rock Tomb",
    "Sand Tomb",
    "Bullet Seed",
    "Icicle Spear",
    "Rock Blast",
    "Natural Gift",
    "Feint",
    "Metal Burst",
    "Fling",
    "Seed Bomb",
    "Ice Shard",
    "Psycho Cut",
    "Head Smash",
    "Gunk Shot",
    "Magnet Bomb",
    "Stone Edge",
    "Attack Order",
    "Smack Down",
    "Bulldoze",
    "Freeze Shock",
    "Ice Crash",
    "Precipice Blades",
    "Bolt Strike",
    "Pyro Ball",
    "Grav Apple",
    "Aura Wheel",
    "Drum Beating",
    "Dragon Darts",
    "Salt Cure",
}

DIRECT_SPECIAL_ATTACKS = {
    "Petal Dance",
    "Grass Knot",
    "Draining Kiss",
    "Electro Drift"
}
BORNS_SIMPLE_TEAM_OF_3 = [5, 26]

type_chart = [
    # Normal  Fight  Fly  Pois  Grou  Rock  Bug   Ghos  Stee  Fire  Wate  Gras  Elec  Psyc  Ice   Drag  Dark  Fair
    [  1.0,   1.0,  1.0,  1.0,  1.0,  0.5,  1.0,  0.0,  0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0],  # Normal
    [  2.0,   1.0,  0.5,  0.5,  1.0,  2.0,  0.5,  0.0,  2.0,  1.0,  1.0,  1.0,  1.0,  0.5,  2.0,  1.0,  2.0,  0.5],  # Fighting
    [  1.0,   2.0,  1.0,  1.0,  1.0,  0.5,  2.0,  1.0,  0.5,  1.0,  1.0,  2.0,  0.5,  1.0,  1.0,  1.0,  1.0,  1.0],  # Flying
    [  1.0,   1.0,  1.0,  0.5,  0.5,  0.5,  1.0,  0.5,  0.0,  1.0,  1.0,  2.0,  1.0,  1.0,  1.0,  1.0,  1.0,  2.0],  # Poison
    [  1.0,   1.0,  0.0,  2.0,  1.0,  2.0,  0.5,  1.0,  2.0,  2.0,  1.0,  0.5,  2.0,  1.0,  1.0,  1.0,  1.0,  1.0],  # Ground
    [  1.0,   0.5,  2.0,  1.0,  0.5,  1.0,  2.0,  1.0,  0.5,  2.0,  1.0,  1.0,  1.0,  1.0,  2.0,  1.0,  1.0,  1.0],  # Rock
    [  1.0,   0.5,  0.5,  0.5,  1.0,  1.0,  1.0,  0.5,  0.5,  0.5,  1.0,  2.0,  1.0,  2.0,  1.0,  1.0,  2.0,  0.5],  # Bug
    [  0.0,   1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  2.0,  1.0,  1.0,  1.0,  1.0,  1.0,  2.0,  1.0,  1.0,  0.5,  1.0],  # Ghost
    [  1.0,   1.0,  1.0,  1.0,  1.0,  2.0,  1.0,  1.0,  0.5,  0.5,  0.5,  1.0,  0.5,  1.0,  2.0,  1.0,  1.0,  2.0],  # Steel
    [  1.0,   1.0,  1.0,  1.0,  1.0,  0.5,  2.0,  1.0,  2.0,  0.5,  0.5,  2.0,  1.0,  1.0,  2.0,  0.5,  1.0,  1.0],  # Fire
    [  1.0,   1.0,  1.0,  1.0,  2.0,  2.0,  1.0,  1.0,  1.0,  2.0,  0.5,  0.5,  1.0,  1.0,  1.0,  0.5,  1.0,  1.0],  # Water
    [  1.0,   1.0,  0.5,  0.5,  2.0,  2.0,  0.5,  1.0,  0.5,  0.5,  2.0,  0.5,  1.0,  1.0,  1.0,  0.5,  1.0,  1.0],  # Grass
    [  1.0,   1.0,  2.0,  1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  1.0,  2.0,  0.5,  0.5,  1.0,  1.0,  0.5,  1.0,  1.0],  # Electric
    [  1.0,   2.0,  1.0,  2.0,  1.0,  1.0,  1.0,  1.0,  0.5,  1.0,  1.0,  1.0,  1.0,  0.5,  1.0,  1.0,  0.0,  1.0],  # Psychic
    [  1.0,   1.0,  2.0,  1.0,  2.0,  1.0,  1.0,  1.0,  0.5,  0.5,  0.5,  2.0,  1.0,  1.0,  0.5,  2.0,  1.0,  1.0],  # Ice
    [  1.0,   1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  2.0,  1.0,  0.0],  # Dragon
    [  1.0,   0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  2.0,  1.0,  1.0,  1.0,  1.0,  1.0,  2.0,  1.0,  1.0,  0.5,  0.5],  # Dark
    [  1.0,   2.0,  1.0,  0.5,  1.0,  1.0,  1.0,  1.0,  0.5,  0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  2.0,  2.0,  1.0]   # Fairy
]

nature_chart = {
    # key : nature / value : [1,1,1,1,1] ([atk, def, spa, spd, spe])
    # Reduced     Atk                          Def                      Spe. Atk                     Spe. Def                      Speed
    "Hardy": [1, 1, 1, 1, 1],     "Lonely": [1.1, 0.9, 1, 1, 1], "Adamant": [1.1, 1, 0.9, 1, 1],  "Naughty":[1.1, 1, 1, 0.9, 1], "Brave":   [1.1, 1, 1, 1, 0.9], # Atk Boosted
    "Bold":  [0.9, 1.1, 1, 1, 1], "Docile": [1, 1, 1, 1, 1],     "Impish":  [1, 1.1, 0.9, 1, 1],  "Lax":    [1, 1.1, 1, 0.9, 1], "Relaxed": [1, 1.1, 1, 1, 0.9], # Def Boosted
    "Modest":[0.9, 1, 1.1, 1, 1], "Mild":   [1, 0.9, 1.1, 1, 1], "Bashful": [1, 1, 1, 1, 1],      "Rash":   [1, 1, 1.1, 0.9, 1], "Quiet":   [1, 1, 1.1, 1, 0.9],   # Spe. Atk Boosted
    "Calm":  [0.9, 1, 1, 1.1, 1], "Gentle": [1, 0.9, 1, 1.1, 1], "Careful": [1, 1, 0.9, 1.1, 1],  "Quirky": [1, 1, 1, 1, 1],     "Sassy":   [1, 1, 1, 1.1, 0.9], # Spe. Def Boosted
    "Timid": [0.9, 1, 1, 1, 1.1], "Hasty":  [1, 0.9, 1, 1, 1.1], "Jolly":   [1, 1, 0.9, 1, 1.1],  "Naive":  [1, 1, 1, 0.9, 1.1], "Serious": [1, 1, 1, 1, 1], # Speed Boosted
}
    
def can_terastallize(pokemon, fight, team_id):
    """
    Vérifie si un Pokémon peut téracristaliser.
    """
    # Vérifier si déjà téracristallisé
    if pokemon.tera_activated:
        return False
    
    # Vérifier si l'équipe a déjà utilisé sa téracristalisation
    if hasattr(fight, 'tera_used_team1') and hasattr(fight, 'tera_used_team2'):
        if team_id == 1 and fight.tera_used_team1:
            return False
        if team_id == 2 and fight.tera_used_team2:
            return False
    
    return True

def can_use_attack(pokemon, attack):
    """
    Vérifie si un Pokémon peut utiliser une attaque donnée.
    Retourne (True, "") si l'attaque peut être utilisée, 
    ou (False, "raison") si elle ne peut pas être utilisée.
    """
    # Vérifier si l'attaque a des PP disponibles
    if pokemon.get_attack_pp(attack) <= 0:
        return False, f"{pokemon.name} n'a plus de PP pour {attack.name} !"
    
    # Vérifier Heal Block : empêche l'utilisation d'attaques de soin
    if getattr(pokemon, 'heal_blocked', False) and "heal" in attack.flags:
        return False, f"{pokemon.name} ne peut pas utiliser {attack.name} car il est sous l'effet de Heal Block !"
    
    # Vérifier Encore : force l'utilisation d'une attaque spécifique
    if pokemon.encored_turns > 0 and pokemon.encored_attack:
        if attack != pokemon.encored_attack:
            return False, f"{pokemon.name} est sous l'effet d'Encore et doit utiliser {pokemon.encored_attack.name} !"
    
    # Vérifier Choice items : verrouille sur une attaque spécifique
    if pokemon.item and "Choice" in pokemon.item and pokemon.locked_attack:
        if attack != pokemon.locked_attack:
            return False, f"{pokemon.name} est verrouillé sur {pokemon.locked_attack.name} par {pokemon.item} !"
    
    # Vérifier si l'attaque est de type Status
    if attack.category == "Status":
        # Vérifier Taunt
        if pokemon.is_taunted():
            return False, f"{pokemon.name} est provoqué et ne peut pas utiliser d'attaques de statut !"
        
        # Vérifier Assault Vest (Veste de Combat)
        if pokemon.item == "Assault Vest":
            return False, f"{pokemon.name} porte une Veste de Combat et ne peut pas utiliser d'attaques de statut !"
    
    return True, ""

def possible_attacks(pokemon):
    """
    Retourne la liste des attaques possibles par le pokemon
    """
    attacks = [pokemon.attack1, pokemon.attack2, pokemon.attack3, pokemon.attack4]
    possible = []
    
    for atk in attacks:
        if atk is not None:
            can_use, _ = can_use_attack(pokemon, atk)
            if can_use:
                possible.append(atk)
    
    return possible

def transform_pokemon(pokemon, new_pokemon_name: str):
    """
    Transforme un Pokémon en un autre Pokémon pour les pokémons qui changent de forme
    comme Békaglaçon, Morpeko, etc.
    """
    from import_pokemon_team_from_json import import_pokemon_from_pokedex
    # Importer les données du nouveau Pokémon
    new_pokemon_data = import_pokemon_from_pokedex(new_pokemon_name)
    attributes_that_musnt_be_replaced = ["stats", "stats_with_no_modifier", "max_hp", "base_stats"]
    for attr in pokemon.attributes():
        if attr not in attributes_that_musnt_be_replaced:
            # Remplacer l'attribut par celui du nouveau Pokémon
            setattr(new_pokemon_data, attr, getattr(pokemon, attr))
    return new_pokemon_data

def evaluate_type_efficiency(poke1, poke2):
    """
    Evalue l'efficacité des types du pokemon1 face à ceux du pokemon2.

    :param poke1: Le premier Pokémon à évaluer.
    :param poke2: Pokemon sur lequel on évalue l'efficacité des types de poke1.
    :return: Un coefficient compris entre x(1/2)**9 et x(2)**9, valeurs possibles (1/2)**n et (2)**n ou n appartient à [0, 9].
    """
    efficiency = 1.0
    for type2 in poke2.original_types:
        for type1 in poke1.original_types:
            efficiency *= type_chart[POKEMON_TYPES_ID[type1]][POKEMON_TYPES_ID[type2]]

    if poke2.tera_activated:
        for type1 in poke1.original_types: 
            efficiency *= type_chart[POKEMON_TYPES_ID[type1]][POKEMON_TYPES_ID[poke2.types[0]]]

    if poke1.tera_activated:
        for type2 in poke2.original_types:
            efficiency *= type_chart[POKEMON_TYPES_ID[poke1.types[0]]][POKEMON_TYPES_ID[type2]]

    return efficiency     

        
