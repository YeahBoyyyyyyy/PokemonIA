import random
from abc import ABC, abstractmethod
import os
from Materials.utilities import *
from colors_utils import Colors
from pokemon import pokemon

class PokemonAI(ABC):
    """Classe abstraite pour toutes les IA Pokémon"""
    
    def __init__(self, team_id, name="Generic AI"):
        self.team_id = team_id  # 1 ou 2
        self.name = name
        self.decisions_made = 0
        self.total_battles = 0
        self.wins = 0
    
    @abstractmethod
    def choose_action(self, fight, available_actions):
        """
        Choisit une action parmi les actions disponibles.
        
        Args:
            fight: Instance de la classe Fight
            available_actions: Dict contenant les actions possibles
                {
                    'attacks': [attack1, attack2, attack3, attack4],
                    'switches': [pokemon1, pokemon2, ...],  # Pokémon vivants
                    'can_terastallize': True/False
                }
        
        Returns:
            tuple: (action_type, action_data, extra_data)
            - ("attack", attack_instance, can_tera) 
            - ("switch", team_index, None)
            - ("terastallize", attack_index, None)
        """
        pass
    
    def get_available_actions(self, fight):
        """
        Détermine les actions disponibles pour l'IA.
        
        Returns:
            dict: Actions disponibles
        """
        # Déterminer quelle équipe et quel Pokémon actif
        if self.team_id == 1:
            active_pokemon = fight.active1
            team = fight.team1
            tera_used = getattr(fight, 'tera_used_team1', False)
        else:
            active_pokemon = fight.active2
            team = fight.team2
            tera_used = getattr(fight, 'tera_used_team2', False)

        possible_attacks = active_pokemon.get_usable_attacks()

        if active_pokemon.can_switch:
            switches = [p for p in team if p.current_hp > 0 and p != active_pokemon]

        # Actions disponibles
        if switches:
            available_actions = {
                'attacks': possible_attacks,
                'switches': switches,
                'can_terastallize': not tera_used and not active_pokemon.tera_activated
            }
        else:
            available_actions = {
                'attacks': possible_attacks,
                'switches': [],  # Toujours inclure la clé 'switches' dans available_actions
                'can_terastallize': not tera_used and not active_pokemon.tera_activated
            }
            
        
        return available_actions
    
    def choose_switch_in(self, fight):
        """
        Détermine quel pokemon choisit pour remplacer le pokémo actuel sur le terrain.
        
        Returns:
            int: Index du Pokémon à faire entrer dans l'équipe
        """

    def get_pokemon_info(self, fight):
        """Récupère les informations sur les Pokémon pour l'IA"""
        if self.team_id == 1:
            my_pokemon = fight.active1
            enemy_pokemon = fight.active2
            my_team = fight.team1
            enemy_team = fight.team2
        else:
            my_pokemon = fight.active2
            enemy_pokemon = fight.active1
            my_team = fight.team2
            enemy_team = fight.team1
        
        return {
            'my_pokemon': my_pokemon,
            'enemy_pokemon': enemy_pokemon,
            'my_team': my_team,
            'enemy_team': enemy_team
        }
    
