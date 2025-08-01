"""
Gestionnaire de PP pour le système de combat Pokémon.
Ce module fournit des utilitaires pour initialiser et gérer les PP des Pokémon.
"""

def initialize_pokemon_pp(pokemon):
    """
    Initialise les PP d'un Pokémon en fonction de ses attaques actuelles.
    
    :param pokemon: Le Pokémon dont on veut initialiser les PP
    """
    attacks = [pokemon.attack1, pokemon.attack2, pokemon.attack3, pokemon.attack4]
    
    for i, attack in enumerate(attacks, 1):
        if attack is not None:
            pokemon.set_attack(i, attack)
        else:
            # Réinitialiser les PP à 0 si pas d'attaque
            setattr(pokemon, f'pp{i}', 0)
            setattr(pokemon, f'max_pp{i}', 0)

def setup_team_pp(team):
    """
    Initialise les PP de tous les Pokémon d'une équipe.
    
    :param team: Liste des Pokémon de l'équipe
    """
    for pokemon in team:
        initialize_pokemon_pp(pokemon)

def restore_team_pp(team):
    """
    Restaure tous les PP de tous les Pokémon d'une équipe (Centre Pokémon).
    
    :param team: Liste des Pokémon de l'équipe
    """
    for pokemon in team:
        pokemon.restore_all_pp()

def display_pp_status(pokemon):
    """
    Affiche le statut des PP d'un Pokémon.
    
    :param pokemon: Le Pokémon dont on veut afficher les PP
    """
    print(f"\nStatut PP de {pokemon.name}:")
    attacks = [pokemon.attack1, pokemon.attack2, pokemon.attack3, pokemon.attack4]
    
    for i, attack in enumerate(attacks, 1):
        if attack is not None:
            current_pp = getattr(pokemon, f'pp{i}', 0)
            max_pp = getattr(pokemon, f'max_pp{i}', 0)
            status = "✓" if current_pp > 0 else "✗"
            print(f"  {status} {attack.name}: {current_pp}/{max_pp} PP")
        else:
            print(f"  - Slot {i}: Vide")
