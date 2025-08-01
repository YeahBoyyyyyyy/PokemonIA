"""
Module pour l'extraction de l'état du jeu pour l'IA
"""

import numpy as np
from fight import Fight
from pokemon import pokemon
from donnees import POKEMON_TYPES_ID, WEATHER, TERRAIN

class GameStateExtractor:
    """Classe pour extraire l'état du jeu sous forme vectorielle pour l'IA"""
    
    def __init__(self):
        self.type_encoding = POKEMON_TYPES_ID
        self.weather_encoding = {w: i for i, w in enumerate(WEATHER)}
        self.terrain_encoding = {t: i for i, t in enumerate(TERRAIN)}
        
    def extract_pokemon_state(self, pokemon: pokemon) -> np.ndarray:
        """Extrait l'état d'un Pokémon sous forme de vecteur"""
        state = []
        
        # Stats actuelles (6 valeurs normalisées)
        stats = [
            pokemon.current_hp / pokemon.max_hp,  # HP ratio
            pokemon.stats["Attack"] / 400,  # Normalisé sur base ~400 max
            pokemon.stats["Defense"] / 400,
            pokemon.stats["Sp. Atk"] / 400,
            pokemon.stats["Sp. Def"] / 400,
            pokemon.stats["Speed"] / 400
        ]
        state.extend(stats)
        
        # Modificateurs de stats (5 valeurs entre -6 et +6, normalisées)
        modifiers = [mod / 6.0 for mod in pokemon.stats_modifier]
        state.extend(modifiers)
        
        # Types encodés en one-hot (18 types possibles)
        type_vector = [0] * 18
        for ptype in pokemon.types:
            type_vector[self.type_encoding[ptype]] = 1
        state.extend(type_vector)
        
        # Téracristalisation
        tera_vector = [0] * 19  # 18 types + non activé
        if pokemon.tera_activated:
            tera_vector[self.type_encoding[pokemon.tera_type]] = 1
        else:
            tera_vector[18] = 1  # Non activé
        state.extend(tera_vector)
        
        # Statut (6 statuts possibles + aucun)
        status_vector = [0] * 7
        status_map = {
            None: 0, "burn": 1, "freeze": 2, "paralysis": 3,
            "poison": 4, "badly_poisoned": 5, "sleep": 6
        }
        status_vector[status_map.get(pokemon.status, 0)] = 1
        state.extend(status_vector)
        
        # Attaques disponibles (4 slots)
        attacks_vector = []
        for i in range(4):
            attack = getattr(pokemon, f"attack{i+1}", None)
            if attack:
                # Encodage de l'attaque : [type, catégorie, puissance, précision]
                attacks_vector.extend([
                    self.type_encoding[attack.type] / 18,  # Type normalisé
                    {"Physical": 0, "Special": 1, "Status": 2}[attack.category] / 2,
                    (attack.base_power if attack.base_power else 0) / 250,  # Puissance normalisée
                    attack.accuracy / 100 if isinstance(attack.accuracy, (int, float)) else 1.0
                ])
            else:
                attacks_vector.extend([0, 0, 0, 0])  # Pas d'attaque
        state.extend(attacks_vector)
        
        return np.array(state, dtype=np.float32)
    
    def extract_field_state(self, fight: Fight) -> np.ndarray:
        """Extrait l'état du terrain de combat"""
        state = []
        
        # Météo (encodage one-hot)
        weather_vector = [0] * len(WEATHER)
        if fight.weather["current"]:
            weather_vector[self.weather_encoding[fight.weather["current"]]] = 1
        else:
            weather_vector[self.weather_encoding["None"]] = 1
        state.extend(weather_vector)
        
        # Tours de météo restants (normalisé)
        weather_turns = (fight.weather_turn_left / 8.0) if fight.weather_turn_left else 0
        state.append(weather_turns)
        
        # Terrain (encodage one-hot)
        terrain_vector = [0] * len(TERRAIN)
        if fight.field:
            terrain_vector[self.terrain_encoding[fight.field]] = 1
        else:
            terrain_vector[self.terrain_encoding["None"]] = 1
        state.extend(terrain_vector)
        
        # Tours de terrain restants (normalisé)
        field_turns = (fight.field_turn_left / 8.0) if fight.field_turn_left else 0
        state.append(field_turns)
        
        # Hazards équipe 1
        hazards1 = [
            fight.hazards_team1["Spikes"] / 3,  # Max 3 couches
            fight.hazards_team1["Toxic Spikes"] / 2,  # Max 2 couches
            int(fight.hazards_team1["Stealth Rock"]),
            int(fight.hazards_team1["Sticky Web"])
        ]
        state.extend(hazards1)
        
        # Hazards équipe 2
        hazards2 = [
            fight.hazards_team2["Spikes"] / 3,
            fight.hazards_team2["Toxic Spikes"] / 2,
            int(fight.hazards_team2["Stealth Rock"]),
            int(fight.hazards_team2["Sticky Web"])
        ]
        state.extend(hazards2)
        
        # Écrans de protection (normalisé sur 8 tours max)
        screens1 = [
            fight.screen_turn_left_team1.get("Reflect", 0) / 8,
            fight.screen_turn_left_team1.get("Light Screen", 0) / 8,
            fight.screen_turn_left_team1.get("Aurora Veil", 0) / 8
        ]
        state.extend(screens1)
        
        screens2 = [
            fight.screen_turn_left_team2.get("Reflect", 0) / 8,
            fight.screen_turn_left_team2.get("Light Screen", 0) / 8,
            fight.screen_turn_left_team2.get("Aurora Veil", 0) / 8
        ]
        state.extend(screens2)
        
        return np.array(state, dtype=np.float32)
    
    def extract_full_game_state(self, fight: Fight, team_perspective: int = 1) -> np.ndarray:
        """Extrait l'état complet du jeu du point de vue d'une équipe"""
        
        # Pokémon actifs
        my_active = fight.active1 if team_perspective == 1 else fight.active2
        opponent_active = fight.active2 if team_perspective == 1 else fight.active1
        
        my_state = self.extract_pokemon_state(my_active)
        opponent_state = self.extract_pokemon_state(opponent_active)
        
        # Équipes complètes (information partielle pour l'adversaire)
        my_team = fight.team1 if team_perspective == 1 else fight.team2
        opponent_team = fight.team2 if team_perspective == 1 else fight.team1
        
        # État de mon équipe (information complète)
        my_team_state = []
        for pokemon in my_team:
            if pokemon != my_active:  # Pas le Pokémon actuel
                my_team_state.append(self.extract_pokemon_state(pokemon))
        
        # État de l'équipe adverse (information limitée - seulement HP et types visibles)
        opponent_team_state = []
        for pokemon in opponent_team:
            if pokemon != opponent_active:
                # Information limitée : seulement ce qui est visible
                limited_state = [
                    pokemon.current_hp / pokemon.max_hp if pokemon.current_hp > 0 else 0,
                    # Types (visibles)
                    *([1 if ptype in pokemon.types else 0 for ptype in self.type_encoding.keys()]),
                    # Le reste est inconnu (rempli de 0)
                    *([0] * 50)  # Placeholder pour les autres informations
                ]
                opponent_team_state.append(np.array(limited_state, dtype=np.float32))
        
        # État du terrain
        field_state = self.extract_field_state(fight)
        
        # Informations générales
        general_info = [
            fight.turn / 100,  # Numéro de tour normalisé
            int(getattr(fight, 'tera_used_team1', False)) if team_perspective == 1 else int(getattr(fight, 'tera_used_team2', False)),
            int(getattr(fight, 'tera_used_team2', False)) if team_perspective == 1 else int(getattr(fight, 'tera_used_team1', False))
        ]
        
        # Concaténer tous les états
        full_state = np.concatenate([
            my_state,
            opponent_state,
            *my_team_state,
            *opponent_team_state,
            field_state,
            np.array(general_info, dtype=np.float32)
        ])
        
        return full_state

def get_action_space_size():
    """Retourne la taille de l'espace d'actions possibles"""
    # 4 attaques + 5 changements de Pokémon + téracristalisation = 10 actions maximum
    return 10

def encode_action(action_type: str, action_index: int = 0, tera_type: str = None) -> int:
    """Encode une action en entier pour l'IA"""
    if action_type == "attack":
        return action_index  # 0-3
    elif action_type == "switch":
        return 4 + action_index  # 4-8 (5 Pokémon de réserve max)
    elif action_type == "tera":
        return 9  # Action spéciale téracristalisation
    return 0

def decode_action(action_int: int) -> tuple:
    """Décode un entier d'action en action lisible"""
    if 0 <= action_int <= 3:
        return ("attack", action_int)
    elif 4 <= action_int <= 8:
        return ("switch", action_int - 4)
    elif action_int == 9:
        return ("tera", 0)
    return ("attack", 0)  # Action par défaut
