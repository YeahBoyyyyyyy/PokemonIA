"""
Module d'intégration de l'IA avec le système de combat existant
"""

from fight import Fight
from pokemon_ai import PokemonAI, RandomAI, HeuristicAI, NeuralNetworkAI
from battle_interface import can_use_attack, can_terastallize
import random

class AIBattleManager:
    """Gestionnaire de combat avec IA"""
    
    def __init__(self, team1, team2, ai1: PokemonAI = None, ai2: PokemonAI = None):
        self.fight = Fight(team1, team2)
        self.ai1 = ai1 or RandomAI(1)
        self.ai2 = ai2 or RandomAI(2)
        
        # Surcharger les méthodes de choix du Fight
        self.fight.player_choice_switch = self._ai_choice_switch
    
    def _ai_choice_switch(self, team_id):
        """Gère les changements forcés avec l'IA"""
        ai = self.ai1 if team_id == 1 else self.ai2
        team = self.fight.team1 if team_id == 1 else self.fight.team2
        current_active = self.fight.active1 if team_id == 1 else self.fight.active2
        
        available_pokemon = [i for i, p in enumerate(team) if p.current_hp > 0 and p != current_active]
        
        if available_pokemon:
            choice = ai.choose_switch_pokemon(self.fight, available_pokemon)
            self.fight.player_switch(team_id, choice)
    
    def get_available_actions(self, team_id) -> list:
        """Retourne les actions disponibles pour une équipe"""
        actions = []
        
        active = self.fight.active1 if team_id == 1 else self.fight.active2
        team = self.fight.team1 if team_id == 1 else self.fight.team2
        
        # Vérifier si on peut attaquer
        attacks = [active.attack1, active.attack2, active.attack3, active.attack4]
        valid_attacks = [atk for atk in attacks if atk is not None]
        if valid_attacks:
            actions.append("attack")
        
        # Vérifier si on peut changer de Pokémon
        available_pokemon = [p for p in team if p.current_hp > 0 and p != active]
        if available_pokemon:
            actions.append("switch")
        
        # Vérifier si on peut téracristalliser
        can_tera, _ = can_terastallize(active, self.fight, team_id)
        if can_tera:
            actions.append("tera")
        
        return actions
    
    def execute_ai_action(self, team_id):
        """Exécute une action choisie par l'IA"""
        ai = self.ai1 if team_id == 1 else self.ai2
        available_actions = self.get_available_actions(team_id)
        
        if not available_actions:
            return None
        
        action_type, action_index, tera_type = ai.choose_action(self.fight, available_actions)
        
        active = self.fight.active1 if team_id == 1 else self.fight.active2
        
        if action_type == "attack":
            attacks = [active.attack1, active.attack2, active.attack3, active.attack4]
            if 0 <= action_index < len(attacks) and attacks[action_index] is not None:
                attack = attacks[action_index]
                can_use, reason = can_use_attack(active, attack)
                if can_use:
                    return ("attack", attack, None)
                else:
                    print(f"Impossible d'utiliser {attack.name}: {reason}")
                    # Fallback vers première attaque disponible
                    for atk in attacks:
                        if atk and can_use_attack(active, atk)[0]:
                            return ("attack", atk, None)
        
        elif action_type == "switch":
            team = self.fight.team1 if team_id == 1 else self.fight.team2
            if (0 <= action_index < len(team) and 
                team[action_index].current_hp > 0 and 
                team[action_index] != active):
                return ("switch", action_index, None)
        
        elif action_type == "tera":
            can_tera, reason = can_terastallize(active, self.fight, team_id)
            if can_tera:
                return ("tera", tera_type or active.tera_type, None)
            else:
                print(f"Impossible de téracristalliser: {reason}")
        
        # Action par défaut si échec
        attacks = [active.attack1, active.attack2, active.attack3, active.attack4]
        for atk in attacks:
            if atk and can_use_attack(active, atk)[0]:
                return ("attack", atk, None)
        
        return None
    
    def run_ai_battle(self, max_turns=100, verbose=True):
        """Lance un combat entièrement géré par IA"""
        turn = 0
        
        while turn < max_turns and not self.fight.check_battle_end():
            turn += 1
            
            if verbose:
                print(f"\n{'='*50}")
                print(f"TOUR {turn}")
                print(f"{'='*50}")
                self.fight.print_fight_status()
            
            # Actions des deux IA
            action1 = self.execute_ai_action(1)
            action2 = self.execute_ai_action(2)
            
            if verbose:
                print(f"\nActions choisies:")
                print(f"IA 1: {action1}")
                print(f"IA 2: {action2}")
            
            # Résoudre le tour
            if action1 and action2:
                self.fight.resolve_turn(action1, action2)
            
            # Gestion de fin de tour
            self.fight.manage_temporary_status(self.fight.active1)
            self.fight.manage_temporary_status(self.fight.active2)
            
            # Effets de fin de tour
            self.fight.apply_weather_effects()
            self.fight.apply_status_damage(self.fight.active1)
            self.fight.apply_status_damage(self.fight.active2)
            
            self.fight.weather_update()
            self.fight.field_update()
            self.fight.screen_update()
            self.fight.tailwind_update()
            
            # Vérifier les KO et changements forcés
            if self.fight.active1.current_hp <= 0:
                if not self.fight.is_team_defeated(self.fight.team1):
                    self._ai_choice_switch(1)
            
            if self.fight.active2.current_hp <= 0:
                if not self.fight.is_team_defeated(self.fight.team2):
                    self._ai_choice_switch(2)
            
            if verbose:
                print(f"\nFin du tour {turn}")
        
        # Résultat final
        if self.fight.check_battle_end():
            if verbose:
                print(f"\nCombat terminé après {turn} tours!")
        else:
            if verbose:
                print(f"\nCombat interrompu après {max_turns} tours (limite atteinte)")
        
        return self.get_battle_result()
    
    def get_battle_result(self):
        """Retourne le résultat du combat"""
        if self.fight.is_team_defeated(self.fight.team1):
            return {"winner": 2, "loser": 1}
        elif self.fight.is_team_defeated(self.fight.team2):
            return {"winner": 1, "loser": 2}
        else:
            return {"winner": None, "loser": None}  # Match nul/inachevé

