'''
fichier regroupant tous les talents de pokemon et créant un dictionnaire regroupant tous leurs effets.
'''

import pokemon as PK
import pokemon_datas as STATS

pokemon_talents = {
    "Absorbant": {
    "description": "Restaure 1/4 des PV perdus lorsque le Pokémon subit une attaque de type Eau.",
    "effect": lambda pokemon, attaque=None, attaque_adverse=None, terrain=None, meteo=None:
        setattr(
            pokemon,
            "current_hp",
            min(
                pokemon.current_hp + int(pokemon.stats["HP"] * 0.25),
                pokemon.stats["HP"]
            )
        ) if attaque_adverse and attaque_adverse.get("type") == "Water" else None
    },
    "Chlorophylle": {
        "description": "Double la vitesse du Pokémon lorsque le temps est ensoleillé.",
        "effect": lambda pokemon, attaque=None, attaque_adverse=None, terrain=None, meteo=None: 
            setattr(pokemon, "stats_modifier", [0, 0, 0, 0, 0, 2]) if attaque_adverse and meteo == "Sunny" else None
    },
    "Engrais": {
        "description": "Augmente la puissance des attaques de type Plante de 50% lorsque les PV du Pokémon sont inférieurs à 1/3 de ses PV max.",
        "effect": lambda pokemon, attaque=None, attaque_adverse=None, terrain=None, meteo=None:
            setattr(
                attaque,
                "basePower",
                int(attaque.puissance * 1.5)
            ) if pokemon.current_hp < pokemon.stats["HP"] // 3 and attaque and attaque.type == "Plant" else None
    },
    "Torrent": {
        "description": "Augmente la puissance des attaques de type Eau de 50% lorsque les PV du Pokémon sont inférieurs à 1/3 de ses PV max.",
        "effect": lambda pokemon, attaque=None, attaque_adverse=None, terrain=None, meteo=None:
            setattr(
                attaque,
                "basePower",
                int(attaque.puissance * 1.5)
            ) if pokemon.current_hp < pokemon.stats["HP"] // 3 and attaque and attaque.type == "Water" else None
    },
    "Brasier": {
        "description": "Augmente la puissance des attaques de type Feu de 50% lorsque les PV du Pokémon sont inférieurs à 1/3 de ses PV max.",
        "effect": lambda pokemon, attaque=None, attaque_adverse=None, terrain=None, meteo=None:
            setattr(
                attaque,
                "basePower",
                int(attaque.puissance * 1.5)
            ) if pokemon.current_hp < pokemon.stats["HP"] // 3 and attaque and attaque.type == "Fire" else None
    },
}

def effet_talent(pokemon, talent, attaque=None, attaque_adverse=None):
    """
    Applique l'effet du talent du Pokémon.
    
    :param pokemon: Instance de la classe Pokemon.
    :param talent: Nom du talent à appliquer.
    :param attaque: Instance de l'attaque (si applicable).
    :param attaque_adverse: Instance de l'attaque adverse (si applicable).
    :return: Valeur après application de l'effet du talent.
    """
    if talent in pokemon_talents:
        effet = pokemon_talents[talent]["effet"]
        return effet(pokemon, attaque, attaque_adverse)
    else:
        raise ValueError(f"Talent '{talent}' inconnu.")
    
def import_pokemon(name):
    raw_pokemon = STATS.pokemon_data["Charizard"]
    pokemon = PK.Pokemon(
        name = name,
        talent = raw_pokemon["abilities"][0],
        type1 = raw_pokemon["types"][0],
        type2 = raw_pokemon["types"][1] if len(raw_pokemon["types"]) > 1 else None,
    )
    stats_list = raw_pokemon["stats"] # Dictionnaire avec pour clé HP, Attack, Defense, Special Attack, Special Defense, Speed
    for i in stats_list: 
        pokemon.stats[i] = stats_list[i]
    return pokemon

Dracaufeu = import_pokemon("Charizard")
Dracaufeu.talent = "Absorbant"

Dracaufeu.current_hp = Dracaufeu.stats['HP']  - 10
print(f"PV de {Dracaufeu.name} avant effet du talent {Dracaufeu.talent} : {Dracaufeu.current_hp}")

effet_talent(Dracaufeu, Dracaufeu.talent, attaque=None, attaque_adverse={"type": "Eau"})
print(f"PV après effet du talent {Dracaufeu.talent} : {Dracaufeu.current_hp}")


