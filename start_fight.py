import pokemon as pk
from battle_interface import launch_battle
from import_pokemon_team_from_json import import_team_from_json

# Créer l'équipe française
french_team = import_team_from_json(1)
competitive_team = import_team_from_json(4)

print("Quelle équipe utiliser ?")
print("1. Équipe compétitive anglaise")
print("2. Équipe française avec surnoms")
choice = input("Votre choix (1 ou 2) : ")

opponent_team = []

if choice == "2":
    selected_team = french_team
    opponent_team = competitive_team
    print("Équipe française créée !")
else:
    selected_team = competitive_team
    opponent_team = french_team
    print("Équipe compétitive créée !")

print("=" * 50)
for i, pokemon in enumerate(selected_team, 1):
    display_name = getattr(pokemon, 'nickname', pokemon.name)
    print(f"{i}. {display_name} ({pokemon.name})")
    print(f"   Talent: {pokemon.talent}")
    print(f"   Objet: {pokemon.item}")
    print(f"   Tera Type: {pokemon.tera_type}")
    print(f"   Nature: {pokemon.nature}")
    print(f"   EVs: {pokemon.evs}")
    print(f"   Attaques: {pokemon.attack1.name}, {pokemon.attack2.name}, {pokemon.attack3.name}, {pokemon.attack4.name}")
    print()

# Lancer le combat avec l'équipe sélectionnée
launch_battle(selected_team, opponent_team)