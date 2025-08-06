import random
from abc import ABC, abstractmethod
from utilities import *
from colors_utils import Colors

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
        
        # Actions disponibles
        available_actions = {
            'attacks': [atk for atk in active_pokemon.get_usable_attacks()],
            'switches': [p for p in team if p.current_hp > 0 and p != active_pokemon],
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
    
class PLAYERAI(PokemonAI):
    """Joueur Humain qui rentre ses actions manuellement comme dans battle_interface.py"""

    def choose_action(self, fight, available_actions):
        return 

class RandomAI(PokemonAI):
    """IA Pokémon qui choisit des actions aléatoires"""
    
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
        if available_actions['switches']:
            possible_actions.append('switch')
        
        # Téracristaliser (si possible ET si on a des attaques)
        if available_actions['can_terastallize'] and available_actions['attacks']:
            possible_actions.append('terastallize')
        
        # Si aucune action possible, forcer l'attaque (Struggle)
        if not possible_actions:
            return ('attack', Struggle, False)

        # Choisir aléatoirement avec pondération
        if len(possible_actions) == 1:
            action_type = possible_actions[0]
        else:
            # Pondération : 80% attaque, 15% switch, 5% tera
            weights = []
            for action in possible_actions:
                if action == 'attack':
                    weights.append(0.8)
                elif action == 'switch':
                    weights.append(0.15)
                elif action == 'terastallize':
                    weights.append(0.05)
            
            action_type = random.choices(possible_actions, weights=weights)[0]
        
        # Exécuter l'action choisie
        if action_type == 'attack':
            if available_actions['attacks']:
                # Récuperer l'instance de l'attaque choisie
                attack = random.choice(available_actions['attacks'])
                return ('attack', attack, False)
            else:
                return ('attack', Struggle, False)  # Struggle

        elif action_type == 'switch':
            if available_actions['switches']:
                # Récupérer l'index dans l'équipe complète
                team_index = self.choose_switch_in(fight)
                return ('switch', team_index, None)
            else:
                # Fallback vers attaque si pas de switch possible
                return ('attack', Struggle, False)

        elif action_type == 'terastallize':
            if available_actions['can_terastallize'] and available_actions['attacks']:
                attack = random.choice(available_actions['attacks'])
                return ('terastallize', attack, None)
            else:
                return ('attack', Struggle, False)  # Struggle
        
        # Fallback de sécurité
        return ('attack', Struggle, False)  # Struggle

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

        # Actions disponibles
        available_actions = {
            'attacks': possible_attacks,
            'switches': [p for p in team if p.current_hp > 0 and p != active_pokemon],
            'can_terastallize': not tera_used and not active_pokemon.tera_activated
        }

        return available_actions


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
                        return ('attack', Struggle, False)
                    
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

class HeuristicAI(PokemonAI):
    def __init__(self, team_id, aggression_level=0.7):
        super().__init__(team_id, "Heuristic AI")
        self.aggression_level = aggression_level  # 0-1, influence attaque vs switch
    
    def choose_action(self, fight, available_actions):
        # 1. Évaluer la situation actuelle
        # 2. Calculer les scores pour chaque action
        # 3. Choisir la meilleure action
        return

    def evaluate_attack_damage(self, my_attack, enemy_pokemon):
        # Estimer les dégâts approximatifs
        return
    
    def calculate_type_advantage(self, my_pokemon, enemy_pokemon):
        # Calculer l'avantage/désavantage de type
        return
        
    def assess_hp_danger(self, pokemon):
        # Évaluer si HP en danger (critique/moyen/safe)
        return
        
    def find_best_switch(self, available_switches, enemy_pokemon):
        # Trouver le meilleur switch selon les matchups
        return