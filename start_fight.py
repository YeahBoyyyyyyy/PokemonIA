import pokemon as pk
import pokemon_datas as STATS
from fight import Fight
from battle_interface import launch_battle
import pokemon_attacks as ATTACKS


def import_pokemon(name: str):
    raw_pokemon = STATS.pokemon_data[name]
    pokemon = pk.pokemon(STATS.pokemon_data[name])
    return pokemon


def create_competitive_team():
    """
    Crée l'équipe compétitive demandée avec tous les détails
    """
    team = []
    
    # Glimmora @ Focus Sash
    glimmora = import_pokemon("Glimmora")
    glimmora.talent = "Toxic Debris"
    glimmora.item = "Focus Sash"
    glimmora.tera_type = "Ghost"
    glimmora.evs = {"HP": 4, "Attack": 0, "Defense": 0, "Sp. Atk": 252, "Sp. Def": 0, "Speed": 252}
    glimmora.nature = "Timid"
    glimmora.attack1 = ATTACKS.EarthPower()
    glimmora.attack2 = ATTACKS.MortalSpin()
    glimmora.attack3 = ATTACKS.StealthRock()
    glimmora.attack4 = ATTACKS.PowerGem()

    
    # Kingambit @ Black Glasses
    kingambit = import_pokemon("Kingambit")
    kingambit.talent = "Supreme Overlord"
    kingambit.item = "Black Glasses"
    kingambit.tera_type = "Dark"
    kingambit.evs = {"HP": 0, "Attack": 252, "Defense": 4, "Sp. Atk": 0, "Sp. Def": 0, "Speed": 252}
    kingambit.nature = "Adamant"
    kingambit.attack1 = ATTACKS.SuckerPunch()
    kingambit.attack2 = ATTACKS.KowtowCleave()
    kingambit.attack3 = ATTACKS.IronHead()
    kingambit.attack4 = ATTACKS.SwordsDance()
    team.append(kingambit)
    team.append(glimmora)
    
    # Darkrai @ Choice Scarf
    darkrai = import_pokemon("Darkrai")
    darkrai.talent = "Bad Dreams"
    darkrai.item = "Choice Scarf"
    darkrai.tera_type = "Poison"
    darkrai.evs = {"HP": 0, "Attack": 0, "Defense": 0, "Sp. Atk": 252, "Sp. Def": 4, "Speed": 252}
    darkrai.ivs["Attack"] = 0  # IVs: 0 Atk
    darkrai.nature = "Timid"
    darkrai.attack1 = ATTACKS.SludgeBomb()
    darkrai.attack2 = ATTACKS.DarkPulse()
    darkrai.attack3 = ATTACKS.FocusBlast()
    darkrai.attack4 = ATTACKS.IceBeam()
    team.append(darkrai)
    
    # Zamazenta @ Leftovers
    zamazenta = import_pokemon("Zamazenta")
    zamazenta.talent = "Dauntless Shield"
    zamazenta.item = "Leftovers"
    zamazenta.tera_type = "Fire"
    zamazenta.evs = {"HP": 252, "Attack": 0, "Defense": 4, "Sp. Atk": 0, "Sp. Def": 0, "Speed": 252}
    zamazenta.nature = "Jolly"
    zamazenta.attack1 = ATTACKS.BodyPress()
    zamazenta.attack2 = ATTACKS.IronDefense()
    zamazenta.attack3 = ATTACKS.Crunch()
    zamazenta.attack4 = ATTACKS.Roar()
    team.append(zamazenta)
    
    # Dragonite @ Heavy-Duty Boots
    dragonite = import_pokemon("Dragonite")
    dragonite.talent = "Multiscale"
    dragonite.item = "Heavy-Duty Boots"
    dragonite.tera_type = "Normal"
    dragonite.evs = {"HP": 0, "Attack": 252, "Defense": 0, "Sp. Atk": 0, "Sp. Def": 4, "Speed": 252}
    dragonite.nature = "Adamant"
    dragonite.attack1 = ATTACKS.ExtremeSpeed()
    dragonite.attack2 = ATTACKS.DragonDance()
    dragonite.attack3 = ATTACKS.Earthquake()
    dragonite.attack4 = ATTACKS.IceSpinner()
    team.append(dragonite)
    
    # Iron Valiant @ Booster Energy
    iron_valiant = import_pokemon("Iron Valiant")
    iron_valiant.talent = "Quark Drive"
    iron_valiant.item = "Booster Energy"
    iron_valiant.tera_type = "Ghost"
    iron_valiant.evs = {"HP": 0, "Attack": 0, "Defense": 0, "Sp. Atk": 252, "Sp. Def": 4, "Speed": 252}
    iron_valiant.ivs["Attack"] = 0  # IVs: 0 Atk
    iron_valiant.nature = "Timid"
    iron_valiant.attack1 = ATTACKS.MoonBlast()
    iron_valiant.attack2 = ATTACKS.ShadowBall()
    iron_valiant.attack3 = ATTACKS.VacuumWave()
    iron_valiant.attack4 = ATTACKS.CalmMind()
    team.append(iron_valiant)
    
    return team