class RandomAI(PokemonAI):
    """IA Pokémon qui choisit des actions aléatoires"""
    def __init__(self, team_id):
        super().__init__(
            team_id=team_id,
            name="Random AI")

    def choose_action(self, fight, available_actions):
        from Materials.pokemon_attacks import Struggle
        """
        Choisit une action aléatoire parmi les actions disponibles.
        
        Args:
            fight: Instance de la classe Fight
            available_actions: Actions disponibles
        
        Returns:
            tuple: (action_type, action_data, extra_data)
        """
        # Assurer qu'on a bien les actions disponibles
        if available_actions is None:
            available_actions = self.get_available_actions(fight)
        
        # Vérifier les actions possibles
        possible_actions = []
        
        # Attaquer (si on a des attaques utilisables)
        if available_actions['attacks']:
            possible_actions.append('attack')
        
        # Changer (si on a des Pokémon disponibles)
        if 'switches' in available_actions and available_actions['switches'] != []: 
            possible_actions.append('switch')
        
        # Téracristaliser (si possible ET si on a des attaques)
        if available_actions['can_terastallize'] and available_actions['attacks']:
            possible_actions.append('terastallize')
        
        # Si aucune action possible, forcer l'attaque (Struggle)
        if not possible_actions:
            return ('attack', Struggle(), False)

        # Choisir aléatoirement avec pondération
        if len(possible_actions) == 1:
            action_type = possible_actions[0]
        else:
            # Pondération : 80% attaque, 15% switch, 5% tera si peut switch sinon 90% attaque, 10% tera
            weights = []
            if 'switch' in possible_actions:
                if 'terastallize' in possible_actions:
                    weights.extend([0.8, 0.15, 0.05])
                else:
                    weights.extend([0.9, 0.1])
            else:
                if 'terastallize' in possible_actions:
                    weights.extend([0.9, 0.1])
                else:
                    weights.append(1.0)
            action_type = random.choices(possible_actions, weights=weights)[0]
        
        # Exécuter l'action choisie
        if action_type == 'attack':
            if available_actions['attacks']:
                # Récuperer l'instance de l'attaque choisie
                attack = random.choice(available_actions['attacks'])
                return ('attack', attack, False)
            else:
                return ('attack', Struggle(), False)  # Struggle

        elif action_type == 'switch':
            if available_actions['switches']:
                # Récupérer l'index dans l'équipe complète
                team_index = self.choose_switch_in(fight)
                return ('switch', team_index, None)
            else:
                # Fallback vers attaque si pas de switch possible
                return ('attack', Struggle(), False)

        elif action_type == 'terastallize':
            if available_actions['can_terastallize'] and available_actions['attacks']:
                attack = random.choice(available_actions['attacks'])
                return ('terastallize', attack, None)
            else:
                return ('attack', Struggle(), False)  # Struggle
        
        # Fallback de sécurité
        return ('attack', Struggle(), False)  # Struggle

    def choose_switch_in(self, fight):
        """
        Choisit le Pokémon à faire entrer lors d'un changement de pokémon.
        """
        available_pokemon = self.get_available_actions(fight)['switches']
        if not available_pokemon:
            return None
        else:
            # Choisir un Pokémon aléatoire parmi ceux disponibles
            switch_pokemon = random.choice(available_pokemon)
            pokemon_info = self.get_pokemon_info(fight)
            my_team = pokemon_info['my_team']
            poke_index_in_team = my_team.index(switch_pokemon)
            return poke_index_in_team

    """def get_available_actions(self, fight):
        
        Détermine les actions disponibles pour l'IA.
        
        Returns:
            dict: Actions disponibles
        
        # Déterminer quelle équipe et quel Pokémon actif
        if self.team_id == 1:
            active_pokemon = fight.active1
            team = fight.team1
            tera_used = getattr(fight, 'tera_used_team1', False)
        else:
            active_pokemon = fight.active2
            team = fight.team2
            tera_used = getattr(fight, 'tera_used_team2', False)

        possible_attacks = active_pokemon.get_usable_attacks()

        if active_pokemon.can_switch:
            switches = [p for p in team if p.current_hp > 0 and p != active_pokemon]

        # Actions disponibles
        if switches:
            available_actions = {
                'attacks': possible_attacks,
                'switches': switches,
                'can_terastallize': not tera_used and not active_pokemon.tera_activated
            }
        else:
                available_actions = {
                'attacks': possible_attacks,
                'can_terastallize': not tera_used and not active_pokemon.tera_activated
            }

        return available_actions"""


