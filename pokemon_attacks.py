'''
Ce fihiers contient toutes les attaques pokemon, leur type, puissance, précision, et effets spéciaux.


List of flags and their descriptions:

authentic: Ignores a target's substitute.
bite: Power is multiplied by 1.5 when used by a Pokemon with the Ability Strong Jaw.
bullet: Has no effect on Pokemon with the Ability Bulletproof.
charge: The user is unable to make a move between turns.
contact: Makes contact.
defrost: Thaws the user if executed successfully while the user is frozen.
gravity: Prevented from being executed or selected during Gravity's effect.
heal: Prevented from being executed or selected during Heal Block's effect.
mirror: Can be copied by Mirror Move.
nonsky: Prevented from being executed or selected in a Sky Battle.
powder: Has no effect on Grass-type Pokemon, Pokemon with the Ability Overcoat, and Pokemon holding Safety Goggles.
protect: Blocked by Detect, Protect, Spiky Shield, and if not a Status move, King's Shield.
pulse: Power is multiplied by 1.5 when used by a Pokemon with the Ability Mega Launcher.
punch: Power is multiplied by 1.2 when used by a Pokemon with the Ability Iron Fist.
recharge: If this move is successful, the user must recharge on the following turn and cannot make a move.
reflectable: Bounced back to the original user by Magic Coat or the Ability Magic Bounce.
snatch: Can be stolen from the original user and instead used by another Pokemon using Snatch.
sound: Has no effect on Pokemon with the Ability Soundproof.

'''

import pokemon_datas as STATS
import pokemon_talents as TALENTS
import pokemon as PK

attacks = {
            "tackle": { "type": "Normal",
                "basePower": 40, 
                "accuracy": 100, 
                "priority" : 0, 
                "category": "Physical", 
                "PP": 35,
                "multi_target": False, 
                "flags": ["contact", "protect", "mirror"],
                "target": "Foe",
            },
            "ember": { "type": "Fire",
                "basePower": 40, 
                "accuracy": 100, 
                "priority" : 0, 
                "category": "Special", 
                "PP": 25,
                "multi_target": False, 
                "flags": ["protect", "mirror"],
                "target": "Foe",
                "effect": {
                    "burn": {
                        "chance": 10,  # Chance de brûler l'adversaire
                        "effect": lambda pokemon, attaque: pokemon.apply_status("burn") if attaque else None
                    }
                }
            },
            "water_gun": { "type": "Water",
                    "basePower": 40, 
                    "accuracy": 100, 
                    "priority" : 0, 
                    "category": "Special", 
                    "PP": 25,
                    "multi_target": False, 
                    "flags": ["protect", "mirror"],
                    "target": "Foe",
                   
                   },
            "vine_whip": { "type": "Plant",
                    "basePower": 45,
                    "accuracy": 100,
                    "priority" : 0,
                    "category": "Physical",
                    "PP": 25,
                    "multi_target": False,
                    "flags": ["contact", "protect", "mirror"],
                    "target": "Foe",

                    },
            "nuzzle": { "type": "Electric",
                    "basePower": 20,
                    "accuracy": 100,
                    "priority" : 0,
                    "category": "Physical",
                    "PP": 20,
                    "multi_target": False,
                    "flags": ["contact", "protect", "mirror"],
                    "target": "Foe",
                    "effect": {
                        "paralyze": {
                            "chance": 100,  # Chance de paralyser l'adversaire
                            "effect": lambda pokemon, attaque: pokemon.apply_status("paralyzed") if attaque else None
                        }
                    }
            },
            "leech_seed": { "type": "Plant",
                    "basePower": 0,
                    "accuracy": 90,
                    "priority" : 0,
                    "category": "Status",
                    "PP": 10,
                    "multi_target": False,
                    "flags": ["protect"],
                    "target": "Foe",
                    "effect": {
                          "leech_seed": {
                           "chance": 100,  # Chance de planter la graine
                           "effect": lambda pokemon, attaque: pokemon.apply_status("leech_seed") if attaque else None
                          }
                    }
                },
            "protect": { "type": "Normal",
                    "basePower": 0,
                    "precision": True,
                    "priority" : 4,
                    "category": "Status",
                    "PP": 10,
                    "multi_target": False,
                    "flags": [],
                    "target": "User",
                    "effect": {
                         "protect": {
                           "chance": True,  # Chance de protéger le Pokémon
                           "effect": lambda pokemon, attaque: pokemon.apply_status("protected") if attaque else None
                         }
                    }
                },
            "rockslide": { "type": "Rock",
                    "basePower": 75,
                    "accuracy": 90,
                    "priority" : 0,
                    "category": "Physical",
                    "PP": 10,
                    "multi_target": True,  # Peut toucher plusieurs cibles
                    "flags": ["protect", "mirror"],
                    "target": "Foe",
                    "effect": {
                        "flinch": {
                            "chance": 30,  # Chance de faire flancher l'adversaire
                            "effect": lambda pokemon, attaque: pokemon.apply_status("flinch") if attaque else None
                        }
                    }
                },
            "surging_strike": { "type": "Water",
                    "basePower": 25,
                    "accuracy": 100,
                    "priority" : 0,
                    "category": "Physical",
                    "PP": 5,
                    "multi_target": False,
                    "flags": ["contact", "protect", "mirror"],
                    "target": "Foe",
                    "effect": {
                        "critical": {
                            "chance": 100,  # Chance de faire un coup critique
                        }
                    }
                },
            "stone edge": { "type": "Rock",
                    "basePower": 100,
                    "accuracy": 80,
                    "priority" : 0,
                    "category": "Physical",
                    "PP": 5,
                    "multi_target": False,
                    "flags": ["protect", "mirror"],
                    "target": "Foe",
                    "effect": {
                        "critical": {
                            "chance": 12.5,  # Chance de faire un coup critique
                        }
                    }
                },
            "flower_trick": { "type": "Plant",
                    "basePower": 70,
                    "accuracy": 100,
                    "priority" : 0,
                    "category": "Physical",
                    "PP": 10,
                    "multi_target": False,
                    "flags": ["protect", "mirror"],
                    "target": "Foe",
                    "effect": {
                        "critical": {
                            "chance": 100,  # Chance de faire un coup critique
                        }
                    }
                },
}
