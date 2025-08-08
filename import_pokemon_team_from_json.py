import fight
from pokemon import pokemon
import sys
sys.path.append("C:/Users/natha/OneDrive/Desktop/Travail/IA Combats pokémons/PokemonIA/Materials")
from Materials.pokedex_9G_complete import pokemon_data_gen9
from Materials.pokemon_attacks import attack_registry
sys.path.append("C:/Users/natha/OneDrive/Desktop/Travail/IA Combats pokémons/PokemonIA")
import json

def import_team_from_json(id):
    """
    Importe une équipe de Pokémon à partir d'un fichier JSON. Tout est initialisé, stats, tera et PP.
    """
    teamid = "team" + str(id)
    pokemon_team = []
    with open("OUteams.json", "r") as f:
        data = json.load(f)
        # Accéder au contenu et au premier élément qui contient les équipes
        team_data = data.get("content", [{}])[0].get(teamid, {})
    
    for i in range(1, 7):
        if str(i) in team_data:
            carac = team_data[str(i)]
            poke = import_pokemon_from_json(carac)
            pokemon_team.append(poke)

    # Initialiser les PP de l'équipe
    from pp_manager import setup_team_pp
    setup_team_pp(pokemon_team)
    return pokemon_team

def import_pokemon_from_json(carac : dict):
    """
    Importe un Pokémon à partir des caractéristiques fournies dans le dictionnaire issu du fichier JSON.

    :param carac: Dictionnaire contenant les caractéristiques du Pokémon
    :return: Instance de la classe pokemon avec les caractéristiques importées
    """
    raw_poke = pokemon_data_gen9[carac["name"]]
    poke = pokemon(raw_poke)
    poke.talent = carac["ability"]
    poke.item = carac["item"]
    for i,move in zip(range(4), carac["moves"]):
        attack = "attack" + str(i + 1)
        setattr(poke, attack, attack_registry[move])
    poke.tera_type = carac["tera_type"]
    poke.nature = carac["nature"]
    for stat in ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]:
        if stat in carac["evs"]:
            poke.evs[stat] = carac["evs"][stat]
        poke.ivs[stat] = carac["ivs"][stat]
    poke.recalculate_all_stats()  # Recalculer les stats avec les EVs et nature
    return poke