class PlayerAI(PokemonAI):
    """
    Classe pour permettre à un joueur humain de jouer contre une IA.
    Idéale pour l'apprentissage supervisé et le test d'IAs.
    """
    
    def __init__(self, team_id, player_name="Joueur Humain"):
        super().__init__(team_id, player_name)
        self.name = player_name
    
    def choose_action(self, fight, available_actions):
        """
        Affiche les options disponibles et demande au joueur de choisir.
        
        Args:
            fight: Instance de la classe Fight
            available_actions: Actions disponibles
        
        Returns:
            tuple: (action_type, action_data, extra_data)
        """
        from Materials.pokemon_attacks import Struggle
        # Assurer qu'on a bien les actions disponibles
        if available_actions is None:
            available_actions = self.get_available_actions(fight)
        
        print(f"\n{Colors.BOLD}{Colors.TEAM1 if self.team_id == 1 else Colors.TEAM2}=== TOUR DE {self.name.upper()} (Équipe {self.team_id}) ==={Colors.RESET}")
        
        # Afficher le Pokémon actuel
        current_pokemon = fight.active1 if self.team_id == 1 else fight.active2
        print(f"Pokémon actuel: {current_pokemon.name} (HP: {current_pokemon.current_hp}/{current_pokemon.max_hp})")
        
        while True:
            print(f"\n{Colors.BOLD}Choisissez une action:{Colors.RESET}")
            print("1. Attaquer")
            print("2. Changer de Pokémon")
            if available_actions['can_terastallize'] and available_actions['attacks']:
                print("3. Téracristaliser et attaquer")
            
            try:
                choice = input("Votre choix (1-3): ").strip()
                
                if choice == "1":
                    # Attaquer
                    if not available_actions['attacks']:
                        print("Aucune attaque disponible! Utilisation de Struggle...")
                        return ('attack', Struggle(), False)
                    
                    return self._choose_attack(available_actions['attacks'])
                
                elif choice == "2":
                    # Changer de Pokémon
                    if not available_actions['switches']:
                        print("Aucun Pokémon disponible pour le changement!")
                        continue
                    
                    return self._choose_switch(available_actions['switches'], fight)
                
                elif choice == "3":
                    # Téracristaliser
                    if not available_actions['can_terastallize']:
                        print("Téracristalisation déjà utilisée!")
                        continue
                    if not available_actions['attacks']:
                        print("Aucune attaque disponible pour téracristaliser!")
                        continue
                    
                    return self._choose_terastallize(available_actions['attacks'])
                
                else:
                    print("Choix invalide! Veuillez entrer 1, 2 ou 3.")
                    
            except (ValueError, KeyboardInterrupt):
                print("Saisie invalide ou interruption. Veuillez réessayer.")
    
    def _choose_attack(self, attacks):
        """Permet au joueur de choisir une attaque."""
        print(f"\n{Colors.BOLD}Attaques disponibles:{Colors.RESET}")
        for i, attack in enumerate(attacks):
            pp_info = f"(PP: {attack.current_pp}/{attack.max_pp})" if hasattr(attack, 'current_pp') else ""
            print(f"{i+1}. {attack.name} - {attack.type} - Puissance: {attack.base_power} {pp_info}")
        
        while True:
            try:
                attack_choice = input(f"Choisissez une attaque (1-{len(attacks)}): ").strip()
                attack_index = int(attack_choice) - 1
                
                if 0 <= attack_index < len(attacks):
                    return ('attack', attacks[attack_index], False)
                else:
                    print(f"Veuillez choisir un nombre entre 1 et {len(attacks)}.")
                    
            except ValueError:
                print("Veuillez entrer un nombre valide.")
    
    def _choose_switch(self, available_switches, fight):
        """Permet au joueur de choisir un Pokémon pour le changement."""
        print(f"\n{Colors.BOLD}Pokémon disponibles pour le changement:{Colors.RESET}")
        
        # Récupérer l'équipe complète pour les indices
        team = fight.team1 if self.team_id == 1 else fight.team2
        
        for i, pokemon in enumerate(available_switches):
            team_index = team.index(pokemon)
            status_text = f" - {pokemon.status}" if pokemon.status != "normal" else ""
            print(f"{i+1}. {pokemon.name} (HP: {pokemon.current_hp}/{pokemon.max_hp}{status_text}) [Index équipe: {team_index}]")
        
        while True:
            try:
                switch_choice = input(f"Choisissez un Pokémon (1-{len(available_switches)}): ").strip()
                switch_index = int(switch_choice) - 1
                
                if 0 <= switch_index < len(available_switches):
                    # Récupérer l'index dans l'équipe complète
                    chosen_pokemon = available_switches[switch_index]
                    team_index = team.index(chosen_pokemon)
                    return ('switch', team_index, None)
                else:
                    print(f"Veuillez choisir un nombre entre 1 et {len(available_switches)}.")
                    
            except ValueError:
                print("Veuillez entrer un nombre valide.")
    
    def _choose_terastallize(self, attacks):
        """Permet au joueur de choisir une attaque avec téracristalisation."""
        print(f"\n{Colors.BOLD}Téracristalisation + Attaque:{Colors.RESET}")
        print("Choisissez l'attaque à utiliser avec la téracristalisation:")
        
        for i, attack in enumerate(attacks):
            pp_info = f"(PP: {attack.current_pp}/{attack.max_pp})" if hasattr(attack, 'current_pp') else ""
            print(f"{i+1}. {attack.name} - {attack.type} - Puissance: {attack.power} {pp_info}")
        
        while True:
            try:
                attack_choice = input(f"Choisissez une attaque (1-{len(attacks)}): ").strip()
                attack_index = int(attack_choice) - 1
                
                if 0 <= attack_index < len(attacks):
                    return ('terastallize', attack_index, None)
                else:
                    print(f"Veuillez choisir un nombre entre 1 et {len(attacks)}.")
                    
            except ValueError:
                print("Veuillez entrer un nombre valide.")

