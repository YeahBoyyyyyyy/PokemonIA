# item.py
def leftovers_effect(pokemon, fight=None):
    if pokemon.current_hp < pokemon.max_hp:
        heal = int(pokemon.max_hp * 0.0625)
        print(f"{pokemon.name} récupère {heal} PV grâce à ses Restes.")
        pokemon.current_hp = min(pokemon.current_hp + heal, pokemon.max_hp)

def sitrus_berry_effect(pokemon, fight=None):
    if pokemon.current_hp <= pokemon.max_hp * 0.5:
        heal = int(pokemon.max_hp * 0.25)
        print(f"{pokemon.name} consomme une Baie Sitrus et récupère {heal} PV !")
        pokemon.current_hp = min(pokemon.current_hp + heal, pokemon.max_hp)
        pokemon.item = None

def apply_choice_boost(pokemon, fight=None):
    if pokemon.item == "Choice Band":
        pokemon.stats["Attack"] = int(pokemon.stats["Attack"] * 1.5)
    elif pokemon.item == "Choice Specs":
        pokemon.stats["Sp. Atk"] = int(pokemon.stats["Sp. Atk"] * 1.5)
    elif pokemon.item == "Choice Scarf":
        pokemon.stats["Speed"] = int(pokemon.stats["Speed"] * 1.5)

def apply_eviolite(pokemon, fight=None):
    if not pokemon.fully_evolved and pokemon.item == "Eviolite":
        pokemon.stats["Defense"] = int(pokemon.stats["Defense"] * 1.5)
        pokemon.stats["Sp. Def"] = int(pokemon.stats["Sp. Def"] * 1.5)

item_effects = {
    "Leftovers": leftovers_effect,
    "Sitrus Berry": sitrus_berry_effect,
    "Choice Band": apply_choice_boost,
    "Choice Specs": apply_choice_boost,
    "Choice Scarf": apply_choice_boost,
    "Eviolite": apply_eviolite,
}
