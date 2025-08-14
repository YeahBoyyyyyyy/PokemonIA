from fight import Fight
from pokemon import *
import random
from colors_utils import Colors
from utilities import *
from import_pokemon_team_from_json import import_team_from_json, import_random_simple_team
from damage_calc import *
from IA.pokemon_ia import RandomAI, PlayerAI, LowHeuristicAI



# Initialiser les IAs :
# Option 1: IA vs IA (comme avant)
ia1 = LowHeuristicAI(1)
ia2 = RandomAI(2)   

# Option 2: Joueur vs IA (pour l'apprentissage supervisé)
# ia1 = PlayerAI(1, "Joueur Humain")  # Joueur humain
# ia2 = RandomAI(2)  # IA adverse

# Option 3: Joueur vs Joueur
# ia1 = PlayerAI(1, "Joueur Humain 1")  # Joueur humain 1
# ia2 = PlayerAI(2, "Joueur Humain 2")  # Joueur humain 2


def print_fight(ia1, ia2):
    print(f"{Colors.BG_WHITE}{Colors.BOLD}{Colors.BLACK}Le combat oppose une {ia1.name} à une {ia2.name} !{Colors.RESET}{Colors.UNBOLD}{Colors.BG_DEFAULT}")

def battle_manager(team1: list[pokemon], team2: list[pokemon]):
    """
    Gère le combat entre deux équipes de Pokémon. Gère surtout le combat entre deux IA 
    dont les actions sont déterminées par des fonctions dans IA.pokemon.py. On ne mettra des print que pour 
    les informations concernant les IAs.
    
    :param team1: Première équipe de Pokémon qui est l'équipe jouée par l'IA que l'on veut étudier.
    :param team2: Deuxième équipe de Pokémon qui est l'équipe adverse et sert juste à jouer le combat.
    """
    fight = Fight(team1, team2)

    # Initialiser les variables de téracristalisation
    fight.tera_used_team1 = False
    fight.tera_used_team2 = False

    print_fight(ia1, ia2)

    while True:
        ended, winner = fight.check_battle_end()
        if ended:
            print("Battle terminé!")
            if winner == 1:
                print(f"{Colors.GREEN}L'équipe 1 ({ia1.name}) a gagné !{Colors.RESET}")
                ia1.wins += 1
            elif winner == 2:
                print(f"{Colors.RED}L'équipe 2 ({ia2.name}) a gagné !{Colors.RESET}")
                ia2.wins += 1
            ia1.total_battles += 1
            ia2.total_battles += 1
            break

        fight.print_fight_status()
        
        # Plus besoin de pause manuelle car PlayerAI gère son propre rythme
        # input("Appuyez sur Entrée pour continuer...")  # Optionnel pour debug
         
        # Selection des actions pour chaque IA
        available_actions1 = ia1.get_available_actions(fight)
        available_actions2 = ia2.get_available_actions(fight)

        #print(f"Available Actions AI1: {available_actions1}")
        #print(f"Available Actions AI2: {available_actions2}")


        act1 = ia1.choose_action(fight, available_actions1)
        act2 = ia2.choose_action(fight, available_actions2)

        #print(f"Action IA1: {act1}")
        #print(f"Action IA2: {act2}")

        poke1_action = (ia1, act1)
        poke2_action = (ia2, act2)

        fight.new_resolve_turn(poke1_action, poke2_action)

def reset_team(team : list[pokemon]):
    """ Réinitialise l'équipe de Pokémon pour un nouveau combat."""
    for pokemon in team:
        pokemon.pokemon_center()
"""
for i in range(100):
    team_1 = import_team_from_json(import_random_simple_team())
    team_2 = import_team_from_json(import_random_simple_team())
    battle_manager(team_1, team_2)
    reset_team(team_1)
    reset_team(team_2)
"""    
rounds = []
compteur_changement_equipe = 10
for i in range(10):
    for i in range(100):
        if compteur_changement_equipe > 9:
            team_1 = import_team_from_json(import_random_simple_team())
            team_2 = import_team_from_json(import_random_simple_team())
            compteur_changement_equipe = 0
        battle_manager(team_1, team_2)
        reset_team(team_1)
        reset_team(team_2)
        compteur_changement_equipe +=1
    rounds.append(ia1.wins)
    ia1.wins = 0
    

for i in range(len(rounds)):
    print(f"Nombre victoire manche {ia1.name} {i}: {rounds[i]}/100")
"""
ratio_victoire_defaite_par_equipes = []
for i in range(len(nombre_de_victoire_par_equipes)):
    if nombre_de_combats_par_equipes[i] > 0:
        ratio = nombre_de_victoire_par_equipes[i] / nombre_de_combats_par_equipes[i]
    else:
        ratio = 0
    ratio_victoire_defaite_par_equipes.append(ratio)

for i in range(len(ratio_victoire_defaite_par_equipes)):
    print(f"Équipe {i}: {ratio_victoire_defaite_par_equipes[i]}")
"""