class LowHeuristicAI(PokemonAI):
    """
    Simplified AI: Chooses actions based only on type effectiveness.
    """
    def __init__(self, team_id):
        super().__init__(team_id, "Simple Heuristic AI")

    def choose_action(self, fight, available_actions):
        from Materials.pokemon_attacks import Struggle

        if available_actions is None:
            available_actions = self.get_available_actions(fight)

        info = self.get_pokemon_info(fight)
        my_poke = info['my_pokemon']
        enemy = info['enemy_pokemon']

        attacks = available_actions['attacks'] if available_actions['attacks'] else []
        switches = available_actions['switches'] if available_actions['switches'] else []

        # Évaluer l'avantage des types des deux Pokémon
        type_advantage = evaluate_type_efficiency(my_poke, enemy)
        if PRINTING_METHOD:
            print("Évaluation des types :", type_advantage)

        # Si le Pokémon est paralysé ou brûlé, prioriser le switch sauf si il a pu beaucoup de vie.
        if my_poke.status in ["paralyzed", "burned"] and switches and my_poke.current_hp > my_poke.max_hp * 0.4:
            best_switch = self._choose_switch(switches, enemy)
            if best_switch:
                team = fight.team1 if self.team_id == 1 else fight.team2
                best_switch_id = team.index(best_switch)
                return ('switch', best_switch_id, None)

        # Si désavantage de type, prioriser le switch
        if type_advantage < 1:
            if switches:
                best_switch = self._choose_switch(switches, enemy)
                if best_switch:
                    team = fight.team1 if self.team_id == 1 else fight.team2
                    best_switch_id = team.index(best_switch)
                    return ('switch', best_switch_id, None)

        # Si avantage de type ou pas de switch possible, évaluer les attaques
        best_attack = self._choose_attack(attacks, enemy, my_poke)

        # Si aucune attaque offensive efficace, prioriser les attaques de statut
        if not best_attack:
            status_moves = [atk for atk in attacks if atk.category == "Status"]
            if status_moves:
                return ('attack', random.choice(status_moves), False)

        # Si une attaque efficace est trouvée, l'utiliser
        if best_attack:
            # Vérifier si l'attaque a une priorité élevée pour terminer un adversaire faible
            if hasattr(best_attack, 'priority') and best_attack.priority > 0 and enemy.current_hp < best_attack.power:
                return ('attack', best_attack, False)
            return ('attack', best_attack, False)

        # Si aucune option viable, utiliser Struggle
        return ('attack', Struggle, False)

    def _choose_attack(self, attacks, enemy, my_poke):
        """
        Choisit la meilleure attaque en fonction de l'efficacité des types, des talents, des objets et des priorités.
        """
        best_move = None
        highest_score = -1
        for attack in attacks:
            score = 1.0
            move_type = getattr(attack, 'type', None)
            if attack.category != "Status":
                if move_type:
                    # Évaluer l'efficacité des types
                    type_eff = evaluate_type_efficiency(
                        type('Tmp', (), {'original_types': [move_type], 'types': [move_type], 'tera_activated': False})(),
                        enemy
                    )
                    
                # Ajuster le score en fonction des talents de l'ennemi
                if hasattr(enemy, 'talent') and enemy.talent == "Levitate" and move_type == "Ground":
                    type_eff = 0  # L'attaque de type Sol est inefficace

                # Pondérer par la puissance de l'attaque et la priorité
                score = type_eff * attack.power
                if hasattr(attack, 'priority') and attack.priority > 0 and enemy.current_hp < enemy.max_hp * 0.2:
                    score *= 1.2  # Bonus pour les attaques à priorité élevée

                # Ajuster le score en fonction des objets de l'IA
                if hasattr(self, 'item') and self.item == "Choice Band" and attack.category == "Physical":
                    score *= 1.5  # Bonus de puissance pour les attaques physiques
                elif hasattr(self, 'item') and self.item == "Choice Specs" and attack.category == "Special":
                    score *= 1.5  # Bonus de puissance pour les attaques spéciales

                if score > highest_score:
                    highest_score = score
                    best_move = attack
            else:
                if "heal" in attack.flags and my_poke.current_hp < my_poke.max_hp * 0.5:
                    score *= 300  # Bonus de puissance pour les attaques de soin

        return best_move

    def _choose_switch(self, switches, enemy):
        """
        Choisit le Pokémon à faire entrer lors d'un changement de Pokémon, en tenant compte des talents, objets et PV restants.
        """
        best_switch = None
        best_switch_score = float('inf')
        for switch in switches:
            switch_score = evaluate_type_efficiency(switch, enemy)
            if switch_score == 0:
                return switch
            # Prendre en compte les PV restants pour éviter d'envoyer un Pokémon faible
            adjusted_score = switch_score / (switch.current_hp / switch.max_hp)
            if adjusted_score < best_switch_score:
                best_switch_score = adjusted_score
                best_switch = switch

        return best_switch
    
    def choose_switch_in(self, fight):
        """
        Choisit le Pokémon à faire entrer lors d'un changement de pokémon.
        """
        team_id = self.team_id
        team = fight.team1 if team_id == 1 else fight.team2
        if team_id == 1:
            active_pokemon, enemy = fight.active1, fight.active2
        else:
            active_pokemon, enemy = fight.active2, fight.active1

        switches = [p for p in team if p.current_hp > 0 and p != active_pokemon]
        if not switches or switches == []:
            return None
        else:
            best_switch = self._choose_switch(switches, enemy)
            if best_switch:
                team = fight.team1 if self.team_id == 1 else fight.team2
                idx = team.index(best_switch)
            else:
                idx = team.index(switches[0])  # Si aucun switch optimal, prendre le premier disponible
        return idx
    

