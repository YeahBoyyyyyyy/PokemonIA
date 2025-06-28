from fight import *
from pokemon import *
#from pokemon_attacks import *
#from donnees import *
from pokemon_datas import *


pokemon1 = pokemon(pokemon_data["Charizard"])
pokemon2 = pokemon(pokemon_data["Jynx"])


pokemon2.print_pokemon_status()
combat = Fight(pokemon1, pokemon2)
print("-" * 30)
pokemon2.print_modifiers()
print("#" * 30)
combat.print_fight_status()
print("x" * 30)
combat.set_weather("Snow")
combat.add_field_effect("Grassy Terrain")
combat.print_fight_status()
print("x" * 30)
combat.weather_boost_modifier(pokemon2)
combat.next_turn()
print(f"TOUR SUIVANT : NUMERO {combat.turn}")
pokemon2.actualize_stats()
print("-" * 30)
pokemon1.print_pokemon_status()
print("x" * 30)
pokemon2.print_pokemon_status()

