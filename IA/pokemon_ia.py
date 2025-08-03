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
            - ("switch", pokemon_index, None)
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
    
    def choose_action(self, fight, available_actions):
        """
        Choisit une action aléatoire parmi les actions disponibles.
        
        Args:
            fight: Instance de la classe Fight
            available_actions: Actions disponibles
        
        Returns:
            tuple: (action_type, action_data, extra_data)
        """
        action_type = random.choices(['attack', 'switch', 'terastallize'], [0.85, 0.05, 0.10])[0]
        
        if action_type == 'attack':
            attack_index = random.randint(0, len(available_actions['attacks']) - 1)
            can_tera = available_actions['can_terastallize']
            return ('attack', attack_index, can_tera)

        elif action_type == 'switch':
            if available_actions['switches']:
                pokemon_index = random.randint(0, len(available_actions['switches']) - 1)
                return ('switch', pokemon_index, None)
            else:
                return None  # Pas de Pokémon à switcher
        
        elif action_type == 'terastallize':
            if available_actions['can_terastallize']:
                attack_index = random.randint(0, len(available_actions['attacks']) - 1)
                return ('terastallize', attack_index, None)
            else:
                return None  # Pas de possibilité de terastalliser

        print("il s''est rien passé")

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