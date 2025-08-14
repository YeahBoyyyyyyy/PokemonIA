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
    """IA heuristique: choisit l'action avec un score basé sur matchup, dégâts estimés, sécurité HP et opportunités Tera."""
    def __init__(self, team_id, aggression_level=0.65, switch_threshold=0.35, tera_aggression=0.15):
        super().__init__(team_id, "Heuristic AI")
        self.aggression_level = aggression_level  # Importance d'attaquer
        self.switch_threshold = switch_threshold  # En-dessous de ce score, on préfère switch
        self.tera_aggression = tera_aggression    # Bonus si Tera offensive possible
        self.turns = 0

    def choose_action(self, fight, available_actions):
        from Materials.pokemon_attacks import Struggle
        self.turns += 1
        if available_actions is None:
            available_actions = self.get_available_actions(fight)
        info = self.get_pokemon_info(fight)
        my_poke = info['my_pokemon']
        enemy = info['enemy_pokemon']

        attacks = available_actions['attacks'] if available_actions['attacks'] else []
        switches = available_actions['switches'] if available_actions['switches'] else []
        can_tera = available_actions['can_terastallize']

        # 1. Evaluer chaque attaque
        attack_choices = []
        for atk in attacks:
            atk_score, details = self._score_attack(my_poke, enemy, atk, tera=False)
            tera_score = None
            if can_tera:
                tera_score, tera_details = self._score_attack(my_poke, enemy, atk, tera=True)
            attack_choices.append({
                'attack': atk,
                'score': atk_score,
                'details': details,
                'tera_score': tera_score,
                'tera_details': tera_details if can_tera else None
            })

        # 2. Evaluer les switches
        switch_choices = []
        for sw in switches:
            sw_score, sw_details = self._score_switch(sw, enemy)
            switch_choices.append({'pokemon': sw, 'score': sw_score, 'details': sw_details})

        # 3. Décision
        best_attack = max(attack_choices, key=lambda x: x['score'], default=None)
        best_switch = max(switch_choices, key=lambda x: x['score'], default=None)

        # Décider si switch vaut mieux qu'attaquer
        choose_switch = False
        if best_switch and (not best_attack or best_switch['score'] > best_attack['score'] + (1 - self.aggression_level)):
            # Encourager switch si notre HP bas ou matchup mauvais
            hp_ratio = my_poke.current_hp / my_poke.max_hp
            my_matchup = evaluate_pokemon_type_efficiency(my_poke, enemy)
            if hp_ratio < 0.3 or my_matchup < 0.75 or best_switch['score'] - best_attack['score'] > 0.5:
                choose_switch = True

        if choose_switch:
            # Trouver l'index dans l'équipe
            team = fight.team1 if self.team_id == 1 else fight.team2
            idx = team.index(best_switch['pokemon'])
            return ('switch', idx, None)

        # Considérer Tera sur la meilleure attaque
        if best_attack and can_tera and best_attack['tera_score'] is not None:
            tera_gain = best_attack['tera_score'] - best_attack['score']
            # Conditions tactiques pour Tera
            enemy_threat = evaluate_pokemon_type_efficiency(enemy, my_poke)
            offensive_window = tera_gain > 0.35
            finishing = (enemy.current_hp / enemy.max_hp) < 0.35 and best_attack['tera_score'] > best_attack['score']
            survival_need = enemy_threat > 1.5 and my_poke.current_hp / my_poke.max_hp < 0.5
            late_game = self._count_alive(fight, self.team_id) <= 2 or self._count_alive(fight, 3 - self.team_id) <= 2
            if offensive_window and (finishing or late_game or survival_need):
                return ('terastallize', best_attack['attack'], None)

        # Attaque normale
        if best_attack:
            return ('attack', best_attack['attack'], False)

        # Fallback
        return ('attack', Struggle, False)

    def _score_attack(self, my_poke, enemy, attack, tera=False):
        # Base: puissance modifiée
        base_power = getattr(attack, 'base_power', getattr(attack, 'power', 50))
        # STAB (avec Tera si activée)
        stab = 1.0
        move_type = getattr(attack, 'type', None)
        if tera:
            # Simuler Tera sur le premier type actuel (après Tera probable)
            if move_type == my_poke.types[0]:
                stab += 0.5
        else:
            if move_type in my_poke.original_types:
                stab += 0.5
        # Efficacité de type (en utilisant pokemon vs enemy; approximation pour l'attaque)
        type_eff = 1.0
        if move_type and hasattr(enemy, 'original_types'):
            type_eff = 1.0
            # Simplifié: utiliser un poke factice pour calculer (si needed on pourrait créer un wrapper)
            # On approxime via ratio de my_poke vs enemy (déjà multi-typage)
            type_eff = evaluate_pokemon_type_efficiency(type('Tmp', (), {'original_types': [move_type], 'types': [move_type], 'tera_activated': False})(), enemy)
        # HP ratios
        enemy_hp_ratio = enemy.current_hp / enemy.max_hp if enemy.max_hp else 1
        my_hp_ratio = my_poke.current_hp / my_poke.max_hp if my_poke.max_hp else 1

        # Offensive scoring
        raw_damage_est = base_power * stab * type_eff
        normalized_damage = min(raw_damage_est / 120, 1.0)
        pressure = (1 - enemy_hp_ratio) * 0.2  # plus l'ennemi est bas, plus on valorise un finish

        # Sécurité: éviter de suicider si HP très bas
        safety_penalty = 0.0
        if my_hp_ratio < 0.25 and type_eff < 1:
            safety_penalty = 0.15

        score = normalized_damage + pressure - safety_penalty
        if tera:
            score += 0.1  # léger bonus pour opportunité Tera
        details = {
            'power': base_power,
            'stab': stab,
            'type_eff': type_eff,
            'normalized_damage': normalized_damage,
            'pressure': pressure,
            'safety_penalty': safety_penalty,
            'tera': tera
        }
        return score, details

    def _score_switch(self, candidate, enemy):
        # Matchup (types) : plus grand est mieux (notre offensive) et inverse (défense) => on combine
        offensive = evaluate_pokemon_type_efficiency(candidate, enemy)
        defensive = 1 / max(evaluate_pokemon_type_efficiency(enemy, candidate), 0.25)
        hp_ratio = candidate.current_hp / candidate.max_hp if candidate.max_hp else 1
        # Bonus pour HP plus élevé et meilleure défense
        score = (offensive * 0.4) + (defensive * 0.4) + (hp_ratio * 0.2)
        # Pénalité si status grave
        if getattr(candidate, 'status', 'normal') in ['poison', 'burn', 'sleep', 'paralysis']:
            score -= 0.1
        return score, {
            'offensive': offensive,
            'defensive': defensive,
            'hp_ratio': hp_ratio
        }

    def _count_alive(self, fight, team_id):
        team = fight.team1 if team_id == 1 else fight.team2
        return sum(1 for p in team if p.current_hp > 0)

"""
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
        efficiency = evaluate_pokemon_type_efficiency(my_pokemon, enemy_pokemon)
        
        return
        
    def assess_hp_danger(self, pokemon):
        # Évaluer si HP en danger (critique/moyen/safe)
        return
        
    def find_best_switch(self, available_switches, enemy_pokemon):
        # Trouver le meilleur switch selon les matchups
        return
"""