def create_french_team():
    """
    Crée l'équipe française avec les surnoms demandés
    """
    team = []
    
    # 10h du mat' (Moltres) @ Heavy-Duty Boots
    moltres = import_pokemon("Moltres")
    moltres.nickname = "10h du mat'"
    moltres.talent = "Snow Warning"
    moltres.item = "Heavy-Duty Boots"
    moltres.tera_type = "Fairy"
    moltres.evs = {"HP": 248, "Attack": 0, "Defense": 248, "Sp. Atk": 0, "Sp. Def": 0, "Speed": 12}
    moltres.nature = "Bold"
    moltres.recalculate_all_stats()  # Recalcule les stats avec les nouveaux EVs et nature
    
    moltres.attack1 = ATTACKS.FlareBlitz()
    moltres.attack2 = ATTACKS.Sandstorm()
    moltres.attack3 = ATTACKS.SunnyDay()
    moltres.attack4 = ATTACKS.UTurn()
    team.append(moltres)
    
    # Colorier des HLM (Primarina) @ Assault Vest
    primarina = import_pokemon("Primarina")
    primarina.nickname = "Colorier des HLM"
    primarina.talent = "Torrent"
    primarina.item = "Assault Vest"
    primarina.tera_type = "Steel"
    primarina.evs = {"HP": 192, "Attack": 0, "Defense": 0, "Sp. Atk": 252, "Sp. Def": 0, "Speed": 64}
    primarina.nature = "Modest"
    primarina.attack1 = ATTACKS.Surf()
    primarina.attack2 = ATTACKS.MoonBlast()
    primarina.attack3 = ATTACKS.FlipTurn()
    primarina.attack4 = ATTACKS.PsychicNoise()
    team.append(primarina)
    
    # Tant que ça va (Gholdengo) @ Heavy-Duty Boots
    gholdengo = import_pokemon("Gholdengo")
    gholdengo.nickname = "Tant que ça va"
    gholdengo.talent = "Good as Gold"
    gholdengo.item = "Heavy-Duty Boots"
    gholdengo.tera_type = "Water"
    gholdengo.evs = {"HP": 252, "Attack": 0, "Defense": 148, "Sp. Atk": 0, "Sp. Def": 0, "Speed": 108}
    gholdengo.ivs["Attack"] = 0  # IVs: 0 Atk
    gholdengo.nature = "Bold"
    gholdengo.attack1 = ATTACKS.NastyPlot()
    gholdengo.attack2 = ATTACKS.Hex()
    gholdengo.attack3 = ATTACKS.ThunderWave()
    gholdengo.attack4 = ATTACKS.Recover()
    team.append(gholdengo)
    
    # Le goût du sel (Gliscor) @ Toxic Orb
    gliscor = import_pokemon("Gliscor")
    gliscor.nickname = "Le goût du sel"
    gliscor.talent = "Poison Heal"
    gliscor.item = "Toxic Orb"
    gliscor.tera_type = "Fairy"
    gliscor.evs = {"HP": 244, "Attack": 0, "Defense": 36, "Sp. Atk": 0, "Sp. Def": 228, "Speed": 0}
    gliscor.ivs["Speed"] = 30  # IVs: 30 Spe
    gliscor.nature = "Careful"
    gliscor.attack1 = ATTACKS.Earthquake()
    gliscor.attack2 = ATTACKS.StealthRock()
    gliscor.attack3 = ATTACKS.Protect()
    gliscor.attack4 = ATTACKS.Toxic()
    team.append(gliscor)
    
    # Plus peur du Monde (Weavile) @ Heavy-Duty Boots
    weavile = import_pokemon("Weavile")
    weavile.nickname = "Plus peur du Monde"
    weavile.talent = "Pressure"
    weavile.item = "Heavy-Duty Boots"
    weavile.tera_type = "Ice"
    weavile.evs = {"HP": 0, "Attack": 252, "Defense": 0, "Sp. Atk": 0, "Sp. Def": 4, "Speed": 252}
    weavile.nature = "Jolly"
    weavile.attack1 = ATTACKS.KnockOff()
    weavile.attack2 = ATTACKS.TripleAxel()
    weavile.attack3 = ATTACKS.IceShard()
    weavile.attack4 = ATTACKS.LowKick()
    team.append(weavile)
    
    # Etoiles Satellites (Slowking-Galar) @ Heavy-Duty Boots
    slowking_galar = import_pokemon("Slowking-Galar")
    slowking_galar.nickname = "Etoiles Satellites"
    slowking_galar.talent = "Regenerator"
    slowking_galar.item = "Heavy-Duty Boots"
    slowking_galar.tera_type = "Grass"
    slowking_galar.evs = {"HP": 252, "Attack": 0, "Defense": 4, "Sp. Atk": 0, "Sp. Def": 252, "Speed": 0}
    slowking_galar.ivs["Attack"] = 0  # IVs: 0 Atk
    slowking_galar.ivs["Speed"] = 0   # IVs: 0 Spe
    slowking_galar.nature = "Sassy"
    slowking_galar.attack1 = ATTACKS.FutureSight()
    slowking_galar.attack2 = ATTACKS.ChillyReception()
    slowking_galar.attack3 = ATTACKS.SludgeBomb()
    slowking_galar.attack4 = ATTACKS.GrassKnot()
    team.append(slowking_galar)
    
    return team

