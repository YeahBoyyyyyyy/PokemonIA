"""
Stratégie d'entraînement optimale pour l'IA Pokémon
Combinaison intelligente de différents types de données
"""

from ai_battle_manager import AIBattleManager, create_training_data
from pokemon_ai import RandomAI, HeuristicAI
import random
import json

class TrainingDataGenerator:
    """Générateur de données d'entraînement avec stratégie multi-sources"""
    
    def __init__(self, official_teams_file=None):
        self.official_teams = []
        if official_teams_file:
            self.load_official_teams(official_teams_file)
    
    def load_official_teams(self, file_path):
        """Charge les 150 équipes officielles OU Gen 9"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                self.official_teams = json.load(f)
            print(f"Chargé {len(self.official_teams)} équipes officielles")
        except FileNotFoundError:
            print(f"Fichier {file_path} non trouvé")
    
    def generate_random_competitive_team(self):
        """Génère une équipe aléatoire mais avec contraintes compétitives"""
        from pokemon_datas import pokemon_data
        from start_fight import import_pokemon
        import pokemon_attacks as ATTACKS
        
        # Liste des Pokémon viables (tiers OU, UU, RU minimum)
        viable_pokemon = [
            "Dragonite", "Iron Valiant", "Gholdengo", "Gliscor", "Weavile",
            "Slowking-Galar", "Moltres", "Primarina", "Landorus-Therian",
            "Garchomp", "Kingambit", "Great Tusk", "Iron Treads", "Zamazenta",
            "Ogerpon-Wellspring", "Raging Bolt", "Iron Crown", "Gouging Fire",
            "Walking Wake", "Iron Boulder", "Roaring Moon", "Iron Hands",
            "Annihilape", "Chi-Yu", "Chien-Pao", "Ting-Lu", "Wo-Chien",
            "Corviknight", "Toxapex", "Ferrothorn", "Heatran", "Rotom-Wash",
            "Clefable", "Garganacl", "Dondozo", "Clodsire", "Skeledirge",
            "Meowscarada", "Quaquaval", "Tinkaton", "Brambleghast", "Lokix"
        ]
        
        team = []
        selected_pokemon = random.sample(viable_pokemon, 6)
        
        for poke_name in selected_pokemon:
            if poke_name in pokemon_data:
                pokemon = import_pokemon(poke_name)
                
                # Configuration aléatoire mais réaliste
                self._configure_random_pokemon(pokemon)
                team.append(pokemon)
        
        return team
    
    def _configure_random_pokemon(self, pokemon):
        """Configure un Pokémon avec des choix aléatoires mais viables"""
        import pokemon_attacks as ATTACKS
        
        # Natures viables selon le rôle
        physical_natures = ["Adamant", "Jolly", "Impish", "Careful"]
        special_natures = ["Modest", "Timid", "Bold", "Calm"]
        mixed_natures = ["Hasty", "Naive", "Mild", "Rash"]
        
        # Choix de nature basé sur les stats de base
        if pokemon.base_stats["Attack"] > pokemon.base_stats["Sp. Atk"]:
            pokemon.nature = random.choice(physical_natures)
        else:
            pokemon.nature = random.choice(special_natures)
        
        # Distribution d'EVs réaliste
        self._assign_realistic_evs(pokemon)
        
        # Choix d'objet
        viable_items = [
            "Leftovers", "Life Orb", "Choice Band", "Choice Specs", "Choice Scarf",
            "Heavy-Duty Boots", "Assault Vest", "Rocky Helmet", "Focus Sash",
            "Sitrus Berry", "Booster Energy"
        ]
        pokemon.item = random.choice(viable_items)
        
        # Type Tera aléatoire mais pertinent
        all_types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", 
                    "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug",
                    "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]
        pokemon.tera_type = random.choice(all_types)
        
        # Attaques (placeholder - à adapter selon vos attaques disponibles)
        available_attacks = [
            ATTACKS.Flamethrower(), ATTACKS.HydroPump(), ATTACKS.Thunderbolt(),
            ATTACKS.IceBeam(), ATTACKS.Earthquake(), ATTACKS.StoneEdge(),
            ATTACKS.CloseCombat(), ATTACKS.Psychic(), ATTACKS.ShadowBall(),
            ATTACKS.DragonPulse(), ATTACKS.Protect(), ATTACKS.Substitute(),
            ATTACKS.SwordsDance(), ATTACKS.NastyPlot(), ATTACKS.Recover()
        ]
        
        selected_attacks = random.sample(available_attacks, 4)
        pokemon.attack1, pokemon.attack2, pokemon.attack3, pokemon.attack4 = selected_attacks
        
        pokemon.recalculate_all_stats()
    
    def _assign_realistic_evs(self, pokemon):
        """Assigne des EVs de manière réaliste selon le rôle du Pokémon"""
        total_evs = 508  # Maximum autorisé
        
        # Stratégies d'EV courantes
        strategies = [
            # Sweeper physique
            {"HP": 4, "Attack": 252, "Speed": 252},
            # Sweeper spécial  
            {"HP": 4, "Sp. Atk": 252, "Speed": 252},
            # Tank physique
            {"HP": 252, "Attack": 4, "Defense": 252},
            # Tank spécial
            {"HP": 252, "Defense": 4, "Sp. Def": 252},
            # Bulk offensif
            {"HP": 240, "Attack": 252, "Defense": 16},
            # Mixte rapide
            {"HP": 80, "Attack": 176, "Speed": 252}
        ]
        
        strategy = random.choice(strategies)
        
        # Réinitialiser les EVs
        for stat in pokemon.evs:
            pokemon.evs[stat] = strategy.get(stat, 0)
    
    def generate_training_dataset(self, 
                                num_battles_official=1000,
                                num_battles_random=2000, 
                                num_battles_mixed=500):
        """
        Génère un dataset d'entraînement équilibré
        
        :param num_battles_official: Combats entre équipes officielles
        :param num_battles_random: Combats entre équipes aléatoires
        :param num_battles_mixed: Combats équipes officielles vs aléatoires
        """
        all_training_data = []
        
        print("🏆 Phase 1: Combats entre équipes officielles...")
        # Phase 1: Équipes officielles vs équipes officielles
        for i in range(num_battles_official):
            if len(self.official_teams) >= 2:
                team1 = random.choice(self.official_teams)
                team2 = random.choice(self.official_teams)
                
                # S'assurer que ce ne sont pas les mêmes équipes
                while team1 == team2:
                    team2 = random.choice(self.official_teams)
                
                battle_data = self._simulate_battle(team1, team2, "official_vs_official")
                all_training_data.extend(battle_data)
            
            if i % 100 == 0:
                print(f"  Combats officiels: {i}/{num_battles_official}")
        
        print("🎲 Phase 2: Combats entre équipes aléatoires...")
        # Phase 2: Équipes aléatoires vs équipes aléatoires
        for i in range(num_battles_random):
            team1 = self.generate_random_competitive_team()
            team2 = self.generate_random_competitive_team()
            
            battle_data = self._simulate_battle(team1, team2, "random_vs_random")
            all_training_data.extend(battle_data)
            
            if i % 200 == 0:
                print(f"  Combats aléatoires: {i}/{num_battles_random}")
        
        print("🔄 Phase 3: Combats mixtes...")
        # Phase 3: Équipes officielles vs équipes aléatoires
        for i in range(num_battles_mixed):
            if self.official_teams:
                team1 = random.choice(self.official_teams)
                team2 = self.generate_random_competitive_team()
                
                # Alterner qui joue en premier
                if random.random() < 0.5:
                    team1, team2 = team2, team1
                
                battle_data = self._simulate_battle(team1, team2, "mixed")
                all_training_data.extend(battle_data)
            
            if i % 50 == 0:
                print(f"  Combats mixtes: {i}/{num_battles_mixed}")
        
        print(f"✅ Dataset généré: {len(all_training_data)} échantillons d'entraînement")
        return all_training_data
    
    def _simulate_battle(self, team1, team2, battle_type):
        """Simule un combat et extrait les données d'entraînement"""
        from ai_game_state import GameStateExtractor
        
        # Utiliser différentes IA selon le type de combat
        if battle_type == "official_vs_official":
            ai1 = HeuristicAI(1)  # IA plus forte pour équipes officielles
            ai2 = HeuristicAI(2)
        elif battle_type == "random_vs_random":
            ai1 = RandomAI(1)     # IA plus faible pour équipes aléatoires
            ai2 = RandomAI(2)
        else:  # mixed
            ai1 = HeuristicAI(1)  # Équipe officielle
            ai2 = RandomAI(2)     # Équipe aléatoire
        
        battle_manager = AIBattleManager(team1, team2, ai1, ai2)
        state_extractor = GameStateExtractor()
        
        training_samples = []
        turn = 0
        max_turns = 50  # Éviter les combats infinis
        
        while turn < max_turns and not battle_manager.fight.check_battle_end():
            turn += 1
            
            # Extraire l'état pour les deux équipes
            for team_perspective in [1, 2]:
                try:
                    game_state = state_extractor.extract_full_game_state(
                        battle_manager.fight, team_perspective
                    )
                    
                    # Obtenir l'action choisie par l'IA
                    ai = ai1 if team_perspective == 1 else ai2
                    available_actions = battle_manager.get_available_actions(team_perspective)
                    
                    if available_actions:
                        action_type, action_index, tera_type = ai.choose_action(
                            battle_manager.fight, available_actions
                        )
                        
                        # Encoder l'action
                        from ai_game_state import encode_action
                        action_encoded = encode_action(action_type, action_index, tera_type)
                        
                        # Créer l'échantillon d'entraînement
                        training_sample = {
                            "state": game_state.tolist(),
                            "action": action_encoded,
                            "action_type": action_type,
                            "available_actions": available_actions,
                            "turn": turn,
                            "team_perspective": team_perspective,
                            "battle_type": battle_type
                        }
                        
                        training_samples.append(training_sample)
                
                except Exception as e:
                    print(f"Erreur lors de l'extraction d'état: {e}")
                    continue
            
            # Exécuter le tour
            try:
                action1 = battle_manager.execute_ai_action(1)
                action2 = battle_manager.execute_ai_action(2)
                
                if action1 and action2:
                    battle_manager.fight.resolve_turn(action1, action2)
                
            except Exception as e:
                print(f"Erreur lors de l'exécution du tour: {e}")
                break
        
        # Ajouter l'information de résultat final à tous les échantillons
        result = battle_manager.get_battle_result()
        for sample in training_samples:
            sample["final_result"] = result
            sample["total_turns"] = turn
        
        return training_samples

