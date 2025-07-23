from fight import Fight
import pokemon as pk
import pokemon_attacks as ATTACKES
import pokemon_datas as STATS
import random
from donnees import bcolors

def can_use_attack(pokemon, attack):
    """
    Vérifie si un Pokémon peut utiliser une attaque donnée.
    Retourne (True, "") si l'attaque peut être utilisée, 
    ou (False, "raison") si elle ne peut pas être utilisée.
    """
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

# Option pour afficher les stats d'un Pokémon
def print_pokemon_stats(pokemon : pk.pokemon):

    print(f"\n{bcolors.LIGHT_GREEN}Stats de {bcolors.BOLD}{pokemon.name}{bcolors.UNBOLD}:")
    print(f"Talent: {pokemon.talent}")
    print(f"Objet: {pokemon.item}")
    print(f"PV: {pokemon.current_hp}/{pokemon.max_hp}")
    for stat in ["Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]:
        print(f"{stat}: {pokemon.stats[stat]}")
    print(f"Modificateurs de stats: {pokemon.stats_modifier}")
    print(f"Modificateurs de stats cachés: {pokemon.hidden_boost}")
    print(f"{bcolors.LIGHT_RED}Attaques:")
    for i, atk in enumerate([pokemon.attack1, pokemon.attack2, pokemon.attack3, pokemon.attack4], 1):
        if atk:
            print(f"  {i}. {atk.name}")
    print(f"{bcolors.ENDC}")


def choose_switch_pokemon(fight, team_id):
    """
    Permet au joueur de choisir quel Pokémon faire entrer quand son Pokémon actuel est KO.
    """
    team = fight.team1 if team_id == 1 else fight.team2
    team_name = "joueur 1" if team_id == 1 else "joueur 2"
    
    print(f"\n{bcolors.OKYELLOW}Le Pokémon du {team_name} est KO ! Choisissez un remplaçant :{bcolors.ENDC}")
    
    while True:
        available_pokemon = []
        for i, p in enumerate(team):
            if p.current_hp > 0:
                available_pokemon.append((i, p))
        
        if not available_pokemon:
            return None  # Aucun Pokémon disponible
        
        print("\nPokémon disponibles :")
        for idx, (i, p) in enumerate(available_pokemon):
            print(f"{idx}. {p.name} (HP: {p.current_hp}/{p.max_hp})")
        
        choice = input("Choisissez un Pokémon (numéro) : ").strip()
        
        if choice.isdigit():
            choice_idx = int(choice)
            if 0 <= choice_idx < len(available_pokemon):
                pokemon_index = available_pokemon[choice_idx][0]
                fight.player_switch(team_id, pokemon_index)
                return pokemon_index
            else:
                print("Choix invalide.")
        else:
            print("Veuillez entrer un numéro valide.")


def choose_uturn_switch_pokemon(fight, team_id):
    """
    Permet au joueur de choisir quel Pokémon faire entrer après U-turn.
    """
    team = fight.team1 if team_id == 1 else fight.team2
    current_pokemon = fight.active1 if team_id == 1 else fight.active2
    
    print(f"\n{bcolors.OKBLUE}Choisissez le Pokémon à faire entrer après U-turn :{bcolors.ENDC}")
    
    while True:
        available_pokemon = []
        for i, p in enumerate(team):
            if p.current_hp > 0 and p != current_pokemon:
                available_pokemon.append((i, p))
        
        if not available_pokemon:
            return None  # Aucun Pokémon disponible
        
        print("\nPokémon disponibles :")
        for idx, (i, p) in enumerate(available_pokemon):
            print(f"{idx}. {p.name} (HP: {p.current_hp}/{p.max_hp})")
        
        choice = input("Choisissez un Pokémon (numéro) : ").strip()
        
        if choice.isdigit():
            choice_idx = int(choice)
            if 0 <= choice_idx < len(available_pokemon):
                pokemon_index = available_pokemon[choice_idx][0]
                fight.player_switch(team_id, pokemon_index)
                return pokemon_index
            else:
                print("Choix invalide.")
        else:
            print("Veuillez entrer un numéro valide.")


def launch_battle(team1: list[pk.pokemon], team2: list[pk.pokemon]):
    fight = Fight(team1, team2)
    
    # Surcharger la méthode player_choice_switch pour permettre au joueur de choisir
    def player_choice_switch_override(team_id):
        if team_id == 1:  # Joueur humain
            # Vérifier si c'est un changement forcé par U-turn
            current_pokemon = fight.active1 if team_id == 1 else fight.active2
            if current_pokemon.must_switch_after_attack:
                choose_uturn_switch_pokemon(fight, team_id)
            else:
                choose_switch_pokemon(fight, team_id)
        else:  # IA
            fight.auto_switch(team_id)
    
    # Remplacer la méthode de la classe Fight
    fight.player_choice_switch = player_choice_switch_override
    
    fight.fight()

    while True:
        if fight.check_battle_end():
            break

        fight.print_fight_status()

        # Boucle de sélection d'action
        while True:
            attacker = fight.active1
            
            # Afficher le numéro de tour (ajuster +1 car le tour sera incrémenté à la fin)
            print(f"\n{bcolors.OKMAGENTA}═══ TOUR {fight.turn + 1} ═══{bcolors.ENDC}")
            
            print(f"\n{bcolors.LIGHT_BLUE}Choisissez une action pour le joueur 1 :")
            print("1. Attaquer")
            print("2. Changer de Pokémon")
            print("3. Voir les stats d'un Pokémon")
            print("4. Quitter le combat")
            print(f"{bcolors.ENDC}")
            action1 = input("Action (1-4) : ").strip()

            if action1 == "1":
                attacker = fight.active1
                if attacker.charging and attacker.charging_attack:
                    attacks = [attacker.charging_attack]
                else:
                    attacks = [attacker.attack1, attacker.attack2, attacker.attack3, attacker.attack4]

                # Vérifier si le Pokémon est en train de charger une attaque
                if attacker.charging and attacker.charging_attack:
                    # Vérifier si l'attaque de charge peut être utilisée
                    can_use, reason = can_use_attack(attacker, attacker.charging_attack)
                    if not can_use:
                        print(f"\n{bcolors.OKRED}{reason}")
                        print(f"{attacker.name} ne peut pas terminer sa charge !{bcolors.ENDC}")
                        # Dans ce cas, on laisse le joueur choisir une autre attaque
                    else:
                        print(f"\n{bcolors.OKYELLOW}{attacker.name} termine sa charge avec {attacker.charging_attack.name} !{bcolors.ENDC}")
                        act1 = (attacker, attacker.charging_attack)
                        break

                # Afficher des messages informatifs pour Encore et Choice items
                if attacker.encored_turns > 0 and attacker.encored_attack:
                    print(f"\n{bcolors.OKYELLOW}{attacker.name} est sous l'effet d'Encore ! ({attacker.encored_turns} tour(s) restant(s)){bcolors.ENDC}")
                
                if attacker.item and "Choice" in attacker.item and attacker.locked_attack:
                    print(f"\n{bcolors.OKYELLOW}{attacker.name} est verrouillé par {attacker.item} !{bcolors.ENDC}")

                while True:
                    print(f"\n{bcolors.GRAY}Choisissez une attaque (ou tapez R pour revenir en arrière) :")
                    for i, atk in enumerate(attacks):
                        if atk:
                            can_use, reason = can_use_attack(attacker, atk)
                            if can_use:
                                print(f"{i+1}. {atk.name}")
                            else:
                                print(f"{i+1}. {bcolors.DARK_RED}{atk.name} (BLOQUÉE){bcolors.ENDC}")
                                print(f"    {bcolors.GRAY}Raison: {reason}{bcolors.ENDC}")
                    print(f"{bcolors.ENDC}")
                    choice = input("Numéro d'attaque : ").strip()
                    if choice.lower() == "r":
                        break  # Retour au menu principal
                    if choice.isdigit() and 1 <= int(choice) <= len(attacks) and attacks[int(choice)-1]:
                        atk1 = attacks[int(choice) - 1]
                        
                        # Vérifier si l'attaque peut être utilisée (Taunt, Assault Vest, etc.)
                        can_use, reason = can_use_attack(attacker, atk1)
                        if not can_use:
                            print(f"{bcolors.OKRED}{reason}{bcolors.ENDC}")
                            continue  # Demander une autre attaque
                        
                        act1 = (attacker, atk1)
                        break
                    else:
                        print("Choix invalide.")
                else:
                    continue  # En cas de retour, on retourne au menu principal

                if 'act1' in locals():
                    break  # Sortie de la boucle d'action principale

            elif action1 == "2":
                while True:
                    print("\nChoisissez un autre Pokémon dans votre équipe (ou tapez R pour revenir) :")
                    for i, p in enumerate(fight.team1):
                        status = " (KO)" if p.current_hp <= 0 else ""
                        selected = " (actif)" if p == fight.active1 else ""
                        print(f"{i}. {p.name}{status}{selected}")
                    index = input("Index : ").strip()
                    if index.lower() == "r":
                        break  # Retour
                    if index.isdigit():
                        index = int(index)
                        if 0 <= index < len(fight.team1) and fight.team1[index].current_hp > 0 and fight.team1[index] != fight.active1:
                            act1 = ("switch", index)
                            break
                        else:
                            print("Choix invalide.")
                else:
                    continue  # Retour au menu principal
                if 'act1' in locals():
                    break

            elif action1 == "3":
                liste = [fight.active1, fight.active2]
                for i, poke in enumerate(liste):
                    print(f"{i}. {poke.name}")
                choice = input("Numéro du Pokémon à inspecter : ").strip()
                if choice.isdigit() and 0 <= int(choice) < len(liste):
                    print_pokemon_stats(liste[int(choice)])
                else:
                    print("Choix invalide.")

            elif action1 == "4":
                print("Combat terminé.")
                return

            else:
                print("Entrée invalide.")

        # Tour de l'IA
        attacker2 = fight.active2
        attacks2 = [attacker2.attack1, attacker2.attack2, attacker2.attack3, attacker2.attack4]
        valid_attacks = [atk for atk in attacks2 if atk is not None]
        
        if valid_attacks:
            # Vérifier si le Pokémon est en train de charger une attaque (priorité absolue)
            if attacker2.charging and attacker2.charging_attack:
                atk2 = attacker2.charging_attack
            # Vérifier si le Pokémon est sous l'effet d'Encore
            elif attacker2.encored_turns > 0 and attacker2.encored_attack:
                atk2 = attacker2.encored_attack
            # Vérifier si le Pokémon est verrouillé par un objet Choice
            elif attacker2.locked_attack and attacker2.item and "Choice" in attacker2.item:
                atk2 = attacker2.locked_attack
            else:
                atk2 = random.choice(valid_attacks)
            
            act2 = (attacker2, atk2)

            # Résolution du tour
            if isinstance(act1, tuple) and act1[0] == "switch":
                # Switch : le nouveau Pokémon entre AVANT que l'adversaire n'attaque
                fight.player_switch(1, act1[1])
                print(f"\n{fight.active2.name} attaque le nouveau Pokémon !")
                fight.player_attack(fight.active2, atk2, fight.active1)
                # Incrémenter le tour après un switch + attaque
                fight.next_turn()
            else:
                fight.resolve_turn(act1, act2)
        else:
            # Si l'adversaire n'a pas d'attaque, faire seulement le switch
            if isinstance(act1, tuple) and act1[0] == "switch":
                fight.player_switch(1, act1[1])
                # Incrémenter le tour même si seulement un switch
                fight.next_turn()
            print(f"{attacker2.name} n'a pas d'attaque disponible !")


def import_pokemon(name):
    raw_pokemon = STATS.pokemon_data["Charizard"]
    pokemon = pk.pokemon(STATS.pokemon_data[name])
    stats_list = raw_pokemon["stats"] # Dictionnaire avec pour clé HP, Attack, Defense, Special Attack, Special Defense, Speed
    for i in stats_list: 
        pokemon.stats[i] = stats_list[i]
    return pokemon

venusaur = import_pokemon("Venusaur")
venusaur.talent = "Chlorophyll"
venusaur.item = "Choice Band"  # Test Choice Band
venusaur.attack1 = ATTACKES.HydroPump()
venusaur.attack2 = ATTACKES.LightScreen()
venusaur.attack3 = ATTACKES.Spore()
venusaur.attack4 = ATTACKES.RainDance()

duraludon = import_pokemon("Duraludon")
duraludon.talent = "Light Metal"
duraludon.item = "Eviolite"
duraludon.attack1 = ATTACKES.DragonPulse()
duraludon.attack2 = ATTACKES.ElectroShot()
duraludon.attack3 = ATTACKES.Protect()

mew = import_pokemon("Mew")
mew.talent = "Synchronize"
mew.item = "Rocky Helmet"  # Test Rocky Helmet
mew.attack1 = ATTACKES.HydroPump()
mew.attack2 = ATTACKES.Taunt()
mew.attack3 = ATTACKES.Encore()

charizard = import_pokemon("Charizard")
charizard.talent = "Drought"
charizard.item = "Sitrus Berry"
charizard.attack1 = ATTACKES.Substitute()
charizard.attack2 = ATTACKES.Thunderbolt()
charizard.attack3 = ATTACKES.Taunt()

rillaboom = import_pokemon("Rillaboom")
rillaboom.talent = "Grassy Surge"
rillaboom.item = "Assault Vest"
rillaboom.attack1 = ATTACKES.WoodHammer()
rillaboom.attack2 = ATTACKES.UTurn()

garchomp = import_pokemon("Garchomp")
garchomp.talent = "Rough Skin"
garchomp.item = "Rocky Helmet"
garchomp.attack1 = ATTACKES.Earthquake()

launch_battle([rillaboom, venusaur, duraludon], [garchomp])
