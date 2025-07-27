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
    team.append(glimmora)
    
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


# Créer l'équipe compétitive
competitive_team = create_competitive_team()

print("Équipe compétitive créée !")
print("=" * 50)
for i, pokemon in enumerate(competitive_team, 1):
    print(f"{i}. {pokemon.name}")
    print(f"   Talent: {pokemon.talent}")
    print(f"   Objet: {pokemon.item}")
    print(f"   Tera Type: {pokemon.tera_type}")
    print(f"   Nature: {pokemon.nature}")
    print(f"   EVs: {pokemon.evs}")
    print(f"   Attaques: {pokemon.attack1.name}, {pokemon.attack2.name}, {pokemon.attack3.name}, {pokemon.attack4.name}")
    print()

# Lancer le combat avec cette équipe
launch_battle(competitive_team, [])