class HighHeuristicAI(PokemonAI):
    """
    IA avec heuristiques avancées, prenant en compte les changements de type, les talents et les objets.
    """
    def __init__(self, team_id):
        super().__init__(team_id, "High Heuristic AI")

    def choose_action(self, fight, available_actions):
        return
    
    def score_actions(self, fight, attack):
        if self.team_id == 1:
            my_poke = fight.active1
            enemy = fight.active2
            team = fight.team1
        else:
            my_poke = fight.active2
            enemy = fight.active1
            team = fight.team2
        
        def tera_score(poke, attack, enemy):
            """
            Donne un score pour évaluer l'activation de la téracristallisation.

            :return: score (int)
            """
            score = 0
            if attack.type in poke.original_types:
                score -= 100  # Pénalité si l'attaque est du type original
            type_eff = evaluate_type_efficiency(poke, enemy)
            score += type_eff * 80  # Bonus pour l'efficacité du type après téracristallisation
            return score
        
        def score_attacks(my_poke, enemy, fight):  
            """
            Donne un score pour chaque attaque disponible sous forme de dico. 
            
            :return: dico {nom_attaque: score}
            """ 
            available_attacks = possible_attacks(my_poke)
            score = {atk.name: 0 for atk in available_attacks if atk != None}
            for i,atk in zip(range(4), available_attacks):
                if atk != None:
                    from damage_calc import damage_calc
                    damages, chances_of_ko, _, _ = damage_calc(my_poke, enemy, atk, fight)
                    percentages = damages / enemy.max_hp
                    if chances_of_ko > 0.99:
                        score[i] += 1000 # Très haute priorité pour les attaques qui peuvent KO
                    else:
                        score[i] += percentages * 70
            return score

        def score_team_attacks(fight, team):
            """
            Associe à une team un dico de score des attaques pour chaque pokémon.

            :return: dico {poke: {nom_attaque: score}}
            """
            score_team = {poke : None for poke in team if poke.current_hp > 0}
            for poke in team:
                if poke.current_hp > 0:
                    score_team[poke] = score_attacks(fight, poke)
            return score_team    

        def score_poke_on_terrain(fight, poke, score_attack_team):
            """
            Donne un score au pokémon actuel en fonction de plusieurs critères.

            :return: dico {poke: score}
            """

            score = 0
            if poke.current_hp > 0:
                type_eff = evaluate_type_efficiency(poke, enemy)
                score += (1/type_eff) * 100
            if fight.leech_seeded_by == enemy:
                score -= 50
            if poke.status in ["poisoned", "badly_poisoned"]:
                score -= 20
                if poke.status == "badly_poisoned":
                    if poke.toxic_counter and poke.toxic_counter > 1:
                        score -= 10 * poke.toxic_counter
            if poke.stats["Speed"] > enemy.stats["Speed"]:
                score += 20
            else:
                score -= 10

            score_atk = score_attack_team[poke] if score_attack_team[poke] != None else {}

            ## Ajouter le score max des attaques
            score += max(score_atk.values())

            return score   

        def score_switch_in(fight, team, scores_attack_team, enemy):
            score_switch = {poke : 0 for poke in team if poke.current_hp > 0}
            rest_team = [p for p in team if p != my_poke and p.current_hp > 0]
            stat_attack = enemy.stats[category]
            for poke in rest_team:
                if poke.current_hp > 0:
                    if simulate_hazards(fight, fight.hazards_team1 if self.team_id == 1 else fight.hazards_team2, poke) >= poke.current_hp:
                        score_switch[poke] -= 200

                    type_eff = evaluate_type_efficiency(poke, enemy)

                    if poke.status in ["poisoned", "badly_poisoned"]:
                        score_switch[poke] -= 40
                    if scores_attack_team[poke] != None:
                        score_switch[poke] += max(scores_attack_team[poke].values())

                    hazards = fight.hazards_team1 if self.team_id == 1 else fight.hazards_team2
                    if (hazards["Toxic Spikes"] > 0 and poke.status is not None) or hazards["Sticky Web"]:
                        score_switch[poke] -= 50

                    category = "Attack" if enemy.stats["Attack"] > enemy.stats["Special Attack"] else "Special Attack"
                    stat_defense = enemy.stats["Defense" if category == "Attack" else "Special Defense"]
                    if stat_defense > 1.2*stat_attack and type_eff <= 1:
                        score_switch[poke] += 100
                    else:
                        score_switch[poke] -= 150


        def simulate_hazards(fight, hazards, poke):
            damages = 0
            if poke.item != "Heavy-Duty Boots":
                if hazards["Spikes"] > 0 and "Flying" not in poke.types and poke.talent != "Levitate":
                    tier = {1 : 0.125, 2 : 0.1666666667, 3 : 0.25} 
                    damages += int(poke.max_hp * tier[hazards["Spikes"]])
                if hazards["Stealth Rock"]:
                    rock_damage = int(poke.max_hp * 0.125)  # 1/8 des PV max
                    type_eff = get_type_efficiency("Rock", poke)
                    damages += int(rock_damage * type_eff)
            return damages

        scores_attack_team = score_team_attacks(fight, team)
        score_switch = score_switch_in(fight, team, scores_attack_team, enemy)
        score_pokemon_on_terrain = score_poke_on_terrain(fight, my_poke, scores_attack_team)

        score_max, best_poke = 0, None
        best_attack = None
        best_switch_id = None

        for p, s in score_switch.items():
            if s > score_max:
                score_max = s
                best_poke = p
        
        for p, s in scores_attack_team[my_poke].items():
            if p == best_poke:
                s_m = max(scores_attack_team[my_poke].values())
                for atk, sc in scores_attack_team[my_poke].items():
                    if sc == s_m:
                        best_attack = atk
        
        for p, s in score_switch.items():
            if p == best_poke:
                best_switch_id = team.index(p)
        
        if score_pokemon_on_terrain >= score_max:
            return ('attack', best_attack, False)
        else:
            return ('switch', best_switch_id, None)


    def simulate_attack(fight, poke, attack, enemy):
        from Materials.pokemon_attacks import SimulationAttack
        from damage_calc import damage_calc
        fake_attack = SimulationAttack(attack).copy()

        available_attacks = possible_attacks(poke)
        infos_atks = {}
        for attack in available_attacks:
            if attack != None and attack.category != "Status":
                fake_attack.category = "Physical" if attack.category == "Physical" else "Special"
                type = getattr(attack, 'type', None)
                fake_attack.type = type if type != None else "Normal"
                damages, chances_of_ko, _, _ = damage_calc(poke, enemy, fake_attack, fight)
                percentages = damages / enemy.max_hp
                infos_atks[attack] = (damages, chances_of_ko, percentages)
        return infos_atks
                








