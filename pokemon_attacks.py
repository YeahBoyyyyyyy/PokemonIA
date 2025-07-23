import pokemon_datas as STATS
import pokemon_talents as TALENTS
from pokemon_talents import apply_stat_changes
import pokemon as PK
import random


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
protection: Attack destined to protect the user from damage.
pulse: Power is multiplied by 1.5 when used by a Pokemon with the Ability Mega Launcher.
punch: Power is multiplied by 1.2 when used by a Pokemon with the Ability Iron Fist.
recharge: If this move is successful, the user must recharge on the following turn and cannot make a move.
reflectable: Bounced back to the original user by Magic Coat or the Ability Magic Bounce.
sharp: Power is multiplied by 1.5 when used by a Pokemon with the Ability Sharpness.
snatch: Can be stolen from the original user and instead used by another Pokemon using Snatch.
sound: Has no effect on Pokemon with the Ability Soundproof.

'''

import pokemon_datas as STATS
import pokemon_talents as TALENTS
import pokemon as PK
import random

class Attack:
    def __init__(self, name, type_, category, power, accuracy, priority, pp, flags, target, multi_target=False, critical_chance=6.25, guaranteed_critical=False):
        self.name = name
        self.type = type_
        self.category = category
        self.base_power = power
        self.accuracy = accuracy
        self.priority = priority
        self.pp = pp
        self.flags = flags or []
        self.target = target
        self.multi_target = multi_target
        self.critical_chance = critical_chance  # Chance de coup critique, à définir dans les attaques concrètes
        self.guaranteed_critical = False  # Indique si l'attaque est un coup critique garanti

    def apply_effect(self, user : PK.pokemon, target : PK.pokemon, fight):
        pass  # Surcharge dans les attaques concrètes

    def on_condition_attack(self, user, target = None, target_attack = None, fight = None):
        """
        Cette méthode est appelée pour vérifier si l'attaque peut être lancée. Sert principalement pour fake out et first impression.

        :param user: Le Pokémon qui lance l'attaque.
        :param target: Le Pokémon ciblé par l'attaque (optionnel).
        :param target_attack: L'attaque du Pokémon ciblé (optionnel).
        :param fight: L'instance de combat en cours (optionnel).
        :return: True si l'attaque peut être lancée, False sinon.
        """
        return True  # Par défaut, l'attaque peut être lancée
    
    def boosted_attack(self, user, target, fight):
        """
        Vérifie si l'attaque est boostée (par ex : knock off quand l'adversaire a un objet)
        
        :param user: Le Pokémon qui lance l'attaque.
        :param target: Le Pokémon ciblé par l'attaque.
        :param fight: L'instance de combat en cours.
        :return: le multiplicateur de boost.
        """
        return 1.0  # Par défaut, pas de boost
        

class FlameThrower(Attack):
    def __init__(self):
        super().__init__(
            name="Flamethrower",
            type_="Fire",
            category="Special",
            power=90,
            accuracy=100,
            priority=0,
            pp=15,
            flags=["protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        if random.randint(1, 100) <= 10:
            target.apply_status("burn")

class HydroPump(Attack):
    def __init__(self):
        super().__init__(
            name="Hydro Pump",
            type_="Water",
            category="Special",
            power=110,
            accuracy=80,
            priority=0,
            pp=5,
            flags=["protect", "mirror"],
            target="Foe"
        )

class Protect(Attack):
    def __init__(self):
        super().__init__(
            name="Protect",
            type_="Normal",
            category="Status",
            power=0,
            accuracy=100,
            priority=4,
            pp=10,
            flags=["protection"],
            target="User"
        )

    def apply_effect(self, user, target, fight):
        if random.random() < 1 / (2 ** user.protect_turns):
            user.protect = True
            user.protect_turns += 1
        else:
            print("L'attaque échoue !")
            user.protect = False
            user.protect_turns = 0

class RockSlide(Attack):
    def __init__(self):
        super().__init__(
            name="Rockslide",
            type_="Rock",
            category="Physical",
            power=75,
            accuracy=90,
            priority=0,
            pp=10,
            flags=["protect", "mirror"],
            target="Foe",
            multi_target=True
        )

    def apply_effect(self, user, target, fight):
        if random.randint(1, 100) <= 30:
            target.apply_status("flinch")

class SurgingStrike(Attack):
    def __init__(self):
        super().__init__(
            name="Surging Strike",
            type_="Water",
            category="Physical",
            power=25,
            accuracy=100,
            priority=0,
            pp=5,
            flags=["contact", "protect" "mirror"],
            target="Foe"
        )

class LeechSeed(Attack):
    def __init__(self):
        super().__init__(
            name="Leech Seed",
            type_="Grass",
            category="Status",
            power=0,
            accuracy=90,
            priority=0,
            pp=10,
            flags=["protect"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        if "Grass" in target.types:
            print(f"{target.name} est de type Plante : Leech Seed échoue.")
            return
        if target.leech_seeded_by is None:
            target.leech_seeded_by = user
            print(f"{target.name} a été infecté !")

class FlowerTrick(Attack):
    def __init__(self):
        super().__init__(
            name="Flower Trick",
            type_="Grass",
            category="Physical",
            power=70,
            accuracy=100,
            priority=0,
            pp=10,
            flags=["protect", "mirror"],
            target="Foe",
            
        )
        self.guaranteed_critical = True  # Coup critique garanti
        

class RainDance(Attack):
    def __init__(self):
        super().__init__(
            name="Rain Dance",
            type_="Water",
            category="Status",
            power=0,
            accuracy=100,
            priority=0,
            pp=5,
            flags=[],
            target="User"
        )
    
    def apply_effect(self, user, target, fight):
        fight.set_weather("Rain", duration=5)
        print(f"{user.name} invoque la pluie !")

class Recover(Attack):
    def __init__(self):
        super().__init__(
            name="Recover",
            type_="Normal",
            category="Status",
            power=0,
            accuracy=100,
            priority=0,
            pp=10,
            flags=["heal"],
            target="User"
        )

    def apply_effect(self, user, target, fight):
        heal_amount = user.max_hp // 2
        user.current_hp = min(user.max_hp, user.current_hp + heal_amount)
        print(f"{user.name} récupère {heal_amount} PV grâce à Recover.")

class StoneEdge(Attack):
    def __init__(self):
        super().__init__(
            name="Stone Edge",
            type_="Rock",
            category="Physical",
            power=100,
            accuracy=80,
            priority=0,
            pp=5,
            flags=["protect", "mirror"],
            target="Foe"
        )
        self.critical_chance = 12.5  # Chance de coup critique

class Nuzzle(Attack):
    def __init__(self):
        super().__init__(
            name="Nuzzle",
            type_="Electric",
            category="Physical",
            power=20,
            accuracy=100,
            priority=0,
            pp=20,
            flags=["contact", "protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        if target.status == None:
            target.apply_status("paralyzed")
            print(f"{target.name} est paralysé ! Il aura du mal à attaquer.")

class FakeOut(Attack):
    def __init__(self):
        super().__init__(
            name="Fake Out",
            type_="Normal",
            category="Physical",
            power=40,
            accuracy=100,
            priority=3,
            pp=10,
            flags=["contact", "protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        if not target.flinched:
            target.flinched = True
            print(f"{target.name} est flinché par Fake Out !")
        else:
            print(f"{target.name} a déjà été flinché ce tour-ci.")
    
    def on_condition_attack(self, user, target=None, target_attack=None, fight=None):
        if user.first_attack:
            return True
        else:
            print("L'attaque échoue !")
            return False

class Thunderbolt(Attack):
    def __init__(self):
        super().__init__(
            name="Thunderbolt",
            type_="Electric",
            category="Special",
            power=90,
            accuracy=100,
            priority=0,
            pp=15,
            flags=["protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        if random.randint(1, 100) <= 10:
            if target.status == None:
                target.apply_status("paralyzed")
                print(f"{target.name} est paralysé ! Il aura du mal à attaquer.")
class Spore(Attack):
    def __init__(self):
        super().__init__(
            name="Spore",
            type_="Grass",
            category="Status",
            power=0,
            accuracy=100,
            priority=0,
            pp=15,
            flags=["protect"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        if "Grass" in target.types:
            print(f"{target.name} est de type Plante : Spore échoue.")
            return
        if target.status is None:
            target.apply_status("sleep")
            print(f"{target.name} s'endort mimimiimimi !")

class WeatherBall(Attack):
    def __init__(self):
        super().__init__(
            name="Weather Ball",
            type_="Normal",
            category="Special",
            power=50,
            accuracy=100,
            priority=0,
            pp=10,
            flags=["protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        if fight.weather["current"] == "Sunny":
            self.type = "Fire"
            self.base_power = 100
        elif fight.weather["current"] == "Rain":
            self.type = "Water"
            self.base_power = 100
        elif fight.weather["current"] == "Sandstorm":
            self.type = "Rock"
            self.base_power = 100
        elif fight.weather["current"] == "Hail":
            self.type = "Ice"
            self.base_power = 100
        else:
            self.type = "Normal"
            self.base_power = 50

class KnockOff(Attack):
    def __init__(self):
        super().__init__(
            name="Knock Off",
            type_="Dark",
            category="Physical",
            power=65,
            accuracy=100,
            priority=0,
            pp=20,
            flags=["contact", "protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        if target.item:
            print(f"{target.name} perd son objet {target.item} !")
            target.item = None
            target.actualize_stats()

    def boosted_attack(self, user, target, fight):
        if target.item:
            return 1.5

class UTurn(Attack):
    def __init__(self):
        super().__init__(
            name="U-Turn",
            type_="Bug",
            category="Physical",
            power=70,
            accuracy=100,
            priority=0,
            pp=20,
            flags=["contact", "protect", "mirror"],
            target="Foe"
        )

   ## def apply_effect(self, user, target, fight): Plus tard

class WillOWisp(Attack):
    def __init__(self):
        super().__init__(
            name="Will-O-Wisp",
            type_="Fire",
            category="Status",
            power=0,
            accuracy=85,
            priority=0,
            pp=15,
            flags=["protect"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        if target.status is None and "Fire" not in target.types:
            target.apply_status("burn")
            print(f"{target.name} est brûlé !")

class Toxic(Attack):
    def __init__(self):
        super().__init__(
            name="Toxic",
            type_="Poison",
            category="Status",
            power=0,
            accuracy=90,
            priority=0,
            pp=10,
            flags=["protect"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        if target.status is None and "Poison" not in target.types:
            target.apply_status("toxic")
            print(f"{target.name} est empoisonné !")

class IceBeam(Attack):
    def __init__(self):
        super().__init__(
            name="Ice Beam",
            type_="Ice",
            category="Special",
            power=90,
            accuracy=100,
            priority=0,
            pp=10,
            flags=["protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        if random.randint(1, 100) <= 10:
            if target.status is None:
                target.apply_status("frozen")
                print(f"{target.name} est gelé !")

class SuckerPunch(Attack):
    def __init__(self):
        super().__init__(
            name="Sucker Punch",
            type_="Dark",
            category="Physical",
            power=70,
            accuracy=100,
            priority=1,
            pp=5,
            flags=["contact", "protect", "mirror"],
            target="Foe"
        )

    def on_condition_attack(self, user, target, target_atk, fight):
        if target_atk.category != "Status":
            return True
        else:
            print("L'attaque échoue !")
            return False

class Reflect(Attack):
    def __init__(self):
        super().__init__(
            name="Reflect",
            type_="Psychic",
            category="Status",
            power=0,
            accuracy=100,
            priority=0,
            pp=20,
            flags=[],
            target="User"
        )
    
    def apply_effect(self, user, target, fight):
        if not "reflect" in fight.screen:
            fight.screen.append("reflect")
            fight.screen_turn_left["reflect"] = 5
            print(f"{user.name} utilise Reflect ! Les dégâts physiques sont réduits de moitié pour 5 tours.")

class LightScreen(Attack):
    def __init__(self):
        super().__init__(
            name="Light Screen",
            type_="Psychic",
            category="Status",
            power=0,
            accuracy=100,
            priority=0,
            pp=20,
            flags=[],
            target="User"
        )
    
    def apply_effect(self, user, target, fight):
        user_team_id = fight.get_team_id(user)
        screens = fight.screen_team1 if user_team_id == 1 else fight.screen_team2
        
        if "light_screen" not in screens:
            fight.add_screen("light_screen", user_team_id)
            print(f"{user.name} utilise Light Screen ! Les dégâts spéciaux sont réduits de moitié pour son équipe pendant 5 tours.")

class AuroraVeil(Attack):
    def __init__(self):
        super().__init__(
            name="Aurora Veil",
            type_="Ice",
            category="Status",
            power=0,
            accuracy=100,
            priority=0,
            pp=20,
            flags=[],
            target="User"
        )
    
    def apply_effect(self, user, target, fight):
        if not "auroraveil" in fight.screen and fight.weather["current"] == "Snow":
            fight.screen.append("auroraveil")
            fight.screen_turn_left["auroraveil"] = 5
            print(f"{user.name} utilise Aurora Veil ! Les dégâts physiques et spéciaux sont réduits de moitié pour 5 tours.")

class SwordsDance(Attack):
    def __init__(self):
        super().__init__(
            name="Swords Dance",
            type_="Normal",
            category="Status",
            power=0,
            accuracy=100,
            priority=0,
            pp=20,
            flags=[],
            target="User"
        )

    def apply_effect(self, user : PK.pokemon, target, fight):
        stat_changes = {"Attack": 2}
        success = apply_stat_changes(user, stat_changes, "self", fight)
        if success:
            print(f"{user.name} utilise Swords Dance ! Son Attaque augmente de 2 niveaux.")

class CalmMind(Attack):
    def __init__(self):
        super().__init__(
            name="Calm Mind",
            type_="Psychic",
            category="Status",
            power=0,
            accuracy=100,
            priority=0,
            pp=20,
            flags=[],
            target="User"
        )

    def apply_effect(self, user : PK.pokemon, target, fight):
        stat_changes = {"Sp. Atk": 1, "Sp. Def": 1}
        success = apply_stat_changes(user, stat_changes, "self", fight)
        if success:
            print(f"{user.name} utilise Calm Mind ! Son Attaque Spéciale et sa Défense Spéciale augmentent de 1 niveau.")

class BulkUp(Attack):
    def __init__(self):
        super().__init__(
            name="Bulk Up",
            type_="Fighting",
            category="Status",
            power=0,
            accuracy=100,
            priority=0,
            pp=20,
            flags=[],
            target="User"
        )

    def apply_effect(self, user : PK.pokemon, target, fight):
        stat_changes = {"Attack": 1, "Defense": 1}
        success = apply_stat_changes(user, stat_changes, "self", fight)
        if success:
            print(f"{user.name} utilise Bulk Up ! Son Attaque et sa Défense augmentent de 1 niveau.")

class CloseCombat(Attack):
    def __init__(self):
        super().__init__(
            name="Close Combat",
            type_="Fighting",
            category="Physical",
            power=120,
            accuracy=100,
            priority=0,
            pp=5,
            flags=["contact", "protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        stat_changes = {"Defense": -1, "Sp. Def": -1}
        apply_stat_changes(user, stat_changes, "self", fight)

class Psychic(Attack):
    def __init__(self):
        super().__init__(
            name="Psychic",
            type_="Psychic",
            category="Special",
            power=90,
            accuracy=100,
            priority=0,
            pp=10,
            flags=["protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        if random.randint(1, 100) <= 10:
            stat_changes = {"Sp. Def": -1}
            success = apply_stat_changes(target, stat_changes, "opponent", fight)
            if success:
                print(f"{target.name} subit une baisse de sa Défense Spéciale !")

class DragonPulse(Attack):
    def __init__(self):
        super().__init__(
            name="Dragon Pulse",
            type_="Dragon",
            category="Special",
            power=85,
            accuracy=100,
            priority=0,
            pp=10,
            flags=["protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        # Pas d'effet secondaire pour Dragon Pulse
        pass

class ElectroShot(Attack):
    def __init__(self):
        super().__init__(
            name="Electro Shot",
            type_="Electric",
            category="Special",
            power=130,
            accuracy=100,
            priority=0,
            pp=10,
            flags=["protect", "mirror", "charge"],
            target="Foe"
        )
    
    def apply_effect(self, user, target, fight):
        # Si c'est sous la pluie, pas de charge et boost direct
        if fight.weather["current"] == "Rain":
            apply_stat_changes(user, {"Sp. Atk": 1}, "self", fight)
            print(f"{user.name} absorbe l'électricité de la pluie ! Son Attaque Spéciale augmente !")
            return "attack"  # Attaque immédiatement
        
        # Au premier tour sans pluie : se charge
        if not user.charging or user.charging_attack != self:
            user.charging = True
            user.charging_attack = self
            apply_stat_changes(user, {"Sp. Atk": 1}, "self", fight)
            print(f"{user.name} se charge d'électricité ! Son Attaque Spéciale augmente !")
            return "charging"  # Indique que l'attaque est en cours de charge
        else:
            # Au deuxième tour : attaque (sans boost supplémentaire)
            user.charging = False
            user.charging_attack = None
            print(f"{user.name} relâche l'électricité accumulée !")
            return "attack"  # Indique que l'attaque est exécutée
    
    def on_condition_attack(self, user, target=None, target_attack=None, fight=None):
        # L'attaque peut toujours être utilisée
        return True



class GrassKnot(Attack):
    def __init__(self):
        super().__init__(
            name="Grass Knot",
            type_="Grass",
            category="Special",
            power=20,  # Puissance de base minimale
            accuracy=100,
            priority=0,
            pp=20,
            flags=["contact", "protect", "mirror"],
            target="Foe"
        )
    
    def get_power(self, user, target, fight):
        """
        Calcule la puissance de Grass Knot en fonction du poids de la cible.
        
        :param user: Le Pokémon qui lance l'attaque.
        :param target: Le Pokémon ciblé par l'attaque.
        :param fight: L'instance de combat en cours.
        :return: La puissance de l'attaque basée sur le poids de la cible.
        """
        weight = target.weight  # Poids de la cible en kg
        if weight < 10:
            return 20
        elif weight < 25:
            return 40
        elif weight < 50:
            return 60
        elif weight < 100:
            return 80
        elif weight < 200:
            return 100
        else:
            return 120

class SolarBeam(Attack):
    def __init__(self):
        super().__init__(
            name="Solar Beam",
            type_="Grass",
            category="Special",
            power=120,
            accuracy=100,
            priority=0,
            pp=10,
            flags=["protect", "mirror", "charge"],
            target="Foe"
        )
    
    def apply_effect(self, user, target, fight):
        # Si c'est ensoleillé, pas de charge
        if fight.weather["current"] == "Sunny":
            print(f"{user.name} absorbe la lumière du soleil et attaque immédiatement !")
            return "attack"  # Attaque immédiatement
        
        # Au premier tour sans soleil : se charge
        if not user.charging or user.charging_attack != self:
            user.charging = True
            user.charging_attack = self
            print(f"{user.name} absorbe la lumière du soleil !")
            return "charging"  # Indique que l'attaque est en cours de charge
        else:
            # Au deuxième tour : attaque
            user.charging = False
            user.charging_attack = None
            return "attack"  # Indique que l'attaque est exécutée

class SkyAttack(Attack):
    def __init__(self):
        super().__init__(
            name="Sky Attack",
            type_="Flying",
            category="Physical",
            power=140,
            accuracy=90,
            priority=0,
            pp=5,
            flags=["protect", "mirror", "charge"],
            target="Foe"
        )
        self.critical_chance = 12.5  # Taux de critique élevé
    
    def apply_effect(self, user, target, fight):
        # Au premier tour : se charge
        if not user.charging or user.charging_attack != self:
            user.charging = True
            user.charging_attack = self
            print(f"{user.name} s'élève haut dans le ciel !")
            return "charging"
        else:
            # Au deuxième tour : attaque avec chance de flinch
            user.charging = False
            user.charging_attack = None
            if random.randint(1, 100) <= 30:
                target.apply_status("flinch")
                print(f"{target.name} est flinché par l'attaque surprise !")
            return "attack"

class Bounce(Attack):
    def __init__(self):
        super().__init__(
            name="Bounce",
            type_="Flying",
            category="Physical",
            power=85,
            accuracy=85,
            priority=0,
            pp=5,
            flags=["contact", "protect", "mirror", "charge"],
            target="Foe"
        )
    
    def apply_effect(self, user, target, fight):
        # Au premier tour : s'envole
        if not user.charging or user.charging_attack != self:
            user.charging = True
            user.charging_attack = self
            print(f"{user.name} s'envole dans les airs !")
            return "charging"
        else:
            # Au deuxième tour : attaque avec chance de paralyser
            user.charging = False
            user.charging_attack = None
            if random.randint(1, 100) <= 30:
                if target.status is None:
                    target.apply_status("paralyzed")
                    print(f"{target.name} est paralysé par l'impact !")
            return "attack"

class Dig(Attack):
    def __init__(self):
        super().__init__(
            name="Dig",
            type_="Ground",
            category="Physical",
            power=80,
            accuracy=100,
            priority=0,
            pp=10,
            flags=["contact", "protect", "mirror", "charge"],
            target="Foe"
        )
    
    def apply_effect(self, user, target, fight):
        # Au premier tour : creuse
        if not user.charging or user.charging_attack != self:
            user.charging = True
            user.charging_attack = self
            print(f"{user.name} creuse un tunnel sous terre !")
            return "charging"
        else:
            # Au deuxième tour : attaque depuis le sous-sol
            user.charging = False
            user.charging_attack = None
            print(f"{user.name} surgit du sol pour attaquer !")
            return "attack"

class HyperBeam(Attack):
    def __init__(self):
        super().__init__(
            name="Hyper Beam",
            type_="Normal",
            category="Special",
            power=150,
            accuracy=90,
            priority=0,
            pp=5,
            flags=["protect", "mirror", "recharge"],
            target="Foe"
        )
    
    def apply_effect(self, user, target, fight):
        # Hyper Beam oblige le Pokémon à se reposer au tour suivant
        user.must_recharge = True
        print(f"{user.name} doit se reposer au prochain tour après cette attaque puissante !")
        
class Encore(Attack):
    def __init__(self):
        super().__init__(
            name="Encore",
            type_="Normal",
            category="Status",
            power=0,
            accuracy=100,
            priority=0,
            pp=5,
            flags=["protect", "mirror"],  # Peut être reflété par Magic Coat
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
            
        # Assurer que les attributs existent
        if not hasattr(target, 'encored_turns'):
            target.encored_turns = 0
        if not hasattr(target, 'last_used_attack'):
            target.last_used_attack = None
        if not hasattr(target, 'encored_attack'):
            target.encored_attack = None
            
        # Vérifier si le Pokémon est déjà sous l'effet d'Encore
        if target.encored_turns > 0:
            print(f"{target.name} est déjà sous l'effet d'Encore !")
            return
            
        # Vérifier si le Pokémon a utilisé une attaque récemment
        if not target.last_used_attack:
            print(f"{target.name} n'a pas utilisé d'attaque récemment ! Encore échoue.")
            return
            
        # Vérifier si l'attaque peut être répétée (exclure certaines attaques)
        non_encore_attacks = ["Transform", "Mimic", "Encore", "Struggle"]
        if target.last_used_attack.name in non_encore_attacks:
            print(f"{target.last_used_attack.name} ne peut pas être répétée avec Encore !")
            return
            
        # Appliquer l'effet Encore
        target.encored_turns = 3  # Selon les règles officielles, dure 3 tours
        target.encored_attack = target.last_used_attack
        print(f"{target.name} est forcé de répéter {target.last_used_attack.name} pendant 3 tours grâce à Encore !")

class Substitute(Attack):
    def __init__(self):
        super().__init__(
            name="Substitute",
            type_="Normal",
            category="Status",
            power=0,
            accuracy=100,
            priority=0,
            pp=10,
            flags=[],
            target="User"
        )

    def apply_effect(self, user, target, fight):
        if user.current_hp > user.max_hp // 4 and not user.has_substitute():
            substitute_hp = user.max_hp // 4
            fight.damage_method(user, substitute_hp, bypass_substitute=True)  # Le Pokémon sacrifie 1/4 de ses PV
            user.substitute_hp = substitute_hp
            print(f"{user.name} crée un clone avec {substitute_hp} PV !")
        elif user.has_substitute():
            print(f"{user.name} a déjà un clone !")
        else:
            print(f"{user.name} n'a pas assez de PV pour créer un clone !")

class Snarl(Attack):
    def __init__(self):
        super().__init__(
            name="Snarl",
            type_="Dark",
            category="Special",
            power=55,
            accuracy=95,
            priority=0,
            pp=15,
            flags=["protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        stat_changes = {"Sp. Atk": -1}
        success = apply_stat_changes(target, stat_changes, "opponent", fight)
        if success:
            print(f"{target.name} subit une baisse de sa Défense Spéciale !")

class Roost(Attack):
    def __init__(self):
        super().__init__(
            name="Roost",
            type_="Flying",
            category="Status",
            power=0,
            accuracy=100,
            priority=0,
            pp=10,
            flags=["heal"],
            target="User"
        )

        ######## FINIR ########
    def apply_effect(self, user, target, fight):
        heal_amount = user.max_hp // 2
        user.current_hp = min(user.max_hp, user.current_hp + heal_amount)
        user.types.remove("Flying")  # Perd le type Vol pour ce tour
        print(f"{user.name} se repose et récupère {heal_amount} PV ! Il perd temporairement son type Vol.")

class LeafBlade(Attack):
    def __init__(self):
        super().__init__(
            name="Leaf Blade",
            type_="Grass",
            category="Physical",
            power=90,
            accuracy=100,
            priority=0,
            pp=15,
            flags=["contact", "protect", "mirror", "sharp"],
            target="Foe"
        )
        self.critical_chance = 12.5  # Taux de critique élevé

    def apply_effect(self, user, target, fight):
        # Pas d'effet secondaire pour Leaf Blade
        pass

class ThunderWave(Attack):
    def __init__(self):
        super().__init__(
            name="Thunder Wave",
            type_="Electric",
            category="Status",
            power=0,
            accuracy=90,
            priority=0,
            pp=20,
            flags=["protect"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        if target.status is None and "Electric" not in target.types:
            target.apply_status("paralyzed")
            print(f"{target.name} est paralysé ! Il aura du mal à attaquer.")
        else:
            print(f"{target.name} est déjà affecté ou immunisé contre la paralysie.")

class Taunt(Attack):
    """Attaque qui n'est pas bloquée par les substituts"""
    def __init__(self):
        super().__init__(
            name="Taunt",
            type_="Dark",
            category="Status",
            power=0,
            accuracy=100,
            priority=0,
            pp=20,
            flags=["protect"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        # Simuler l'effet de Taunt (empêche les attaques de statut)
        print(f"{target.name} est provoqué et ne peut plus utiliser d'attaques de statut !")

class Absorb(Attack):
    """Attaque drainante qui draine des PV du clone"""
    def __init__(self):
        super().__init__(
            name="Absorb",
            type_="Grass",
            category="Special",
            power=20,
            accuracy=100,
            priority=0,
            pp=25,
            flags=["protect", "mirror", "heal"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        # Cette méthode sera appelée après le calcul des dégâts pour le drain
        pass

class PerishSong(Attack):
    """Attaque sonore qui ignore les substituts"""
    def __init__(self):
        super().__init__(
            name="Perish Song",
            type_="Normal",
            category="Status",
            power=0,
            accuracy=100,
            priority=0,
            pp=5,
            flags=["sound"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        print(f"{target.name} entend le Chant Perish ! Il sera K.O. dans 3 tours !")

class Tackle(Attack):
    """Attaque simple pour les tests"""
    def __init__(self):
        super().__init__(
            name="Tackle",
            type_="Normal",
            category="Physical",
            power=40,
            accuracy=100,
            priority=0,
            pp=35,
            flags=["contact", "protect", "mirror"],
            target="Foe"
        )