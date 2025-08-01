"""
Interface IA pour les combats Pokémon
"""

from abc import ABC, abstractmethod
import random
from typing import List, Tuple, Optional
from ai_game_state import GameStateExtractor, encode_action, decode_action

class PokemonAI(ABC):
    """Classe abstraite pour les IA Pokémon"""
    
    def __init__(self, team_id: int):
        self.team_id = team_id
        self.game_state_extractor = GameStateExtractor()
    
    @abstractmethod
    def choose_action(self, fight, available_actions: List[str]) -> Tuple[str, int, Optional[str]]:
        """
        Choisit une action à effectuer
        
        Returns:
            Tuple (action_type, action_index, tera_type)
            - action_type: "attack", "switch", "tera"
            - action_index: index de l'attaque ou du Pokémon
            - tera_type: type de téracristalisation si applicable
        """
        pass
    
    @abstractmethod
    def choose_switch_pokemon(self, fight, available_pokemon: List[int]) -> int:
        """Choisit un Pokémon de remplacement (switchs forcés)"""
        pass

class RandomAI(PokemonAI):
    """IA qui joue aléatoirement - baseline pour comparaison"""
    
    def choose_action(self, fight, available_actions: List[str]) -> Tuple[str, int, Optional[str]]:
        action_type = random.choice(available_actions)
        
        if action_type == "attack":
            # Choisir une attaque disponible
            active = fight.active1 if self.team_id == 1 else fight.active2
            attacks = [active.attack1, active.attack2, active.attack3, active.attack4]
            valid_attacks = [i for i, atk in enumerate(attacks) if atk is not None]
            action_index = random.choice(valid_attacks) if valid_attacks else 0
            return ("attack", action_index, None)
            
        elif action_type == "switch":
            # Choisir un Pokémon de remplacement
            team = fight.team1 if self.team_id == 1 else fight.team2
            active = fight.active1 if self.team_id == 1 else fight.active2
            available = [i for i, p in enumerate(team) if p.current_hp > 0 and p != active]
            action_index = random.choice(available) if available else 0
            return ("switch", action_index, None)
            
        elif action_type == "tera":
            # Téracristalisation aléatoire
            active = fight.active1 if self.team_id == 1 else fight.active2
            return ("tera", 0, active.tera_type)
            
        return ("attack", 0, None)
    
    def choose_switch_pokemon(self, fight, available_pokemon: List[int]) -> int:
        return random.choice(available_pokemon) if available_pokemon else 0

class NeuralNetworkAI(PokemonAI):
    """IA basée sur un réseau de neurones"""
    
    def __init__(self, team_id: int, model=None):
        super().__init__(team_id)
        self.model = model  # Modèle de réseau de neurones
        self.epsilon = 0.1  # Pour l'exploration durant l'entraînement
        self.training = False
    
    def choose_action(self, fight, available_actions: List[str]) -> Tuple[str, int, Optional[str]]:
        if self.model is None:
            # Fallback vers IA aléatoire si pas de modèle
            return RandomAI(self.team_id).choose_action(fight, available_actions)
        
        # Extraire l'état du jeu
        game_state = self.game_state_extractor.extract_full_game_state(fight, self.team_id)
        
        # Exploration aléatoire durant l'entraînement
        if self.training and random.random() < self.epsilon:
            return RandomAI(self.team_id).choose_action(fight, available_actions)
        
        # Prédiction du modèle
        try:
            action_probs = self.model.predict(game_state.reshape(1, -1))[0]
            action_int = action_probs.argmax()
            action_type, action_index = decode_action(action_int)
            
            # Valider que l'action est possible
            if action_type in available_actions:
                if action_type == "attack":
                    active = fight.active1 if self.team_id == 1 else fight.active2
                    attacks = [active.attack1, active.attack2, active.attack3, active.attack4]
                    if action_index < len(attacks) and attacks[action_index] is not None:
                        return (action_type, action_index, None)
                
                elif action_type == "switch":
                    team = fight.team1 if self.team_id == 1 else fight.team2
                    active = fight.active1 if self.team_id == 1 else fight.active2
                    if (action_index < len(team) and 
                        team[action_index].current_hp > 0 and 
                        team[action_index] != active):
                        return (action_type, action_index, None)
                
                elif action_type == "tera":
                    active = fight.active1 if self.team_id == 1 else fight.active2
                    tera_used = (fight.tera_used_team1 if self.team_id == 1 
                               else fight.tera_used_team2)
                    if not tera_used and not active.tera_activated:
                        return (action_type, 0, active.tera_type)
            
            # Action invalide, fallback vers aléatoire
            return RandomAI(self.team_id).choose_action(fight, available_actions)
            
        except Exception as e:
            print(f"Erreur dans l'IA : {e}")
            return RandomAI(self.team_id).choose_action(fight, available_actions)
    
    def choose_switch_pokemon(self, fight, available_pokemon: List[int]) -> int:
        if self.model is None or not available_pokemon:
            return RandomAI(self.team_id).choose_switch_pokemon(fight, available_pokemon)
        
        # Pour les switchs forcés, utiliser une logique simplifiée
        # (peut être étendu avec un modèle séparé)
        game_state = self.game_state_extractor.extract_full_game_state(fight, self.team_id)
        
        try:
            # Utiliser le modèle pour évaluer les Pokémon disponibles
            best_choice = available_pokemon[0]
            best_score = -float('inf')
            
            for pokemon_idx in available_pokemon:
                # Simuler le switch et évaluer
                # (logique simplifiée - peut être améliorée)
                team = fight.team1 if self.team_id == 1 else fight.team2
                pokemon = team[pokemon_idx]
                
                # Score basé sur les HP et matchup de types
                hp_ratio = pokemon.current_hp / pokemon.max_hp
                score = hp_ratio * 100  # Score de base
                
                # Bonus/malus selon le matchup (simplifiée)
                opponent = fight.active2 if self.team_id == 1 else fight.active1
                # ... logique de matchup ...
                
                if score > best_score:
                    best_score = score
                    best_choice = pokemon_idx
            
            return best_choice
            
        except Exception as e:
            print(f"Erreur dans le choix de switch : {e}")
            return RandomAI(self.team_id).choose_switch_pokemon(fight, available_pokemon)
    
    def set_training_mode(self, training: bool):
        """Active/désactive le mode entraînement"""
        self.training = training
    
    def set_epsilon(self, epsilon: float):
        """Définit le taux d'exploration"""
        self.epsilon = epsilon

