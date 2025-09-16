"""
Pokédex complet contenant tous les Pokémon disponibles en génération 9.
Données extraites du fichier pokemon_datas.py existant et complétées via l'API PokeAPI
"""

pokemon_data_gen9 = {
    "Venusaur": {
        "name": "Venusaur",
        "types": ["Grass", "Poison"],
        "abilities": ["Overgrow", "Chlorophyll"],
        "stats": {
            "HP": 80,
            "Attack": 82,
            "Defense": 83,
            "Sp. Atk": 100,
            "Sp. Def": 100,
            "Speed": 80,
        },
        "weight": 100.0,
        "fully_evolved": True
    },
    "Charizard": {
        "name": "Charizard",
        "types": ["Fire", "Flying"],
        "abilities": ["Blaze", "Solar Power"],
        "stats": {
            "HP": 78,
            "Attack": 84,
            "Defense": 78,
            "Sp. Atk": 109,
            "Sp. Def": 85,
            "Speed": 100,
        },
        "weight": 90.5,
        "fully_evolved": True
    },
    "Blastoise": {
        "name": "Blastoise",
        "types": ["Water"],
        "abilities": ["Torrent", "Rain Dish"],
        "stats": {
            "HP": 79,
            "Attack": 83,
            "Defense": 100,
            "Sp. Atk": 85,
            "Sp. Def": 105,
            "Speed": 78,
        },
        "weight": 85.5,
        "fully_evolved": True
    },
    "Arbok": {
        "name": "Arbok",
        "types": ["Poison"],
        "abilities": ["Intimidate", "Shed Skin", "Unnerve"],
        "stats": {
            "HP": 60,
            "Attack": 95,
            "Defense": 69,
            "Sp. Atk": 65,
            "Sp. Def": 79,
            "Speed": 80,
        },
        "weight": 65.0,
        "fully_evolved": True
    },
    "Pikachu": {
        "name": "Pikachu",
        "types": ["Electric"],
        "abilities": ["Static", "Lightning Rod"],
        "stats": {
            "HP": 35,
            "Attack": 55,
            "Defense": 40,
            "Sp. Atk": 50,
            "Sp. Def": 50,
            "Speed": 90,
        },
        "weight": 6.0,
        "fully_evolved": False
    },
    "Raichu": {
        "name": "Raichu",
        "types": ["Electric"],
        "abilities": ["Static", "Lightning Rod"],
        "stats": {
            "HP": 60,
            "Attack": 90,
            "Defense": 55,
            "Sp. Atk": 90,
            "Sp. Def": 80,
            "Speed": 110,
        },
        "weight": 30.0,
        "fully_evolved": True
    },
    "Raichu-Alola": {
        "name": "Raichu-Alola",
        "types": ["Electric", "Psychic"],
        "abilities": ["Surge Surfer"],
        "stats": {
            "HP": 60,
            "Attack": 85,
            "Defense": 50,
            "Sp. Atk": 95,
            "Sp. Def": 85,
            "Speed": 110,
        },
        "weight": 21.0,
        "fully_evolved": True
    },
    "Sandslash": {
        "name": "Sandslash",
        "types": ["Ground"],
        "abilities": ["Sand Veil", "Sand Rush"],
        "stats": {
            "HP": 75,
            "Attack": 100,
            "Defense": 110,
            "Sp. Atk": 45,
            "Sp. Def": 55,
            "Speed": 65,
        },
        "weight": 29.5,
        "fully_evolved": True
    },
    "Sandslash-Alola": {
        "name": "Sandslash-Alola",
        "types": ["Ice", "Steel"],
        "abilities": ["Snow Cloak", "Slush Rush"],
        "stats": {
            "HP": 75,
            "Attack": 100,
            "Defense": 120,
            "Sp. Atk": 25,
            "Sp. Def": 65,
            "Speed": 65,
        },
        "weight": 55.0,
        "fully_evolved": True
    },
    "Clefairy": {
        "name": "Clefairy",
        "types": ["Fairy"],
        "abilities": ["Cute Charm", "Magic Guard", "Friend Guard"],
        "stats": {
            "HP": 70,
            "Attack": 45,
            "Defense": 48,
            "Sp. Atk": 60,
            "Sp. Def": 65,
            "Speed": 35,
        },
        "weight": 7.5,
        "fully_evolved": True
    },
    "Clefable": {
        "name": "Clefable",
        "types": ["Fairy"],
        "abilities": ["Cute Charm", "Magic Guard", "Unaware"],
        "stats": {
            "HP": 95,
            "Attack": 70,
            "Defense": 73,
            "Sp. Atk": 95,
            "Sp. Def": 90,
            "Speed": 60,
        },
        "weight": 40.0,
        "fully_evolved": True
    },
    "Ninetales": {
        "name": "Ninetales",
        "types": ["Fire"],
        "abilities": ["Flash Fire", "Drought"],
        "stats": {
            "HP": 73,
            "Attack": 76,
            "Defense": 75,
            "Sp. Atk": 81,
            "Sp. Def": 100,
            "Speed": 100,
        },
        "weight": 19.9,
        "fully_evolved": True
    },
    "Ninetales-Alola": {
        "name": "Ninetales-Alola",
        "types": ["Ice", "Fairy"],
        "abilities": ["Snow Cloak", "Snow Warning"],
        "stats": {
            "HP": 73,
            "Attack": 67,
            "Defense": 75,
            "Sp. Atk": 81,
            "Sp. Def": 100,
            "Speed": 109,
        },
        "weight": 19.9,
        "fully_evolved": True
    },
    "Jigglypuff": {
        "name": "Jigglypuff",
        "types": ["Normal", "Fairy"],
        "abilities": ["Cute Charm", "Competitive", "Friend Guard"],
        "stats": {
            "HP": 115,
            "Attack": 45,
            "Defense": 20,
            "Sp. Atk": 45,
            "Sp. Def": 25,
            "Speed": 20,
        },
        "weight": 5.5,
        "fully_evolved": True
    },
    "Wigglytuff": {
        "name": "Wigglytuff",
        "types": ["Normal", "Fairy"],
        "abilities": ["Cute Charm", "Competitive", "Frisk"],
        "stats": {
            "HP": 140,
            "Attack": 70,
            "Defense": 45,
            "Sp. Atk": 85,
            "Sp. Def": 50,
            "Speed": 45,
        },
        "weight": 12.0,
        "fully_evolved": True
    },
    "Vileplume": {
        "name": "Vileplume",
        "types": ["Grass", "Poison"],
        "abilities": ["Chlorophyll", "Effect Spore"],
        "stats": {
            "HP": 75,
            "Attack": 80,
            "Defense": 85,
            "Sp. Atk": 110,
            "Sp. Def": 90,
            "Speed": 50,
        },
        "weight": 18.6,
        "fully_evolved": True
    },
    "Venomoth": {
        "name": "Venomoth",
        "types": ["Bug", "Poison"],
        "abilities": ["Shield Dust", "Tinted Lens", "Wonder Skin"],
        "stats": {
            "HP": 70,
            "Attack": 65,
            "Defense": 60,
            "Sp. Atk": 90,
            "Sp. Def": 75,
            "Speed": 90,
        },
        "weight": 12.5,
        "fully_evolved": True
    },
    "Dugtrio": {
        "name": "Dugtrio",
        "types": ["Ground"],
        "abilities": ["Sand Veil", "Arena Trap", "Sand Force"],
        "stats": {
            "HP": 35,
            "Attack": 100,
            "Defense": 50,
            "Sp. Atk": 50,
            "Sp. Def": 70,
            "Speed": 120,
        },
        "weight": 33.3,
        "fully_evolved": True
    },
    "Dugtrio-Alola": {
        "name": "Dugtrio-Alola",
        "types": ["Ground", "Steel"],
        "abilities": ["Sand Veil", "Tangling Hair", "Sand Force"],
        "stats": {
            "HP": 35,
            "Attack": 100,
            "Defense": 60,
            "Sp. Atk": 50,
            "Sp. Def": 70,
            "Speed": 110,
        },
        "weight": 66.6,
        "fully_evolved": True
    },
    "Persian": {
        "name": "Persian",
        "types": ["Normal"],
        "abilities": ["Limber", "Technician", "Unnerve"],
        "stats": {
            "HP": 65,
            "Attack": 70,
            "Defense": 60,
            "Sp. Atk": 65,
            "Sp. Def": 65,
            "Speed": 115,
        },
        "weight": 32.0,
        "fully_evolved": True
    },
    "Persian-Alola": {
        "name": "Persian-Alola",
        "types": ["Dark"],
        "abilities": ["Fur Coat", "Technician", "Rattled"],
        "stats": {
            "HP": 65,
            "Attack": 60,
            "Defense": 60,
            "Sp. Atk": 75,
            "Sp. Def": 65,
            "Speed": 115,
        },
        "weight": 33.0,
        "fully_evolved": True
    },
    "Primeape": {
        "name": "Primeape",
        "types": ["Fighting"],
        "abilities": ["Vital Spirit", "Anger Point", "Defiant"],
        "stats": {
            "HP": 65,
            "Attack": 105,
            "Defense": 60,
            "Sp. Atk": 60,
            "Sp. Def": 70,
            "Speed": 95,
        },
        "weight": 32.0,
        "fully_evolved": True
    },
    "Arcanine": {
        "name": "Arcanine",
        "types": ["Fire"],
        "abilities": ["Intimidate", "Flash Fire", "Justified"],
        "stats": {
            "HP": 90,
            "Attack": 110,
            "Defense": 80,
            "Sp. Atk": 100,
            "Sp. Def": 80,
            "Speed": 95,
        },
        "weight": 155.0,
        "fully_evolved": True
    },
    "Arcanine-Hisui": {
        "name": "Arcanine-Hisui",
        "types": ["Fire", "Rock"],
        "abilities": ["Intimidate", "Flash Fire", "Rock Head"],
        "stats": {
            "HP": 95,
            "Attack": 115,
            "Defense": 80,
            "Sp. Atk": 95,
            "Sp. Def": 80,
            "Speed": 90,
        },
        "weight": 168.0,
        "fully_evolved": True
    },
    "Poliwrath": {
        "name": "Poliwrath",
        "types": ["Water", "Fighting"],
        "abilities": ["Water Absorb", "Damp", "Swift Swim"],
        "stats": {
            "HP": 90,
            "Attack": 95,
            "Defense": 95,
            "Sp. Atk": 70,
            "Sp. Def": 90,
            "Speed": 70,
        },
        "weight": 54.0,
        "fully_evolved": True
    },
    "Victreebel": {
        "name": "Victreebel",
        "types": ["Grass", "Poison"],
        "abilities": ["Chlorophyll", "Gluttony"],
        "stats": {
            "HP": 80,
            "Attack": 105,
            "Defense": 65,
            "Sp. Atk": 100,
            "Sp. Def": 70,
            "Speed": 70,
        },
        "weight": 15.5,
        "fully_evolved": True
    },
    "Tentacruel": {
        "name": "Tentacruel",
        "types": ["Water", "Poison"],
        "abilities": ["Clear Body", "Liquid Ooze", "Rain Dish"],
        "stats": {
            "HP": 80,
            "Attack": 70,
            "Defense": 65,
            "Sp. Atk": 80,
            "Sp. Def": 120,
            "Speed": 100,
        },
        "weight": 55.0,
        "fully_evolved": True
    },
    "Golem": {
        "name": "Golem",
        "types": ["Rock", "Ground"],
        "abilities": ["Rock Head", "Sturdy", "Sand Veil"],
        "stats": {
            "HP": 80,
            "Attack": 120,
            "Defense": 130,
            "Sp. Atk": 55,
            "Sp. Def": 65,
            "Speed": 45,
        },
        "weight": 300.0,
        "fully_evolved": True
    },
    "Golem-Alola": {
        "name": "Golem-Alola",
        "types": ["Rock", "Electric"],
        "abilities": ["Magnet Pull", "Sturdy", "Galvanize"],
        "stats": {
            "HP": 80,
            "Attack": 120,
            "Defense": 130,
            "Sp. Atk": 55,
            "Sp. Def": 65,
            "Speed": 45,
        },
        "weight": 316.0,
        "fully_evolved": True
    },
    "Slowbro": {
        "name": "Slowbro",
        "types": ["Water", "Psychic"],
        "abilities": ["Oblivious", "Own Tempo", "Regenerator"],
        "stats": {
            "HP": 95,
            "Attack": 75,
            "Defense": 110,
            "Sp. Atk": 100,
            "Sp. Def": 80,
            "Speed": 30,
        },
        "weight": 78.5,
        "fully_evolved": True
    },
    "Slowking": {
        "name": "Slowking",
        "types": ["Water", "Psychic"],
        "abilities": ["Oblivious", "Own Tempo", "Regenerator"],
        "stats": {
            "HP": 95,
            "Attack": 75,
            "Defense": 80,
            "Sp. Atk": 100,
            "Sp. Def": 110,
            "Speed": 30,
        },
        "weight": 79.5,
        "fully_evolved": True
    },
    "Slowbro-Galar": {
        "name": "Slowbro-Galar",
        "types": ["Poison", "Psychic"],
        "abilities": ["Quick Draw", "Own Tempo", "Regenerator"],
        "stats": {
            "HP": 95,
            "Attack": 100,
            "Defense": 95,
            "Sp. Atk": 100,
            "Sp. Def": 70,
            "Speed": 30,
        },
        "weight": 70.5,
        "fully_evolved": True
    },
    "Dodrio": {
        "name": "Dodrio",
        "types": ["Normal", "Flying"],
        "abilities": ["Run Away", "Early Bird", "Tangled Feet"],
        "stats": {
            "HP": 60,
            "Attack": 110,
            "Defense": 70,
            "Sp. Atk": 60,
            "Sp. Def": 60,
            "Speed": 110,
        },
        "weight": 85.2,
        "fully_evolved": True
    },
    "Dewgong": {
        "name": "Dewgong",
        "types": ["Water", "Ice"],
        "abilities": ["Thick Fat", "Hydration", "Ice Body"],
        "stats": {
            "HP": 90,
            "Attack": 70,
            "Defense": 80,
            "Sp. Atk": 70,
            "Sp. Def": 95,
            "Speed": 70,
        },
        "weight": 120.0,
        "fully_evolved": True
    },
    "Muk": {
        "name": "Muk",
        "types": ["Poison"],
        "abilities": ["Stench", "Sticky Hold", "Poison Touch"],
        "stats": {
            "HP": 105,
            "Attack": 105,
            "Defense": 75,
            "Sp. Atk": 65,
            "Sp. Def": 100,
            "Speed": 50,
        },
        "weight": 30.0,
        "fully_evolved": True
    },
    "Muk-Alola": {
        "name": "Muk-Alola",
        "types": ["Poison", "Dark"],
        "abilities": ["Poison Touch", "Gluttony", "Power Of Alchemy"],
        "stats": {
            "HP": 105,
            "Attack": 105,
            "Defense": 75,
            "Sp. Atk": 65,
            "Sp. Def": 100,
            "Speed": 50,
        },
        "weight": 52.0,
        "fully_evolved": True
    },
    "Cloyster": {
        "name": "Cloyster",
        "types": ["Water", "Ice"],
        "abilities": ["Shell Armor", "Skill Link", "Overcoat"],
        "stats": {
            "HP": 50,
            "Attack": 95,
            "Defense": 180,
            "Sp. Atk": 85,
            "Sp. Def": 45,
            "Speed": 70,
        },
        "weight": 132.5,
        "fully_evolved": True
    },
    "Gengar": {
        "name": "Gengar",
        "types": ["Ghost", "Poison"],
        "abilities": ["Cursed Body"],
        "stats": {
            "HP": 60,
            "Attack": 65,
            "Defense": 60,
            "Sp. Atk": 130,
            "Sp. Def": 75,
            "Speed": 110,
        },
        "weight": 40.5,
        "fully_evolved": True
    },
    "Hypno": {
        "name": "Hypno",
        "types": ["Psychic"],
        "abilities": ["Insomnia", "Forewarn", "Inner Focus"],
        "stats": {
            "HP": 85,
            "Attack": 73,
            "Defense": 70,
            "Sp. Atk": 73,
            "Sp. Def": 115,
            "Speed": 67,
        },
        "weight": 75.6,
        "fully_evolved": True
    },
    "Electrode": {
        "name": "Electrode",
        "types": ["Electric"],
        "abilities": ["Soundproof", "Static", "Aftermath"],
        "stats": {
            "HP": 60,
            "Attack": 50,
            "Defense": 70,
            "Sp. Atk": 80,
            "Sp. Def": 80,
            "Speed": 150,
        },
        "weight": 66.6,
        "fully_evolved": True
    },
    "Electrode-Hisui": {
        "name": "Electrode-Hisui",
        "types": ["Electric", "Grass"],
        "abilities": ["Soundproof", "Static", "Aftermath"],
        "stats": {
            "HP": 60,
            "Attack": 50,
            "Defense": 70,
            "Sp. Atk": 80,
            "Sp. Def": 80,
            "Speed": 150,
        },
        "weight": 71.0,
        "fully_evolved": True
    },
    "Exeggutor": {
        "name": "Exeggutor",
        "types": ["Grass", "Psychic"],
        "abilities": ["Chlorophyll", "Harvest"],
        "stats": {
            "HP": 95,
            "Attack": 105,
            "Defense": 85,
            "Sp. Atk": 125,
            "Sp. Def": 75,
            "Speed": 55,
        },
        "weight": 120.0,
        "fully_evolved": True
    },
    "Exeggutor-Alola": {
        "name": "Exeggutor-Alola",
        "types": ["Grass", "Dragon"],
        "abilities": ["Frisk", "Harvest"],
        "stats": {
            "HP": 95,
            "Attack": 105,
            "Defense": 85,
            "Sp. Atk": 125,
            "Sp. Def": 75,
            "Speed": 45,
        },
        "weight": 415.6,
        "fully_evolved": True
    },
    "Hitmonlee": {
        "name": "Hitmonlee",
        "types": ["Fighting"],
        "abilities": ["Limber", "Reckless", "Unburden"],
        "stats": {
            "HP": 50,
            "Attack": 120,
            "Defense": 53,
            "Sp. Atk": 35,
            "Sp. Def": 110,
            "Speed": 87,
        },
        "weight": 49.8,
        "fully_evolved": True
    },
    "Hitmonchan": {
        "name": "Hitmonchan",
        "types": ["Fighting"],
        "abilities": ["Keen Eye", "Iron Fist", "Inner Focus"],
        "stats": {
            "HP": 50,
            "Attack": 105,
            "Defense": 79,
            "Sp. Atk": 35,
            "Sp. Def": 110,
            "Speed": 76,
        },
        "weight": 50.2,
        "fully_evolved": True
    },
    "Weezing": {
        "name": "Weezing",
        "types": ["Poison"],
        "abilities": ["Levitate", "Neutralizing Gas", "Stench"],
        "stats": {
            "HP": 65,
            "Attack": 90,
            "Defense": 120,
            "Sp. Atk": 85,
            "Sp. Def": 70,
            "Speed": 60,
        },
        "weight": 9.5,
        "fully_evolved": True
    },
    "Weezing-Galar": {
        "name": "Weezing-Galar",
        "types": ["Poison", "Fairy"],
        "abilities": ["Levitate", "Neutralizing Gas", "Misty Surge"],
        "stats": {
            "HP": 65,
            "Attack": 90,
            "Defense": 120,
            "Sp. Atk": 85,
            "Sp. Def": 70,
            "Speed": 60,
        },
        "weight": 16.0,
        "fully_evolved": True
    },
    "Rhydon": {
        "name": "Rhydon",
        "types": ["Ground", "Rock"],
        "abilities": ["Lightning Rod", "Rock Head", "Reckless"],
        "stats": {
            "HP": 105,
            "Attack": 130,
            "Defense": 120,
            "Sp. Atk": 45,
            "Sp. Def": 45,
            "Speed": 40,
        },
        "weight": 120.0,
        "fully_evolved": False
    },
    "Chansey": {
        "name": "Chansey",
        "types": ["Normal"],
        "abilities": ["Natural Cure", "Serene Grace", "Healer"],
        "stats": {
            "HP": 250,
            "Attack": 5,
            "Defense": 5,
            "Sp. Atk": 35,
            "Sp. Def": 105,
            "Speed": 50,
        },
        "weight": 34.6,
        "fully_evolved": False
    },
    "Mew": {
        "name": "Mew",
        "types": ["Psychic"],
        "abilities": ["Synchronize"],
        "stats": {
            "HP": 100,
            "Attack": 100,
            "Defense": 100,
            "Sp. Atk": 100,
            "Sp. Def": 100,
            "Speed": 100,
        },
        "weight": 4.0,
        "fully_evolved": True
    },
    "Scyther": {
        "name": "Scyther",
        "types": ["Bug", "Flying"],
        "abilities": ["Swarm", "Technician", "Steadfast"],
        "stats": {
            "HP": 70,
            "Attack": 110,
            "Defense": 80,
            "Sp. Atk": 55,
            "Sp. Def": 80,
            "Speed": 105,
        },
        "weight": 56.0,
        "fully_evolved": False
    },
    "Electabuzz": {
        "name": "Electabuzz",
        "types": ["Electric"],
        "abilities": ["Static", "Vital Spirit"],
        "stats": {
            "HP": 65,
            "Attack": 83,
            "Defense": 57,
            "Sp. Atk": 95,
            "Sp. Def": 85,
            "Speed": 105,
        },
        "weight": 30.0,
        "fully_evolved": False
    },
    "Magmar": {
        "name": "Magmar",
        "types": ["Fire"],
        "abilities": ["Flame Body", "Vital Spirit"],
        "stats": {
            "HP": 65,
            "Attack": 95,
            "Defense": 57,
            "Sp. Atk": 100,
            "Sp. Def": 85,
            "Speed": 93,
        },
        "weight": 44.5,
        "fully_evolved": False
    },
    "Tauros": {
        "name": "Tauros",
        "types": ["Normal"],
        "abilities": ["Intimidate", "Anger Point", "Sheer Force"],
        "stats": {
            "HP": 75,
            "Attack": 100,
            "Defense": 95,
            "Sp. Atk": 40,
            "Sp. Def": 70,
            "Speed": 110,
        },
        "weight": 88.4,
        "fully_evolved": True
    },
    "Gyarados": {
        "name": "Gyarados",
        "types": ["Water", "Flying"],
        "abilities": ["Intimidate", "Moxie"],
        "stats": {
            "HP": 95,
            "Attack": 125,
            "Defense": 79,
            "Sp. Atk": 60,
            "Sp. Def": 100,
            "Speed": 81,
        },
        "weight": 235.0,
        "fully_evolved": True
    },
    "Lapras": {
        "name": "Lapras",
        "types": ["Water", "Ice"],
        "abilities": ["Water Absorb", "Shell Armor", "Hydration"],
        "stats": {
            "HP": 130,
            "Attack": 85,
            "Defense": 80,
            "Sp. Atk": 85,
            "Sp. Def": 95,
            "Speed": 60,
        },
        "weight": 220.0,
        "fully_evolved": True
    },
    "Ditto": {
        "name": "Ditto",
        "types": ["Normal"],
        "abilities": ["Limber", "Imposter"],
        "stats": {
            "HP": 48,
            "Attack": 48,
            "Defense": 48,
            "Sp. Atk": 48,
            "Sp. Def": 48,
            "Speed": 48,
        },
        "weight": 4.0,
        "fully_evolved": True
    },
    "Eevee": {
        "name": "Eevee",
        "types": ["Normal"],
        "abilities": ["Run Away", "Adaptability", "Anticipation"],
        "stats": {
            "HP": 55,
            "Attack": 55,
            "Defense": 50,
            "Sp. Atk": 45,
            "Sp. Def": 65,
            "Speed": 55,
        },
        "weight": 6.5,
        "fully_evolved": True
    },
    "Vaporeon": {
        "name": "Vaporeon",
        "types": ["Water"],
        "abilities": ["Water Absorb", "Hydration"],
        "stats": {
            "HP": 130,
            "Attack": 65,
            "Defense": 60,
            "Sp. Atk": 110,
            "Sp. Def": 95,
            "Speed": 65,
        },
        "weight": 29.0,
        "fully_evolved": True
    },
    "Jolteon": {
        "name": "Jolteon",
        "types": ["Electric"],
        "abilities": ["Volt Absorb", "Quick Feet"],
        "stats": {
            "HP": 65,
            "Attack": 65,
            "Defense": 60,
            "Sp. Atk": 110,
            "Sp. Def": 95,
            "Speed": 130,
        },
        "weight": 24.5,
        "fully_evolved": True
    },
    "Flareon": {
        "name": "Flareon",
        "types": ["Fire"],
        "abilities": ["Flash Fire", "Guts"],
        "stats": {
            "HP": 65,
            "Attack": 130,
            "Defense": 60,
            "Sp. Atk": 95,
            "Sp. Def": 110,
            "Speed": 65,
        },
        "weight": 25.0,
        "fully_evolved": True
    },
    "Porygon": {
        "name": "Porygon",
        "types": ["Normal"],
        "abilities": ["Trace", "Download", "Analytic"],
        "stats": {
            "HP": 65,
            "Attack": 60,
            "Defense": 70,
            "Sp. Atk": 85,
            "Sp. Def": 75,
            "Speed": 40,
        },
        "weight": 36.5,
        "fully_evolved": True
    },
    "Snorlax": {
        "name": "Snorlax",
        "types": ["Normal"],
        "abilities": ["Immunity", "Thick Fat", "Gluttony"],
        "stats": {
            "HP": 160,
            "Attack": 110,
            "Defense": 65,
            "Sp. Atk": 65,
            "Sp. Def": 110,
            "Speed": 30,
        },
        "weight": 460.0,
        "fully_evolved": True
    },
    "Articuno": {
        "name": "Articuno",
        "types": ["Ice", "Flying"],
        "abilities": ["Pressure", "Snow Cloak"],
        "stats": {
            "HP": 90,
            "Attack": 85,
            "Defense": 100,
            "Sp. Atk": 95,
            "Sp. Def": 125,
            "Speed": 85,
        },
        "weight": 55.4,
        "fully_evolved": True
    },
    "Articuno-Galar": {
        "name": "Articuno-Galar",
        "types": ["Psychic", "Flying"],
        "abilities": ["Competitive"],
        "stats": {
            "HP": 90,
            "Attack": 85,
            "Defense": 85,
            "Sp. Atk": 125,
            "Sp. Def": 100,
            "Speed": 95,
        },
        "weight": 50.9,
        "fully_evolved": True
    },
    "Zapdos": {
        "name": "Zapdos",
        "types": ["Electric", "Flying"],
        "abilities": ["Pressure", "Static"],
        "stats": {
            "HP": 90,
            "Attack": 90,
            "Defense": 85,
            "Sp. Atk": 125,
            "Sp. Def": 90,
            "Speed": 100,
        },
        "weight": 52.6,
        "fully_evolved": True
    },
    "Zapdos-Galar": {
        "name": "Zapdos-Galar",
        "types": ["Fighting", "Flying"],
        "abilities": ["Defiant"],
        "stats": {
            "HP": 90,
            "Attack": 125,
            "Defense": 90,
            "Sp. Atk": 85,
            "Sp. Def": 90,
            "Speed": 100,
        },
        "weight": 58.2,
        "fully_evolved": True
    },
    "Moltres": {
        "name": "Moltres",
        "types": ["Fire", "Flying"],
        "abilities": ["Pressure", "Flame Body"],
        "stats": {
            "HP": 90,
            "Attack": 100,
            "Defense": 90,
            "Sp. Atk": 125,
            "Sp. Def": 85,
            "Speed": 90,
        },
        "weight": 60.0,
        "fully_evolved": True
    },
    "Moltres-Galar": {
        "name": "Moltres-Galar",
        "types": ["Dark", "Flying"],
        "abilities": ["Berserk"],
        "stats": {
            "HP": 90,
            "Attack": 85,
            "Defense": 90,
            "Sp. Atk": 100,
            "Sp. Def": 125,
            "Speed": 90,
        },
        "weight": 66.0,
        "fully_evolved": True
    },
    "Dragonite": {
        "name": "Dragonite",
        "types": ["Dragon", "Flying"],
        "abilities": ["Inner Focus", "Multiscale"],
        "stats": {
            "HP": 91,
            "Attack": 134,
            "Defense": 95,
            "Sp. Atk": 100,
            "Sp. Def": 100,
            "Speed": 80,
        },
        "weight": 210.0,
        "fully_evolved": True
    },
    "Mewtwo": {
        "name": "Mewtwo",
        "types": ["Psychic"],
        "abilities": ["Pressure", "Unnerve"],
        "stats": {
            "HP": 106,
            "Attack": 110,
            "Defense": 90,
            "Sp. Atk": 154,
            "Sp. Def": 90,
            "Speed": 130,
        },
        "weight": 122.0,
        "fully_evolved": True
    },
    "Meganium": {
        "name": "Meganium",
        "types": ["Grass"],
        "abilities": ["Overgrow", "Leaf Guard"],
        "stats": {
            "HP": 80,
            "Attack": 82,
            "Defense": 100,
            "Sp. Atk": 83,
            "Sp. Def": 100,
            "Speed": 80,
        },
        "weight": 100.5,
        "fully_evolved": True
    },
    "Typhlosion": {
        "name": "Typhlosion",
        "types": ["Fire"],
        "abilities": ["Blaze", "Flash Fire"],
        "stats": {
            "HP": 78,
            "Attack": 84,
            "Defense": 78,
            "Sp. Atk": 109,
            "Sp. Def": 85,
            "Speed": 100,
        },
        "weight": 79.5,
        "fully_evolved": True
    },
    "Typhlosion-Hisui": {
        "name": "Typhlosion-Hisui",
        "types": ["Fire", "Ghost"],
        "abilities": ["Blaze", "Frisk"],
        "stats": {
            "HP": 73,
            "Attack": 84,
            "Defense": 78,
            "Sp. Atk": 119,
            "Sp. Def": 85,
            "Speed": 95,
        },
        "weight": 69.8,
        "fully_evolved": True
    },
    "Feraligatr": {
        "name": "Feraligatr",
        "types": ["Water"],
        "abilities": ["Torrent", "Sheer Force"],
        "stats": {
            "HP": 85,
            "Attack": 105,
            "Defense": 100,
            "Sp. Atk": 79,
            "Sp. Def": 83,
            "Speed": 78,
        },
        "weight": 88.8,
        "fully_evolved": True
    },
    "Furret": {
        "name": "Furret",
        "types": ["Normal"],
        "abilities": ["Run Away", "Keen Eye", "Frisk"],
        "stats": {
            "HP": 85,
            "Attack": 76,
            "Defense": 64,
            "Sp. Atk": 45,
            "Sp. Def": 55,
            "Speed": 90,
        },
        "weight": 32.5,
        "fully_evolved": True
    },
    "Noctowl": {
        "name": "Noctowl",
        "types": ["Normal", "Flying"],
        "abilities": ["Insomnia", "Keen Eye", "Tinted Lens"],
        "stats": {
            "HP": 100,
            "Attack": 50,
            "Defense": 50,
            "Sp. Atk": 86,
            "Sp. Def": 96,
            "Speed": 70,
        },
        "weight": 40.8,
        "fully_evolved": True
    },
    "Ariados": {
        "name": "Ariados",
        "types": ["Bug", "Poison"],
        "abilities": ["Swarm", "Insomnia", "Sniper"],
        "stats": {
            "HP": 70,
            "Attack": 90,
            "Defense": 70,
            "Sp. Atk": 60,
            "Sp. Def": 70,
            "Speed": 40,
        },
        "weight": 33.5,
        "fully_evolved": True
    },
    "Lanturn": {
        "name": "Lanturn",
        "types": ["Water", "Electric"],
        "abilities": ["Volt Absorb", "Illuminate", "Water Absorb"],
        "stats": {
            "HP": 125,
            "Attack": 58,
            "Defense": 58,
            "Sp. Atk": 76,
            "Sp. Def": 76,
            "Speed": 67,
        },
        "weight": 22.5,
        "fully_evolved": True
    },
    "Ampharos": {
        "name": "Ampharos",
        "types": ["Electric"],
        "abilities": ["Static", "Plus"],
        "stats": {
            "HP": 90,
            "Attack": 75,
            "Defense": 85,
            "Sp. Atk": 115,
            "Sp. Def": 90,
            "Speed": 55,
        },
        "weight": 61.5,
        "fully_evolved": True
    },
    "Bellossom": {
        "name": "Bellossom",
        "types": ["Grass"],
        "abilities": ["Chlorophyll", "Healer"],
        "stats": {
            "HP": 75,
            "Attack": 80,
            "Defense": 95,
            "Sp. Atk": 90,
            "Sp. Def": 100,
            "Speed": 50,
        },
        "weight": 5.8,
        "fully_evolved": True
    },
    "Azumarill": {
        "name": "Azumarill",
        "types": ["Water", "Fairy"],
        "abilities": ["Thick Fat", "Huge Power", "Sap Sipper"],
        "stats": {
            "HP": 100,
            "Attack": 50,
            "Defense": 80,
            "Sp. Atk": 60,
            "Sp. Def": 80,
            "Speed": 50,
        },
        "weight": 28.5,
        "fully_evolved": True
    },
    "Sudowoodo": {
        "name": "Sudowoodo",
        "types": ["Rock"],
        "abilities": ["Sturdy", "Rock Head", "Rattled"],
        "stats": {
            "HP": 70,
            "Attack": 100,
            "Defense": 115,
            "Sp. Atk": 30,
            "Sp. Def": 65,
            "Speed": 30,
        },
        "weight": 38.0,
        "fully_evolved": True
    },
    "Politoed": {
        "name": "Politoed",
        "types": ["Water"],
        "abilities": ["Water Absorb", "Damp", "Drizzle"],
        "stats": {
            "HP": 90,
            "Attack": 75,
            "Defense": 75,
            "Sp. Atk": 90,
            "Sp. Def": 100,
            "Speed": 70,
        },
        "weight": 33.9,
        "fully_evolved": True
    },
    "Jumpluff": {
        "name": "Jumpluff",
        "types": ["Grass", "Flying"],
        "abilities": ["Chlorophyll", "Leaf Guard", "Infiltrator"],
        "stats": {
            "HP": 75,
            "Attack": 55,
            "Defense": 70,
            "Sp. Atk": 55,
            "Sp. Def": 95,
            "Speed": 110,
        },
        "weight": 3.0,
        "fully_evolved": True
    },
    "Sunflora": {
        "name": "Sunflora",
        "types": ["Grass"],
        "abilities": ["Chlorophyll", "Solar Power", "Early Bird"],
        "stats": {
            "HP": 75,
            "Attack": 75,
            "Defense": 55,
            "Sp. Atk": 105,
            "Sp. Def": 85,
            "Speed": 30,
        },
        "weight": 8.5,
        "fully_evolved": True
    },
    "Quagsire": {
        "name": "Quagsire",
        "types": ["Water", "Ground"],
        "abilities": ["Damp", "Water Absorb", "Unaware"],
        "stats": {
            "HP": 95,
            "Attack": 85,
            "Defense": 85,
            "Sp. Atk": 65,
            "Sp. Def": 65,
            "Speed": 35,
        },
        "weight": 75.0,
        "fully_evolved": True
    },
    "Espeon": {
        "name": "Espeon",
        "types": ["Psychic"],
        "abilities": ["Synchronize", "Magic Bounce"],
        "stats": {
            "HP": 65,
            "Attack": 65,
            "Defense": 60,
            "Sp. Atk": 130,
            "Sp. Def": 95,
            "Speed": 110,
        },
        "weight": 26.5,
        "fully_evolved": True
    },
    "Umbreon": {
        "name": "Umbreon",
        "types": ["Dark"],
        "abilities": ["Synchronize", "Inner Focus"],
        "stats": {
            "HP": 95,
            "Attack": 65,
            "Defense": 110,
            "Sp. Atk": 60,
            "Sp. Def": 130,
            "Speed": 65,
        },
        "weight": 27.0,
        "fully_evolved": True
    },
    "Murkrow": {
        "name": "Murkrow",
        "types": ["Dark", "Flying"],
        "abilities": ["Insomnia", "Super Luck", "Prankster"],
        "stats": {
            "HP": 60,
            "Attack": 85,
            "Defense": 42,
            "Sp. Atk": 85,
            "Sp. Def": 42,
            "Speed": 91,
        },
        "weight": 2.1,
        "fully_evolved": True
    },
    "Slowking-Galar": {
        "name": "Slowking-Galar",
        "types": ["Poison", "Psychic"],
        "abilities": ["Curious Medicine", "Own Tempo", "Regenerator"],
        "stats": {
            "HP": 95,
            "Attack": 65,
            "Defense": 80,
            "Sp. Atk": 110,
            "Sp. Def": 110,
            "Speed": 30,
        },
        "weight": 79.5,
        "fully_evolved": True
    },
    "Misdreavus": {
        "name": "Misdreavus",
        "types": ["Ghost"],
        "abilities": ["Levitate"],
        "stats": {
            "HP": 60,
            "Attack": 60,
            "Defense": 60,
            "Sp. Atk": 85,
            "Sp. Def": 85,
            "Speed": 85,
        },
        "weight": 1.0,
        "fully_evolved": True
    },
    "Girafarig": {
        "name": "Girafarig",
        "types": ["Normal", "Psychic"],
        "abilities": ["Inner Focus", "Early Bird", "Sap Sipper"],
        "stats": {
            "HP": 70,
            "Attack": 80,
            "Defense": 65,
            "Sp. Atk": 90,
            "Sp. Def": 65,
            "Speed": 85,
        },
        "weight": 41.5,
        "fully_evolved": True
    },
    "Forretress": {
        "name": "Forretress",
        "types": ["Bug", "Steel"],
        "abilities": ["Sturdy", "Overcoat"],
        "stats": {
            "HP": 75,
            "Attack": 90,
            "Defense": 140,
            "Sp. Atk": 60,
            "Sp. Def": 60,
            "Speed": 40,
        },
        "weight": 125.8,
        "fully_evolved": True
    },
    "Dunsparce": {
        "name": "Dunsparce",
        "types": ["Normal"],
        "abilities": ["Serene Grace", "Run Away", "Rattled"],
        "stats": {
            "HP": 100,
            "Attack": 70,
            "Defense": 70,
            "Sp. Atk": 65,
            "Sp. Def": 65,
            "Speed": 45,
        },
        "weight": 14.0,
        "fully_evolved": True
    },
    "Granbull": {
        "name": "Granbull",
        "types": ["Fairy"],
        "abilities": ["Intimidate", "Quick Feet", "Rattled"],
        "stats": {
            "HP": 90,
            "Attack": 120,
            "Defense": 75,
            "Sp. Atk": 60,
            "Sp. Def": 60,
            "Speed": 45,
        },
        "weight": 48.7,
        "fully_evolved": True
    },
    "Qwilfish": {
        "name": "Qwilfish",
        "types": ["Water", "Poison"],
        "abilities": ["Poison Point", "Swift Swim", "Intimidate"],
        "stats": {
            "HP": 65,
            "Attack": 95,
            "Defense": 85,
            "Sp. Atk": 55,
            "Sp. Def": 55,
            "Speed": 85,
        },
        "weight": 3.9,
        "fully_evolved": True
    },
    "Qwilfish-Hisui": {
        "name": "Qwilfish-Hisui",
        "types": ["Dark", "Poison"],
        "abilities": ["Poison Point", "Swift Swim", "Intimidate"],
        "stats": {
            "HP": 65,
            "Attack": 95,
            "Defense": 85,
            "Sp. Atk": 55,
            "Sp. Def": 55,
            "Speed": 85,
        },
        "weight": 3.9,
        "fully_evolved": True
    },
    "Scizor": {
        "name": "Scizor",
        "types": ["Bug", "Steel"],
        "abilities": ["Swarm", "Technician", "Light Metal"],
        "stats": {
            "HP": 70,
            "Attack": 130,
            "Defense": 100,
            "Sp. Atk": 55,
            "Sp. Def": 80,
            "Speed": 65,
        },
        "weight": 90.0,
        "fully_evolved": True
    },
    "Heracross": {
        "name": "Heracross",
        "types": ["Bug", "Fighting"],
        "abilities": ["Swarm", "Guts", "Moxie"],
        "stats": {
            "HP": 80,
            "Attack": 125,
            "Defense": 75,
            "Sp. Atk": 40,
            "Sp. Def": 95,
            "Speed": 85,
        },
        "weight": 54.0,
        "fully_evolved": True
    },
    "Ursaring": {
        "name": "Ursaring",
        "types": ["Normal"],
        "abilities": ["Guts", "Quick Feet", "Unnerve"],
        "stats": {
            "HP": 90,
            "Attack": 130,
            "Defense": 75,
            "Sp. Atk": 75,
            "Sp. Def": 75,
            "Speed": 55,
        },
        "weight": 125.8,
        "fully_evolved": True
    },
    "Magcargo": {
        "name": "Magcargo",
        "types": ["Fire", "Rock"],
        "abilities": ["Magma Armor", "Flame Body", "Weak Armor"],
        "stats": {
            "HP": 60,
            "Attack": 50,
            "Defense": 120,
            "Sp. Atk": 90,
            "Sp. Def": 80,
            "Speed": 30,
        },
        "weight": 55.0,
        "fully_evolved": True
    },
    "Piloswine": {
        "name": "Piloswine",
        "types": ["Ice", "Ground"],
        "abilities": ["Oblivious", "Snow Cloak", "Thick Fat"],
        "stats": {
            "HP": 100,
            "Attack": 100,
            "Defense": 80,
            "Sp. Atk": 60,
            "Sp. Def": 60,
            "Speed": 50,
        },
        "weight": 55.8,
        "fully_evolved": True
    },
    "Delibird": {
        "name": "Delibird",
        "types": ["Ice", "Flying"],
        "abilities": ["Vital Spirit", "Hustle", "Insomnia"],
        "stats": {
            "HP": 45,
            "Attack": 55,
            "Defense": 45,
            "Sp. Atk": 65,
            "Sp. Def": 45,
            "Speed": 75,
        },
        "weight": 16.0,
        "fully_evolved": True
    },
    "Skarmory": {
        "name": "Skarmory",
        "types": ["Steel", "Flying"],
        "abilities": ["Keen Eye", "Sturdy", "Weak Armor"],
        "stats": {
            "HP": 65,
            "Attack": 80,
            "Defense": 140,
            "Sp. Atk": 40,
            "Sp. Def": 70,
            "Speed": 70,
        },
        "weight": 50.5,
        "fully_evolved": True
    },
    "Houndoom": {
        "name": "Houndoom",
        "types": ["Dark", "Fire"],
        "abilities": ["Early Bird", "Flash Fire", "Unnerve"],
        "stats": {
            "HP": 75,
            "Attack": 90,
            "Defense": 50,
            "Sp. Atk": 110,
            "Sp. Def": 80,
            "Speed": 95,
        },
        "weight": 35.0,
        "fully_evolved": True
    },
    "Kingdra": {
        "name": "Kingdra",
        "types": ["Water", "Dragon"],
        "abilities": ["Swift Swim", "Sniper", "Damp"],
        "stats": {
            "HP": 75,
            "Attack": 95,
            "Defense": 95,
            "Sp. Atk": 95,
            "Sp. Def": 95,
            "Speed": 85,
        },
        "weight": 152.0,
        "fully_evolved": True
    },
    "Donphan": {
        "name": "Donphan",
        "types": ["Ground"],
        "abilities": ["Sturdy", "Sand Veil"],
        "stats": {
            "HP": 90,
            "Attack": 120,
            "Defense": 120,
            "Sp. Atk": 60,
            "Sp. Def": 60,
            "Speed": 50,
        },
        "weight": 120.0,
        "fully_evolved": True
    },
    "Porygon2": {
        "name": "Porygon2",
        "types": ["Normal"],
        "abilities": ["Trace", "Download", "Analytic"],
        "stats": {
            "HP": 85,
            "Attack": 80,
            "Defense": 90,
            "Sp. Atk": 105,
            "Sp. Def": 95,
            "Speed": 60,
        },
        "weight": 32.5,
        "fully_evolved": True
    },
    "Hitmontop": {
        "name": "Hitmontop",
        "types": ["Fighting"],
        "abilities": ["Intimidate", "Technician", "Steadfast"],
        "stats": {
            "HP": 50,
            "Attack": 95,
            "Defense": 95,
            "Sp. Atk": 35,
            "Sp. Def": 110,
            "Speed": 70,
        },
        "weight": 48.0,
        "fully_evolved": True
    },
    "Blissey": {
        "name": "Blissey",
        "types": ["Normal"],
        "abilities": ["Natural Cure", "Serene Grace", "Healer"],
        "stats": {
            "HP": 255,
            "Attack": 10,
            "Defense": 10,
            "Sp. Atk": 75,
            "Sp. Def": 135,
            "Speed": 55,
        },
        "weight": 46.8,
        "fully_evolved": True
    },
    "Raikou": {
        "name": "Raikou",
        "types": ["Electric"],
        "abilities": ["Pressure", "Inner Focus"],
        "stats": {
            "HP": 90,
            "Attack": 85,
            "Defense": 75,
            "Sp. Atk": 115,
            "Sp. Def": 100,
            "Speed": 115,
        },
        "weight": 178.0,
        "fully_evolved": True
    },
    "Entei": {
        "name": "Entei",
        "types": ["Fire"],
        "abilities": ["Pressure", "Inner Focus"],
        "stats": {
            "HP": 115,
            "Attack": 115,
            "Defense": 85,
            "Sp. Atk": 90,
            "Sp. Def": 75,
            "Speed": 100,
        },
        "weight": 198.0,
        "fully_evolved": True
    },
    "Suicune": {
        "name": "Suicune",
        "types": ["Water"],
        "abilities": ["Pressure", "Inner Focus"],
        "stats": {
            "HP": 100,
            "Attack": 75,
            "Defense": 115,
            "Sp. Atk": 90,
            "Sp. Def": 115,
            "Speed": 85,
        },
        "weight": 187.0,
        "fully_evolved": True
    },
    "Tyranitar": {
        "name": "Tyranitar",
        "types": ["Rock", "Dark"],
        "abilities": ["Sand Stream", "Unnerve"],
        "stats": {
            "HP": 100,
            "Attack": 134,
            "Defense": 110,
            "Sp. Atk": 95,
            "Sp. Def": 100,
            "Speed": 61,
        },
        "weight": 202.0,
        "fully_evolved": True
    },
    "Lugia": {
        "name": "Lugia",
        "types": ["Psychic", "Flying"],
        "abilities": ["Pressure", "Multiscale"],
        "stats": {
            "HP": 106,
            "Attack": 90,
            "Defense": 130,
            "Sp. Atk": 90,
            "Sp. Def": 154,
            "Speed": 110,
        },
        "weight": 216.0,
        "fully_evolved": True
    },
    "Ho-oh": {
        "name": "Ho-oh",
        "types": ["Fire", "Flying"],
        "abilities": ["Pressure", "Regenerator"],
        "stats": {
            "HP": 106,
            "Attack": 130,
            "Defense": 90,
            "Sp. Atk": 110,
            "Sp. Def": 154,
            "Speed": 90,
        },
        "weight": 199.0,
        "fully_evolved": True
    },
    "Sceptile": {
        "name": "Sceptile",
        "types": ["Grass"],
        "abilities": ["Overgrow", "Unburden"],
        "stats": {
            "HP": 70,
            "Attack": 85,
            "Defense": 65,
            "Sp. Atk": 105,
            "Sp. Def": 85,
            "Speed": 120,
        },
        "weight": 52.2,
        "fully_evolved": True
    },
    "Blaziken": {
        "name": "Blaziken",
        "types": ["Fire", "Fighting"],
        "abilities": ["Blaze", "Speed Boost"],
        "stats": {
            "HP": 80,
            "Attack": 120,
            "Defense": 70,
            "Sp. Atk": 110,
            "Sp. Def": 70,
            "Speed": 80,
        },
        "weight": 52.0,
        "fully_evolved": True
    },
    "Swampert": {
        "name": "Swampert",
        "types": ["Water", "Ground"],
        "abilities": ["Torrent", "Damp"],
        "stats": {
            "HP": 100,
            "Attack": 110,
            "Defense": 90,
            "Sp. Atk": 85,
            "Sp. Def": 90,
            "Speed": 60,
        },
        "weight": 81.9,
        "fully_evolved": True
    },
    "Mightyena": {
        "name": "Mightyena",
        "types": ["Dark"],
        "abilities": ["Intimidate", "Quick Feet"],
        "stats": {
            "HP": 70,
            "Attack": 90,
            "Defense": 70,
            "Sp. Atk": 60,
            "Sp. Def": 70,
            "Speed": 70,
        },
        "weight": 37.0,
        "fully_evolved": True
    },
    "Ludicolo": {
        "name": "Ludicolo",
        "types": ["Water", "Grass"],
        "abilities": ["Swift Swim", "Rain Dish", "Own Tempo"],
        "stats": {
            "HP": 80,
            "Attack": 70,
            "Defense": 70,
            "Sp. Atk": 90,
            "Sp. Def": 100,
            "Speed": 70,
        },
        "weight": 55.0,
        "fully_evolved": True
    },
    "Shiftry": {
        "name": "Shiftry",
        "types": ["Grass", "Dark"],
        "abilities": ["Chlorophyll", "Wind Rider", "Pickpocket"],
        "stats": {
            "HP": 90,
            "Attack": 100,
            "Defense": 60,
            "Sp. Atk": 90,
            "Sp. Def": 60,
            "Speed": 80,
        },
        "weight": 59.6,
        "fully_evolved": True
    },
    "Pelipper": {
        "name": "Pelipper",
        "types": ["Water", "Flying"],
        "abilities": ["Keen Eye", "Drizzle", "Rain Dish"],
        "stats": {
            "HP": 60,
            "Attack": 50,
            "Defense": 100,
            "Sp. Atk": 95,
            "Sp. Def": 70,
            "Speed": 65,
        },
        "weight": 28.0,
        "fully_evolved": True
    },
    "Gardevoir": {
        "name": "Gardevoir",
        "types": ["Psychic", "Fairy"],
        "abilities": ["Synchronize", "Trace", "Telepathy"],
        "stats": {
            "HP": 68,
            "Attack": 65,
            "Defense": 65,
            "Sp. Atk": 125,
            "Sp. Def": 115,
            "Speed": 80,
        },
        "weight": 48.4,
        "fully_evolved": True
    },
    "Masquerain": {
        "name": "Masquerain",
        "types": ["Bug", "Flying"],
        "abilities": ["Intimidate", "Unnerve"],
        "stats": {
            "HP": 70,
            "Attack": 60,
            "Defense": 62,
            "Sp. Atk": 100,
            "Sp. Def": 82,
            "Speed": 80,
        },
        "weight": 3.6,
        "fully_evolved": True
    },
    "Vigoroth": {
        "name": "Vigoroth",
        "types": ["Normal"],
        "abilities": ["Vital Spirit"],
        "stats": {
            "HP": 80,
            "Attack": 80,
            "Defense": 80,
            "Sp. Atk": 55,
            "Sp. Def": 55,
            "Speed": 90,
        },
        "weight": 46.5,
        "fully_evolved": True
    },
    "Slaking": {
        "name": "Slaking",
        "types": ["Normal"],
        "abilities": ["Truant"],
        "stats": {
            "HP": 150,
            "Attack": 160,
            "Defense": 100,
            "Sp. Atk": 95,
            "Sp. Def": 65,
            "Speed": 100,
        },
        "weight": 130.5,
        "fully_evolved": True
    },
    "Hariyama": {
        "name": "Hariyama",
        "types": ["Fighting"],
        "abilities": ["Thick Fat", "Guts", "Sheer Force"],
        "stats": {
            "HP": 144,
            "Attack": 120,
            "Defense": 60,
            "Sp. Atk": 40,
            "Sp. Def": 60,
            "Speed": 50,
        },
        "weight": 253.8,
        "fully_evolved": True
    },
    "Sableye": {
        "name": "Sableye",
        "types": ["Dark", "Ghost"],
        "abilities": ["Keen Eye", "Stall", "Prankster"],
        "stats": {
            "HP": 50,
            "Attack": 75,
            "Defense": 75,
            "Sp. Atk": 65,
            "Sp. Def": 65,
            "Speed": 50,
        },
        "weight": 11.0,
        "fully_evolved": True
    },
    "Mawile": {
        "name": "Mawile",
        "types": ["Steel", "Fairy"],
        "abilities": ["Hyper Cutter", "Intimidate", "Sheer Force"],
        "stats": {
            "HP": 50,
            "Attack": 85,
            "Defense": 85,
            "Sp. Atk": 55,
            "Sp. Def": 55,
            "Speed": 50,
        },
        "weight": 11.5,
        "fully_evolved": True
    },
    "Plusle": {
        "name": "Plusle",
        "types": ["Electric"],
        "abilities": ["Plus", "Lightning Rod"],
        "stats": {
            "HP": 60,
            "Attack": 50,
            "Defense": 40,
            "Sp. Atk": 85,
            "Sp. Def": 75,
            "Speed": 95,
        },
        "weight": 4.2,
        "fully_evolved": True
    },
    "Minun": {
        "name": "Minun",
        "types": ["Electric"],
        "abilities": ["Minus", "Volt Absorb"],
        "stats": {
            "HP": 60,
            "Attack": 40,
            "Defense": 50,
            "Sp. Atk": 75,
            "Sp. Def": 85,
            "Speed": 95,
        },
        "weight": 4.2,
        "fully_evolved": True
    },
    "Volbeat": {
        "name": "Volbeat",
        "types": ["Bug"],
        "abilities": ["Illuminate", "Swarm", "Prankster"],
        "stats": {
            "HP": 65,
            "Attack": 73,
            "Defense": 75,
            "Sp. Atk": 47,
            "Sp. Def": 85,
            "Speed": 85,
        },
        "weight": 17.7,
        "fully_evolved": True
    },
    "Illumise": {
        "name": "Illumise",
        "types": ["Bug"],
        "abilities": ["Oblivious", "Tinted Lens", "Prankster"],
        "stats": {
            "HP": 65,
            "Attack": 47,
            "Defense": 75,
            "Sp. Atk": 73,
            "Sp. Def": 85,
            "Speed": 85,
        },
        "weight": 17.7,
        "fully_evolved": True
    },
    "Swalot": {
        "name": "Swalot",
        "types": ["Poison"],
        "abilities": ["Liquid Ooze", "Sticky Hold", "Gluttony"],
        "stats": {
            "HP": 100,
            "Attack": 73,
            "Defense": 83,
            "Sp. Atk": 73,
            "Sp. Def": 83,
            "Speed": 55,
        },
        "weight": 80.0,
        "fully_evolved": True
    },
    "Camerupt": {
        "name": "Camerupt",
        "types": ["Fire", "Ground"],
        "abilities": ["Magma Armor", "Solid Rock", "Anger Point"],
        "stats": {
            "HP": 70,
            "Attack": 100,
            "Defense": 70,
            "Sp. Atk": 105,
            "Sp. Def": 75,
            "Speed": 40,
        },
        "weight": 220.0,
        "fully_evolved": True
    },
    "Torkoal": {
        "name": "Torkoal",
        "types": ["Fire"],
        "abilities": ["White Smoke", "Drought", "Shell Armor"],
        "stats": {
            "HP": 70,
            "Attack": 85,
            "Defense": 140,
            "Sp. Atk": 85,
            "Sp. Def": 70,
            "Speed": 20,
        },
        "weight": 80.4,
        "fully_evolved": True
    },
    "Grumpig": {
        "name": "Grumpig",
        "types": ["Psychic"],
        "abilities": ["Thick Fat", "Own Tempo", "Gluttony"],
        "stats": {
            "HP": 80,
            "Attack": 45,
            "Defense": 65,
            "Sp. Atk": 90,
            "Sp. Def": 110,
            "Speed": 80,
        },
        "weight": 71.5,
        "fully_evolved": True
    },
    "Cacturne": {
        "name": "Cacturne",
        "types": ["Grass", "Dark"],
        "abilities": ["Sand Veil", "Water Absorb"],
        "stats": {
            "HP": 70,
            "Attack": 115,
            "Defense": 60,
            "Sp. Atk": 115,
            "Sp. Def": 60,
            "Speed": 55,
        },
        "weight": 77.4,
        "fully_evolved": True
    },
    "Altaria": {
        "name": "Altaria",
        "types": ["Dragon", "Flying"],
        "abilities": ["Natural Cure", "Cloud Nine"],
        "stats": {
            "HP": 75,
            "Attack": 70,
            "Defense": 90,
            "Sp. Atk": 70,
            "Sp. Def": 105,
            "Speed": 80,
        },
        "weight": 20.6,
        "fully_evolved": True
    },
    "Zangoose": {
        "name": "Zangoose",
        "types": ["Normal"],
        "abilities": ["Immunity", "Toxic Boost"],
        "stats": {
            "HP": 73,
            "Attack": 115,
            "Defense": 60,
            "Sp. Atk": 60,
            "Sp. Def": 60,
            "Speed": 90,
        },
        "weight": 40.3,
        "fully_evolved": True
    },
    "Seviper": {
        "name": "Seviper",
        "types": ["Poison"],
        "abilities": ["Shed Skin", "Infiltrator"],
        "stats": {
            "HP": 73,
            "Attack": 100,
            "Defense": 60,
            "Sp. Atk": 100,
            "Sp. Def": 60,
            "Speed": 65,
        },
        "weight": 52.5,
        "fully_evolved": True
    },
    "Whiscash": {
        "name": "Whiscash",
        "types": ["Water", "Ground"],
        "abilities": ["Oblivious", "Anticipation", "Hydration"],
        "stats": {
            "HP": 110,
            "Attack": 78,
            "Defense": 73,
            "Sp. Atk": 76,
            "Sp. Def": 71,
            "Speed": 60,
        },
        "weight": 23.6,
        "fully_evolved": True
    },
    "Crawdaunt": {
        "name": "Crawdaunt",
        "types": ["Water", "Dark"],
        "abilities": ["Hyper Cutter", "Shell Armor", "Adaptability"],
        "stats": {
            "HP": 63,
            "Attack": 120,
            "Defense": 85,
            "Sp. Atk": 90,
            "Sp. Def": 55,
            "Speed": 55,
        },
        "weight": 32.8,
        "fully_evolved": True
    },
    "Milotic": {
        "name": "Milotic",
        "types": ["Water"],
        "abilities": ["Marvel Scale", "Competitive", "Cute Charm"],
        "stats": {
            "HP": 95,
            "Attack": 60,
            "Defense": 79,
            "Sp. Atk": 100,
            "Sp. Def": 125,
            "Speed": 81,
        },
        "weight": 162.0,
        "fully_evolved": True
    },
    "Banette": {
        "name": "Banette",
        "types": ["Ghost"],
        "abilities": ["Insomnia", "Frisk", "Cursed Body"],
        "stats": {
            "HP": 64,
            "Attack": 115,
            "Defense": 65,
            "Sp. Atk": 83,
            "Sp. Def": 63,
            "Speed": 65,
        },
        "weight": 12.5,
        "fully_evolved": True
    },
    "Dusclops": {
        "name": "Dusclops",
        "types": ["Ghost"],
        "abilities": ["Pressure", "Frisk"],
        "stats": {
            "HP": 40,
            "Attack": 70,
            "Defense": 130,
            "Sp. Atk": 60,
            "Sp. Def": 130,
            "Speed": 25,
        },
        "weight": 30.6,
        "fully_evolved": True
    },
    "Tropius": {
        "name": "Tropius",
        "types": ["Grass", "Flying"],
        "abilities": ["Chlorophyll", "Solar Power", "Harvest"],
        "stats": {
            "HP": 99,
            "Attack": 68,
            "Defense": 83,
            "Sp. Atk": 72,
            "Sp. Def": 87,
            "Speed": 51,
        },
        "weight": 100.0,
        "fully_evolved": True
    },
    "Chimecho": {
        "name": "Chimecho",
        "types": ["Psychic"],
        "abilities": ["Levitate"],
        "stats": {
            "HP": 75,
            "Attack": 50,
            "Defense": 80,
            "Sp. Atk": 95,
            "Sp. Def": 90,
            "Speed": 65,
        },
        "weight": 1.0,
        "fully_evolved": True
    },
    "Glalie": {
        "name": "Glalie",
        "types": ["Ice"],
        "abilities": ["Inner Focus", "Ice Body", "Moody"],
        "stats": {
            "HP": 80,
            "Attack": 80,
            "Defense": 80,
            "Sp. Atk": 80,
            "Sp. Def": 80,
            "Speed": 80,
        },
        "weight": 256.5,
        "fully_evolved": True
    },
    "Luvdisc": {
        "name": "Luvdisc",
        "types": ["Water"],
        "abilities": ["Swift Swim", "Hydration"],
        "stats": {
            "HP": 43,
            "Attack": 30,
            "Defense": 55,
            "Sp. Atk": 40,
            "Sp. Def": 65,
            "Speed": 97,
        },
        "weight": 8.7,
        "fully_evolved": True
    },
    "Salamence": {
        "name": "Salamence",
        "types": ["Dragon", "Flying"],
        "abilities": ["Intimidate", "Moxie"],
        "stats": {
            "HP": 95,
            "Attack": 135,
            "Defense": 80,
            "Sp. Atk": 110,
            "Sp. Def": 80,
            "Speed": 100,
        },
        "weight": 102.6,
        "fully_evolved": True
    },
    "Metagross": {
        "name": "Metagross",
        "types": ["Steel", "Psychic"],
        "abilities": ["Clear Body", "Light Metal"],
        "stats": {
            "HP": 80,
            "Attack": 135,
            "Defense": 130,
            "Sp. Atk": 95,
            "Sp. Def": 90,
            "Speed": 70,
        },
        "weight": 550.0,
        "fully_evolved": True
    },
    "Regice": {
        "name": "Regice",
        "types": ["Ice"],
        "abilities": ["Clear Body", "Ice Body"],
        "stats": {
            "HP": 80,
            "Attack": 50,
            "Defense": 100,
            "Sp. Atk": 100,
            "Sp. Def": 200,
            "Speed": 50,
        },
        "weight": 175.0,
        "fully_evolved": True
    },
    "Registeel": {
        "name": "Registeel",
        "types": ["Steel"],
        "abilities": ["Clear Body", "Light Metal"],
        "stats": {
            "HP": 80,
            "Attack": 75,
            "Defense": 150,
            "Sp. Atk": 75,
            "Sp. Def": 150,
            "Speed": 50,
        },
        "weight": 205.0,
        "fully_evolved": True
    },
    "Regirock": {
        "name": "Regirock",
        "types": ["Rock"],
        "abilities": ["Clear Body", "Sturdy"],
        "stats": {
            "HP": 80,
            "Attack": 100,
            "Defense": 200,
            "Sp. Atk": 50,
            "Sp. Def": 100,
            "Speed": 50,
        },
        "weight": 230.0,
        "fully_evolved": True
    },
    "Latias": {
        "name": "Latias",
        "types": ["Dragon", "Psychic"],
        "abilities": ["Levitate"],
        "stats": {
            "HP": 80,
            "Attack": 80,
            "Defense": 90,
            "Sp. Atk": 110,
            "Sp. Def": 130,
            "Speed": 110,
        },
        "weight": 40.0,
        "fully_evolved": True
    },
    "Latios": {
        "name": "Latios",
        "types": ["Dragon", "Psychic"],
        "abilities": ["Levitate"],
        "stats": {
            "HP": 80,
            "Attack": 90,
            "Defense": 80,
            "Sp. Atk": 130,
            "Sp. Def": 110,
            "Speed": 110,
        },
        "weight": 60.0,
        "fully_evolved": True
    },
    "Kyogre": {
        "name": "Kyogre",
        "types": ["Water"],
        "abilities": ["Drizzle"],
        "stats": {
            "HP": 100,
            "Attack": 100,
            "Defense": 90,
            "Sp. Atk": 150,
            "Sp. Def": 140,
            "Speed": 90,
        },
        "weight": 352.0,
        "fully_evolved": True
    },
    "Groudon": {
        "name": "Groudon",
        "types": ["Ground"],
        "abilities": ["Drought"],
        "stats": {
            "HP": 100,
            "Attack": 150,
            "Defense": 140,
            "Sp. Atk": 100,
            "Sp. Def": 90,
            "Speed": 90,
        },
        "weight": 950.0,
        "fully_evolved": True
    },
    "Rayquaza": {
        "name": "Rayquaza",
        "types": ["Dragon", "Flying"],
        "abilities": ["Air Lock"],
        "stats": {
            "HP": 105,
            "Attack": 150,
            "Defense": 90,
            "Sp. Atk": 150,
            "Sp. Def": 90,
            "Speed": 95,
        },
        "weight": 206.5,
        "fully_evolved": True
    },
    "Jirachi": {
        "name": "Jirachi",
        "types": ["Steel", "Psychic"],
        "abilities": ["Serene Grace"],
        "stats": {
            "HP": 100,
            "Attack": 100,
            "Defense": 100,
            "Sp. Atk": 100,
            "Sp. Def": 100,
            "Speed": 100,
        },
        "weight": 1.1,
        "fully_evolved": True
    },
    "Deoxys": {
        "name": "Deoxys",
        "types": ["Psychic"],
        "abilities": ["Pressure"],
        "stats": {
            "HP": 50,
            "Attack": 150,
            "Defense": 50,
            "Sp. Atk": 150,
            "Sp. Def": 50,
            "Speed": 150,
        },
        "weight": 60.8,
        "fully_evolved": True
    },
    "Deoxys-Speed": {
        "name": "Deoxys-Speed",
        "types": ["Psychic"],
        "abilities": ["Pressure", "Keen Eye"],
        "stats": {
            "HP": 50,
            "Attack": 95,
            "Defense": 90,
            "Sp. Atk": 95,
            "Sp. Def": 90,
            "Speed": 180,
        },
        "weight": 60.8,
        "fully_evolved": True
    },
    "Deoxys-Attack": {
        "name": "Deoxys-Attack",
        "types": ["Psychic"],
        "abilities": ["Pressure"],
        "stats": {
            "HP": 50,
            "Attack": 180,
            "Defense": 20,
            "Sp. Atk": 180,
            "Sp. Def": 20,
            "Speed": 150,
        },
        "weight": 60.8,
        "fully_evolved": True
    },
    "Deoxys-Defense": {
        "name": "Deoxys-Defense",
        "types": ["Psychic"],
        "abilities": ["Pressure"],
        "stats": {
            "HP": 50,
            "Attack": 70,
            "Defense": 160,
            "Sp. Atk": 70,
            "Sp. Def": 160,
            "Speed": 90,
        },
        "weight": 60.8,
        "fully_evolved": True
    },
    "Torterra": {
        "name": "Torterra",
        "types": ["Grass", "Ground"],
        "abilities": ["Overgrow", "Shell Armor"],
        "stats": {
            "HP": 95,
            "Attack": 109,
            "Defense": 105,
            "Sp. Atk": 75,
            "Sp. Def": 85,
            "Speed": 56,
        },
        "weight": 310.0,
        "fully_evolved": True
    },
    "Infernape": {
        "name": "Infernape",
        "types": ["Fire", "Fighting"],
        "abilities": ["Blaze", "Iron Fist"],
        "stats": {
            "HP": 76,
            "Attack": 104,
            "Defense": 71,
            "Sp. Atk": 104,
            "Sp. Def": 71,
            "Speed": 108,
        },
        "weight": 55.0,
        "fully_evolved": True
    },
    "Empoleon": {
        "name": "Empoleon",
        "types": ["Water", "Steel"],
        "abilities": ["Torrent", "Competitive"],
        "stats": {
            "HP": 84,
            "Attack": 86,
            "Defense": 88,
            "Sp. Atk": 111,
            "Sp. Def": 101,
            "Speed": 60,
        },
        "weight": 84.5,
        "fully_evolved": True
    },
    "Staraptor": {
        "name": "Staraptor",
        "types": ["Normal", "Flying"],
        "abilities": ["Intimidate", "Reckless"],
        "stats": {
            "HP": 85,
            "Attack": 120,
            "Defense": 70,
            "Sp. Atk": 50,
            "Sp. Def": 60,
            "Speed": 100,
        },
        "weight": 24.9,
        "fully_evolved": True
    },
    "Bibarel": {
        "name": "Bibarel",
        "types": ["Normal", "Water"],
        "abilities": ["Simple", "Unaware", "Moody"],
        "stats": {
            "HP": 79,
            "Attack": 85,
            "Defense": 60,
            "Sp. Atk": 55,
            "Sp. Def": 60,
            "Speed": 71,
        },
        "weight": 31.5,
        "fully_evolved": True
    },
    "Kricketune": {
        "name": "Kricketune",
        "types": ["Bug"],
        "abilities": ["Swarm", "Technician"],
        "stats": {
            "HP": 77,
            "Attack": 85,
            "Defense": 51,
            "Sp. Atk": 55,
            "Sp. Def": 51,
            "Speed": 65,
        },
        "weight": 25.5,
        "fully_evolved": True
    },
    "Luxray": {
        "name": "Luxray",
        "types": ["Electric"],
        "abilities": ["Rivalry", "Intimidate", "Guts"],
        "stats": {
            "HP": 80,
            "Attack": 120,
            "Defense": 79,
            "Sp. Atk": 95,
            "Sp. Def": 79,
            "Speed": 70,
        },
        "weight": 42.0,
        "fully_evolved": True
    },
    "Rampardos": {
        "name": "Rampardos",
        "types": ["Rock"],
        "abilities": ["Mold Breaker", "Sheer Force"],
        "stats": {
            "HP": 97,
            "Attack": 165,
            "Defense": 60,
            "Sp. Atk": 65,
            "Sp. Def": 50,
            "Speed": 58,
        },
        "weight": 102.5,
        "fully_evolved": True
    },
    "Bastiodon": {
        "name": "Bastiodon",
        "types": ["Rock", "Steel"],
        "abilities": ["Sturdy", "Soundproof"],
        "stats": {
            "HP": 60,
            "Attack": 52,
            "Defense": 168,
            "Sp. Atk": 47,
            "Sp. Def": 138,
            "Speed": 30,
        },
        "weight": 149.5,
        "fully_evolved": True
    },
    "Vespiquen": {
        "name": "Vespiquen",
        "types": ["Bug", "Flying"],
        "abilities": ["Pressure", "Unnerve"],
        "stats": {
            "HP": 70,
            "Attack": 80,
            "Defense": 102,
            "Sp. Atk": 80,
            "Sp. Def": 102,
            "Speed": 40,
        },
        "weight": 38.5,
        "fully_evolved": True
    },
    "Pachirisu": {
        "name": "Pachirisu",
        "types": ["Electric"],
        "abilities": ["Run Away", "Pickup", "Volt Absorb"],
        "stats": {
            "HP": 60,
            "Attack": 45,
            "Defense": 70,
            "Sp. Atk": 45,
            "Sp. Def": 90,
            "Speed": 95,
        },
        "weight": 3.9,
        "fully_evolved": True
    },
    "Floatzel": {
        "name": "Floatzel",
        "types": ["Water"],
        "abilities": ["Swift Swim", "Water Veil"],
        "stats": {
            "HP": 85,
            "Attack": 105,
            "Defense": 55,
            "Sp. Atk": 85,
            "Sp. Def": 50,
            "Speed": 115,
        },
        "weight": 33.5,
        "fully_evolved": True
    },
    "Cherrim": {
        "name": "Cherrim",
        "types": ["Grass"],
        "abilities": ["Flower Gift"],
        "stats": {
            "HP": 70,
            "Attack": 60,
            "Defense": 70,
            "Sp. Atk": 87,
            "Sp. Def": 78,
            "Speed": 85,
        },
        "weight": 9.3,
        "fully_evolved": True
    },
    "Gastrodon": {
        "name": "Gastrodon",
        "types": ["Water", "Ground"],
        "abilities": ["Sticky Hold", "Storm Drain", "Sand Force"],
        "stats": {
            "HP": 111,
            "Attack": 83,
            "Defense": 68,
            "Sp. Atk": 92,
            "Sp. Def": 82,
            "Speed": 39,
        },
        "weight": 29.9,
        "fully_evolved": True
    },
    "Ambipom": {
        "name": "Ambipom",
        "types": ["Normal"],
        "abilities": ["Technician", "Pickup", "Skill Link"],
        "stats": {
            "HP": 75,
            "Attack": 100,
            "Defense": 66,
            "Sp. Atk": 60,
            "Sp. Def": 66,
            "Speed": 115,
        },
        "weight": 20.3,
        "fully_evolved": True
    },
    "Drifblim": {
        "name": "Drifblim",
        "types": ["Ghost", "Flying"],
        "abilities": ["Aftermath", "Unburden", "Flare Boost"],
        "stats": {
            "HP": 150,
            "Attack": 80,
            "Defense": 44,
            "Sp. Atk": 90,
            "Sp. Def": 54,
            "Speed": 80,
        },
        "weight": 15.0,
        "fully_evolved": True
    },
    "Lopunny": {
        "name": "Lopunny",
        "types": ["Normal"],
        "abilities": ["Cute Charm", "Klutz", "Limber"],
        "stats": {
            "HP": 65,
            "Attack": 76,
            "Defense": 84,
            "Sp. Atk": 54,
            "Sp. Def": 96,
            "Speed": 105,
        },
        "weight": 33.3,
        "fully_evolved": True
    },
    "Mismagius": {
        "name": "Mismagius",
        "types": ["Ghost"],
        "abilities": ["Levitate"],
        "stats": {
            "HP": 60,
            "Attack": 60,
            "Defense": 60,
            "Sp. Atk": 105,
            "Sp. Def": 105,
            "Speed": 105,
        },
        "weight": 4.4,
        "fully_evolved": True
    },
    "Honchkrow": {
        "name": "Honchkrow",
        "types": ["Dark", "Flying"],
        "abilities": ["Insomnia", "Super Luck", "Moxie"],
        "stats": {
            "HP": 100,
            "Attack": 125,
            "Defense": 52,
            "Sp. Atk": 105,
            "Sp. Def": 52,
            "Speed": 71,
        },
        "weight": 27.3,
        "fully_evolved": True
    },
    "Purugly": {
        "name": "Purugly",
        "types": ["Normal"],
        "abilities": ["Thick Fat", "Own Tempo", "Defiant"],
        "stats": {
            "HP": 71,
            "Attack": 82,
            "Defense": 64,
            "Sp. Atk": 64,
            "Sp. Def": 59,
            "Speed": 112,
        },
        "weight": 43.8,
        "fully_evolved": True
    },
    "Skuntank": {
        "name": "Skuntank",
        "types": ["Poison", "Dark"],
        "abilities": ["Stench", "Aftermath", "Keen Eye"],
        "stats": {
            "HP": 103,
            "Attack": 93,
            "Defense": 67,
            "Sp. Atk": 71,
            "Sp. Def": 61,
            "Speed": 84,
        },
        "weight": 38.0,
        "fully_evolved": True
    },
    "Bronzong": {
        "name": "Bronzong",
        "types": ["Steel", "Psychic"],
        "abilities": ["Levitate", "Heatproof", "Heavy Metal"],
        "stats": {
            "HP": 67,
            "Attack": 89,
            "Defense": 116,
            "Sp. Atk": 79,
            "Sp. Def": 116,
            "Speed": 33,
        },
        "weight": 187.0,
        "fully_evolved": True
    },
    "Spiritomb": {
        "name": "Spiritomb",
        "types": ["Ghost", "Dark"],
        "abilities": ["Pressure", "Infiltrator"],
        "stats": {
            "HP": 50,
            "Attack": 92,
            "Defense": 108,
            "Sp. Atk": 92,
            "Sp. Def": 108,
            "Speed": 35,
        },
        "weight": 108.0,
        "fully_evolved": True
    },
    "Garchomp": {
        "name": "Garchomp",
        "types": ["Dragon", "Ground"],
        "abilities": ["Rough Skin", "Sand Veil"],
        "stats": {
            "HP": 108,
            "Attack": 130,
            "Defense": 95,
            "Sp. Atk": 80,
            "Sp. Def": 85,
            "Speed": 102,
        },
        "weight": 95.0,
        "fully_evolved": True
    },
    "Lucario": {
        "name": "Lucario",
        "types": ["Fighting", "Steel"],
        "abilities": ["Steadfast", "Inner Focus", "Justified"],
        "stats": {
            "HP": 70,
            "Attack": 110,
            "Defense": 70,
            "Sp. Atk": 115,
            "Sp. Def": 70,
            "Speed": 90,
        },
        "weight": 54.0,
        "fully_evolved": True
    },
    "Hippowdon": {
        "name": "Hippowdon",
        "types": ["Ground"],
        "abilities": ["Sand Stream", "Sand Force"],
        "stats": {
            "HP": 108,
            "Attack": 112,
            "Defense": 118,
            "Sp. Atk": 68,
            "Sp. Def": 72,
            "Speed": 47,
        },
        "weight": 300.0,
        "fully_evolved": True
    },
    "Drapion": {
        "name": "Drapion",
        "types": ["Poison", "Dark"],
        "abilities": ["Battle Armor", "Sniper", "Keen Eye"],
        "stats": {
            "HP": 70,
            "Attack": 90,
            "Defense": 110,
            "Sp. Atk": 60,
            "Sp. Def": 75,
            "Speed": 95,
        },
        "weight": 61.5,
        "fully_evolved": True
    },
    "Toxicroak": {
        "name": "Toxicroak",
        "types": ["Poison", "Fighting"],
        "abilities": ["Anticipation", "Dry Skin", "Poison Touch"],
        "stats": {
            "HP": 83,
            "Attack": 106,
            "Defense": 65,
            "Sp. Atk": 86,
            "Sp. Def": 65,
            "Speed": 85,
        },
        "weight": 44.4,
        "fully_evolved": True
    },
    "Carnivine": {
        "name": "Carnivine",
        "types": ["Grass"],
        "abilities": ["Levitate"],
        "stats": {
            "HP": 74,
            "Attack": 100,
            "Defense": 72,
            "Sp. Atk": 90,
            "Sp. Def": 72,
            "Speed": 46,
        },
        "weight": 27.0,
        "fully_evolved": True
    },
    "Lumineon": {
        "name": "Lumineon",
        "types": ["Water"],
        "abilities": ["Swift Swim", "Storm Drain", "Water Veil"],
        "stats": {
            "HP": 69,
            "Attack": 69,
            "Defense": 76,
            "Sp. Atk": 69,
            "Sp. Def": 86,
            "Speed": 91,
        },
        "weight": 24.0,
        "fully_evolved": True
    },
    "Abomasnow": {
        "name": "Abomasnow",
        "types": ["Grass", "Ice"],
        "abilities": ["Snow Warning", "Soundproof"],
        "stats": {
            "HP": 90,
            "Attack": 92,
            "Defense": 75,
            "Sp. Atk": 92,
            "Sp. Def": 85,
            "Speed": 60,
        },
        "weight": 135.5,
        "fully_evolved": True
    },
    "Weavile": {
        "name": "Weavile",
        "types": ["Dark", "Ice"],
        "abilities": ["Pressure", "Pickpocket"],
        "stats": {
            "HP": 70,
            "Attack": 120,
            "Defense": 65,
            "Sp. Atk": 45,
            "Sp. Def": 85,
            "Speed": 125,
        },
        "weight": 34.0,
        "fully_evolved": True
    },
    "Magnezone": {
        "name": "Magnezone",
        "types": ["Electric", "Steel"],
        "abilities": ["Magnet Pull", "Sturdy"],
        "stats": {
            "HP": 70,
            "Attack": 70,
            "Defense": 115,
            "Sp. Atk": 130,
            "Sp. Def": 90,
            "Speed": 60,
        },
        "weight": 60.0,
        "fully_evolved": True
    },
    "Rhyperior": {
        "name": "Rhyperior",
        "types": ["Ground", "Rock"],
        "abilities": ["Lightning Rod", "Solid Rock", "Reckless"],
        "stats": {
            "HP": 115,
            "Attack": 140,
            "Defense": 130,
            "Sp. Atk": 55,
            "Sp. Def": 55,
            "Speed": 40,
        },
        "weight": 282.8,
        "fully_evolved": True
    },
    "Electivire": {
        "name": "Electivire",
        "types": ["Electric"],
        "abilities": ["Motor Drive", "Vital Spirit"],
        "stats": {
            "HP": 75,
            "Attack": 123,
            "Defense": 67,
            "Sp. Atk": 95,
            "Sp. Def": 85,
            "Speed": 95,
        },
        "weight": 138.6,
        "fully_evolved": True
    },
    "Magmortar": {
        "name": "Magmortar",
        "types": ["Fire"],
        "abilities": ["Flame Body", "Vital Spirit"],
        "stats": {
            "HP": 75,
            "Attack": 95,
            "Defense": 67,
            "Sp. Atk": 125,
            "Sp. Def": 95,
            "Speed": 83,
        },
        "weight": 68.0,
        "fully_evolved": True
    },
    "Gliscor": {
        "name": "Gliscor",
        "types": ["Ground", "Flying"],
        "abilities": ["Hyper Cutter", "Sand Veil", "Poison Heal"],
        "stats": {
            "HP": 75,
            "Attack": 95,
            "Defense": 125,
            "Sp. Atk": 45,
            "Sp. Def": 75,
            "Speed": 95,
        },
        "weight": 42.5,
        "fully_evolved": True
    },
    "Mamoswine": {
        "name": "Mamoswine",
        "types": ["Ice", "Ground"],
        "abilities": ["Oblivious", "Snow Cloak", "Thick Fat"],
        "stats": {
            "HP": 110,
            "Attack": 130,
            "Defense": 80,
            "Sp. Atk": 70,
            "Sp. Def": 60,
            "Speed": 80,
        },
        "weight": 291.0,
        "fully_evolved": True
    },
    "Porygon-Z": {
        "name": "Porygon-Z",
        "types": ["Normal"],
        "abilities": ["Adaptability", "Download", "Analytic"],
        "stats": {
            "HP": 85,
            "Attack": 80,
            "Defense": 70,
            "Sp. Atk": 135,
            "Sp. Def": 75,
            "Speed": 90,
        },
        "weight": 34.0,
        "fully_evolved": True
    },
    "Gallade": {
        "name": "Gallade",
        "types": ["Psychic", "Fighting"],
        "abilities": ["Steadfast", "Sharpness", "Justified"],
        "stats": {
            "HP": 68,
            "Attack": 125,
            "Defense": 65,
            "Sp. Atk": 65,
            "Sp. Def": 115,
            "Speed": 80,
        },
        "weight": 52.0,
        "fully_evolved": True
    },
    "Probopass": {
        "name": "Probopass",
        "types": ["Rock", "Steel"],
        "abilities": ["Sturdy", "Magnet Pull", "Sand Force"],
        "stats": {
            "HP": 60,
            "Attack": 55,
            "Defense": 145,
            "Sp. Atk": 75,
            "Sp. Def": 150,
            "Speed": 40,
        },
        "weight": 340.0,
        "fully_evolved": True
    },
    "Dusknoir": {
        "name": "Dusknoir",
        "types": ["Ghost"],
        "abilities": ["Pressure", "Frisk"],
        "stats": {
            "HP": 45,
            "Attack": 100,
            "Defense": 135,
            "Sp. Atk": 65,
            "Sp. Def": 135,
            "Speed": 45,
        },
        "weight": 106.6,
        "fully_evolved": True
    },
    "Froslass": {
        "name": "Froslass",
        "types": ["Ice", "Ghost"],
        "abilities": ["Snow Cloak", "Cursed Body"],
        "stats": {
            "HP": 70,
            "Attack": 80,
            "Defense": 70,
            "Sp. Atk": 80,
            "Sp. Def": 70,
            "Speed": 110,
        },
        "weight": 26.6,
        "fully_evolved": True
    },
    "Rotom": {
        "name": "Rotom",
        "types": ["Electric", "Ghost"],
        "abilities": ["Levitate"],
        "stats": {
            "HP": 50,
            "Attack": 50,
            "Defense": 77,
            "Sp. Atk": 95,
            "Sp. Def": 77,
            "Speed": 91,
        },
        "weight": 0.3,
        "fully_evolved": True
    },
    "Rotom-Wash": {
        "name": "Rotom-Wash",
        "types": ["Electric", "Water"],
        "abilities": ["Levitate"],
        "stats": {
            "HP": 50,
            "Attack": 65,
            "Defense": 107,
            "Sp. Atk": 105,
            "Sp. Def": 107,
            "Speed": 86,
        },
        "weight": 0.3,
        "fully_evolved": True
    },
    "Rotom-Heat": {
        "name": "Rotom-Heat",
        "types": ["Electric", "Fire"],
        "abilities": ["Levitate"],
        "stats": {
            "HP": 50,
            "Attack": 65,
            "Defense": 107,
            "Sp. Atk": 105,
            "Sp. Def": 107,
            "Speed": 86,
        },
        "weight": 0.3,
        "fully_evolved": True
    },
    "Rotom-Fan": {
        "name": "Rotom-Fan",
        "types": ["Electric", "Flying"],
        "abilities": ["Levitate"],
        "stats": {
            "HP": 50,
            "Attack": 65,
            "Defense": 107,
            "Sp. Atk": 105,
            "Sp. Def": 107,
            "Speed": 86,
        },
        "weight": 0.3,
        "fully_evolved": True
    },
    "Rotom-Frost": {
        "name": "Rotom-Frost",
        "types": ["Electric", "Ice"],
        "abilities": ["Levitate"],
        "stats": {
            "HP": 50,
            "Attack": 65,
            "Defense": 107,
            "Sp. Atk": 105,
            "Sp. Def": 107,
            "Speed": 86,
        },
        "weight": 0.3,
        "fully_evolved": True
    },
    "Rotom-Mow": {
        "name": "Rotom-Mow",
        "types": ["Electric", "Grass"],
        "abilities": ["Levitate"],
        "stats": {
            "HP": 50,
            "Attack": 65,
            "Defense": 107,
            "Sp. Atk": 105,
            "Sp. Def": 107,
            "Speed": 86,
        },
        "weight": 0.3,
        "fully_evolved": True
    },
    "Uxie": {
        "name": "Uxie",
        "types": ["Psychic"],
        "abilities": ["Levitate"],
        "stats": {
            "HP": 75,
            "Attack": 75,
            "Defense": 130,
            "Sp. Atk": 75,
            "Sp. Def": 130,
            "Speed": 95,
        },
        "weight": 0.3,
        "fully_evolved": True
    },
    "Mesprit": {
        "name": "Mesprit",
        "types": ["Psychic"],
        "abilities": ["Levitate"],
        "stats": {
            "HP": 80,
            "Attack": 105,
            "Defense": 105,
            "Sp. Atk": 105,
            "Sp. Def": 105,
            "Speed": 80,
        },
        "weight": 0.3,
        "fully_evolved": True
    },
    "Azelf": {
        "name": "Azelf",
        "types": ["Psychic"],
        "abilities": ["Levitate"],
        "stats": {
            "HP": 75,
            "Attack": 125,
            "Defense": 70,
            "Sp. Atk": 125,
            "Sp. Def": 70,
            "Speed": 115,
        },
        "weight": 0.3,
        "fully_evolved": True
    },
    "Dialga": {
        "name": "Dialga",
        "types": ["Steel", "Dragon"],
        "abilities": ["Pressure", "Telepathy"],
        "stats": {
            "HP": 100,
            "Attack": 120,
            "Defense": 120,
            "Sp. Atk": 150,
            "Sp. Def": 100,
            "Speed": 90,
        },
        "weight": 683.0,
        "fully_evolved": True
    },
    "Dialga-Origin": {
        "name": "Dialga-Origin",
        "types": ["Steel", "Dragon"],
        "abilities": ["Pressure", "Telepathy"],
        "stats": {
            "HP": 100,
            "Attack": 100,
            "Defense": 120,
            "Sp. Atk": 150,
            "Sp. Def": 120,
            "Speed": 90,
        },
        "weight": 848.7,
        "fully_evolved": True
    },
    "Palkia": {
        "name": "Palkia",
        "types": ["Water", "Dragon"],
        "abilities": ["Pressure", "Telepathy"],
        "stats": {
            "HP": 90,
            "Attack": 120,
            "Defense": 100,
            "Sp. Atk": 150,
            "Sp. Def": 120,
            "Speed": 100,
        },
        "weight": 336.0,
        "fully_evolved": True
    },
    "Palkia-Origin": {
        "name": "Palkia-Origin",
        "types": ["Water", "Dragon"],
        "abilities": ["Pressure", "Telepathy"],
        "stats": {
            "HP": 90,
            "Attack": 100,
            "Defense": 100,
            "Sp. Atk": 150,
            "Sp. Def": 120,
            "Speed": 120,
        },
        "weight": 659.0,
        "fully_evolved": True
    },
    "Heatran": {
        "name": "Heatran",
        "types": ["Fire", "Steel"],
        "abilities": ["Flash Fire", "Flame Body"],
        "stats": {
            "HP": 91,
            "Attack": 90,
            "Defense": 106,
            "Sp. Atk": 130,
            "Sp. Def": 106,
            "Speed": 77,
        },
        "weight": 430.0,
        "fully_evolved": True
    },
    "Regigigas": {
        "name": "Regigigas",
        "types": ["Normal"],
        "abilities": ["Slow Start"],
        "stats": {
            "HP": 110,
            "Attack": 160,
            "Defense": 110,
            "Sp. Atk": 80,
            "Sp. Def": 110,
            "Speed": 100,
        },
        "weight": 420.0,
        "fully_evolved": True
    },
    "Giratina-Altered": {
        "name": "Giratina-Altered",
        "types": ["Ghost", "Dragon"],
        "abilities": ["Pressure", "Telepathy"],
        "stats": {
            "HP": 150,
            "Attack": 100,
            "Defense": 120,
            "Sp. Atk": 100,
            "Sp. Def": 120,
            "Speed": 90,
        },
        "weight": 750.0,
        "fully_evolved": True
    },
    "Giratina-Origin": {
        "name": "Giratina-Origin",
        "types": ["Ghost", "Dragon"],
        "abilities": ["Levitate"],
        "stats": {
            "HP": 150,
            "Attack": 120,
            "Defense": 100,
            "Sp. Atk": 120,
            "Sp. Def": 100,
            "Speed": 90,
        },
        "weight": 650.0,
        "fully_evolved": True
    },
    "Cresselia": {
        "name": "Cresselia",
        "types": ["Psychic"],
        "abilities": ["Levitate"],
        "stats": {
            "HP": 120,
            "Attack": 70,
            "Defense": 110,
            "Sp. Atk": 75,
            "Sp. Def": 120,
            "Speed": 85,
        },
        "weight": 85.6,
        "fully_evolved": True
    },
    "Phione": {
        "name": "Phione",
        "types": ["Water"],
        "abilities": ["Hydration"],
        "stats": {
            "HP": 80,
            "Attack": 80,
            "Defense": 80,
            "Sp. Atk": 80,
            "Sp. Def": 80,
            "Speed": 80,
        },
        "weight": 3.1,
        "fully_evolved": True
    },
    "Manaphy": {
        "name": "Manaphy",
        "types": ["Water"],
        "abilities": ["Hydration"],
        "stats": {
            "HP": 100,
            "Attack": 100,
            "Defense": 100,
            "Sp. Atk": 100,
            "Sp. Def": 100,
            "Speed": 100,
        },
        "weight": 1.4,
        "fully_evolved": True
    },
    "Darkrai": {
        "name": "Darkrai",
        "types": ["Dark"],
        "abilities": ["Bad Dreams"],
        "stats": {
            "HP": 70,
            "Attack": 90,
            "Defense": 90,
            "Sp. Atk": 135,
            "Sp. Def": 90,
            "Speed": 125,
        },
        "weight": 50.5,
        "fully_evolved": True
    },
    "Shaymin-Land": {
        "name": "Shaymin-Land",
        "types": ["Grass"],
        "abilities": ["Natural Cure"],
        "stats": {
            "HP": 100,
            "Attack": 100,
            "Defense": 100,
            "Sp. Atk": 100,
            "Sp. Def": 100,
            "Speed": 100,
        },
        "weight": 2.1,
        "fully_evolved": True
    },
    "Shaymin-Sky": {
        "name": "Shaymin-Sky",
        "types": ["Grass", "Flying"],
        "abilities": ["Serene Grace"],
        "stats": {
            "HP": 100,
            "Attack": 103,
            "Defense": 75,
            "Sp. Atk": 120,
            "Sp. Def": 75,
            "Speed": 127,
        },
        "weight": 5.2,
        "fully_evolved": True
    },
    "Arceus": {
        "name": "Arceus",
        "types": ["Normal"],
        "abilities": ["Multitype"],
        "stats": {
            "HP": 120,
            "Attack": 120,
            "Defense": 120,
            "Sp. Atk": 120,
            "Sp. Def": 120,
            "Speed": 120,
        },
        "weight": 320.0,
        "fully_evolved": True
    },
    "Serperior": {
        "name": "Serperior",
        "types": ["Grass"],
        "abilities": ["Overgrow", "Contrary"],
        "stats": {
            "HP": 75,
            "Attack": 75,
            "Defense": 95,
            "Sp. Atk": 75,
            "Sp. Def": 95,
            "Speed": 113,
        },
        "weight": 63.0,
        "fully_evolved": True
    },
    "Emboar": {
        "name": "Emboar",
        "types": ["Fire", "Fighting"],
        "abilities": ["Blaze", "Reckless"],
        "stats": {
            "HP": 110,
            "Attack": 123,
            "Defense": 65,
            "Sp. Atk": 100,
            "Sp. Def": 65,
            "Speed": 65,
        },
        "weight": 150.0,
        "fully_evolved": True
    },
    "Samurott": {
        "name": "Samurott",
        "types": ["Water"],
        "abilities": ["Torrent", "Shell Armor"],
        "stats": {
            "HP": 95,
            "Attack": 100,
            "Defense": 85,
            "Sp. Atk": 108,
            "Sp. Def": 70,
            "Speed": 70,
        },
        "weight": 94.6,
        "fully_evolved": True
    },
    "Samurott-Hisui": {
        "name": "Samurott-Hisui",
        "types": ["Water", "Ice"],
        "abilities": ["Torrent", "Shell Armor"],
        "stats": {
            "HP": 90,
            "Attack": 108,
            "Defense": 80,
            "Sp. Atk": 100,
            "Sp. Def": 65,
            "Speed": 85,
        },
        "weight": 58.2,
        "fully_evolved": True
    },
    "Zebstrika": {
        "name": "Zebstrika",
        "types": ["Electric"],
        "abilities": ["Lightning Rod", "Motor Drive", "Sap Sipper"],
        "stats": {
            "HP": 75,
            "Attack": 100,
            "Defense": 63,
            "Sp. Atk": 80,
            "Sp. Def": 63,
            "Speed": 116,
        },
        "weight": 79.5,
        "fully_evolved": True
    },
    "Excadrill": {
        "name": "Excadrill",
        "types": ["Ground", "Steel"],
        "abilities": ["Sand Rush", "Mold Breaker"],
        "stats": {
            "HP": 110,
            "Attack": 135,
            "Defense": 60,
            "Sp. Atk": 50,
            "Sp. Def": 65,
            "Speed": 88,
        },
        "weight": 40.4,
        "fully_evolved": True
    },
    "Conkeldurr": {
        "name": "Conkeldurr",
        "types": ["Fighting"],
        "abilities": ["Guts", "Iron Fist", "Sheer Force"],
        "stats": {
            "HP": 105,
            "Attack": 140,
            "Defense": 95,
            "Sp. Atk": 55,
            "Sp. Def": 65,
            "Speed": 45,
        },
        "weight": 87.0,
        "fully_evolved": True
    },
    "Leavanny": {
        "name": "Leavanny",
        "types": ["Bug", "Grass"],
        "abilities": ["Swarm", "Chlorophyll", "Overcoat"],
        "stats": {
            "HP": 75,
            "Attack": 103,
            "Defense": 80,
            "Sp. Atk": 70,
            "Sp. Def": 80,
            "Speed": 92,
        },
        "weight": 20.5,
        "fully_evolved": True
    },
    "Whimsicott": {
        "name": "Whimsicott",
        "types": ["Grass", "Fairy"],
        "abilities": ["Prankster", "Infiltrator", "Chlorophyll"],
        "stats": {
            "HP": 60,
            "Attack": 67,
            "Defense": 85,
            "Sp. Atk": 77,
            "Sp. Def": 75,
            "Speed": 116,
        },
        "weight": 6.6,
        "fully_evolved": True
    },
    "Lilligant": {
        "name": "Lilligant",
        "types": ["Grass"],
        "abilities": ["Chlorophyll", "Own Tempo", "Leaf Guard"],
        "stats": {
            "HP": 70,
            "Attack": 60,
            "Defense": 75,
            "Sp. Atk": 110,
            "Sp. Def": 75,
            "Speed": 90,
        },
        "weight": 16.3,
        "fully_evolved": True
    },
    "Lilligant-Hisui": {
        "name": "Lilligant-Hisui",
        "types": ["Grass", "Fighting"],
        "abilities": ["Chlorophyll", "Hustle", "Leaf Guard"],
        "stats": {
            "HP": 70,
            "Attack": 105,
            "Defense": 75,
            "Sp. Atk": 50,
            "Sp. Def": 75,
            "Speed": 105,
        },
        "weight": 19.2,
        "fully_evolved": True
    },
    "Krookodile": {
        "name": "Krookodile",
        "types": ["Ground", "Dark"],
        "abilities": ["Intimidate", "Moxie"],
        "stats": {
            "HP": 95,
            "Attack": 117,
            "Defense": 80,
            "Sp. Atk": 65,
            "Sp. Def": 70,
            "Speed": 92,
        },
        "weight": 96.3,
        "fully_evolved": True
    },
    "Scrafty": {
        "name": "Scrafty",
        "types": ["Dark", "Fighting"],
        "abilities": ["Shed Skin", "Moxie", "Intimidate"],
        "stats": {
            "HP": 65,
            "Attack": 90,
            "Defense": 115,
            "Sp. Atk": 45,
            "Sp. Def": 115,
            "Speed": 58,
        },
        "weight": 30.0,
        "fully_evolved": True
    },
    "Zoroark": {
        "name": "Zoroark",
        "types": ["Dark"],
        "abilities": ["Illusion"],
        "stats": {
            "HP": 60,
            "Attack": 105,
            "Defense": 60,
            "Sp. Atk": 120,
            "Sp. Def": 60,
            "Speed": 105,
        },
        "weight": 81.1,
        "fully_evolved": True
    },
    "Zoroark-Hisui": {
        "name": "Zoroark-Hisui",
        "types": ["Normal", "Ghost"],
        "abilities": ["Illusion"],
        "stats": {
            "HP": 55,
            "Attack": 100,
            "Defense": 60,
            "Sp. Atk": 125,
            "Sp. Def": 60,
            "Speed": 110,
        },
        "weight": 73.0,
        "fully_evolved": True
    },
    "Cinccino": {
        "name": "Cinccino",
        "types": ["Normal"],
        "abilities": ["Cute Charm", "Technician", "Skill Link"],
        "stats": {
            "HP": 75,
            "Attack": 95,
            "Defense": 60,
            "Sp. Atk": 65,
            "Sp. Def": 60,
            "Speed": 115,
        },
        "weight": 7.5,
        "fully_evolved": True
    },
    "Gothitelle": {
        "name": "Gothitelle",
        "types": ["Psychic"],
        "abilities": ["Frisk", "Competitive", "Shadow Tag"],
        "stats": {
            "HP": 70,
            "Attack": 55,
            "Defense": 95,
            "Sp. Atk": 95,
            "Sp. Def": 110,
            "Speed": 65,
        },
        "weight": 44.0,
        "fully_evolved": True
    },
    "Reuniclus": {
        "name": "Reuniclus",
        "types": ["Psychic"],
        "abilities": ["Overcoat", "Magic Guard", "Regenerator"],
        "stats": {
            "HP": 110,
            "Attack": 65,
            "Defense": 75,
            "Sp. Atk": 125,
            "Sp. Def": 85,
            "Speed": 30,
        },
        "weight": 20.1,
        "fully_evolved": True
    },
    "Swanna": {
        "name": "Swanna",
        "types": ["Water", "Flying"],
        "abilities": ["Keen Eye", "Big Pecks", "Hydration"],
        "stats": {
            "HP": 75,
            "Attack": 87,
            "Defense": 63,
            "Sp. Atk": 87,
            "Sp. Def": 63,
            "Speed": 98,
        },
        "weight": 24.2,
        "fully_evolved": True
    },
    "Sawsbuck": {
        "name": "Sawsbuck",
        "types": ["Normal", "Grass"],
        "abilities": ["Chlorophyll", "Sap Sipper", "Serene Grace"],
        "stats": {
            "HP": 80,
            "Attack": 100,
            "Defense": 70,
            "Sp. Atk": 60,
            "Sp. Def": 70,
            "Speed": 95,
        },
        "weight": 92.5,
        "fully_evolved": True
    },
    "Amoonguss": {
        "name": "Amoonguss",
        "types": ["Grass", "Poison"],
        "abilities": ["Effect Spore", "Regenerator"],
        "stats": {
            "HP": 114,
            "Attack": 85,
            "Defense": 70,
            "Sp. Atk": 85,
            "Sp. Def": 80,
            "Speed": 30,
        },
        "weight": 10.5,
        "fully_evolved": True
    },
    "Alomomola": {
        "name": "Alomomola",
        "types": ["Water"],
        "abilities": ["Healer", "Hydration", "Regenerator"],
        "stats": {
            "HP": 165,
            "Attack": 75,
            "Defense": 80,
            "Sp. Atk": 40,
            "Sp. Def": 45,
            "Speed": 65,
        },
        "weight": 31.6,
        "fully_evolved": True
    },
    "Galvantula": {
        "name": "Galvantula",
        "types": ["Bug", "Electric"],
        "abilities": ["Compound Eyes", "Unnerve", "Swarm"],
        "stats": {
            "HP": 70,
            "Attack": 77,
            "Defense": 60,
            "Sp. Atk": 97,
            "Sp. Def": 60,
            "Speed": 108,
        },
        "weight": 14.3,
        "fully_evolved": True
    },
    "Eelektross": {
        "name": "Eelektross",
        "types": ["Electric"],
        "abilities": ["Levitate"],
        "stats": {
            "HP": 85,
            "Attack": 115,
            "Defense": 80,
            "Sp. Atk": 105,
            "Sp. Def": 80,
            "Speed": 50,
        },
        "weight": 80.5,
        "fully_evolved": True
    },
    "Chandelure": {
        "name": "Chandelure",
        "types": ["Ghost", "Fire"],
        "abilities": ["Flash Fire", "Infiltrator"],
        "stats": {
            "HP": 60,
            "Attack": 55,
            "Defense": 90,
            "Sp. Atk": 145,
            "Sp. Def": 90,
            "Speed": 80,
        },
        "weight": 34.0,
        "fully_evolved": True
    },
    "Haxorus": {
        "name": "Haxorus",
        "types": ["Dragon"],
        "abilities": ["Rivalry", "Unnerve", "Mold Breaker"],
        "stats": {
            "HP": 76,
            "Attack": 147,
            "Defense": 90,
            "Sp. Atk": 60,
            "Sp. Def": 70,
            "Speed": 97,
        },
        "weight": 105.5,
        "fully_evolved": True
    },
    "Beartic": {
        "name": "Beartic",
        "types": ["Ice"],
        "abilities": ["Snow Cloak", "Slush Rush", "Swift Swim"],
        "stats": {
            "HP": 95,
            "Attack": 130,
            "Defense": 80,
            "Sp. Atk": 70,
            "Sp. Def": 80,
            "Speed": 50,
        },
        "weight": 260.0,
        "fully_evolved": True
    },
    "Cryogonal": {
        "name": "Cryogonal",
        "types": ["Ice"],
        "abilities": ["Levitate"],
        "stats": {
            "HP": 80,
            "Attack": 50,
            "Defense": 50,
            "Sp. Atk": 95,
            "Sp. Def": 135,
            "Speed": 105,
        },
        "weight": 148.0,
        "fully_evolved": True
    },
    "Mienshao": {
        "name": "Mienshao",
        "types": ["Fighting"],
        "abilities": ["Inner Focus", "Regenerator", "Reckless"],
        "stats": {
            "HP": 65,
            "Attack": 125,
            "Defense": 60,
            "Sp. Atk": 95,
            "Sp. Def": 60,
            "Speed": 105,
        },
        "weight": 35.5,
        "fully_evolved": True
    },
    "Golurk": {
        "name": "Golurk",
        "types": ["Ground", "Ghost"],
        "abilities": ["Iron Fist", "Klutz", "No Guard"],
        "stats": {
            "HP": 89,
            "Attack": 124,
            "Defense": 80,
            "Sp. Atk": 55,
            "Sp. Def": 80,
            "Speed": 55,
        },
        "weight": 330.0,
        "fully_evolved": True
    },
    "Bisharp": {
        "name": "Bisharp",
        "types": ["Dark", "Steel"],
        "abilities": ["Defiant", "Pressure"],
        "stats": {
            "HP": 65,
            "Attack": 125,
            "Defense": 100,
            "Sp. Atk": 60,
            "Sp. Def": 70,
            "Speed": 70,
        },
        "weight": 70.0,
        "fully_evolved": True
    },
    "Braviary": {
        "name": "Braviary",
        "types": ["Normal", "Flying"],
        "abilities": ["Keen Eye", "Sheer Force", "Defiant"],
        "stats": {
            "HP": 100,
            "Attack": 123,
            "Defense": 75,
            "Sp. Atk": 57,
            "Sp. Def": 75,
            "Speed": 80,
        },
        "weight": 41.0,
        "fully_evolved": True
    },
    "Braviary-Hisui": {
        "name": "Braviary-Hisui",
        "types": ["Psychic", "Flying"],
        "abilities": ["Keen Eye", "Sheer Force", "Tinted Lens"],
        "stats": {
            "HP": 110,
            "Attack": 83,
            "Defense": 70,
            "Sp. Atk": 112,
            "Sp. Def": 70,
            "Speed": 65,
        },
        "weight": 43.4,
        "fully_evolved": True
    },
    "Mandibuzz": {
        "name": "Mandibuzz",
        "types": ["Dark", "Flying"],
        "abilities": ["Big Pecks", "Overcoat", "Weak Armor"],
        "stats": {
            "HP": 110,
            "Attack": 65,
            "Defense": 105,
            "Sp. Atk": 55,
            "Sp. Def": 95,
            "Speed": 80,
        },
        "weight": 39.5,
        "fully_evolved": True
    },
    "Hydreigon": {
        "name": "Hydreigon",
        "types": ["Dark", "Dragon"],
        "abilities": ["Levitate"],
        "stats": {
            "HP": 92,
            "Attack": 105,
            "Defense": 90,
            "Sp. Atk": 125,
            "Sp. Def": 90,
            "Speed": 98,
        },
        "weight": 160.0,
        "fully_evolved": True
    },
    "Volcarona": {
        "name": "Volcarona",
        "types": ["Bug", "Fire"],
        "abilities": ["Flame Body", "Swarm"],
        "stats": {
            "HP": 85,
            "Attack": 60,
            "Defense": 65,
            "Sp. Atk": 135,
            "Sp. Def": 105,
            "Speed": 100,
        },
        "weight": 46.0,
        "fully_evolved": True
    },
    "Cobalion": {
        "name": "Cobalion",
        "types": ["Steel", "Fighting"],
        "abilities": ["Justified"],
        "stats": {
            "HP": 91,
            "Attack": 90,
            "Defense": 129,
            "Sp. Atk": 90,
            "Sp. Def": 72,
            "Speed": 108,
        },
        "weight": 250.0,
        "fully_evolved": True
    },
    "Terrakion": {
        "name": "Terrakion",
        "types": ["Rock", "Fighting"],
        "abilities": ["Justified"],
        "stats": {
            "HP": 91,
            "Attack": 129,
            "Defense": 90,
            "Sp. Atk": 72,
            "Sp. Def": 90,
            "Speed": 108,
        },
        "weight": 260.0,
        "fully_evolved": True
    },
    "Virizion": {
        "name": "Virizion",
        "types": ["Grass", "Fighting"],
        "abilities": ["Justified"],
        "stats": {
            "HP": 91,
            "Attack": 90,
            "Defense": 72,
            "Sp. Atk": 90,
            "Sp. Def": 129,
            "Speed": 108,
        },
        "weight": 200.0,
        "fully_evolved": True
    },
    "Tornadus-Incarnate": {
        "name": "Tornadus-Incarnate",
        "types": ["Flying"],
        "abilities": ["Prankster", "Defiant"],
        "stats": {
            "HP": 79,
            "Attack": 115,
            "Defense": 70,
            "Sp. Atk": 125,
            "Sp. Def": 80,
            "Speed": 111,
        },
        "weight": 63.0,
        "fully_evolved": True
    },
    "Tornadus-Therian": {
        "name": "Tornadus-Therian",
        "types": ["Flying"],
        "abilities": ["Regenerator"],
        "stats": {
            "HP": 79,
            "Attack": 100,
            "Defense": 80,
            "Sp. Atk": 110,
            "Sp. Def": 90,
            "Speed": 121,
        },
        "weight": 63.0,
        "fully_evolved": True
    },
    "Thundurus-Incarnate": {
        "name": "Thundurus-Incarnate",
        "types": ["Electric", "Flying"],
        "abilities": ["Prankster", "Defiant"],
        "stats": {
            "HP": 79,
            "Attack": 115,
            "Defense": 70,
            "Sp. Atk": 125,
            "Sp. Def": 80,
            "Speed": 111,
        },
        "weight": 61.0,
        "fully_evolved": True
    },
    "Thundurus-Therian": {
        "name": "Thundurus-Therian",
        "types": ["Electric", "Flying"],
        "abilities": ["Volt Absorb"],
        "stats": {
            "HP": 79,
            "Attack": 105,
            "Defense": 70,
            "Sp. Atk": 145,
            "Sp. Def": 80,
            "Speed": 101,
        },
        "weight": 61.0,
        "fully_evolved": True
    },
    "Landorus-Incarnate": {
        "name": "Landorus-Incarnate",
        "types": ["Ground", "Flying"],
        "abilities": ["Sand Force", "Sheer Force"],
        "stats": {
            "HP": 89,
            "Attack": 125,
            "Defense": 90,
            "Sp. Atk": 115,
            "Sp. Def": 80,
            "Speed": 101,
        },
        "weight": 68.0,
        "fully_evolved": True
    },
    "Landorus-Therian": {
        "name": "Landorus-Therian",
        "types": ["Ground", "Flying"],
        "abilities": ["Intimidate"],
        "stats": {
            "HP": 89,
            "Attack": 145,
            "Defense": 90,
            "Sp. Atk": 105,
            "Sp. Def": 80,
            "Speed": 91,
        },
        "weight": 68.0,
        "fully_evolved": True
    },
    "Reshiram": {
        "name": "Reshiram",
        "types": ["Dragon", "Fire"],
        "abilities": ["Turboblaze"],
        "stats": {
            "HP": 100,
            "Attack": 120,
            "Defense": 100,
            "Sp. Atk": 150,
            "Sp. Def": 120,
            "Speed": 90,
        },
        "weight": 330.0,
        "fully_evolved": True
    },
    "Zekrom": {
        "name": "Zekrom",
        "types": ["Dragon", "Electric"],
        "abilities": ["Teravolt"],
        "stats": {
            "HP": 100,
            "Attack": 150,
            "Defense": 120,
            "Sp. Atk": 120,
            "Sp. Def": 100,
            "Speed": 90,
        },
        "weight": 345.0,
        "fully_evolved": True
    },
    "Kyurem": {
        "name": "Kyurem",
        "types": ["Dragon", "Ice"],
        "abilities": ["Pressure"],
        "stats": {
            "HP": 125,
            "Attack": 130,
            "Defense": 90,
            "Sp. Atk": 130,
            "Sp. Def": 90,
            "Speed": 95,
        },
        "weight": 325.0,
        "fully_evolved": True
    },
    "Kyurem-Black": {
        "name": "Kyurem-Black",
        "types": ["Dragon", "Ice"],
        "abilities": ["Teravolt"],
        "stats": {
            "HP": 125,
            "Attack": 170,
            "Defense": 100,
            "Sp. Atk": 120,
            "Sp. Def": 90,
            "Speed": 95,
        },
        "weight": 325.0,
        "fully_evolved": True
    },
    "Kyurem-White": {
        "name": "Kyurem-White",
        "types": ["Dragon", "Ice"],
        "abilities": ["Turboblaze"],
        "stats": {
            "HP": 125,
            "Attack": 120,
            "Defense": 90,
            "Sp. Atk": 170,
            "Sp. Def": 100,
            "Speed": 95,
        },
        "weight": 325.0,
        "fully_evolved": True
    },
    "Keldeo-Resolute": {
        "name": "Keldeo-Resolute",
        "types": ["Water", "Fighting"],
        "abilities": ["Justified"],
        "stats": {
            "HP": 91,
            "Attack": 72,
            "Defense": 90,
            "Sp. Atk": 129,
            "Sp. Def": 90,
            "Speed": 108,
        },
        "weight": 48.5,
        "fully_evolved": True
    },
    "Genesect": {
        "name": "Genesect",
        "types": ["Bug", "Steel"],
        "abilities": ["Download"],
        "stats": {
            "HP": 71,
            "Attack": 120,
            "Defense": 95,
            "Sp. Atk": 120,
            "Sp. Def": 95,
            "Speed": 99,
        },
        "weight": 82.5,
        "fully_evolved": True
    },
    "Chesnaught": {
        "name": "Chesnaught",
        "types": ["Grass", "Fighting"],
        "abilities": ["Overgrow", "Bulletproof"],
        "stats": {
            "HP": 88,
            "Attack": 107,
            "Defense": 122,
            "Sp. Atk": 74,
            "Sp. Def": 75,
            "Speed": 64,
        },
        "weight": 90.0,
        "fully_evolved": True
    },
    "Delphox": {
        "name": "Delphox",
        "types": ["Fire", "Psychic"],
        "abilities": ["Blaze", "Magician"],
        "stats": {
            "HP": 75,
            "Attack": 69,
            "Defense": 72,
            "Sp. Atk": 114,
            "Sp. Def": 100,
            "Speed": 104,
        },
        "weight": 39.0,
        "fully_evolved": True
    },
    "Greninja": {
        "name": "Greninja",
        "types": ["Water", "Dark"],
        "abilities": ["Torrent", "Protean"],
        "stats": {
            "HP": 72,
            "Attack": 95,
            "Defense": 67,
            "Sp. Atk": 103,
            "Sp. Def": 71,
            "Speed": 122,
        },
        "weight": 40.0,
        "fully_evolved": True
    },
    "Talonflame": {
        "name": "Talonflame",
        "types": ["Fire", "Flying"],
        "abilities": ["Flame Body", "Gale Wings"],
        "stats": {
            "HP": 78,
            "Attack": 81,
            "Defense": 71,
            "Sp. Atk": 74,
            "Sp. Def": 69,
            "Speed": 126,
        },
        "weight": 24.5,
        "fully_evolved": True
    },
    "Vivillon": {
        "name": "Vivillon",
        "types": ["Bug", "Flying"],
        "abilities": ["Shield Dust", "Compound Eyes", "Friend Guard"],
        "stats": {
            "HP": 80,
            "Attack": 52,
            "Defense": 50,
            "Sp. Atk": 90,
            "Sp. Def": 50,
            "Speed": 89,
        },
        "weight": 17.0,
        "fully_evolved": True
    },
    "Pyroar": {
        "name": "Pyroar",
        "types": ["Fire", "Normal"],
        "abilities": ["Rivalry", "Unnerve", "Moxie"],
        "stats": {
            "HP": 86,
            "Attack": 68,
            "Defense": 72,
            "Sp. Atk": 109,
            "Sp. Def": 66,
            "Speed": 106,
        },
        "weight": 81.5,
        "fully_evolved": True
    },
    "Florges": {
        "name": "Florges",
        "types": ["Fairy"],
        "abilities": ["Flower Veil", "Symbiosis"],
        "stats": {
            "HP": 78,
            "Attack": 65,
            "Defense": 68,
            "Sp. Atk": 112,
            "Sp. Def": 154,
            "Speed": 75,
        },
        "weight": 10.0,
        "fully_evolved": True
    },
    "Gogoat": {
        "name": "Gogoat",
        "types": ["Grass"],
        "abilities": ["Sap Sipper", "Grass Pelt"],
        "stats": {
            "HP": 123,
            "Attack": 100,
            "Defense": 62,
            "Sp. Atk": 97,
            "Sp. Def": 81,
            "Speed": 68,
        },
        "weight": 91.0,
        "fully_evolved": True
    },
    "Malamar": {
        "name": "Malamar",
        "types": ["Dark", "Psychic"],
        "abilities": ["Contrary", "Suction Cups", "Infiltrator"],
        "stats": {
            "HP": 86,
            "Attack": 92,
            "Defense": 88,
            "Sp. Atk": 68,
            "Sp. Def": 75,
            "Speed": 73,
        },
        "weight": 47.0,
        "fully_evolved": True
    },
    "Dragalge": {
        "name": "Dragalge",
        "types": ["Poison", "Dragon"],
        "abilities": ["Poison Point", "Poison Touch", "Adaptability"],
        "stats": {
            "HP": 65,
            "Attack": 75,
            "Defense": 90,
            "Sp. Atk": 97,
            "Sp. Def": 123,
            "Speed": 44,
        },
        "weight": 81.5,
        "fully_evolved": True
    },
    "Clawitzer": {
        "name": "Clawitzer",
        "types": ["Water"],
        "abilities": ["Mega Launcher"],
        "stats": {
            "HP": 71,
            "Attack": 73,
            "Defense": 88,
            "Sp. Atk": 120,
            "Sp. Def": 89,
            "Speed": 59,
        },
        "weight": 35.3,
        "fully_evolved": True
    },
    "Sylveon": {
        "name": "Sylveon",
        "types": ["Fairy"],
        "abilities": ["Cute Charm", "Pixilate"],
        "stats": {
            "HP": 95,
            "Attack": 65,
            "Defense": 65,
            "Sp. Atk": 110,
            "Sp. Def": 130,
            "Speed": 60,
        },
        "weight": 23.5,
        "fully_evolved": True
    },
    "Hawlucha": {
        "name": "Hawlucha",
        "types": ["Fighting", "Flying"],
        "abilities": ["Limber", "Unburden", "Mold Breaker"],
        "stats": {
            "HP": 78,
            "Attack": 92,
            "Defense": 75,
            "Sp. Atk": 74,
            "Sp. Def": 63,
            "Speed": 118,
        },
        "weight": 21.5,
        "fully_evolved": True
    },
    "Dedenne": {
        "name": "Dedenne",
        "types": ["Electric", "Fairy"],
        "abilities": ["Cheek Pouch", "Pickup", "Plus"],
        "stats": {
            "HP": 67,
            "Attack": 58,
            "Defense": 57,
            "Sp. Atk": 81,
            "Sp. Def": 67,
            "Speed": 101,
        },
        "weight": 2.2,
        "fully_evolved": True
    },
    "Carbink": {
        "name": "Carbink",
        "types": ["Rock", "Fairy"],
        "abilities": ["Clear Body", "Sturdy"],
        "stats": {
            "HP": 50,
            "Attack": 50,
            "Defense": 150,
            "Sp. Atk": 50,
            "Sp. Def": 150,
            "Speed": 50,
        },
        "weight": 5.7,
        "fully_evolved": True
    },
    "Goodra": {
        "name": "Goodra",
        "types": ["Dragon"],
        "abilities": ["Sap Sipper", "Hydration", "Gooey"],
        "stats": {
            "HP": 90,
            "Attack": 100,
            "Defense": 70,
            "Sp. Atk": 110,
            "Sp. Def": 150,
            "Speed": 80,
        },
        "weight": 150.5,
        "fully_evolved": True
    },
    "Klefki": {
        "name": "Klefki",
        "types": ["Steel", "Fairy"],
        "abilities": ["Prankster", "Magician"],
        "stats": {
            "HP": 57,
            "Attack": 80,
            "Defense": 91,
            "Sp. Atk": 80,
            "Sp. Def": 87,
            "Speed": 75,
        },
        "weight": 3.0,
        "fully_evolved": True
    },
    "Trevenant": {
        "name": "Trevenant",
        "types": ["Ghost", "Grass"],
        "abilities": ["Natural Cure", "Frisk", "Harvest"],
        "stats": {
            "HP": 85,
            "Attack": 110,
            "Defense": 76,
            "Sp. Atk": 65,
            "Sp. Def": 82,
            "Speed": 56,
        },
        "weight": 71.0,
        "fully_evolved": True
    },
    "Avalugg": {
        "name": "Avalugg",
        "types": ["Ice"],
        "abilities": ["Own Tempo", "Ice Body", "Sturdy"],
        "stats": {
            "HP": 95,
            "Attack": 117,
            "Defense": 184,
            "Sp. Atk": 44,
            "Sp. Def": 46,
            "Speed": 28,
        },
        "weight": 505.0,
        "fully_evolved": True
    },
    "Noivern": {
        "name": "Noivern",
        "types": ["Flying", "Dragon"],
        "abilities": ["Frisk", "Infiltrator"],
        "stats": {
            "HP": 85,
            "Attack": 70,
            "Defense": 80,
            "Sp. Atk": 97,
            "Sp. Def": 80,
            "Speed": 123,
        },
        "weight": 85.0,
        "fully_evolved": True
    },
    "Diancie": {
        "name": "Diancie",
        "types": ["Rock", "Fairy"],
        "abilities": ["Clear Body"],
        "stats": {
            "HP": 50,
            "Attack": 100,
            "Defense": 150,
            "Sp. Atk": 100,
            "Sp. Def": 150,
            "Speed": 50,
        },
        "weight": 8.8,
        "fully_evolved": True
    },
    "Hoopa-Unbound": {
        "name": "Hoopa-Unbound",
        "types": ["Psychic", "Dark"],
        "abilities": ["Magician"],
        "stats": {
            "HP": 80,
            "Attack": 160,
            "Defense": 60,
            "Sp. Atk": 170,
            "Sp. Def": 130,
            "Speed": 80,
        },
        "weight": 490.0,
        "fully_evolved": True
    },
    "Hoopa-Confined": {
        "name": "Hoopa-Confined",
        "types": ["Psychic", "Ghost"],
        "abilities": ["Magician"],
        "stats": {
            "HP": 80,
            "Attack": 110,
            "Defense": 60,
            "Sp. Atk": 150,
            "Sp. Def": 130,
            "Speed": 70,
        },
        "weight": 9.0,
        "fully_evolved": True
    },
    "Volcanion": {
        "name": "Volcanion",
        "types": ["Fire", "Water"],
        "abilities": ["Water Absorb"],
        "stats": {
            "HP": 80,
            "Attack": 110,
            "Defense": 120,
            "Sp. Atk": 130,
            "Sp. Def": 90,
            "Speed": 70,
        },
        "weight": 195.0,
        "fully_evolved": True
    },
    "Decidueye": {
        "name": "Decidueye",
        "types": ["Grass", "Ghost"],
        "abilities": ["Overgrow", "Long Reach"],
        "stats": {
            "HP": 78,
            "Attack": 107,
            "Defense": 75,
            "Sp. Atk": 100,
            "Sp. Def": 100,
            "Speed": 70,
        },
        "weight": 36.0,
        "fully_evolved": True
    },
    "Decidueye-Hisui": {
        "name": "Decidueye-Hisui",
        "types": ["Grass", "Fighting"],
        "abilities": ["Overgrow", "Scrappy"],
        "stats": {
            "HP": 88,
            "Attack": 112,
            "Defense": 80,
            "Sp. Atk": 95,
            "Sp. Def": 95,
            "Speed": 60,
        },
        "weight": 37.0,
        "fully_evolved": True
    },
    "Incineroar": {
        "name": "Incineroar",
        "types": ["Fire", "Dark"],
        "abilities": ["Blaze", "Intimidate"],
        "stats": {
            "HP": 95,
            "Attack": 115,
            "Defense": 90,
            "Sp. Atk": 80,
            "Sp. Def": 90,
            "Speed": 60,
        },
        "weight": 83.0,
        "fully_evolved": True
    },
    "Primarina": {
        "name": "Primarina",
        "types": ["Water", "Fairy"],
        "abilities": ["Torrent", "Liquid Voice"],
        "stats": {
            "HP": 80,
            "Attack": 74,
            "Defense": 74,
            "Sp. Atk": 126,
            "Sp. Def": 116,
            "Speed": 60,
        },
        "weight": 44.0,
        "fully_evolved": True
    },
    "Toucannon": {
        "name": "Toucannon",
        "types": ["Normal", "Flying"],
        "abilities": ["Keen Eye", "Skill Link", "Sheer Force"],
        "stats": {
            "HP": 80,
            "Attack": 120,
            "Defense": 75,
            "Sp. Atk": 75,
            "Sp. Def": 75,
            "Speed": 60,
        },
        "weight": 26.0,
        "fully_evolved": True
    },
    "Gumshoos": {
        "name": "Gumshoos",
        "types": ["Normal"],
        "abilities": ["Stakeout", "Strong Jaw", "Adaptability"],
        "stats": {
            "HP": 88,
            "Attack": 110,
            "Defense": 60,
            "Sp. Atk": 55,
            "Sp. Def": 60,
            "Speed": 45,
        },
        "weight": 14.2,
        "fully_evolved": True
    },
    "Vikavolt": {
        "name": "Vikavolt",
        "types": ["Bug", "Electric"],
        "abilities": ["Levitate"],
        "stats": {
            "HP": 77,
            "Attack": 70,
            "Defense": 90,
            "Sp. Atk": 145,
            "Sp. Def": 75,
            "Speed": 43,
        },
        "weight": 45.0,
        "fully_evolved": True
    },
    "Crabominable": {
        "name": "Crabominable",
        "types": ["Fighting", "Ice"],
        "abilities": ["Hyper Cutter", "Iron Fist", "Anger Point"],
        "stats": {
            "HP": 97,
            "Attack": 132,
            "Defense": 77,
            "Sp. Atk": 62,
            "Sp. Def": 67,
            "Speed": 43,
        },
        "weight": 180.0,
        "fully_evolved": True
    },
    "Oricorio-Baile": {
        "name": "Oricorio-Baile",
        "types": ["Fire", "Flying"],
        "abilities": ["Dancer"],
        "stats": {
            "HP": 75,
            "Attack": 70,
            "Defense": 70,
            "Sp. Atk": 98,
            "Sp. Def": 70,
            "Speed": 93,
        },
        "weight": 3.4,
        "fully_evolved": True
    },
    "Oricorio-Pom-Pom": {
        "name": "Oricorio-Pom-Pom",
        "types": ["Electric", "Flying"],
        "abilities": ["Dancer"],
        "stats": {
            "HP": 75,
            "Attack": 70,
            "Defense": 70,
            "Sp. Atk": 98,
            "Sp. Def": 70,
            "Speed": 93,
        },
        "weight": 3.4,
        "fully_evolved": True
    },
    "Oricorio-Pau": {
        "name": "Oricorio-Pau",
        "types": ["Psychic", "Flying"],
        "abilities": ["Dancer"],
        "stats": {
            "HP": 75,
            "Attack": 70,
            "Defense": 70,
            "Sp. Atk": 98,
            "Sp. Def": 70,
            "Speed": 93,
        },
        "weight": 3.4,
        "fully_evolved": True
    },
    "Oricorio-Sensu": {
        "name": "Oricorio-Sensu",
        "types": ["Ghost", "Flying"],
        "abilities": ["Dancer"],
        "stats": {
            "HP": 75,
            "Attack": 70,
            "Defense": 70,
            "Sp. Atk": 98,
            "Sp. Def": 70,
            "Speed": 93,
        },
        "weight": 3.4,
        "fully_evolved": True
    },
    "Ribombee": {
        "name": "Ribombee",
        "types": ["Bug", "Fairy"],
        "abilities": ["Honey Gather", "Shield Dust", "Sweet Veil"],
        "stats": {
            "HP": 60,
            "Attack": 55,
            "Defense": 60,
            "Sp. Atk": 95,
            "Sp. Def": 70,
            "Speed": 124,
        },
        "weight": 0.5,
        "fully_evolved": True
    },
    "Lycanroc-Midday": {
        "name": "Lycanroc-Midday",
        "types": ["Rock"],
        "abilities": ["Sand Rush", "Keen Eye"],
        "stats": {
            "HP": 75,
            "Attack": 110,
            "Defense": 65,
            "Sp. Atk": 55,
            "Sp. Def": 65,
            "Speed": 112,
        },
        "weight": 25.0,
        "fully_evolved": True
    },
    "Lycanroc-Midnight": {
        "name": "Lycanroc-Midnight",
        "types": ["Rock"],
        "abilities": ["Keen Eye", "Vital Spirit", "No Guard"],
        "stats": {
            "HP": 85,
            "Attack": 115,
            "Defense": 75,
            "Sp. Atk": 55,
            "Sp. Def": 75,
            "Speed": 82,
        },
        "weight": 25.0,
        "fully_evolved": True
    },
    "Lycanroc-Dusk": {
        "name": "Lycanroc-Dusk",
        "types": ["Rock"],
        "abilities": ["Tough Claws"],
        "stats": {
            "HP": 75,
            "Attack": 117,
            "Defense": 65,
            "Sp. Atk": 55,
            "Sp. Def": 65,
            "Speed": 110,
        },
        "weight": 25.0,
        "fully_evolved": True
    },
    "Toxapex": {
        "name": "Toxapex",
        "types": ["Water", "Poison"],
        "abilities": ["Merciless", "Regenerator"],
        "stats": {
            "HP": 50,
            "Attack": 63,
            "Defense": 152,
            "Sp. Atk": 53,
            "Sp. Def": 142,
            "Speed": 35,
        },
        "weight": 14.5,
        "fully_evolved": True
    },
    "Mudsdale": {
        "name": "Mudsdale",
        "types": ["Ground"],
        "abilities": ["Own Tempo", "Stamina", "Inner Focus"],
        "stats": {
            "HP": 100,
            "Attack": 125,
            "Defense": 100,
            "Sp. Atk": 55,
            "Sp. Def": 85,
            "Speed": 35,
        },
        "weight": 920.0,
        "fully_evolved": True
    },
    "Araquanid": {
        "name": "Araquanid",
        "types": ["Water", "Bug"],
        "abilities": ["Water Bubble"],
        "stats": {
            "HP": 68,
            "Attack": 70,
            "Defense": 92,
            "Sp. Atk": 50,
            "Sp. Def": 132,
            "Speed": 42,
        },
        "weight": 82.0,
        "fully_evolved": True
    },
    "Lurantis": {
        "name": "Lurantis",
        "types": ["Grass"],
        "abilities": ["Leaf Guard", "Contrary"],
        "stats": {
            "HP": 70,
            "Attack": 105,
            "Defense": 90,
            "Sp. Atk": 80,
            "Sp. Def": 90,
            "Speed": 45,
        },
        "weight": 18.5,
        "fully_evolved": True
    },
    "Salazzle": {
        "name": "Salazzle",
        "types": ["Poison", "Fire"],
        "abilities": ["Corrosion", "Oblivious"],
        "stats": {
            "HP": 68,
            "Attack": 64,
            "Defense": 60,
            "Sp. Atk": 111,
            "Sp. Def": 60,
            "Speed": 117,
        },
        "weight": 22.2,
        "fully_evolved": True
    },
    "Tsareena": {
        "name": "Tsareena",
        "types": ["Grass"],
        "abilities": ["Leaf Guard", "Queenly Majesty", "Sweet Veil"],
        "stats": {
            "HP": 72,
            "Attack": 120,
            "Defense": 98,
            "Sp. Atk": 50,
            "Sp. Def": 98,
            "Speed": 72,
        },
        "weight": 21.4,
        "fully_evolved": True
    },
    "Comfey": {
        "name": "Comfey",
        "types": ["Fairy"],
        "abilities": ["Flower Veil", "Triage", "Natural Cure"],
        "stats": {
            "HP": 51,
            "Attack": 52,
            "Defense": 90,
            "Sp. Atk": 82,
            "Sp. Def": 110,
            "Speed": 100,
        },
        "weight": 0.3,
        "fully_evolved": True
    },
    "Oranguru": {
        "name": "Oranguru",
        "types": ["Normal", "Psychic"],
        "abilities": ["Inner Focus", "Telepathy", "Symbiosis"],
        "stats": {
            "HP": 90,
            "Attack": 60,
            "Defense": 80,
            "Sp. Atk": 90,
            "Sp. Def": 110,
            "Speed": 60,
        },
        "weight": 76.0,
        "fully_evolved": True
    },
    "Passimian": {
        "name": "Passimian",
        "types": ["Fighting"],
        "abilities": ["Receiver", "Defiant"],
        "stats": {
            "HP": 100,
            "Attack": 120,
            "Defense": 90,
            "Sp. Atk": 40,
            "Sp. Def": 60,
            "Speed": 80,
        },
        "weight": 82.8,
        "fully_evolved": True
    },
    "Palossand": {
        "name": "Palossand",
        "types": ["Ghost", "Ground"],
        "abilities": ["Water Compaction", "Sand Veil"],
        "stats": {
            "HP": 85,
            "Attack": 75,
            "Defense": 110,
            "Sp. Atk": 100,
            "Sp. Def": 75,
            "Speed": 35,
        },
        "weight": 250.0,
        "fully_evolved": True
    },
    "Komala": {
        "name": "Komala",
        "types": ["Normal"],
        "abilities": ["Comatose"],
        "stats": {
            "HP": 65,
            "Attack": 115,
            "Defense": 65,
            "Sp. Atk": 75,
            "Sp. Def": 95,
            "Speed": 65,
        },
        "weight": 19.9,
        "fully_evolved": True
    },
    "Mimikyu": {
        "name": "Mimikyu",
        "types": ["Ghost", "Fairy"],
        "abilities": ["Disguise"],
        "stats": {
            "HP": 55,
            "Attack": 90,
            "Defense": 80,
            "Sp. Atk": 50,
            "Sp. Def": 105,
            "Speed": 96,
        },
        "weight": 0.7,
        "fully_evolved": True
    },
    "Bruxish": {
        "name": "Bruxish",
        "types": ["Water", "Psychic"],
        "abilities": ["Dazzling", "Strong Jaw", "Wonder Skin"],
        "stats": {
            "HP": 68,
            "Attack": 105,
            "Defense": 70,
            "Sp. Atk": 70,
            "Sp. Def": 70,
            "Speed": 92,
        },
        "weight": 19.0,
        "fully_evolved": True
    },
    "Kommo-o": {
        "name": "Kommo-o",
        "types": ["Dragon", "Fighting"],
        "abilities": ["Bulletproof", "Soundproof"],
        "stats": {
            "HP": 75,
            "Attack": 110,
            "Defense": 125,
            "Sp. Atk": 100,
            "Sp. Def": 105,
            "Speed": 85,
        },
        "weight": 78.2,
        "fully_evolved": True
    },
    "Tapu-Koko": {
        "name": "Tapu-Koko",
        "types": ["Electric", "Fairy"],
        "abilities": ["Electric Surge", "Telepathy"],
        "stats": {
            "HP": 70,
            "Attack": 115,
            "Defense": 85,
            "Sp. Atk": 95,
            "Sp. Def": 75,
            "Speed": 130,
        },
        "weight": 20.5,
        "fully_evolved": True
    },
    "Tapu-Lele": {
        "name": "Tapu-Lele",
        "types": ["Psychic", "Fairy"],
        "abilities": ["Psychic Surge", "Telepathy"],
        "stats": {
            "HP": 70,
            "Attack": 85,
            "Defense": 75,
            "Sp. Atk": 130,
            "Sp. Def": 115,
            "Speed": 95,
        },
        "weight": 18.6,
        "fully_evolved": True
    },
    "Tapu-Bulu": {
        "name": "Tapu-Bulu",
        "types": ["Grass", "Fairy"],
        "abilities": ["Grassy Surge", "Telepathy"],
        "stats": {
            "HP": 70,
            "Attack": 130,
            "Defense": 115,
            "Sp. Atk": 85,
            "Sp. Def": 95,
            "Speed": 75,
        },
        "weight": 45.5,
        "fully_evolved": True
    },
    "Tapu-Fini": {
        "name": "Tapu-Fini",
        "types": ["Water", "Fairy"],
        "abilities": ["Misty Surge", "Telepathy"],
        "stats": {
            "HP": 70,
            "Attack": 75,
            "Defense": 115,
            "Sp. Atk": 95,
            "Sp. Def": 130,
            "Speed": 85,
        },
        "weight": 21.2,
        "fully_evolved": True
    },
    "Solgaleo": {
        "name": "Solgaleo",
        "types": ["Psychic", "Steel"],
        "abilities": ["Full Metal Body"],
        "stats": {
            "HP": 137,
            "Attack": 137,
            "Defense": 107,
            "Sp. Atk": 113,
            "Sp. Def": 89,
            "Speed": 97,
        },
        "weight": 230.0,
        "fully_evolved": True
    },
    "Lunala": {
        "name": "Lunala",
        "types": ["Psychic", "Ghost"],
        "abilities": ["Shadow Shield"],
        "stats": {
            "HP": 137,
            "Attack": 113,
            "Defense": 89,
            "Sp. Atk": 137,
            "Sp. Def": 107,
            "Speed": 97,
        },
        "weight": 120.0,
        "fully_evolved": True
    },
    "Necrozma": {
        "name": "Necrozma",
        "types": ["Psychic"],
        "abilities": ["Prism Armor"],
        "stats": {
            "HP": 97,
            "Attack": 107,
            "Defense": 101,
            "Sp. Atk": 127,
            "Sp. Def": 89,
            "Speed": 79,
        },
        "weight": 230.0,
        "fully_evolved": True
    },
    "Necrozma-Dusk-Mane": {
        "name": "Necrozma-Dusk-Mane",
        "types": ["Psychic", "Steel"],
        "abilities": ["Prism Armor"],
        "stats": {
            "HP": 97,
            "Attack": 157,
            "Defense": 127,
            "Sp. Atk": 113,
            "Sp. Def": 109,
            "Speed": 77,
        },
        "weight": 460.0,
        "fully_evolved": True
    },
    "Necrozma-Dawn-Wings": {
        "name": "Necrozma-Dawn-Wings",
        "types": ["Psychic", "Ghost"],
        "abilities": ["Prism Armor"],
        "stats": {
            "HP": 97,
            "Attack": 113,
            "Defense": 109,
            "Sp. Atk": 157,
            "Sp. Def": 127,
            "Speed": 77,
        },
        "weight": 350.0,
        "fully_evolved": True
    },
    "Magearna": {
        "name": "Magearna",
        "types": ["Steel", "Fairy"],
        "abilities": ["Soul Heart"],
        "stats": {
            "HP": 80,
            "Attack": 95,
            "Defense": 115,
            "Sp. Atk": 130,
            "Sp. Def": 115,
            "Speed": 65,
        },
        "weight": 80.5,
        "fully_evolved": True
    },
    "Rillaboom": {
        "name": "Rillaboom",
        "types": ["Grass"],
        "abilities": ["Overgrow", "Grassy Surge"],
        "stats": {
            "HP": 100,
            "Attack": 125,
            "Defense": 90,
            "Sp. Atk": 60,
            "Sp. Def": 80,
            "Speed": 85,
        },
        "weight": 90.0,
        "fully_evolved": True
    },
    "Cinderace": {
        "name": "Cinderace",
        "types": ["Fire"],
        "abilities": ["Blaze", "Libero"],
        "stats": {
            "HP": 80,
            "Attack": 116,
            "Defense": 75,
            "Sp. Atk": 65,
            "Sp. Def": 75,
            "Speed": 119,
        },
        "weight": 33.0,
        "fully_evolved": True
    },
    "Inteleon": {
        "name": "Inteleon",
        "types": ["Water"],
        "abilities": ["Torrent", "Sniper"],
        "stats": {
            "HP": 70,
            "Attack": 85,
            "Defense": 65,
            "Sp. Atk": 125,
            "Sp. Def": 65,
            "Speed": 120,
        },
        "weight": 45.2,
        "fully_evolved": True
    },
    "Greedent": {
        "name": "Greedent",
        "types": ["Normal"],
        "abilities": ["Cheek Pouch", "Gluttony"],
        "stats": {
            "HP": 120,
            "Attack": 95,
            "Defense": 95,
            "Sp. Atk": 55,
            "Sp. Def": 75,
            "Speed": 20,
        },
        "weight": 6.0,
        "fully_evolved": True
    },
    "Corviknight": {
        "name": "Corviknight",
        "types": ["Flying", "Steel"],
        "abilities": ["Pressure", "Mirror Armor"],
        "stats": {
            "HP": 98,
            "Attack": 87,
            "Defense": 105,
            "Sp. Atk": 53,
            "Sp. Def": 85,
            "Speed": 67,
        },
        "weight": 75.0,
        "fully_evolved": True
    },
    "Drednaw": {
        "name": "Drednaw",
        "types": ["Water", "Rock"],
        "abilities": ["Strong Jaw", "Shell Armor", "Swift Swim"],
        "stats": {
            "HP": 90,
            "Attack": 115,
            "Defense": 90,
            "Sp. Atk": 48,
            "Sp. Def": 68,
            "Speed": 74,
        },
        "weight": 115.5,
        "fully_evolved": True
    },
    "Coalossal": {
        "name": "Coalossal",
        "types": ["Rock", "Fire"],
        "abilities": ["Steam Engine", "Flame Body", "Flash Fire"],
        "stats": {
            "HP": 110,
            "Attack": 80,
            "Defense": 120,
            "Sp. Atk": 80,
            "Sp. Def": 90,
            "Speed": 30,
        },
        "weight": 310.5,
        "fully_evolved": True
    },
    "Flapple": {
        "name": "Flapple",
        "types": ["Grass", "Dragon"],
        "abilities": ["Ripen", "Gluttony", "Hustle"],
        "stats": {
            "HP": 70,
            "Attack": 110,
            "Defense": 80,
            "Sp. Atk": 95,
            "Sp. Def": 60,
            "Speed": 70,
        },
        "weight": 1.0,
        "fully_evolved": True
    },
    "Appletun": {
        "name": "Appletun",
        "types": ["Grass", "Dragon"],
        "abilities": ["Ripen", "Gluttony", "Thick Fat"],
        "stats": {
            "HP": 110,
            "Attack": 85,
            "Defense": 80,
            "Sp. Atk": 100,
            "Sp. Def": 80,
            "Speed": 30,
        },
        "weight": 13.0,
        "fully_evolved": True
    },
    "Sandaconda": {
        "name": "Sandaconda",
        "types": ["Ground"],
        "abilities": ["Sand Spit", "Shed Skin", "Sand Veil"],
        "stats": {
            "HP": 72,
            "Attack": 107,
            "Defense": 125,
            "Sp. Atk": 65,
            "Sp. Def": 70,
            "Speed": 71,
        },
        "weight": 65.5,
        "fully_evolved": True
    },
    "Cramorant": {
        "name": "Cramorant",
        "types": ["Flying", "Water"],
        "abilities": ["Gulp Missile"],
        "stats": {
            "HP": 70,
            "Attack": 85,
            "Defense": 55,
            "Sp. Atk": 85,
            "Sp. Def": 95,
            "Speed": 85,
        },
        "weight": 18.0,
        "fully_evolved": True
    },
    "Barraskewda": {
        "name": "Barraskewda",
        "types": ["Water"],
        "abilities": ["Swift Swim", "Propeller Tail"],
        "stats": {
            "HP": 61,
            "Attack": 123,
            "Defense": 60,
            "Sp. Atk": 60,
            "Sp. Def": 50,
            "Speed": 136,
        },
        "weight": 30.0,
        "fully_evolved": True
    },
    "Toxtricity": {
        "name": "Toxtricity",
        "types": ["Electric", "Poison"],
        "abilities": ["Punk Rock", "Technician"],
        "stats": {
            "HP": 75,
            "Attack": 98,
            "Defense": 70,
            "Sp. Atk": 114,
            "Sp. Def": 70,
            "Speed": 75,
        },
        "weight": 40.0,
        "fully_evolved": True
    },
    "Polteageist": {
        "name": "Polteageist",
        "types": ["Ghost"],
        "abilities": ["Weak Armor", "Cursed Body"],
        "stats": {
            "HP": 60,
            "Attack": 65,
            "Defense": 65,
            "Sp. Atk": 134,
            "Sp. Def": 114,
            "Speed": 70,
        },
        "weight": 0.4,
        "fully_evolved": True
    },
    "Hatterene": {
        "name": "Hatterene",
        "types": ["Psychic", "Fairy"],
        "abilities": ["Healer", "Anticipation", "Magic Bounce"],
        "stats": {
            "HP": 57,
            "Attack": 90,
            "Defense": 95,
            "Sp. Atk": 136,
            "Sp. Def": 103,
            "Speed": 29,
        },
        "weight": 5.1,
        "fully_evolved": True
    },
    "Grimmsnarl": {
        "name": "Grimmsnarl",
        "types": ["Dark", "Fairy"],
        "abilities": ["Prankster", "Frisk"],
        "stats": {
            "HP": 95,
            "Attack": 120,
            "Defense": 65,
            "Sp. Atk": 95,
            "Sp. Def": 75,
            "Speed": 60,
        },
        "weight": 61.0,
        "fully_evolved": True
    },
    "Perrserker": {
        "name": "Perrserker",
        "types": ["Steel"],
        "abilities": ["Battle Armor", "Tough Claws", "Steely Spirit"],
        "stats": {
            "HP": 70,
            "Attack": 110,
            "Defense": 100,
            "Sp. Atk": 50,
            "Sp. Def": 60,
            "Speed": 50,
        },
        "weight": 28.0,
        "fully_evolved": True
    },
    "Alcremie": {
        "name": "Alcremie",
        "types": ["Fairy"],
        "abilities": ["Sweet Veil", "Aroma Veil"],
        "stats": {
            "HP": 65,
            "Attack": 60,
            "Defense": 75,
            "Sp. Atk": 110,
            "Sp. Def": 121,
            "Speed": 64,
        },
        "weight": 0.5,
        "fully_evolved": True
    },
    "Falinks": {
        "name": "Falinks",
        "types": ["Fighting"],
        "abilities": ["Battle Armor", "Defiant"],
        "stats": {
            "HP": 65,
            "Attack": 100,
            "Defense": 100,
            "Sp. Atk": 70,
            "Sp. Def": 60,
            "Speed": 75,
        },
        "weight": 62.0,
        "fully_evolved": True
    },
    "Pincurchin": {
        "name": "Pincurchin",
        "types": ["Electric"],
        "abilities": ["Lightning Rod", "Electric Surge"],
        "stats": {
            "HP": 48,
            "Attack": 101,
            "Defense": 95,
            "Sp. Atk": 91,
            "Sp. Def": 85,
            "Speed": 15,
        },
        "weight": 1.0,
        "fully_evolved": True
    },
    "Frosmoth": {
        "name": "Frosmoth",
        "types": ["Ice", "Bug"],
        "abilities": ["Shield Dust", "Ice Scales"],
        "stats": {
            "HP": 70,
            "Attack": 65,
            "Defense": 60,
            "Sp. Atk": 125,
            "Sp. Def": 90,
            "Speed": 65,
        },
        "weight": 42.0,
        "fully_evolved": True
    },
    "Stonjourner": {
        "name": "Stonjourner",
        "types": ["Rock"],
        "abilities": ["Power Spot"],
        "stats": {
            "HP": 100,
            "Attack": 125,
            "Defense": 135,
            "Sp. Atk": 20,
            "Sp. Def": 20,
            "Speed": 70,
        },
        "weight": 520.0,
        "fully_evolved": True
    },
    "Indeedee-Male": {
        "name": "Indeedee-Male",
        "types": ["Psychic", "Normal"],
        "abilities": ["Inner Focus", "Synchronize", "Psychic Surge"],
        "stats": {
            "HP": 60,
            "Attack": 65,
            "Defense": 55,
            "Sp. Atk": 105,
            "Sp. Def": 95,
            "Speed": 95,
        },
        "weight": 28.0,
        "fully_evolved": True
    },
    "Indeedee-Female": {
        "name": "Indeedee-Female",
        "types": ["Psychic", "Normal"],
        "abilities": ["Own Tempo", "Synchronize", "Psychic Surge"],
        "stats": {
            "HP": 70,
            "Attack": 55,
            "Defense": 65,
            "Sp. Atk": 95,
            "Sp. Def": 105,
            "Speed": 85,
        },
        "weight": 28.0,
        "fully_evolved": True
    },
    "Morpeko-Full-Belly": {
        "name": "Morpeko-Full-Belly",
        "types": ["Electric", "Dark"],
        "abilities": ["Hunger Switch"],
        "stats": {
            "HP": 58,
            "Attack": 95,
            "Defense": 58,
            "Sp. Atk": 70,
            "Sp. Def": 58,
            "Speed": 97,
        },
        "weight": 3.0,
        "fully_evolved": True
    },
    "Morpeko-Hangry": {
        "name": "Morpeko-Hangry",
        "types": ["Electric", "Dark"],
        "abilities": ["Hunger Switch"],
        "stats": {
            "HP": 58,
            "Attack": 95,
            "Defense": 58,
            "Sp. Atk": 70,
            "Sp. Def": 58,
            "Speed": 97,
        },
        "weight": 3.0,
        "fully_evolved": True
    },
    "Copperajah": {
        "name": "Copperajah",
        "types": ["Steel"],
        "abilities": ["Sheer Force", "Heavy Metal"],
        "stats": {
            "HP": 122,
            "Attack": 130,
            "Defense": 69,
            "Sp. Atk": 80,
            "Sp. Def": 69,
            "Speed": 30,
        },
        "weight": 650.0,
        "fully_evolved": True
    },
    "Duraludon": {
        "name": "Duraludon",
        "types": ["Steel", "Dragon"],
        "abilities": ["Light Metal", "Heavy Metal", "Stalwart"],
        "stats": {
            "HP": 70,
            "Attack": 95,
            "Defense": 115,
            "Sp. Atk": 120,
            "Sp. Def": 50,
            "Speed": 85,
        },
        "weight": 40.0,
        "fully_evolved": False
    },
    "Archaludon": {
        "name": "Archaludon",
        "types": ["Steel", "Dragon"],
        "abilities": ["Sturdy", "Stalwart", "Stamina"],
        "stats": {
            "HP": 90,
            "Attack": 105,
            "Defense": 130,
            "Sp. Atk": 125,
            "Sp. Def": 65,
            "Speed": 85,
        },
        "weight": 60.0,
        "fully_evolved": False
    },
    "Dragapult": {
        "name": "Dragapult",
        "types": ["Dragon", "Ghost"],
        "abilities": ["Clear Body", "Infiltrator"],
        "stats": {
            "HP": 88,
            "Attack": 120,
            "Defense": 75,
            "Sp. Atk": 100,
            "Sp. Def": 75,
            "Speed": 142,
        },
        "weight": 50.5,
        "fully_evolved": True
    },
    "Zacian": {
        "name": "Zacian",
        "types": ["Fairy"],
        "abilities": ["Intrepid Sword"],
        "stats": {
            "HP": 92,
            "Attack": 130,
            "Defense": 115,
            "Sp. Atk": 80,
            "Sp. Def": 115,
            "Speed": 138,
        },
        "weight": 210.0,
        "fully_evolved": True
    },
    "Zamazenta": {
        "name": "Zamazenta",
        "types": ["Fighting"],
        "abilities": ["Dauntless Shield"],
        "stats": {
            "HP": 92,
            "Attack": 130,
            "Defense": 115,
            "Sp. Atk": 80,
            "Sp. Def": 115,
            "Speed": 138,
        },
        "weight": 210.0,
        "fully_evolved": True
    },
    "Eternatus": {
        "name": "Eternatus",
        "types": ["Poison", "Dragon"],
        "abilities": ["Pressure"],
        "stats": {
            "HP": 140,
            "Attack": 85,
            "Defense": 95,
            "Sp. Atk": 145,
            "Sp. Def": 95,
            "Speed": 130,
        },
        "weight": 950.0,
        "fully_evolved": True
    },
    "Urshifu-Single-Strike": {
        "name": "Urshifu-Single-Strike",
        "types": ["Fighting", "Dark"],
        "abilities": ["Unseen Fist"],
        "stats": {
            "HP": 100,
            "Attack": 130,
            "Defense": 100,
            "Sp. Atk": 63,
            "Sp. Def": 60,
            "Speed": 97,
        },
        "weight": 105.0,
        "fully_evolved": True
    },
    "Urshifu-Rapid-Strike": {
        "name": "Urshifu-Rapid-Strike",
        "types": ["Fighting", "Water"],
        "abilities": ["Unseen Fist"],
        "stats": {
            "HP": 100,
            "Attack": 130,
            "Defense": 100,
            "Sp. Atk": 63,
            "Sp. Def": 60,
            "Speed": 97,
        },
        "weight": 105.0,
        "fully_evolved": True
    },
    "Zarude": {
        "name": "Zarude",
        "types": ["Dark", "Grass"],
        "abilities": ["Leaf Guard"],
        "stats": {
            "HP": 105,
            "Attack": 120,
            "Defense": 105,
            "Sp. Atk": 70,
            "Sp. Def": 95,
            "Speed": 105,
        },
        "weight": 70.0,
        "fully_evolved": True
    },
    "Regieleki": {
        "name": "Regieleki",
        "types": ["Electric"],
        "abilities": ["Transistor"],
        "stats": {
            "HP": 80,
            "Attack": 100,
            "Defense": 50,
            "Sp. Atk": 100,
            "Sp. Def": 50,
            "Speed": 200,
        },
        "weight": 145.0,
        "fully_evolved": True
    },
    "Regidrago": {
        "name": "Regidrago",
        "types": ["Dragon"],
        "abilities": ["Dragons Maw"],
        "stats": {
            "HP": 200,
            "Attack": 100,
            "Defense": 50,
            "Sp. Atk": 100,
            "Sp. Def": 50,
            "Speed": 80,
        },
        "weight": 200.0,
        "fully_evolved": True
    },
    "Glastrier": {
        "name": "Glastrier",
        "types": ["Ice"],
        "abilities": ["Chilling Neigh"],
        "stats": {
            "HP": 100,
            "Attack": 145,
            "Defense": 130,
            "Sp. Atk": 65,
            "Sp. Def": 110,
            "Speed": 30,
        },
        "weight": 800.0,
        "fully_evolved": True
    },
    "Spectrier": {
        "name": "Spectrier",
        "types": ["Ghost"],
        "abilities": ["Grim Neigh"],
        "stats": {
            "HP": 100,
            "Attack": 65,
            "Defense": 60,
            "Sp. Atk": 145,
            "Sp. Def": 80,
            "Speed": 130,
        },
        "weight": 44.5,
        "fully_evolved": True
    },
    "Calyrex": {
        "name": "Calyrex",
        "types": ["Psychic", "Grass"],
        "abilities": ["Unnerve"],
        "stats": {
            "HP": 100,
            "Attack": 80,
            "Defense": 80,
            "Sp. Atk": 80,
            "Sp. Def": 80,
            "Speed": 80,
        },
        "weight": 7.7,
        "fully_evolved": True
    },
    "Calyrex-Shadow-Rider": {
        "name": "Calyrex-Shadow-Rider",
        "types": ["Psychic", "Ghost"],
        "abilities": ["As One Spectrier"],
        "stats": {
            "HP": 100,
            "Attack": 85,
            "Defense": 80,
            "Sp. Atk": 165,
            "Sp. Def": 100,
            "Speed": 150,
        },
        "weight": 53.6,
        "fully_evolved": True
    },
    "Calyrex-Ice-Rider": {
        "name": "Calyrex-Ice-Rider",
        "types": ["Psychic", "Ice"],
        "abilities": ["As One Glastrier"],
        "stats": {
            "HP": 100,
            "Attack": 165,
            "Defense": 150,
            "Sp. Atk": 85,
            "Sp. Def": 130,
            "Speed": 50,
        },
        "weight": 809.1,
        "fully_evolved": True
    },
    "Ursaluna": {
        "name": "Ursaluna",
        "types": ["Ground", "Normal"],
        "abilities": ["Guts", "Bulletproof", "Unnerve"],
        "stats": {
            "HP": 130,
            "Attack": 140,
            "Defense": 105,
            "Sp. Atk": 45,
            "Sp. Def": 80,
            "Speed": 50,
        },
        "weight": 290.0,
        "fully_evolved": True
    },
    "Wyrdeer": {
        "name": "Wyrdeer",
        "types": ["Normal", "Psychic"],
        "abilities": ["Intimidate", "Frisk", "Sap Sipper"],
        "stats": {
            "HP": 103,
            "Attack": 105,
            "Defense": 72,
            "Sp. Atk": 105,
            "Sp. Def": 75,
            "Speed": 65,
        },
        "weight": 95.1,
        "fully_evolved": True
    },
    "Kleavor": {
        "name": "Kleavor",
        "types": ["Bug", "Rock"],
        "abilities": ["Sharpness", "Swarm", "Sheer Force"],
        "stats": {
            "HP": 70,
            "Attack": 135,
            "Defense": 95,
            "Sp. Atk": 45,
            "Sp. Def": 70,
            "Speed": 85,
        },
        "weight": 45.0,
        "fully_evolved": True
    },
    "Basculegion-Male": {
        "name": "Basculegion-Male",
        "types": ["Water", "Ghost"],
        "abilities": ["Swift Swim", "Adaptability", "Mold Breaker"],
        "stats": {
            "HP": 120,
            "Attack": 112,
            "Defense": 65,
            "Sp. Atk": 80,
            "Sp. Def": 75,
            "Speed": 78,
        },
        "weight": 110.0,
        "fully_evolved": True
    },
    "Basculegion-Female": {
        "name": "Basculegion-Female",
        "types": ["Water", "Ghost"],
        "abilities": ["Swift Swim", "Adaptability", "Mold Breaker"],
        "stats": {
            "HP": 120,
            "Attack": 92,
            "Defense": 65,
            "Sp. Atk": 100,
            "Sp. Def": 75,
            "Speed": 78,
        },
        "weight": 110.0,
        "fully_evolved": True
    },
    "Sneasler": {
        "name": "Sneasler",
        "types": ["Fighting", "Poison"],
        "abilities": ["Pressure", "Unburden", "Poison Touch"],
        "stats": {
            "HP": 80,
            "Attack": 130,
            "Defense": 60,
            "Sp. Atk": 40,
            "Sp. Def": 80,
            "Speed": 120,
        },
        "weight": 43.0,
        "fully_evolved": True
    },
    "Overqwil": {
        "name": "Overqwil",
        "types": ["Dark", "Poison"],
        "abilities": ["Poison Point", "Swift Swim", "Intimidate"],
        "stats": {
            "HP": 85,
            "Attack": 115,
            "Defense": 95,
            "Sp. Atk": 65,
            "Sp. Def": 65,
            "Speed": 85,
        },
        "weight": 60.5,
        "fully_evolved": True
    },
    "Enamorus-Incarnate": {
        "name": "Enamorus-Incarnate",
        "types": ["Fairy", "Flying"],
        "abilities": ["Cute Charm", "Contrary"],
        "stats": {
            "HP": 74,
            "Attack": 115,
            "Defense": 70,
            "Sp. Atk": 135,
            "Sp. Def": 80,
            "Speed": 106,
        },
        "weight": 48.0,
        "fully_evolved": True
    },
    "Enamorus-Therian": {
        "name": "Enamorus-Therian",
        "types": ["Fairy", "Flying"],
        "abilities": ["Overcoat"],
        "stats": {
            "HP": 74,
            "Attack": 115,
            "Defense": 110,
            "Sp. Atk": 135,
            "Sp. Def": 100,
            "Speed": 46,
        },
        "weight": 48.0,
        "fully_evolved": True
    },
    "Meowscarada": {
        "name": "Meowscarada",
        "types": ["Grass", "Dark"],
        "abilities": ["Overgrow", "Protean"],
        "stats": {
            "HP": 76,
            "Attack": 110,
            "Defense": 70,
            "Sp. Atk": 81,
            "Sp. Def": 70,
            "Speed": 123,
        },
        "weight": 33.0,
        "fully_evolved": True
    },
    "Skeledirge": {
        "name": "Skeledirge",
        "types": ["Fire", "Ghost"],
        "abilities": ["Blaze", "Unaware"],
        "stats": {
            "HP": 104,
            "Attack": 75,
            "Defense": 100,
            "Sp. Atk": 110,
            "Sp. Def": 75,
            "Speed": 66,
        },
        "weight": 150.0,
        "fully_evolved": True
    },
    "Quaquaval": {
        "name": "Quaquaval",
        "types": ["Water", "Fighting"],
        "abilities": ["Torrent", "Moxie"],
        "stats": {
            "HP": 85,
            "Attack": 120,
            "Defense": 80,
            "Sp. Atk": 85,
            "Sp. Def": 75,
            "Speed": 85,
        },
        "weight": 70.0,
        "fully_evolved": True
    },
    "Spidops": {
        "name": "Spidops",
        "types": ["Bug"],
        "abilities": ["Insomnia", "Stakeout"],
        "stats": {
            "HP": 60,
            "Attack": 79,
            "Defense": 92,
            "Sp. Atk": 52,
            "Sp. Def": 86,
            "Speed": 35,
        },
        "weight": 16.5,
        "fully_evolved": True
    },
    "Lokix": {
        "name": "Lokix",
        "types": ["Bug", "Dark"],
        "abilities": ["Swarm", "Tinted Lens"],
        "stats": {
            "HP": 71,
            "Attack": 102,
            "Defense": 78,
            "Sp. Atk": 52,
            "Sp. Def": 55,
            "Speed": 92,
        },
        "weight": 17.5,
        "fully_evolved": True
    },
    "Pawmot": {
        "name": "Pawmot",
        "types": ["Electric", "Fighting"],
        "abilities": ["Volt Absorb", "Natural Cure", "Iron Fist"],
        "stats": {
            "HP": 70,
            "Attack": 115,
            "Defense": 70,
            "Sp. Atk": 70,
            "Sp. Def": 60,
            "Speed": 105,
        },
        "weight": 41.0,
        "fully_evolved": True
    },
    "Maushold": {
        "name": "Maushold",
        "types": ["Normal"],
        "abilities": ["Friend Guard", "Technician"],
        "stats": {
            "HP": 74,
            "Attack": 75,
            "Defense": 70,
            "Sp. Atk": 65,
            "Sp. Def": 75,
            "Speed": 111,
        },
        "weight": 2.3,
        "fully_evolved": True
    },
    "Dachsbun": {
        "name": "Dachsbun",
        "types": ["Fairy"],
        "abilities": ["Well Baked Body", "Aroma Veil"],
        "stats": {
            "HP": 57,
            "Attack": 80,
            "Defense": 115,
            "Sp. Atk": 50,
            "Sp. Def": 80,
            "Speed": 95,
        },
        "weight": 14.9,
        "fully_evolved": True
    },
    "Arboliva": {
        "name": "Arboliva",
        "types": ["Grass", "Normal"],
        "abilities": ["Seed Sower", "Harvest"],
        "stats": {
            "HP": 78,
            "Attack": 69,
            "Defense": 90,
            "Sp. Atk": 125,
            "Sp. Def": 109,
            "Speed": 39,
        },
        "weight": 48.2,
        "fully_evolved": True
    },
    "Garganacl": {
        "name": "Garganacl",
        "types": ["Rock"],
        "abilities": ["Purifying Salt", "Sturdy", "Clear Body"],
        "stats": {
            "HP": 100,
            "Attack": 100,
            "Defense": 130,
            "Sp. Atk": 45,
            "Sp. Def": 90,
            "Speed": 35,
        },
        "weight": 240.0,
        "fully_evolved": True
    },
    "Charcadet": {
        "name": "Charcadet",
        "types": ["Fire"],
        "abilities": ["Flash Fire", "Flame Body"],
        "stats": {
            "HP": 40,
            "Attack": 50,
            "Defense": 40,
            "Sp. Atk": 50,
            "Sp. Def": 40,
            "Speed": 35,
        },
        "weight": 10.5,
        "fully_evolved": True
    },
    "Armarouge": {
        "name": "Armarouge",
        "types": ["Fire", "Psychic"],
        "abilities": ["Flash Fire", "Infiltrator"],
        "stats": {
            "HP": 85,
            "Attack": 60,
            "Defense": 100,
            "Sp. Atk": 125,
            "Sp. Def": 80,
            "Speed": 75,
        },
        "weight": 85.0,
        "fully_evolved": True
    },
    "Ceruledge": {
        "name": "Ceruledge",
        "types": ["Fire", "Ghost"],
        "abilities": ["Flash Fire", "Infiltrator"],
        "stats": {
            "HP": 75,
            "Attack": 125,
            "Defense": 80,
            "Sp. Atk": 60,
            "Sp. Def": 100,
            "Speed": 85,
        },
        "weight": 62.0,
        "fully_evolved": True
    },
    "Bellibolt": {
        "name": "Bellibolt",
        "types": ["Electric"],
        "abilities": ["Electromorphosis", "Static", "Damp"],
        "stats": {
            "HP": 109,
            "Attack": 64,
            "Defense": 91,
            "Sp. Atk": 103,
            "Sp. Def": 83,
            "Speed": 45,
        },
        "weight": 113.0,
        "fully_evolved": True
    },
    "Kilowattrel": {
        "name": "Kilowattrel",
        "types": ["Electric", "Flying"],
        "abilities": ["Wind Power", "Volt Absorb", "Competitive"],
        "stats": {
            "HP": 70,
            "Attack": 70,
            "Defense": 60,
            "Sp. Atk": 105,
            "Sp. Def": 60,
            "Speed": 125,
        },
        "weight": 38.6,
        "fully_evolved": True
    },
    "Mabosstiff": {
        "name": "Mabosstiff",
        "types": ["Dark"],
        "abilities": ["Intimidate", "Guard Dog", "Stakeout"],
        "stats": {
            "HP": 80,
            "Attack": 120,
            "Defense": 90,
            "Sp. Atk": 60,
            "Sp. Def": 70,
            "Speed": 85,
        },
        "weight": 61.0,
        "fully_evolved": True
    },
    "Grafaiai": {
        "name": "Grafaiai",
        "types": ["Poison", "Normal"],
        "abilities": ["Unburden", "Poison Touch", "Prankster"],
        "stats": {
            "HP": 63,
            "Attack": 95,
            "Defense": 65,
            "Sp. Atk": 80,
            "Sp. Def": 72,
            "Speed": 110,
        },
        "weight": 27.2,
        "fully_evolved": True
    },
    "Brambleghast": {
        "name": "Brambleghast",
        "types": ["Grass", "Ghost"],
        "abilities": ["Harvest", "Infiltrator"],
        "stats": {
            "HP": 55,
            "Attack": 115,
            "Defense": 70,
            "Sp. Atk": 80,
            "Sp. Def": 70,
            "Speed": 90,
        },
        "weight": 6.0,
        "fully_evolved": True
    },
    "Toedscruel": {
        "name": "Toedscruel",
        "types": ["Ground", "Grass"],
        "abilities": ["Mycelium Might", "Mycelium Might"],
        "stats": {
            "HP": 80,
            "Attack": 70,
            "Defense": 65,
            "Sp. Atk": 80,
            "Sp. Def": 120,
            "Speed": 100,
        },
        "weight": 58.0,
        "fully_evolved": True
    },
    "Klawf": {
        "name": "Klawf",
        "types": ["Rock"],
        "abilities": ["Anger Shell", "Shell Armor", "Regenerator"],
        "stats": {
            "HP": 70,
            "Attack": 100,
            "Defense": 115,
            "Sp. Atk": 35,
            "Sp. Def": 55,
            "Speed": 75,
        },
        "weight": 79.0,
        "fully_evolved": True
    },
    "Scovillain": {
        "name": "Scovillain",
        "types": ["Grass", "Fire"],
        "abilities": ["Chlorophyll", "Insomnia", "Moody"],
        "stats": {
            "HP": 65,
            "Attack": 108,
            "Defense": 65,
            "Sp. Atk": 108,
            "Sp. Def": 65,
            "Speed": 75,
        },
        "weight": 15.0,
        "fully_evolved": True
    },
    "Rabsca": {
        "name": "Rabsca",
        "types": ["Bug", "Psychic"],
        "abilities": ["Synchronize", "Telepathy"],
        "stats": {
            "HP": 75,
            "Attack": 50,
            "Defense": 85,
            "Sp. Atk": 115,
            "Sp. Def": 100,
            "Speed": 45,
        },
        "weight": 3.5,
        "fully_evolved": True
    },
    "Espathra": {
        "name": "Espathra",
        "types": ["Psychic"],
        "abilities": ["Opportunist", "Speed Boost"],
        "stats": {
            "HP": 95,
            "Attack": 60,
            "Defense": 60,
            "Sp. Atk": 101,
            "Sp. Def": 60,
            "Speed": 105,
        },
        "weight": 50.0,
        "fully_evolved": True
    },
    "Tinkaton": {
        "name": "Tinkaton",
        "types": ["Fairy", "Steel"],
        "abilities": ["Mold Breaker", "Own Tempo", "Pickpocket"],
        "stats": {
            "HP": 85,
            "Attack": 75,
            "Defense": 77,
            "Sp. Atk": 70,
            "Sp. Def": 105,
            "Speed": 94,
        },
        "weight": 112.8,
        "fully_evolved": True
    },
    "Wugtrio": {
        "name": "Wugtrio",
        "types": ["Water"],
        "abilities": ["Gooey", "Rattled", "Sand Veil"],
        "stats": {
            "HP": 35,
            "Attack": 100,
            "Defense": 50,
            "Sp. Atk": 50,
            "Sp. Def": 70,
            "Speed": 120,
        },
        "weight": 5.4,
        "fully_evolved": True
    },
    "Bombirdier": {
        "name": "Bombirdier",
        "types": ["Flying", "Dark"],
        "abilities": ["Big Pecks", "Keen Eye", "Rocky Payload"],
        "stats": {
            "HP": 70,
            "Attack": 103,
            "Defense": 85,
            "Sp. Atk": 60,
            "Sp. Def": 85,
            "Speed": 82,
        },
        "weight": 42.9,
        "fully_evolved": True
    },
    "Revavroom": {
        "name": "Revavroom",
        "types": ["Steel", "Poison"],
        "abilities": ["Overcoat", "Filter"],
        "stats": {
            "HP": 80,
            "Attack": 119,
            "Defense": 90,
            "Sp. Atk": 54,
            "Sp. Def": 67,
            "Speed": 90,
        },
        "weight": 120.0,
        "fully_evolved": True
    },
    "Cyclizar": {
        "name": "Cyclizar",
        "types": ["Dragon", "Normal"],
        "abilities": ["Shed Skin", "Regenerator"],
        "stats": {
            "HP": 70,
            "Attack": 95,
            "Defense": 65,
            "Sp. Atk": 85,
            "Sp. Def": 65,
            "Speed": 121,
        },
        "weight": 63.0,
        "fully_evolved": True
    },
    "Orthworm": {
        "name": "Orthworm",
        "types": ["Steel"],
        "abilities": ["Earth Eater", "Sand Veil"],
        "stats": {
            "HP": 70,
            "Attack": 85,
            "Defense": 145,
            "Sp. Atk": 60,
            "Sp. Def": 55,
            "Speed": 65,
        },
        "weight": 310.0,
        "fully_evolved": True
    },
    "Glimmora": {
        "name": "Glimmora",
        "types": ["Rock", "Poison"],
        "abilities": ["Toxic Debris"],
        "stats": {
            "HP": 80,
            "Attack": 110,
            "Defense": 70,
            "Sp. Atk": 130,
            "Sp. Def": 80,
            "Speed": 100,
        },
        "weight": 40.0,
        "fully_evolved": True
    },
    "Houndstone": {
        "name": "Houndstone",
        "types": ["Ghost"],
        "abilities": ["Sand Rush", "Fluffy"],
        "stats": {
            "HP": 72,
            "Attack": 101,
            "Defense": 100,
            "Sp. Atk": 50,
            "Sp. Def": 97,
            "Speed": 68,
        },
        "weight": 15.0,
        "fully_evolved": True
    },
    "Flamigo": {
        "name": "Flamigo",
        "types": ["Flying", "Fighting"],
        "abilities": ["Scrappy", "Tangled Feet", "Costar"],
        "stats": {
            "HP": 82,
            "Attack": 115,
            "Defense": 74,
            "Sp. Atk": 75,
            "Sp. Def": 64,
            "Speed": 90,
        },
        "weight": 37.0,
        "fully_evolved": True
    },
    "Cetitan": {
        "name": "Cetitan",
        "types": ["Ice"],
        "abilities": ["Thick Fat", "Slush Rush", "Sheer Force"],
        "stats": {
            "HP": 170,
            "Attack": 113,
            "Defense": 65,
            "Sp. Atk": 45,
            "Sp. Def": 55,
            "Speed": 73,
        },
        "weight": 700.0,
        "fully_evolved": True
    },
    "Veluza": {
        "name": "Veluza",
        "types": ["Water", "Psychic"],
        "abilities": ["Mold Breaker", "Sharpness"],
        "stats": {
            "HP": 90,
            "Attack": 102,
            "Defense": 73,
            "Sp. Atk": 78,
            "Sp. Def": 65,
            "Speed": 70,
        },
        "weight": 90.0,
        "fully_evolved": True
    },
    "Dondozo": {
        "name": "Dondozo",
        "types": ["Water"],
        "abilities": ["Unaware", "Oblivious", "Water Veil"],
        "stats": {
            "HP": 150,
            "Attack": 100,
            "Defense": 115,
            "Sp. Atk": 65,
            "Sp. Def": 65,
            "Speed": 35,
        },
        "weight": 220.0,
        "fully_evolved": True
    }, 
    "Tatsugiri": {
        "name": "Tatsugiri",
        "types": ["Dragon", "Water"],
        "abilities": ["Commander", "Storm Drain"],
        "stats": {
            "HP": 68,
            "Attack": 50,
            "Defense": 60,
            "Sp. Atk": 120,
            "Sp. Def": 95,
            "Speed": 82,
        },
        "weight": 8.0,
        "fully_evolved": True
    },
    "Annihilape": {
        "name": "Annihilape",
        "types": ["Fighting", "Ghost"],
        "abilities": ["Defiant"],
        "stats": {
            "HP": 110,
            "Attack": 115,
            "Defense": 70,
            "Sp. Atk": 50,
            "Sp. Def": 80,
            "Speed": 90,
        },
        "weight": 61.0,
        "fully_evolved": True
    },
    "Clodsire": {
        "name": "Clodsire",
        "types": ["Poison", "Ground"],
        "abilities": ["Poison Point", "Water Absorb", "Unaware"],
        "stats": {
            "HP": 130,
            "Attack": 75,
            "Defense": 60,
            "Sp. Atk": 45,
            "Sp. Def": 100,
            "Speed": 20,
        },
        "weight": 223.0,
        "fully_evolved": True
    },
    "Farigiraf": {
        "name": "Farigiraf",
        "types": ["Normal", "Psychic"],
        "abilities": ["Cud Chew", "Armor Tail", "Sap Sipper"],
        "stats": {
            "HP": 120,
            "Attack": 90,
            "Defense": 70,
            "Sp. Atk": 110,
            "Sp. Def": 70,
            "Speed": 60,
        },
        "weight": 160.0,
        "fully_evolved": True
    },
    "Kingambit": {
        "name": "Kingambit",
        "types": ["Dark", "Steel"],
        "abilities": ["Defiant"],
        "stats": {
            "HP": 100,
            "Attack": 135,
            "Defense": 120,
            "Sp. Atk": 60,
            "Sp. Def": 85,
            "Speed": 50,
        },
        "weight": 110.0,
        "fully_evolved": True
    },
    "Great-Tusk": {
        "name": "Great-Tusk",
        "types": ["Ground", "Fighting"],
        "abilities": ["Protosynthesis"],
        "stats": {
            "HP": 115,
            "Attack": 131,
            "Defense": 131,
            "Sp. Atk": 53,
            "Sp. Def": 53,
            "Speed": 87,
        },
        "weight": 320.0,
        "fully_evolved": True
    },
    "Scream-Tail": {
        "name": "Scream-Tail",
        "types": ["Fairy", "Psychic"],
        "abilities": ["Protosynthesis"],
        "stats": {
            "HP": 115,
            "Attack": 65,
            "Defense": 99,
            "Sp. Atk": 65,
            "Sp. Def": 115,
            "Speed": 111,
        },
        "weight": 8.0,
        "fully_evolved": True
    },
    "Brute-Bonnet": {
        "name": "Brute-Bonnet",
        "types": ["Grass", "Dark"],
        "abilities": ["Protosynthesis"],
        "stats": {
            "HP": 111,
            "Attack": 127,
            "Defense": 99,
            "Sp. Atk": 79,
            "Sp. Def": 99,
            "Speed": 55,
        },
        "weight": 21.0,
        "fully_evolved": True
    },
    "Flutter-Mane": {
        "name": "Flutter-Mane",
        "types": ["Ghost", "Fairy"],
        "abilities": ["Protosynthesis"],
        "stats": {
            "HP": 55,
            "Attack": 55,
            "Defense": 55,
            "Sp. Atk": 135,
            "Sp. Def": 135,
            "Speed": 135,
        },
        "weight": 4.0,
        "fully_evolved": True
    },
    "Slither-Wing": {
        "name": "Slither-Wing",
        "types": ["Bug", "Fighting"],
        "abilities": ["Protosynthesis"],
        "stats": {
            "HP": 85,
            "Attack": 135,
            "Defense": 79,
            "Sp. Atk": 85,
            "Sp. Def": 105,
            "Speed": 81,
        },
        "weight": 92.0,
        "fully_evolved": True
    },
    "Sandy-Shocks": {
        "name": "Sandy-Shocks",
        "types": ["Electric", "Ground"],
        "abilities": ["Protosynthesis"],
        "stats": {
            "HP": 85,
            "Attack": 81,
            "Defense": 97,
            "Sp. Atk": 121,
            "Sp. Def": 85,
            "Speed": 101,
        },
        "weight": 60.0,
        "fully_evolved": True
    },
    "Iron-Treads": {
        "name": "Iron-Treads",
        "types": ["Ground", "Steel"],
        "abilities": ["Quark Drive"],
        "stats": {
            "HP": 90,
            "Attack": 112,
            "Defense": 120,
            "Sp. Atk": 72,
            "Sp. Def": 70,
            "Speed": 106,
        },
        "weight": 240.0,
        "fully_evolved": True
    },
    "Iron-Bundle": {
        "name": "Iron-Bundle",
        "types": ["Ice", "Water"],
        "abilities": ["Quark Drive"],
        "stats": {
            "HP": 56,
            "Attack": 80,
            "Defense": 114,
            "Sp. Atk": 124,
            "Sp. Def": 60,
            "Speed": 136,
        },
        "weight": 11.0,
        "fully_evolved": True
    },
    "Iron-Hands": {
        "name": "Iron-Hands",
        "types": ["Fighting", "Electric"],
        "abilities": ["Quark Drive"],
        "stats": {
            "HP": 154,
            "Attack": 140,
            "Defense": 108,
            "Sp. Atk": 50,
            "Sp. Def": 68,
            "Speed": 50,
        },
        "weight": 380.7,
        "fully_evolved": True
    },
    "Iron-Jugulis": {
        "name": "Iron-Jugulis",
        "types": ["Dark", "Flying"],
        "abilities": ["Quark Drive"],
        "stats": {
            "HP": 94,
            "Attack": 80,
            "Defense": 86,
            "Sp. Atk": 122,
            "Sp. Def": 80,
            "Speed": 108,
        },
        "weight": 111.0,
        "fully_evolved": True
    },
    "Iron-Moth": {
        "name": "Iron-Moth",
        "types": ["Fire", "Poison"],
        "abilities": ["Quark Drive"],
        "stats": {
            "HP": 80,
            "Attack": 70,
            "Defense": 60,
            "Sp. Atk": 140,
            "Sp. Def": 110,
            "Speed": 110,
        },
        "weight": 36.0,
        "fully_evolved": True
    },
    "Iron-Thorns": {
        "name": "Iron-Thorns",
        "types": ["Rock", "Electric"],
        "abilities": ["Quark Drive"],
        "stats": {
            "HP": 100,
            "Attack": 134,
            "Defense": 110,
            "Sp. Atk": 70,
            "Sp. Def": 84,
            "Speed": 72,
        },
        "weight": 303.0,
        "fully_evolved": True
    },
    "Baxcalibur": {
        "name": "Baxcalibur",
        "types": ["Dragon"],
        "abilities": ["Thermal Exchange", "Ice Body"],
        "stats": {
            "HP": 115,
            "Attack": 145,
            "Defense": 92,
            "Sp. Atk": 75,
            "Sp. Def": 86,
            "Speed": 87,
        },
        "weight": 210.0,
        "fully_evolved": True
    },
    "Gholdengo": {
        "name": "Gholdengo",
        "types": ["Steel", "Ghost"],
        "abilities": ["Good as Gold"],
        "stats": {
            "HP": 87,
            "Attack": 60,
            "Defense": 95,
            "Sp. Atk": 133,
            "Sp. Def": 91,
            "Speed": 84,
        },
        "weight": 30.0,
        "fully_evolved": True
    },
    "Wo-Chien": {
        "name": "Wo-Chien",
        "types": ["Grass", "Dark"],
        "abilities": ["Tablets of Ruin"],
        "stats": {
            "HP": 85,
            "Attack": 85,
            "Defense": 100,
            "Sp. Atk": 95,
            "Sp. Def": 135,
            "Speed": 70,
        },
        "weight": 120.0,
        "fully_evolved": True
    },
    "Chien-Pao": {
        "name": "Chien-Pao",
        "types": ["Dark", "Ice"],
        "abilities": ["Sword of Ruin"],
        "stats": {
            "HP": 80,
            "Attack": 120,
            "Defense": 80,
            "Sp. Atk": 90,
            "Sp. Def": 65,
            "Speed": 135,
        },
        "weight": 152.2,
        "fully_evolved": True
    },
    "Ting-Lu": {
        "name": "Ting-Lu",
        "types": ["Ground", "Dark"],
        "abilities": ["Vessel of Ruin"],
        "stats": {
            "HP": 155,
            "Attack": 110,
            "Defense": 125,
            "Sp. Atk": 55,
            "Sp. Def": 80,
            "Speed": 45,
        },
        "weight": 220.0,
        "fully_evolved": True
    },
    "Chi-Yu": {
        "name": "Chi-Yu",
        "types": ["Fire", "Dark"],
        "abilities": ["Beads of Ruin"],
        "stats": {
            "HP": 55,
            "Attack": 80,
            "Defense": 80,
            "Sp. Atk": 135,
            "Sp. Def": 120,
            "Speed": 100,
        },
        "weight": 20.0,
        "fully_evolved": True
    },
    "Roaring Moon": {
        "name": "Roaring Moon",
        "types": ["Dragon", "Dark"],
        "abilities": ["Protosynthesis"],
        "stats": {
            "HP": 105,
            "Attack": 139,
            "Defense": 71,
            "Sp. Atk": 55,
            "Sp. Def": 101,
            "Speed": 119,
        },
        "weight": 380.0,
        "fully_evolved": True
    },
    "Iron-Valiant": {
        "name": "Iron-Valiant",
        "types": ["Fairy", "Fighting"],
        "abilities": ["Quark Drive"],
        "stats": {
            "HP": 74,
            "Attack": 130,
            "Defense": 90,
            "Sp. Atk": 120,
            "Sp. Def": 60,
            "Speed": 116,
        },
        "weight": 35.0,
        "fully_evolved": True
    },
    "Koraidon": {
        "name": "Koraidon",
        "types": ["Fighting", "Dragon"],
        "abilities": ["Orichalcum Pulse"],
        "stats": {
            "HP": 100,
            "Attack": 135,
            "Defense": 115,
            "Sp. Atk": 85,
            "Sp. Def": 100,
            "Speed": 135,
        },
        "weight": 303.0,
        "fully_evolved": True
    },
    "Miraidon": {
        "name": "Miraidon",
        "types": ["Electric", "Dragon"],
        "abilities": ["Hadron Engine"],
        "stats": {
            "HP": 100,
            "Attack": 85,
            "Defense": 100,
            "Sp. Atk": 135,
            "Sp. Def": 115,
            "Speed": 135,
        },
        "weight": 240.0,
        "fully_evolved": True
    },
    "Walking Wake": {
        "name": "Walking Wake",
        "types": ["Water", "Dragon"],
        "abilities": ["Protosynthesis"],
        "stats": {
            "HP": 99,
            "Attack": 83,
            "Defense": 91,
            "Sp. Atk": 125,
            "Sp. Def": 83,
            "Speed": 109,
        },
        "weight": 280.0,
        "fully_evolved": True
    },
    "Iron-Leaves": {
        "name": "Iron-Leaves",
        "types": ["Grass", "Psychic"],
        "abilities": ["Quark Drive"],
        "stats": {
            "HP": 90,
            "Attack": 130,
            "Defense": 88,
            "Sp. Atk": 70,
            "Sp. Def": 108,
            "Speed": 104,
        },
        "weight": 125.0,
        "fully_evolved": True
    },
    "Dipplin": {
        "name": "Dipplin",
        "types": ["Grass", "Dragon"],
        "abilities": ["Supersweet Syrup", "Gluttony", "Sticky Hold"],
        "stats": {
            "HP": 80,
            "Attack": 80,
            "Defense": 110,
            "Sp. Atk": 95,
            "Sp. Def": 80,
            "Speed": 40,
        },
        "weight": 9.7,
        "fully_evolved": True
    },
    "Sinistcha": {
        "name": "Sinistcha",
        "types": ["Grass", "Ghost"],
        "abilities": ["Hospitality", "Heatproof"],
        "stats": {
            "HP": 71,
            "Attack": 60,
            "Defense": 106,
            "Sp. Atk": 121,
            "Sp. Def": 80,
            "Speed": 70,
        },
        "weight": 2.2,
        "fully_evolved": True
    },
    "Okidogi": {
        "name": "Okidogi",
        "types": ["Poison", "Fighting"],
        "abilities": ["Toxic Chain", "Guard Dog"],
        "stats": {
            "HP": 88,
            "Attack": 128,
            "Defense": 115,
            "Sp. Atk": 58,
            "Sp. Def": 86,
            "Speed": 80,
        },
        "weight": 92.2,
        "fully_evolved": True
    },
    "Munkidori": {
        "name": "Munkidori",
        "types": ["Poison", "Psychic"],
        "abilities": ["Toxic Chain", "Frisk"],
        "stats": {
            "HP": 88,
            "Attack": 75,
            "Defense": 66,
            "Sp. Atk": 130,
            "Sp. Def": 90,
            "Speed": 106,
        },
        "weight": 12.2,
        "fully_evolved": True
    },
    "Fezandipiti": {
        "name": "Fezandipiti",
        "types": ["Poison", "Fairy"],
        "abilities": ["Toxic Chain", "Technician"],
        "stats": {
            "HP": 88,
            "Attack": 91,
            "Defense": 82,
            "Sp. Atk": 70,
            "Sp. Def": 125,
            "Speed": 99,
        },
        "weight": 30.1,
        "fully_evolved": True
    },
    "Gouging-Fire": {
        "name": "Gouging-Fire",
        "types": ["Fire", "Dragon"],
        "abilities": ["Protosynthesis"],
        "stats": {
            "HP": 105,
            "Attack": 115,
            "Defense": 121,
            "Sp. Atk": 65,
            "Sp. Def": 93,
            "Speed": 91,
        },
        "weight": 590.0,
        "fully_evolved": True
    },
    "Raging-Bolt": {
        "name": "Raging-Bolt",
        "types": ["Electric", "Dragon"],
        "abilities": ["Protosynthesis"],
        "stats": {
            "HP": 125,
            "Attack": 73,
            "Defense": 91,
            "Sp. Atk": 137,
            "Sp. Def": 89,
            "Speed": 75,
        },
        "weight": 480.0,
        "fully_evolved": True
    },
    "Iron-Boulder": {
        "name": "Iron-Boulder",
        "types": ["Rock", "Psychic"],
        "abilities": ["Quark Drive"],
        "stats": {
            "HP": 90,
            "Attack": 120,
            "Defense": 80,
            "Sp. Atk": 68,
            "Sp. Def": 108,
            "Speed": 124,
        },
        "weight": 162.5,
        "fully_evolved": True
    },
    "Iron-Crown": {
        "name": "Iron-Crown",
        "types": ["Steel", "Psychic"],
        "abilities": ["Quark Drive"],
        "stats": {
            "HP": 90,
            "Attack": 72,
            "Defense": 100,
            "Sp. Atk": 122,
            "Sp. Def": 108,
            "Speed": 98,
        },
        "weight": 156.0,
        "fully_evolved": True
    },
    "Terapagos": {
        "name": "Terapagos",
        "types": ["Normal"],
        "abilities": ["Tera Shift"],
        "stats": {
            "HP": 160,
            "Attack": 105,
            "Defense": 110,
            "Sp. Atk": 130,
            "Sp. Def": 110,
            "Speed": 85,
        },
        "weight": 6.5,
        "fully_evolved": True
    },
    "Pecharunt": {
        "name": "Pecharunt",
        "types": ["Poison", "Ghost"],
        "abilities": ["Poison Puppeteer"],
        "stats": {
            "HP": 88,
            "Attack": 88,
            "Defense": 160,
            "Sp. Atk": 88,
            "Sp. Def": 88,
            "Speed": 88,
        },
        "weight": 0.3,
        "fully_evolved": True
    },
    "Basculin": {
        "name": "Basculin",
        "types": ["Water"],
        "abilities": ["Reckless", "Adaptability", "Mold Breaker"],
        "stats": {
            "HP": 70,
            "Attack": 92,
            "Defense": 65,
            "Sp. Atk": 80,
            "Sp. Def": 55,
            "Speed": 98,
        },
        "weight": 18.0,
        "fully_evolved": True
    },
    "Meloetta": {
        "name": "Meloetta",
        "types": ["Normal", "Psychic"],
        "abilities": ["Serene Grace"],
        "stats": {
            "HP": 100,
            "Attack": 77,
            "Defense": 77,
            "Sp. Atk": 128,
            "Sp. Def": 128,
            "Speed": 90,
        },
        "weight": 6.5,
        "fully_evolved": True
    },
    "Meowstic": {
        "name": "Meowstic",
        "types": ["Psychic"],
        "abilities": ["Keen Eye", "Infiltrator", "Prankster"],
        "stats": {
            "HP": 74,
            "Attack": 48,
            "Defense": 76,
            "Sp. Atk": 83,
            "Sp. Def": 81,
            "Speed": 104,
        },
        "weight": 8.5,
        "fully_evolved": True
    },
    "Minior-Core": {
        "name": "Minior-Core",
        "types": ["Rock", "Flying"],
        "abilities": ["Shields Down"],
        "stats": {
            "HP": 60,
            "Attack": 100,
            "Defense": 60,
            "Sp. Atk": 100,
            "Sp. Def": 60,
            "Speed": 120,
        },
        "weight": 0.3,
        "fully_evolved": True
    },
    "Minior-Meteor": {
        "name": "Minior-Meteor",
        "types": ["Rock", "Flying"],
        "abilities": ["Shields Down"],
        "stats": {
            "HP": 60,
            "Attack": 60,
            "Defense": 100,
            "Sp. Atk": 60,
            "Sp. Def": 100,
            "Speed": 60,
        },
        "weight": 40.0,
        "fully_evolved": True
    },
    "Eiscue-Ice-Face": {
        "name": "Eiscue-Ice-Face",
        "types": ["Ice"],
        "abilities": ["Ice Face"],
        "stats": {
            "HP": 75,
            "Attack": 80,
            "Defense": 110,
            "Sp. Atk": 65,
            "Sp. Def": 90,
            "Speed": 50,
        },
        "weight": 89.0,
        "fully_evolved": True
    },
    "Eiscue-No-Ice-Face": {
        "name": "Eiscue-No-Ice-Face",
        "types": ["Ice"],
        "abilities": ["Ice Face"],
        "stats": {
            "HP": 75,
            "Attack": 80,
            "Defense": 70,
            "Sp. Atk": 65,
            "Sp. Def": 90,
            "Speed": 130,
        },
        "weight": 89.0,
        "fully_evolved": True
    },
    "Palafin": {
        "name": "Palafin",
        "types": ["Water"],
        "abilities": ["Zero To Hero"],
        "stats": {
            "HP": 100,
            "Attack": 70,
            "Defense": 72,
            "Sp. Atk": 53,
            "Sp. Def": 62,
            "Speed": 100,
        },
        "weight": 60.2,
        "fully_evolved": True
    },
    "Palafin-Hero": {
        "name": "Palafin-Hero",
        "types": ["Water"],
        "abilities": ["Zero To Hero"],
        "stats": {
            "HP": 100,
            "Attack": 140,
            "Defense": 72,
            "Sp. Atk": 53,
            "Sp. Def": 62,
            "Speed": 100,
        },
        "weight": 60.2,
        "fully_evolved": True
    }, 
    "Tauros-Paldea-Combat": {
        "name": "Tauros-Paldea-Combat",
        "types": ["Fighting"],
        "abilities": ["Intimidate", "Anger Point", "Cud Chew"],
        "stats": {
            "HP": 75,
            "Attack": 110,
            "Defense": 105,
            "Sp. Atk": 30,
            "Sp. Def": 70,
            "Speed": 100,
        },
        "weight": 85.0,
        "fully_evolved": True
    },
    "Tauros-Paldea-Blaze": {
        "name": "Tauros-Paldea-Blaze",
        "types": ["Fighting", "Fire"],
        "abilities": ["Intimidate", "Anger Point", "Cud Chew"],
        "stats": {
            "HP": 75,
            "Attack": 110,
            "Defense": 105,
            "Sp. Atk": 30,
            "Sp. Def": 70,
            "Speed": 100,
        },
        "weight": 85.0,
        "fully_evolved": True
    },
    "Tauros-Paldea-Aqua": {
        "name": "Tauros-Paldea-Aqua",
        "types": ["Fighting", "Water"],
        "abilities": ["Intimidate", "Anger Point", "Cud Chew"],
        "stats": {
            "HP": 75,
            "Attack": 110,
            "Defense": 105,
            "Sp. Atk": 30,
            "Sp. Def": 70,
            "Speed": 100,
        },
        "weight": 85.0,
        "fully_evolved": True
    },
    "Oinkologne": {
        "name": "Oinkologne",
        "types": ["Normal"],
        "abilities": ["Lingering Aroma", "Gluttony", "Thick Fat"],
        "stats": {
            "HP": 110,
            "Attack": 100,
            "Defense": 75,
            "Sp. Atk": 59,
            "Sp. Def": 80,
            "Speed": 65,
        },
        "weight": 120.0,
        "fully_evolved": True
    },
    "Squawkabilly": {
        "name": "Squawkabilly",
        "types": ["Normal", "Flying"],
        "abilities": ["Intimidate", "Hustle", "Guts"],
        "stats": {
            "HP": 82,
            "Attack": 96,
            "Defense": 51,
            "Sp. Atk": 45,
            "Sp. Def": 51,
            "Speed": 92,
        },
        "weight": 2.4,
        "fully_evolved": True
    },
    "Dudunsparce": {
        "name": "Dudunsparce",
        "types": ["Normal"],
        "abilities": ["Serene Grace", "Run Away", "Rattled"],
        "stats": {
            "HP": 125,
            "Attack": 100,
            "Defense": 80,
            "Sp. Atk": 85,
            "Sp. Def": 75,
            "Speed": 55,
        },
        "weight": 39.2,
        "fully_evolved": True
    },
    "Ogerpon-Teal": {
        "name": "Ogerpon-Teal",
        "types": ["Grass"],
        "abilities": ["Defiant"],
        "stats": {
            "HP": 80,
            "Attack": 120,
            "Defense": 84,
            "Sp. Atk": 60,
            "Sp. Def": 96,
            "Speed": 110,
        },
        "weight": 39.8,
        "fully_evolved": True
    },
    "Ogerpon-Wellspring": {
        "name": "Ogerpon-Wellspring",
        "types": ["Grass", "Water"],
        "abilities": ["Water Absorb"],
        "stats": {
            "HP": 80,
            "Attack": 120,
            "Defense": 84,
            "Sp. Atk": 60,
            "Sp. Def": 96,
            "Speed": 110,
        },
        "weight": 39.8,
        "fully_evolved": True
    },
    "Ogerpon-Hearthflame": {
        "name": "Ogerpon-Hearthflame",
        "types": ["Grass", "Fire"],
        "abilities": ["Mold Breaker"],
        "stats": {
            "HP": 80,
            "Attack": 120,
            "Defense": 84,
            "Sp. Atk": 60,
            "Sp. Def": 96,
            "Speed": 110,
        },
        "weight": 39.8,
        "fully_evolved": True
    },
    "Ogerpon-Cornerstone": {
        "name": "Ogerpon-Cornerstone",
        "types": ["Grass", "Rock"],
        "abilities": ["Sturdy"],
        "stats": {
            "HP": 80,
            "Attack": 120,
            "Defense": 84,
            "Sp. Atk": 60,
            "Sp. Def": 96,
            "Speed": 110,
        },
        "weight": 39.8,
        "fully_evolved": True
    },
    "Yanmega": {
        "name": "Yanmega",
        "types": ["Bug", "Flying"],
        "abilities": ["Speed Boost", "Tinted Lens"],
        "stats": {
            "HP": 86,
            "Attack": 76,
            "Defense": 86,
            "Sp. Atk": 116,
            "Sp. Def": 56,
            "Speed": 95,
        },
        "weight": 51.5,
        "fully_evolved": True
    },
}