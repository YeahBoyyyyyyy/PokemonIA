import random
from abc import ABC, abstractmethod
from utilities import *

class PokemonAI(ABC):
    """Classe abstraite pour toutes les IA Pokémon"""
    
    def __init__(self, team_id, name="Generic AI"):
        self.team_id = team_id  # 1 ou 2
        self.name = name
        self.decisions_made = 0
        self.total_battles = 0
    
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
            - ("attack", attack_index, can_tera) 
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
            'attacks': active_pokemon.attacks,
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