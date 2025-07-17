from fight import Fight
import pokemon as pk
import pokemon_attacks as ATTACKES
import pokemon_datas as STATS
import random
from donnees import bcolors

# Option pour afficher les stats d'un Pokémon
def print_pokemon_stats(pokemon : pk.pokemon):

    print(f"\n{bcolors.LIGHT_GREEN}Stats de {bcolors.BOLD}{pokemon.name}{bcolors.UNBOLD}:")
    print(f"Talent: {pokemon.talent}")
    print(f"Objet: {pokemon.item}")
    print(f"PV: {pokemon.current_hp}/{pokemon.max_hp}")
    for stat in ["Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]:
        print(f"{stat}: {pokemon.stats[stat]}")
    print(f"{bcolors.LIGHT_RED}Attaques:")
    for i, atk in enumerate([pokemon.attack1, pokemon.attack2, pokemon.attack3, pokemon.attack4], 1):
        if atk:
            print(f"  {i}. {atk.name}")
    print(f"{bcolors.ENDC}")


def launch_battle(team1 : list[pk.pokemon], team2 : list[pk.pokemon]):
    fight = Fight(team1, team2)
    fight.fight()

    while True:
        if fight.check_battle_end():
            break

        fight.print_fight_status()

        action1 = None
        while action1 not in ["1", "2"]:
            print(f"\n{bcolors.LIGHT_BLUE}Choisissez une action pour le joueur 1 :")
            print("1. Attaquer")
            print("2. Changer de Pokémon")
            print("3. Voir les stats d'un Pokémon'")
            print(f"4. Quitter le combat{bcolors.ENDC}")

            action1 = input("Action (1 ou 2) : ").strip()

            if action1 == "3":
                liste = [fight.active1, fight.active2]
                for i in range(len(liste)):
                    print(f"{i}. {liste[i].name}")
                choice = int(input("Numéro du Pokémon dont vous voulez voir les stats : "))
                try:
                    print_pokemon_stats(liste[choice])
                except IndexError:
                    print("Choix invalide.")
                continue
            elif action1 == "4":
                print("Combat terminé.")
                return
        
        if action1 == "1":
            attacker = fight.active1
            attacks = [attacker.attack1, attacker.attack2, attacker.attack3, attacker.attack4]
            print(f"{bcolors.GRAY}Choisissez une attaque :")
            for i, atk in enumerate(attacks):
                if atk:
                    print(f"{i+1}. {atk.name}")
            choice = int(input("Numéro d'attaque : ")) - 1
            atk1 = attacks[choice]
            act1 = (attacker, atk1)
            print(f'{bcolors.ENDC}')
        elif action1 == "2":
            print("Choisissez un autre Pokémon dans votre équipe :")
            for i, p in enumerate(fight.team1):
                status = " (KO)" if p.current_hp <= 0 else ""
                selected = " (actif)" if p == fight.active1 else ""
                print(f"{i}. {p.name}{status}{selected}")
            while True:
                index = int(input("Index du Pokémon à envoyer : "))
                if 0 <= index < len(fight.team1) and fight.team1[index].current_hp > 0 and fight.team1[index] != fight.active1:
                    break
                print("Choix invalide.")
            act1 = ("switch", index)
        else:
            print("Entrée invalide. Tour sauté.")
            continue

        # Choix IA joueur 2 (attaque aléatoire)
        attacker2 = fight.active2
        attacks2 = [attacker2.attack1, attacker2.attack2, attacker2.attack3, attacker2.attack4]
        atk2 = random.choice([atk for atk in attacks2 if atk is not None])
        act2 = (attacker2, atk2)

        # Résolution du tour avec support switch
        if act1[0] == "switch":
            fight.player_switch(1, act1[1])
        else:
            fight.resolve_turn(act1, act2)

def import_pokemon(name):
    raw_pokemon = STATS.pokemon_data["Charizard"]
    pokemon = pk.pokemon(STATS.pokemon_data[name])
    stats_list = raw_pokemon["stats"] # Dictionnaire avec pour clé HP, Attack, Defense, Special Attack, Special Defense, Speed
    for i in stats_list: 
        pokemon.stats[i] = stats_list[i]
    return pokemon

venusaur = import_pokemon("Venusaur")
venusaur.talent = "Flash Fire"
venusaur.item = "Leftovers"
venusaur.attack1 = ATTACKES.KnockOff()
venusaur.attack2 = ATTACKES.FakeOut()
venusaur.attack3 = ATTACKES.Protect()
venusaur.attack4 = ATTACKES.RainDance()
print(venusaur.talent)

charizard = import_pokemon("Charizard")
charizard.talent = "Drought"
charizard.item = "Choice Specs"
charizard.attack2 = ATTACKES.FlameThrower()

launch_battle([venusaur], [charizard])

