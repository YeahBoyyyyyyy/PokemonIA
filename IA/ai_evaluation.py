"""
Système d'évaluation pour mesurer les performances de l'IA Pokémon
"""

from ai_battle_manager import AIBattleManager, evaluate_ai_performance
from pokemon_ai import RandomAI, HeuristicAI, NeuralNetworkAI
from start_fight import create_competitive_team, create_french_team
import random
import time
import json

class AIEvaluator:
    """Classe pour évaluer les performances d'une IA Pokémon"""
    
    def __init__(self, ai_to_test, team_generator_func=None):
        self.ai_to_test = ai_to_test
        self.team_generator = team_generator_func or create_competitive_team
        self.results = {}
    
    def evaluate_vs_random_ai(self, num_battles=100, verbose=False):
        """
        Test 1: IA vs Random AI
        Objectif: >80% de winrate
        """
        print(f"\n🎲 Test 1: {self.ai_to_test.__class__.__name__} vs Random AI")
        print(f"Objectif: >80% de winrate")
        print("="*50)
        
        wins = 0
        total_turns = 0
        
        for i in range(num_battles):
            # Créer les équipes
            team1 = self.team_generator()
            team2 = self.team_generator()
            
            # Alterner qui joue en premier
            if i % 2 == 0:
                ai1 = self.ai_to_test
                ai2 = RandomAI(2)
                our_team = 1
            else:
                ai1 = RandomAI(1)
                ai2 = self.ai_to_test
                our_team = 2
            
            # Lancer le combat
            battle_manager = AIBattleManager(team1, team2, ai1, ai2)
            result = battle_manager.run_ai_battle(max_turns=50, verbose=False)
            
            # Compter les victoires
            if result["winner"] == our_team:
                wins += 1
            
            total_turns += battle_manager.fight.turn
            
            if verbose and (i + 1) % 20 == 0:
                current_winrate = (wins / (i + 1)) * 100
                print(f"  Combats {i+1}/{num_battles}: {current_winrate:.1f}% de victoires")
        
        winrate = (wins / num_battles) * 100
        avg_turns = total_turns / num_battles
        
        result = {
            "opponent": "Random AI",
            "battles": num_battles,
            "wins": wins,
            "winrate": winrate,
            "avg_turns_per_battle": avg_turns,
            "status": "✅ RÉUSSI" if winrate >= 80 else "❌ ÉCHEC",
            "target": 80.0
        }
        
        self.results["vs_random"] = result
        self._print_test_result(result)
        return result
    
    def evaluate_vs_heuristic_ai(self, num_battles=100, verbose=False):
        """
        Test 2: IA vs Heuristic AI
        Objectif: >60% de winrate
        """
        print(f"\n🧠 Test 2: {self.ai_to_test.__class__.__name__} vs Heuristic AI")
        print(f"Objectif: >60% de winrate")
        print("="*50)
        
        wins = 0
        total_turns = 0
        total_damage_dealt = 0
        total_damage_received = 0
        
        for i in range(num_battles):
            # Créer les équipes
            team1 = self.team_generator()
            team2 = self.team_generator()
            
            # Alterner qui joue en premier
            if i % 2 == 0:
                ai1 = self.ai_to_test
                ai2 = HeuristicAI(2)
                our_team = 1
            else:
                ai1 = HeuristicAI(1)
                ai2 = self.ai_to_test
                our_team = 2
            
            # Lancer le combat
            battle_manager = AIBattleManager(team1, team2, ai1, ai2)
            result = battle_manager.run_ai_battle(max_turns=50, verbose=False)
            
            # Compter les victoires
            if result["winner"] == our_team:
                wins += 1
            
            total_turns += battle_manager.fight.turn
            
            # Calculer les dégâts moyens (approximation)
            our_team_obj = battle_manager.fight.team1 if our_team == 1 else battle_manager.fight.team2
            enemy_team_obj = battle_manager.fight.team2 if our_team == 1 else battle_manager.fight.team1
            
            our_remaining_hp = sum(p.current_hp for p in our_team_obj)
            enemy_remaining_hp = sum(p.current_hp for p in enemy_team_obj)
            our_max_hp = sum(p.max_hp for p in our_team_obj)
            enemy_max_hp = sum(p.max_hp for p in enemy_team_obj)
            
            total_damage_dealt += (enemy_max_hp - enemy_remaining_hp)
            total_damage_received += (our_max_hp - our_remaining_hp)
            
            if verbose and (i + 1) % 20 == 0:
                current_winrate = (wins / (i + 1)) * 100
                print(f"  Combats {i+1}/{num_battles}: {current_winrate:.1f}% de victoires")
        
        winrate = (wins / num_battles) * 100
        avg_turns = total_turns / num_battles
        avg_damage_per_turn = (total_damage_dealt / total_turns) if total_turns > 0 else 0
        
        result = {
            "opponent": "Heuristic AI",
            "battles": num_battles,
            "wins": wins,
            "winrate": winrate,
            "avg_turns_per_battle": avg_turns,
            "avg_damage_per_turn": avg_damage_per_turn,
            "status": "✅ RÉUSSI" if winrate >= 60 else "❌ ÉCHEC",
            "target": 60.0
        }
        
        self.results["vs_heuristic"] = result
        self._print_test_result(result)
        return result
    
    def evaluate_generalization(self, num_battles=50, verbose=False):
        """
        Test 3: Test de généralisation sur équipes non vues
        Objectif: >50% de winrate
        """
        print(f"\n🔍 Test 3: Test de généralisation")
        print(f"Objectif: >50% de winrate sur équipes non vues")
        print("="*50)
        
        wins = 0
        pokemon_usage = {}
        switch_count = 0
        tera_usage_count = 0
        total_actions = 0
        
        for i in range(num_battles):
            # Générer des équipes complètement aléatoires
            team1 = self._generate_unseen_team()
            team2 = self._generate_unseen_team()
            
            # Alterner qui joue en premier
            if i % 2 == 0:
                ai1 = self.ai_to_test
                ai2 = HeuristicAI(2)  # Opponent constant
                our_team = 1
            else:
                ai1 = HeuristicAI(1)
                ai2 = self.ai_to_test
                our_team = 2
            
            # Tracker les actions (nécessiterait modification du battle_manager)
            battle_manager = AIBattleManager(team1, team2, ai1, ai2)
            result = battle_manager.run_ai_battle(max_turns=50, verbose=False)
            
            if result["winner"] == our_team:
                wins += 1
            
            # Tracker l'usage des Pokémon
            our_team_obj = battle_manager.fight.team1 if our_team == 1 else battle_manager.fight.team2
            for pokemon in our_team_obj:
                if pokemon.name not in pokemon_usage:
                    pokemon_usage[pokemon.name] = 0
                if pokemon.current_hp < pokemon.max_hp:  # A participé au combat
                    pokemon_usage[pokemon.name] += 1
            
            if verbose and (i + 1) % 10 == 0:
                current_winrate = (wins / (i + 1)) * 100
                print(f"  Combats {i+1}/{num_battles}: {current_winrate:.1f}% de victoires")
        
        winrate = (wins / num_battles) * 100
        diversity_score = len(pokemon_usage) / 6  # Nombre de Pokémon différents utilisés
        
        result = {
            "opponent": "Mixed (équipes non vues)",
            "battles": num_battles,
            "wins": wins,
            "winrate": winrate,
            "pokemon_diversity": diversity_score,
            "different_pokemon_used": len(pokemon_usage),
            "status": "✅ RÉUSSI" if winrate >= 50 else "❌ ÉCHEC",
            "target": 50.0
        }
        
        self.results["generalization"] = result
        self._print_test_result(result)
        return result
    
    def _generate_unseen_team(self):
        """Génère une équipe avec des Pokémon et configurations non vues"""
        from pokemon_datas import pokemon_data
        from start_fight import import_pokemon
        
        # Pool de Pokémon moins communs
        uncommon_pokemon = [
            "Alakazam", "Machamp", "Golem", "Gengar", "Lapras", "Snorlax",
            "Mewtwo", "Typhlosion", "Feraligatr", "Meganium", "Crobat",
            "Ampharos", "Umbreon", "Espeon", "Forretress", "Skarmory",
            "Blaziken", "Swampert", "Sceptile", "Gardevoir", "Slaking",
            "Aggron", "Metagross", "Salamence", "Garchomp", "Lucario"
        ]
        
        team = []
        available_pokemon = [name for name in uncommon_pokemon if name in pokemon_data]
        
        if len(available_pokemon) < 6:
            # Fallback vers des Pokémon plus communs si nécessaire
            available_pokemon.extend(["Charizard", "Blastoise", "Venusaur", "Pikachu"])
        
        selected = random.sample(available_pokemon, min(6, len(available_pokemon)))
        
        for poke_name in selected:
            pokemon = import_pokemon(poke_name)
            
            # Configuration très aléatoire
            all_natures = ["Hardy", "Lonely", "Adamant", "Naughty", "Brave",
                          "Bold", "Docile", "Impish", "Lax", "Relaxed",
                          "Modest", "Mild", "Bashful", "Rash", "Quiet",
                          "Calm", "Gentle", "Careful", "Quirky", "Sassy",
                          "Timid", "Hasty", "Jolly", "Naive", "Serious"]
            
            pokemon.nature = random.choice(all_natures)
            
            # EVs complètement aléatoires
            remaining_evs = 508
            for stat in pokemon.evs:
                if remaining_evs <= 0:
                    break
                max_for_stat = min(252, remaining_evs)
                pokemon.evs[stat] = random.randint(0, max_for_stat)
                remaining_evs -= pokemon.evs[stat]
            
            # Objet aléatoire
            random_items = ["Leftovers", "Life Orb", "Choice Band", "Choice Specs", 
                           "Choice Scarf", "Focus Sash", "Assault Vest"]
            pokemon.item = random.choice(random_items)
            
            # Type Tera aléatoire
            all_types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice",
                        "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug",
                        "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]
            pokemon.tera_type = random.choice(all_types)
            
            pokemon.recalculate_all_stats()
            team.append(pokemon)
        
        return team
    
    def _print_test_result(self, result):
        """Affiche les résultats d'un test de manière formatée"""
        print(f"Résultats vs {result['opponent']}:")
        print(f"  Victoires: {result['wins']}/{result['battles']}")
        print(f"  Winrate: {result['winrate']:.1f}% (objectif: {result['target']}%)")
        print(f"  Status: {result['status']}")
        
        if 'avg_turns_per_battle' in result:
            print(f"  Durée moyenne: {result['avg_turns_per_battle']:.1f} tours/combat")
        
        if 'avg_damage_per_turn' in result:
            print(f"  Dégâts/tour: {result['avg_damage_per_turn']:.0f}")
        
        if 'pokemon_diversity' in result:
            print(f"  Diversité Pokémon: {result['different_pokemon_used']} différents utilisés")
        
        print()
    
    def run_full_evaluation(self, quick_test=False):
        """Lance une évaluation complète de l'IA"""
        print(f"\n🚀 ÉVALUATION COMPLÈTE DE L'IA")
        print(f"IA testée: {self.ai_to_test.__class__.__name__}")
        print("="*60)
        
        num_battles = 20 if quick_test else 100
        
        start_time = time.time()
        
        # Test 1: vs Random AI
        self.evaluate_vs_random_ai(num_battles, verbose=not quick_test)
        
        # Test 2: vs Heuristic AI
        self.evaluate_vs_heuristic_ai(num_battles, verbose=not quick_test)
        
        # Test 3: Généralisation
        generalization_battles = 10 if quick_test else 50
        self.evaluate_generalization(generalization_battles, verbose=not quick_test)
        
        end_time = time.time()
        
        # Résumé final
        self._print_final_summary(end_time - start_time, quick_test)
        
        return self.results
    
    def _print_final_summary(self, elapsed_time, quick_test):
        """Affiche un résumé final des performances"""
        print("\n📊 RÉSUMÉ FINAL")
        print("="*40)
        
        total_tests = len(self.results)
        passed_tests = sum(1 for r in self.results.values() if "✅" in r["status"])
        
        print(f"Tests réussis: {passed_tests}/{total_tests}")
        print(f"Temps d'évaluation: {elapsed_time:.1f}s")
        
        if quick_test:
            print("⚡ Évaluation rapide - Pour des résultats précis, relancez sans quick_test=True")
        
        # Évaluation globale
        if passed_tests == total_tests:
            print("🏆 EXCELLENT: Votre IA est prête pour l'entraînement avancé !")
        elif passed_tests >= 2:
            print("✅ BIEN: Votre IA fonctionne correctement")
        elif passed_tests >= 1:
            print("⚠️  MOYEN: Votre IA a besoin d'améliorations")
        else:
            print("❌ PROBLÈME: Votre IA nécessite des corrections majeures")
        
        print("\nDétails par test:")
        for test_name, result in self.results.items():
            print(f"  {test_name}: {result['winrate']:.1f}% {result['status']}")

