from fight import Fight
from pokemon import *
import random
from colors_utils import Colors
from utilities import *
from import_pokemon_team_from_json import import_team_from_json

teamAI1 = import_team_from_json(5)
teamAI2 = import_team_from_json(6)

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

    # Initialiser les IAs - Exemple: Joueur vs IA
    from IA.pokemon_ia import RandomAI, PlayerAI
    
    # Option 1: IA vs IA (comme avant)
    # ia1 = RandomAI(1)
    # ia2 = RandomAI(2)
    
    # Option 2: Joueur vs IA (pour l'apprentissage supervisé)
    ia1 = PlayerAI(1, "Joueur Humain")  # Joueur humain
    ia2 = RandomAI(2)  # IA adverse
    
    # Option 3: IA vs Joueur
    # ia1 = RandomAI(1)  # IA
    # ia2 = PlayerAI(2, "Joueur Humain")  # Joueur humain
    
    print_fight(ia1, ia2)

    while True:
        if fight.check_battle_end():
            print("Battle terminé!")
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
        

battle_manager(teamAI1, teamAI2)