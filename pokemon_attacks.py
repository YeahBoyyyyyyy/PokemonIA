import pokemon_datas as STATS
import pokemon_talents as TALENTS
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

    def on_condition_attack(self, user):
        """
        Cette méthode est appelée pour vérifier si l'attaque peut être lancée. Sert principalement pour fake out et first impression.

        :param user: Le Pokémon qui lance l'attaque.
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
            flags=[],
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
            flags=[],
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
    
    def on_condition_attack(self, user):
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