# Fonctions utilitaires pour tester rapidement

def quick_ai_test(ai_instance):
    """Test rapide d'une IA (20 combats par test)"""
    evaluator = AIEvaluator(ai_instance)
    return evaluator.run_full_evaluation(quick_test=True)

def full_ai_evaluation(ai_instance):
    """Évaluation complète d'une IA (100+ combats)"""
    evaluator = AIEvaluator(ai_instance)
    return evaluator.run_full_evaluation(quick_test=False)

def compare_ai_performance(ai1, ai2, num_battles=50):
    """Compare directement deux IA"""
    print(f"\n⚔️  COMPARAISON DIRECTE")
    print(f"{ai1.__class__.__name__} vs {ai2.__class__.__name__}")
    print("="*50)
    
    results = evaluate_ai_performance(ai1, ai2, num_battles)
    
    print(f"Résultats sur {num_battles} combats:")
    print(f"  {ai1.__class__.__name__}: {results['ai1_winrate']:.1%} de victoires")
    print(f"  {ai2.__class__.__name__}: {results['ai2_winrate']:.1%} de victoires")
    print(f"  Matchs nuls: {results['draw_rate']:.1%}")
    
    if results['ai1_winrate'] > results['ai2_winrate']:
        print(f"🏆 Gagnant: {ai1.__class__.__name__}")
    elif results['ai2_winrate'] > results['ai1_winrate']:
        print(f"🏆 Gagnant: {ai2.__class__.__name__}")
    else:
        print("🤝 Égalité parfaite !")
    
    return results

# Exemple d'utilisation
if __name__ == "__main__":
    # Test de l'IA heuristique de base
    print("Test de l'IA Heuristique de base...")
    heuristic_ai = HeuristicAI(1)
    results = quick_ai_test(heuristic_ai)
    
    # Comparaison directe Heuristique vs Random
    print("\nComparaison Heuristique vs Random...")
    compare_ai_performance(HeuristicAI(1), RandomAI(2), 30)