# Créer l'équipe compétitive
competitive_team = create_competitive_team()

# Créer l'équipe française
french_team = create_french_team()

for p in competitive_team + french_team:
    p.recalculate_all_stats()  # Recalcule les stats avec les EVs et nature définis

print("Quelle équipe utiliser ?")
print("1. Équipe compétitive anglaise")
print("2. Équipe française avec surnoms")
choice = input("Votre choix (1 ou 2) : ")

opponent_team = []

if choice == "2":
    selected_team = french_team
    opponent_team = competitive_team
    print("Équipe française créée !")
else:
    selected_team = competitive_team
    opponent_team = french_team
    print("Équipe compétitive créée !")

print("=" * 50)
for i, pokemon in enumerate(selected_team, 1):
    display_name = getattr(pokemon, 'nickname', pokemon.name)
    print(f"{i}. {display_name} ({pokemon.name})")
    print(f"   Talent: {pokemon.talent}")
    print(f"   Objet: {pokemon.item}")
    print(f"   Tera Type: {pokemon.tera_type}")
    print(f"   Nature: {pokemon.nature}")
    print(f"   EVs: {pokemon.evs}")
    print(f"   Attaques: {pokemon.attack1.name}, {pokemon.attack2.name}, {pokemon.attack3.name}, {pokemon.attack4.name}")
    print()

# Lancer le combat avec l'équipe sélectionnée
launch_battle(selected_team, opponent_team)