# Fonctions utilitaires pour l'entraînement

def create_training_data(num_battles=1000, ai1_type="random", ai2_type="heuristic"):
    """Génère des données d'entraînement en faisant combattre des IA"""
    from start_fight import create_competitive_team, create_french_team
    
    training_data = []
    
    for i in range(num_battles):
        # Créer les équipes
        team1 = create_competitive_team()
        team2 = create_french_team()
        
        # Créer les IA
        if ai1_type == "random":
            ai1 = RandomAI(1)
        elif ai1_type == "heuristic":
            ai1 = HeuristicAI(1)
        else:
            ai1 = RandomAI(1)
        
        if ai2_type == "random":
            ai2 = RandomAI(2)
        elif ai2_type == "heuristic":
            ai2 = HeuristicAI(2)
        else:
            ai2 = RandomAI(2)
        
        # Lancer le combat
        battle_manager = AIBattleManager(team1, team2, ai1, ai2)
        result = battle_manager.run_ai_battle(verbose=False)
        
        # Extraire les données d'entraînement
        # (États de jeu et actions prises pendant le combat)
        # Cette partie devrait être développée pour sauvegarder
        # les états et actions pendant le combat
        
        if i % 100 == 0:
            print(f"Combat {i}/{num_battles} terminé")
    
    return training_data

def evaluate_ai_performance(ai1, ai2, num_battles=100):
    """Évalue les performances d'une IA contre une autre"""
    from start_fight import create_competitive_team, create_french_team
    
    wins_ai1 = 0
    wins_ai2 = 0
    draws = 0
    
    for i in range(num_battles):
        team1 = create_competitive_team()
        team2 = create_french_team()
        
        battle_manager = AIBattleManager(team1, team2, ai1, ai2)
        result = battle_manager.run_ai_battle(verbose=False)
        
        if result["winner"] == 1:
            wins_ai1 += 1
        elif result["winner"] == 2:
            wins_ai2 += 1
        else:
            draws += 1
    
    return {
        "ai1_winrate": wins_ai1 / num_battles,
        "ai2_winrate": wins_ai2 / num_battles,
        "draw_rate": draws / num_battles,
        "total_battles": num_battles
    }
