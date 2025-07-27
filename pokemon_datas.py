'''
Toutes les statistiques des Pokémon sont stockées dans un fichier CSV.
'''



pokemon_data = {
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
            "Speed": 80
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
            "Speed": 100
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
            "Speed": 78
        },
        "weight": 85.5,
        "fully_evolved": True
    },
    "Butterfree": {
        "name": "Butterfree",
        "types": ["Bug", "Flying"],
        "abilities": ["Compound Eyes", "Tinted Lens"],
        "stats": {
            "HP": 60,
            "Attack": 45,
            "Defense": 50,
            "Sp. Atk": 90,
            "Sp. Def": 80,
            "Speed": 70
        },
        "weight": 32.0,
        "fully_evolved": True
    },
    "Beedrill": {
        "name": "Beedrill",
        "types": ["Bug", "Poison"],
        "abilities": ["Swarm", "Sniper"],
        "stats": {
            "HP": 65,
            "Attack": 90,
            "Defense": 40,
            "Sp. Atk": 45,
            "Sp. Def": 80,
            "Speed": 75
        },
        "weight": 29.5,
        "fully_evolved": True
    },
    "Pidgeot": {
        "name": "Pidgeot",
        "types": ["Normal", "Flying"],
        "abilities": ["Keen Eye", "Tangled Feet", "Big Pecks"],
        "stats": {
            "HP": 83,
            "Attack": 80,
            "Defense": 75,
            "Sp. Atk": 70,
            "Sp. Def": 70,
            "Speed": 101
        },
        "weight": 39.5,
        "fully_evolved": True
    },
    "Raticate": {
        "name": "Raticate",
        "types": ["Normal"],
        "abilities": ["Run Away", "Guts", "Hustle"],
        "stats": {
            "HP": 55,
            "Attack": 81,
            "Defense": 60,
            "Sp. Atk": 50,
            "Sp. Def": 70,
            "Speed": 97
        },
        "weight": 18.5,
        "fully_evolved": True
    },
    "Fearow": {
        "name": "Fearow",
        "types": ["Normal", "Flying"],
        "abilities": ["Keen Eye", "Sniper"],
        "stats": {
            "HP": 65,
            "Attack": 90,
            "Defense": 65,
            "Sp. Atk": 61,
            "Sp. Def": 61,
            "Speed": 100
        },
        "weight": 38.0,
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
            "Speed": 80
        },
        "weight": 65.0,
        "fully_evolved": True
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
            "Speed": 110
        },
        "weight": 30.0,
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
            "Speed": 65
        },
        "weight": 29.5,
        "fully_evolved": True
    },
    "Nidoqueen": {
        "name": "Nidoqueen",
        "types": ["Poison", "Ground"],
        "abilities": ["Poison Point", "Rivalry", "Sheer Force"],
        "stats": {
            "HP": 90,
            "Attack": 92,
            "Defense": 87,
            "Sp. Atk": 75,
            "Sp. Def": 85,
            "Speed": 76
        },
        "weight": 60.0,
        "fully_evolved": True
    },
    "Nidoking": {
        "name": "Nidoking",
        "types": ["Poison", "Ground"],
        "abilities": ["Poison Point", "Rivalry", "Sheer Force"],
        "stats": {
            "HP": 81,
            "Attack": 102,
            "Defense": 77,
            "Sp. Atk": 85,
            "Sp. Def": 75,
            "Speed": 85
        },
        "weight": 62.0,
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
            "Speed": 60
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
            "Speed": 100
        },
        "weight": 19.9,
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
            "Speed": 45
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
            "Speed": 50
        },
        "weight": 18.6,
        "fully_evolved": True
    },
    "Parasect": {
        "name": "Parasect",
        "types": ["Bug", "Grass"],
        "abilities": ["Effect Spore", "Dry Skin", "Damp"],
        "stats": {
            "HP": 60,
            "Attack": 95,
            "Defense": 80,
            "Sp. Atk": 60,
            "Sp. Def": 80,
            "Speed": 30
        },
        "weight": 29.5,
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
            "Speed": 90
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
            "Speed": 120
        },
        "weight": 33.3,
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
            "Speed": 115
        },
        "weight": 32.0,
        "fully_evolved": True
    },
    "Golduck": {
        "name": "Golduck",
        "types": ["Water"],
        "abilities": ["Damp", "Cloud Nine", "Swift Swim"],
        "stats": {
            "HP": 80,
            "Attack": 82,
            "Defense": 78,
            "Sp. Atk": 95,
            "Sp. Def": 80,
            "Speed": 85
        },
        "weight": 76.6,
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
            "Speed": 95
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
            "Speed": 95
        },
        "weight": 155.0,
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
            "Speed": 70
        },
        "weight": 54.0,
        "fully_evolved": True
    },
    "Alakazam": {
        "name": "Alakazam",
        "types": ["Psychic"],
        "abilities": ["Synchronize", "Inner Focus", "Magic Guard"],
        "stats": {
            "HP": 55,
            "Attack": 50,
            "Defense": 45,
            "Sp. Atk": 135,
            "Sp. Def": 95,
            "Speed": 120
        },
        "weight": 48.0,
        "fully_evolved": True
    },
    "Machamp": {
        "name": "Machamp",
        "types": ["Fighting"],
        "abilities": ["Guts", "No Guard", "Steadfast"],
        "stats": {
            "HP": 90,
            "Attack": 130,
            "Defense": 80,
            "Sp. Atk": 65,
            "Sp. Def": 85,
            "Speed": 55
        },
        "weight": 130.0,
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
            "Speed": 70
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
            "Speed": 100
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
            "Speed": 45
        },
        "weight": 300.0,
        "fully_evolved": True
    },
    "Rapidash": {
        "name": "Rapidash",
        "types": ["Fire"],
        "abilities": ["Run Away", "Flash Fire", "Flame Body"],
        "stats": {
            "HP": 65,
            "Attack": 100,
            "Defense": 70,
            "Sp. Atk": 80,
            "Sp. Def": 80,
            "Speed": 105
        },
        "weight": 95.0,
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
            "Speed": 30
        },
        "weight": 78.5,
        "fully_evolved": True
    },
    "Magneton": {
        "name": "Magneton",
        "types": ["Electric", "Steel"],
        "abilities": ["Magnet Pull", "Sturdy", "Analytic"],
        "stats": {
            "HP": 50,
            "Attack": 60,
            "Defense": 95,
            "Sp. Atk": 120,
            "Sp. Def": 70,
            "Speed": 70
        },
        "weight": 60.0,
        "fully_evolved": False  # Evolves into Magnezone
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
            "Speed": 110
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
            "Speed": 70
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
            "Speed": 50
        },
        "weight": 30.0,
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
            "Speed": 70
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
            "Speed": 110
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
            "Speed": 67
        },
        "weight": 75.6,
        "fully_evolved": True
    },
    "Kingler": {
        "name": "Kingler",
        "types": ["Water"],
        "abilities": ["Hyper Cutter", "Shell Armor", "Sheer Force"],
        "stats": {
            "HP": 55,
            "Attack": 130,
            "Defense": 115,
            "Sp. Atk": 50,
            "Sp. Def": 50,
            "Speed": 75
        },
        "weight": 60.0,
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
            "Speed": 150
        },
        "weight": 66.6,
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
            "Speed": 55
        },
        "weight": 120.0,
        "fully_evolved": True
    },
    "Marowak": {
        "name": "Marowak",
        "types": ["Ground"],
        "abilities": ["Rock Head", "Lightning Rod", "Battle Armor"],
        "stats": {
            "HP": 60,
            "Attack": 80,
            "Defense": 110,
            "Sp. Atk": 50,
            "Sp. Def": 80,
            "Speed": 45
        },
        "weight": 45.0,
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
            "Speed": 87
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
            "Speed": 76
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
            "Speed": 60
        },
        "weight": 9.5,
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
            "Speed": 40
        },
        "weight": 120.0,
        "fully_evolved": False  # Evolves into Rhyperior
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
            "Speed": 50
        },
        "weight": 34.6,
        "fully_evolved": False  # Evolves into Blissey
    },
    "Tangela": {
        "name": "Tangela",
        "types": ["Grass"],
        "abilities": ["Chlorophyll", "Leaf Guard", "Regenerator"],
        "stats": {
            "HP": 65,
            "Attack": 55,
            "Defense": 115,
            "Sp. Atk": 100,
            "Sp. Def": 40,
            "Speed": 60
        },
        "weight": 35.0,
        "fully_evolved": False  # Evolves into Tangrowth
    },
    "Kangaskhan": {
        "name": "Kangaskhan",
        "types": ["Normal"],
        "abilities": ["Early Bird", "Scrappy", "Inner Focus"],
        "stats": {
            "HP": 105,
            "Attack": 95,
            "Defense": 80,
            "Sp. Atk": 40,
            "Sp. Def": 80,
            "Speed": 90
        },
        "weight": 80.0,
        "fully_evolved": True
    },
    "Seaking": {
        "name": "Seaking",
        "types": ["Water"],
        "abilities": ["Swift Swim", "Water Veil", "Lightning Rod"],
        "stats": {
            "HP": 80,
            "Attack": 92,
            "Defense": 65,
            "Sp. Atk": 65,
            "Sp. Def": 80,
            "Speed": 68
        },
        "weight": 39.0,
        "fully_evolved": True
    },
    "Starmie": {
        "name": "Starmie",
        "types": ["Water", "Psychic"],
        "abilities": ["Illuminate", "Natural Cure", "Analytic"],
        "stats": {
            "HP": 60,
            "Attack": 75,
            "Defense": 85,
            "Sp. Atk": 100,
            "Sp. Def": 85,
            "Speed": 115
        },
        "weight": 80.0,
        "fully_evolved": True
    },
    "Mr. Mime": {
        "name": "Mr. Mime",
        "types": ["Psychic", "Fairy"],
        "abilities": ["Soundproof", "Filter", "Technician"],
        "stats": {
            "HP": 40,
            "Attack": 45,
            "Defense": 65,
            "Sp. Atk": 100,
            "Sp. Def": 120,
            "Speed": 90
        },
        "weight": 54.5,
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
            "Speed": 105
        },
        "weight": 56.0,
        "fully_evolved": False  # Evolves into Scizor or Kleavor
    },
    "Jynx": {
        "name": "Jynx",
        "types": ["Ice", "Psychic"],
        "abilities": ["Oblivious", "Forewarn", "Dry Skin"],
        "stats": {
            "HP": 65,
            "Attack": 50,
            "Defense": 35,
            "Sp. Atk": 115,
            "Sp. Def": 95,
            "Speed": 95
        },
        "weight": 40.6,
        "fully_evolved": True
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
            "Speed": 105
        },
        "weight": 30.0,
        "fully_evolved": False  # Evolves into Electivire
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
            "Speed": 93
        },
        "weight": 44.5,
        "fully_evolved": False  # Evolves into Magmortar
    },
    "Pinsir": {
        "name": "Pinsir",
        "types": ["Bug"],
        "abilities": ["Hyper Cutter", "Mold Breaker", "Moxie"],
        "stats": {
            "HP": 65,
            "Attack": 125,
            "Defense": 100,
            "Sp. Atk": 55,
            "Sp. Def": 70,
            "Speed": 85
        },
        "weight": 55.0,
        "fully_evolved": True
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
            "Speed": 110
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
            "Speed": 81
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
            "Speed": 60
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
            "Speed": 48
        },
        "weight": 4.0,
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
            "Speed": 65
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
            "Speed": 130
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
            "Speed": 65
        },
        "weight": 25.0,
        "fully_evolved": True
    },
    "Omastar": {
        "name": "Omastar",
        "types": ["Rock", "Water"],
        "abilities": ["Swift Swim", "Shell Armor", "Weak Armor"],
        "stats": {
            "HP": 70,
            "Attack": 60,
            "Defense": 125,
            "Sp. Atk": 115,
            "Sp. Def": 70,
            "Speed": 55
        },
        "weight": 35.0,
        "fully_evolved": True
    },
    "Kabutops": {
        "name": "Kabutops",
        "types": ["Rock", "Water"],
        "abilities": ["Swift Swim", "Battle Armor", "Weak Armor"],
        "stats": {
            "HP": 60,
            "Attack": 115,
            "Defense": 105,
            "Sp. Atk": 65,
            "Sp. Def": 70,
            "Speed": 80
        },
        "weight": 40.5,
        "fully_evolved": True
    },
    "Aerodactyl": {
        "name": "Aerodactyl",
        "types": ["Rock", "Flying"],
        "abilities": ["Rock Head", "Pressure", "Unnerve"],
        "stats": {
            "HP": 80,
            "Attack": 105,
            "Defense": 65,
            "Sp. Atk": 60,
            "Sp. Def": 75,
            "Speed": 130
        },
        "weight": 59.0,
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
            "Speed": 30
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
            "Speed": 85
        },
        "weight": 55.4,
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
            "Speed": 100
        },
        "weight": 52.6,
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
            "Speed": 90
        },
        "weight": 60.0,
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
            "Speed": 80
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
            "Speed": 130
        },
        "weight": 122.0,
        "fully_evolved": True
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
            "Speed": 100
        },
        "weight": 4.0,
        "fully_evolved": True
    },


    #########################################################################################""
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
            "Speed": 85
        },
        "weight": 40.0,
        "fully_evolved": False 
    },
    "Archaludon": {
        "name": "Archaludon",
        "types": ["Steel", "Dragon"],
        "abilities": ["Stamina", "Sturdy", "Stalwart"],
        "stats": {
            "HP": 90,
            "Attack": 105,
            "Defense": 130,
            "Sp. Atk": 125,
            "Sp. Def": 65,
            "Speed": 85
        },
        "weight": 60.0,
        "fully_evolved": True
    },
    "Raging Bolt": {
        "name": "Raging Bolt",
        "types": ["Electric", "Dragon"],
        "abilities": ["Protosynthesis"],
        "stats": {
            "HP": 125,
            "Attack": 73,
            "Defense": 91,
            "Sp. Atk": 137,
            "Sp. Def": 89,
            "Speed": 75
        },
        "weight": 480.0,
        "fully_evolved": True
    },
    "Iron Crown": {
        "name": "Iron Crown",
        "types": ["Steel", "Psychic"],
        "abilities": ["Quark Drive"],
        "stats": {
            "HP": 90,
            "Attack": 72,
            "Defense": 100,
            "Sp. Atk": 122,
            "Sp. Def": 108,
            "Speed": 98
        },
        "weight": 156.0,
        "fully_evolved": True
    },
    "Gouging Fire": {
        "name": "Gouging Fire",
        "types": ["Fire", "Dragon"],
        "abilities": ["Protosynthesis"],
        "stats": {
            "HP": 105,
            "Attack": 115,
            "Defense": 121,
            "Sp. Atk": 65,
            "Sp. Def": 93,
            "Speed": 91
        },
        "weight": 590.0,
        "fully_evolved": True
    },
    "Iron Boulder": {
        "name": "Iron Boulder",
        "types": ["Rock", "Psychic"],
        "abilities": ["Quark Drive"],
        "stats": {
            "HP": 90,
            "Attack": 120,
            "Defense": 80,
            "Sp. Atk": 68,
            "Sp. Def": 108,
            "Speed": 124
        },
        "weight": 162.5,
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
            "Speed": 85
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
            "Speed": 88
        },
        "weight": 0.3,
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
            "Speed": 81
        },
        "weight": 162.0,
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
            "Speed": 70
        },
        "weight": 550.0,
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
            "Speed": 70
        },
        "weight": 37.0,
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
            "Speed": 85
        },
        "weight": 90.0,
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
            "Speed": 102
        },
        "weight": 95.0,
        "fully_evolved": True
    },
    "Chien-Pao": {
        "name": "Chien-Pao",
        "types": ["Dark", "Ice"],
        "abilities": ["Sword of Ruin"],
        "stats": {
            "HP":80,
            "Attack": 120,
            "Defense": 80,
            "Sp. Atk": 90,
            "Sp. Def": 65,
            "Speed": 135
        },
        "weight": 152.2,
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
            "Speed": 70
        },
        "weight": 120.0,
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
            "Speed": 100
        },
        "weight": 20.0,
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
            "Speed": 45
        },
        "weight": 220.0,
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
            "Speed": 138
        },
        "weight": 210.0,
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
            "Speed": 138
        },
        "weight": 210.0,
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
            "Speed": 125
        },
        "weight": 50.5,
        "fully_evolved": True
    },
    "Kingambit": {
        "name": "Kingambit",
        "types": ["Dark", "Steel"],
        "abilities": ["Defiant"],
        "stats": {
            "HP": 100,
            "Attack": 125,
            "Defense": 100,
            "Sp. Atk": 60,
            "Sp. Def": 100,
            "Speed": 70
        },
        "weight": 110.0,
        "fully_evolved": True
    },
    "Iron Valiant": {
        "name": "Iron Valiant",
        "types": ["Fairy", "Fighting"],
        "abilities": ["Quark Drive"],
        "stats": {
            "HP": 70,
            "Attack": 130,
            "Defense": 90,
            "Sp. Atk": 110,
            "Sp. Def": 60,
            "Speed": 120
        },
        "weight": 65.0,
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
            "Speed": 100
        },
        "weight": 40.0,
        "fully_evolved": True
    }
}