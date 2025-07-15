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
        pokemon.stats["Attack"] += int(pokemon.stats_with_no_modifier["Attack"] * 0.5)
    elif pokemon.item == "Choice Specs":
        pokemon.stats["Sp. Atk"] += int(pokemon.stats_with_no_modifier["Sp. Atk"] * 0.5)
    elif pokemon.item == "Choice Scarf":
        pokemon.stats["Speed"] += int(pokemon.stats_with_no_modifier["Speed"] * 0.5)

def apply_eviolite(pokemon, fight=None):
    if not pokemon.fully_evolved and pokemon.item == "Eviolite":
        pokemon.stats["Defense"] += int(pokemon.stats_with_no_modifier["Defense"] * 0.5)
        pokemon.stats["Sp. Def"] += int(pokemon.stats_with_no_modifier["Sp. Def"] * 0.5)

item_registry = {
    "Leftovers": leftovers_effect,
    "Sitrus Berry": sitrus_berry_effect,
    "Choice Band": apply_choice_boost,
    "Choice Specs": apply_choice_boost,
    "Choice Scarf": apply_choice_boost,
    "Eviolite": apply_eviolite,
}

def trigger_item(pokemon, fight=None):
    item = item_registry.get(pokemon.item)
    if item:
        item(pokemon, fight)
    else:
        print(f"{pokemon.name} n'a pas d'effet d'objet actif.")
    return None