class HeuristicAI(PokemonAI):
    """IA basée sur des heuristiques - bon baseline pour l'entraînement"""
    
    def choose_action(self, fight, available_actions: List[str]) -> Tuple[str, int, Optional[str]]:
        active = fight.active1 if self.team_id == 1 else fight.active2
        opponent = fight.active2 if self.team_id == 1 else fight.active1
        
        # Logique de switch si en mauvaise posture
        if "switch" in available_actions and active.current_hp < active.max_hp * 0.2:
            team = fight.team1 if self.team_id == 1 else fight.team2
            available_pokemon = [i for i, p in enumerate(team) if p.current_hp > 0 and p != active]
            if available_pokemon:
                return ("switch", available_pokemon[0], None)
        
        # Téracristalisation si avantageux
        if "tera" in available_actions:
            tera_used = fight.tera_used_team1 if self.team_id == 1 else fight.tera_used_team2
            if not tera_used and not active.tera_activated:
                # Logique simple : téracristalliser si avantage de type
                return ("tera", 0, active.tera_type)
        
        # Choisir la meilleure attaque
        if "attack" in available_actions:
            attacks = [active.attack1, active.attack2, active.attack3, active.attack4]
            best_attack = 0
            best_damage = 0
            
            for i, attack in enumerate(attacks):
                if attack is not None:
                    # Calcul approximatif des dégâts
                    damage = self._estimate_damage(active, attack, opponent, fight)
                    if damage > best_damage:
                        best_damage = damage
                        best_attack = i
            
            return ("attack", best_attack, None)
        
        return ("attack", 0, None)
    
    def choose_switch_pokemon(self, fight, available_pokemon: List[int]) -> int:
        if not available_pokemon:
            return 0
        
        # Choisir le Pokémon avec le plus de HP
        team = fight.team1 if self.team_id == 1 else fight.team2
        best_pokemon = available_pokemon[0]
        best_hp_ratio = 0
        
        for pokemon_idx in available_pokemon:
            pokemon = team[pokemon_idx]
            hp_ratio = pokemon.current_hp / pokemon.max_hp
            if hp_ratio > best_hp_ratio:
                best_hp_ratio = hp_ratio
                best_pokemon = pokemon_idx
        
        return best_pokemon
    
    def _estimate_damage(self, attacker, attack, defender, fight):
        """Estimation approximative des dégâts pour l'heuristique"""
        if attack.category == "Status":
            return 0
        
        # Calcul très simplifié
        base_power = attack.base_power if attack.base_power else 0
        attack_stat = (attacker.stats["Attack"] if attack.category == "Physical" 
                      else attacker.stats["Sp. Atk"])
        defense_stat = (defender.stats["Defense"] if attack.category == "Physical" 
                       else defender.stats["Sp. Def"])
        
        # Efficacité des types (simplifiée)
        type_eff = 1.0  # Calcul complet nécessiterait d'importer le module
        
        # STAB
        stab = 1.5 if attack.type in attacker.types else 1.0
        
        damage = (base_power * attack_stat / defense_stat) * type_eff * stab
        return damage