def create_balanced_training_strategy():
    """
    Stratégie d'entraînement recommandée en phases progressives
    """
    return {
        "phase_1_foundation": {
            "description": "Base solide avec équipes officielles",
            "official_battles": 1500,
            "random_battles": 500,
            "mixed_battles": 200,
            "ai_opponents": ["heuristic", "random"],
            "objective": "Apprendre les bases du méta compétitif"
        },
        
        "phase_2_diversification": {
            "description": "Élargissement avec plus de variété",
            "official_battles": 1000,
            "random_battles": 2000,
            "mixed_battles": 1000,
            "ai_opponents": ["heuristic", "random", "neural_baseline"],
            "objective": "Améliorer la robustesse et généralisation"
        },
        
        "phase_3_refinement": {
            "description": "Affinement avec auto-jeu",
            "self_play_battles": 3000,
            "official_battles": 500,
            "mixed_battles": 500,
            "ai_opponents": ["neural_current", "neural_previous", "heuristic"],
            "objective": "Auto-amélioration et découverte de nouvelles stratégies"
        },
        
        "phase_4_specialization": {
            "description": "Spécialisation sur des archétypes",
            "archetype_focused_battles": 2000,
            "tournament_simulation": 500,
            "ai_opponents": ["neural_specialist", "human_replays"],
            "objective": "Maîtrise avancée et adaptation méta"
        }
    }

# Exemple d'utilisation
if __name__ == "__main__":
    # Initialiser le générateur
    generator = TrainingDataGenerator("official_teams_ou_gen9.json")
    
    # Générer le dataset initial (Phase 1)
    training_data = generator.generate_training_dataset(
        num_battles_official=500,  # Commencer plus petit pour tester
        num_battles_random=1000,
        num_battles_mixed=200
    )
    
    # Sauvegarder les données
    with open("pokemon_training_data_phase1.json", "w") as f:
        json.dump(training_data, f, indent=2)
    
    print(f"✅ Données d'entraînement sauvegardées: {len(training_data)} échantillons")
    
    # Afficher les statistiques
    battle_types = {}
    for sample in training_data:
        bt = sample["battle_type"]
        battle_types[bt] = battle_types.get(bt, 0) + 1
    
    print("\n📊 Répartition des types de combat:")
    for battle_type, count in battle_types.items():
        percentage = (count / len(training_data)) * 100
        print(f"  {battle_type}: {count} échantillons ({percentage:.1f}%)")
