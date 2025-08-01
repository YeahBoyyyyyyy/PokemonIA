import pokemon_datas as STATS
import pokemon_talents as TALENTS
import pokemon as PK
from pokemon import apply_stat_changes
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
ground: Ground-type moves whhose power are diminished by grassy terrain.
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
        :return: Le multiplicateur de puissance (par défaut 1.0).
        """
        return 1.0  # Par défaut, pas de boost
    
    def get_effective_accuracy(self, user, target, fight):
        """
        Calcule la précision effective de l'attaque en tenant compte des conditions.
        
        :param user: Le Pokémon qui lance l'attaque.
        :param target: Le Pokémon ciblé par l'attaque.
        :param fight: L'instance de combat en cours.
        :return: La précision effective (peut être True pour une précision garantie).
        """
        return self.accuracy  # Par défaut, retourne la précision de base
        

class Flamethrower(Attack):
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
            print(f"{target} est brulé !")
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
            accuracy=True,
            priority=0,
            pp=10,
            flags=[],
            target="User"
        )
    
    def apply_effect(self, user, target, fight):
        fight.set_weather("Rain", duration=5)
        print(f"{user.name} invoque la pluie !")

class Sandstorm(Attack):
    def __init__(self):
        super().__init__(
            name="Sandstorm",
            type_="Ground",
            category="Status",
            power=0,
            accuracy=True,
            priority=0,
            pp=10,
            flags=[],
            target="User"
        )
    
    def apply_effect(self, user, target, fight):
        fight.set_weather("Sandstorm", duration=5)
        print(f"{user.name} invoque la tempête de sable !")

class SunnyDay(Attack):
    def __init__(self):
        super().__init__(
            name="Sunny Day",
            type_="Fire",
            category="Status",
            power=0,
            accuracy=True,
            priority=0,
            pp=10,
            flags=[],
            target="User"
        )
    
    def apply_effect(self, user, target, fight):
        if fight.weather["current"] != "Sunny":
            fight.set_weather("Sunny", duration=5)
            print(f"{user.name} invoque le soleil !")

class Recover(Attack):
    def __init__(self):
        super().__init__(
            name="Recover",
            type_="Normal",
            category="Status",
            power=0,
            accuracy=True,
            priority=0,
            pp=10,
            flags=["heal"],
            target="User"
        )

    def apply_effect(self, user, target, fight):
        # Vérifier si l'utilisateur est sous l'effet de Heal Block
        if getattr(user, 'heal_blocked', False):
            print(f"{user.name} ne peut pas utiliser {self.name} car il est sous l'effet de Heal Block !")
            return
            
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
        # Utiliser les types effectifs pour la défense (incluant Tera)
        effective_types = target.get_effective_types_for_defense()
        
        if "Grass" in effective_types:
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

    def apply_effect(self, user, target, fight):
        """
        U-turn force le changement de Pokémon après l'attaque.
        Cela ne se produit que si :
        1. L'utilisateur survit à l'attaque
        2. Il y a un autre Pokémon disponible dans l'équipe
        3. L'utilisateur n'est pas piégé (par Arena Trap, Shadow Tag, etc.)
        """
        # Vérifier si l'utilisateur est encore en vie
        if user.current_hp <= 0:
            print(f"{user.name} est K.O. et ne peut pas utiliser U-turn pour changer !")
            return
        
        # Déterminer quelle équipe possède l'utilisateur
        team_id = fight.get_team_id(user)
        if team_id is None:
            return
            
        team = fight.team1 if team_id == 1 else fight.team2
        
        # Vérifier s'il y a d'autres Pokémon disponibles
        available_pokemon = [p for p in team if p.current_hp > 0 and p != user]
        
        if not available_pokemon:
            print(f"{user.name} ne peut pas changer car il n'y a pas d'autre Pokémon disponible !")
            return
        
        # Marquer que le Pokémon doit changer après l'attaque
        user.must_switch_after_attack = True
        user.switch_reason = "U-Turn"
        print(f"{user.name} doit revenir après U-turn !")

class FlipTurn(Attack):
    def __init__(self):
        super().__init__(
            name="Flip Turn",
            type_="Water",
            category="Physical",
            power=60,
            accuracy=100,
            priority=0,
            pp=20,
            flags=["contact", "protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        """
        Flip Turn force le changement de Pokémon après l'attaque.
        Cela ne se produit que si :
        1. L'utilisateur survit à l'attaque
        2. Il y a un autre Pokémon disponible dans l'équipe
        3. L'utilisateur n'est pas piégé (par Arena Trap, Shadow Tag, etc.)
        """
        # Vérifier si l'utilisateur est encore en vie
        if user.current_hp <= 0:
            print(f"{user.name} est K.O. et ne peut pas utiliser Flip Turn pour changer !")
            return
        
        # Déterminer quelle équipe possède l'utilisateur
        team_id = fight.get_team_id(user)
        if team_id is None:
            return
            
        team = fight.team1 if team_id == 1 else fight.team2
        
        # Vérifier s'il y a d'autres Pokémon disponibles
        available_pokemon = [p for p in team if p.current_hp > 0 and p != user]
        
        if not available_pokemon:
            print(f"{user.name} ne peut pas changer car il n'y a pas d'autre Pokémon disponible !")
            return
        
        # Marquer que le Pokémon doit changer après l'attaque
        user.must_switch_after_attack = True
        user.switch_reason = "Flip Turn"
        print(f"{user.name} doit revenir après Flip Turn !")


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
        # Utiliser les types effectifs pour la défense (incluant Tera)
        effective_types = target.get_effective_types_for_defense()
        
        if target.status is None and "Poison" not in effective_types and "Steel" not in effective_types:
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
        # Si la cible n'attaque pas (switch, KO, etc.), Sucker Punch échoue
        if target_atk is None:
            print("L'attaque échoue !")
            return False
        # Si la cible utilise une attaque de statut, Sucker Punch échoue
        if target_atk.category == "Status":
            print("L'attaque échoue !")
            return False
        # Sinon, l'attaque réussit
        return True

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
        else:
            print("L'attaque échoue")

class LightScreen(Attack):
    def __init__(self):
        super().__init__(
            name="Light Screen",
            type_="Psychic",
            category="Status",
            power=0,
            accuracy=True,
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
        else:
            print("L'attaque échoue.")

class AuroraVeil(Attack):
    def __init__(self):
        super().__init__(
            name="Aurora Veil",
            type_="Ice",
            category="Status",
            power=0,
            accuracy=True,
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
        else:
            print("L'attaque échoue.")

class SwordsDance(Attack):
    def __init__(self):
        super().__init__(
            name="Swords Dance",
            type_="Normal",
            category="Status",
            power=0,
            accuracy=True,
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

class NastyPlot(Attack):
    def __init__(self):
        super().__init__(
            name="Nasty Plot",
            type_="Dark",
            category="Status",
            power=0,
            accuracy=True,
            priority=0,
            pp=20,
            flags=[],
            target="User"
        )

    def apply_effect(self, user : PK.pokemon, target, fight):
        stat_changes = {"Sp. Atk": 2}
        success = apply_stat_changes(user, stat_changes, "self", fight)
        if success:
            print(f"{user.name} utilise Nasty Plot ! Son Attaque Spéciale augmente de 2 niveaux.")

class CalmMind(Attack):
    def __init__(self):
        super().__init__(
            name="Calm Mind",
            type_="Psychic",
            category="Status",
            power=0,
            accuracy=True,
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
            accuracy=True,
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

class IronDefense(Attack):
    def __init__(self):
        super().__init__(
            name="Iron Defense",
            type_="Steel",
            category="Status",
            power=0,
            accuracy=True,
            priority=0,
            pp=15,
            flags=["protect", "mirror"],
            target="User"
        )

    def apply_effect(self, user, target, fight):
        """
        Augmente la Défense de l'utilisateur de 2 niveaux.
        """
        stat_changes = {"Defense": 2}
        success = apply_stat_changes(user, stat_changes, "self", fight)
        
        if success:
            print(f"{user.name} renforce sa Défense avec Iron Defense !")

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

class BehemothBlade(Attack):
    def __init__(self):
        super().__init__(
            name="Behemoth Blade",
            type_="Steel",
            category="Physical",
            power=100,
            accuracy=100,
            priority=0,
            pp=5,
            flags=["contact", "protect", "mirror"],
            target="Foe"
        )
    
    def apply_effect(self, user, target, fight):
        """
        Behemoth Blade fait des dégâts doublés contre les Pokémon Dynamax.
        """
        # En l'absence de système Dynamax, pas d'effet spécial
        pass

class BraveBird(Attack):
    def __init__(self):
        super().__init__(
            name="Brave Bird",
            type_="Flying",
            category="Physical",
            power=120,
            accuracy=100,
            priority=0,
            pp=15,
            flags=["contact", "protect", "mirror"],
            target="Foe"
        )
    
    def apply_effect(self, user, target, fight, damage_dealt=0):
        """
        L'utilisateur subit des dégâts de recul à hauteur de 1/3 des dégâts infligés.
        """
        if damage_dealt > 0:
            recoil_damage = damage_dealt // 3
            fight.damage_method(user, recoil_damage)
            print(f"{user.name} subit {recoil_damage} PV de dégâts de recul après avoir utilisé Brave Bird.")

class DrainingKiss(Attack):
    def __init__(self):
        super().__init__(
            name="Draining Kiss",
            type_="Fairy",
            category="Special",
            power=50,
            accuracy=100,
            priority=0,
            pp=10,
            flags=["contact", "protect", "mirror", "heal"],
            target="Foe"
        )
    
    def apply_effect(self, user, target, fight, damage_dealt=0):
        """
        L'utilisateur récupère 75% des dégâts infligés.
        """
        if damage_dealt > 0:
            healing = int(damage_dealt * 0.75)
            if user.current_hp < user.max_hp:
                actual_healing = min(healing, user.max_hp - user.current_hp)
                user.current_hp += actual_healing
                print(f"{user.name} récupère {actual_healing} PV grâce à Draining Kiss !")

class LeafStorm(Attack):
    def __init__(self):
        super().__init__(
            name="Leaf Storm",
            type_="Grass",
            category="Special",
            power=130,
            accuracy=90,
            priority=0,
            pp=5,
            flags=["protect", "mirror"],
            target="Foe"
        )
    
    def apply_effect(self, user, target, fight):
        """
        Réduit l'Attaque Spéciale de l'utilisateur de 2 niveaux après utilisation.
        """
        stat_changes = {"Sp. Atk": -2}
        success = apply_stat_changes(user, stat_changes, "self", fight)
        if success:
            print(f"L'Attaque Spéciale de {user.name} diminue drastiquement !")

class PlayRough(Attack):
    def __init__(self):
        super().__init__(
            name="Play Rough",
            type_="Fairy",
            category="Physical",
            power=90,
            accuracy=90,
            priority=0,
            pp=10,
            flags=["contact", "protect", "mirror"],
            target="Foe"
        )
    
    def apply_effect(self, user, target, fight):
        """
        A 10% de chance de réduire l'Attaque de la cible d'un niveau.
        """
        if random.random() < 0.1:
            stat_changes = {"Attack": -1}
            success = apply_stat_changes(target, stat_changes, "opponent", fight)
            if success:
                print(f"L'Attaque de {target.name} diminue !")

class ShellSmash(Attack):
    def __init__(self):
        super().__init__(
            name="Shell Smash",
            type_="Normal",
            category="Status",
            power=0,
            accuracy=True,
            priority=0,
            pp=15,
            flags=[],
            target="User"
        )
    
    def apply_effect(self, user, target, fight):
        """
        Réduit la Défense et la Défense Spéciale d'un niveau.
        Augmente l'Attaque, l'Attaque Spéciale et la Vitesse de 2 niveaux.
        """
        stat_changes = {
            "Defense": -1,
            "Sp. Def": -1,
            "Attack": 2,
            "Sp. Atk": 2,
            "Speed": 2
        }
        success = apply_stat_changes(user, stat_changes, "self", fight)
        if success:
            print(f"{user.name} brise sa carapace ! Ses capacités offensives et sa vitesse augmentent énormément !")

class ShiftGear(Attack):
    def __init__(self):
        super().__init__(
            name="Shift Gear",
            type_="Steel",
            category="Status",
            power=0,
            accuracy=True,
            priority=0,
            pp=10,
            flags=[],
            target="User"
        )
    
    def apply_effect(self, user, target, fight):
        """
        Augmente l'Attaque d'un niveau et la Vitesse de 2 niveaux.
        """
        stat_changes = {"Attack": 1, "Speed": 2}
        success = apply_stat_changes(user, stat_changes, "self", fight)
        if success:
            print(f"{user.name} change de vitesse ! Son Attaque et sa Vitesse augmentent !")

class TrickRoom(Attack):
    def __init__(self):
        super().__init__(
            name="Trick Room",
            type_="Psychic",
            category="Status",
            power=0,
            accuracy=True,
            priority=-7,  # Priorité très basse
            pp=5,
            flags=[],
            target="All"
        )
    
    def apply_effect(self, user, target, fight):
        """
        Inverse la priorité de vitesse pendant 5 tours.
        Si Trick Room est déjà actif, le désactive.
        """
        fight.set_trick_room()

class WaveCrash(Attack):
    def __init__(self):
        super().__init__(
            name="Wave Crash",
            type_="Water",
            category="Physical",
            power=120,
            accuracy=100,
            priority=0,
            pp=10,
            flags=["contact", "protect", "mirror"],
            target="Foe"
        )
    
    def apply_effect(self, user, target, fight, damage_dealt=0):
        """
        L'utilisateur subit des dégâts de recul à hauteur de 1/3 des dégâts infligés.
        """
        if damage_dealt > 0:
            recoil_damage = damage_dealt // 3
            fight.damage_method(user, recoil_damage)
            print(f"{user.name} subit {recoil_damage} PV de dégâts de recul après avoir utilisé Wave Crash.")

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
            accuracy=True,
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
            print(f"{target.name} est déjà sous l'effet d'Encore ! L'attaque échoue.")
            return
            
        # Vérifier si le Pokémon a utilisé une attaque récemment
        if not target.last_used_attack:
            print(f"{target.name} n'a pas utilisé d'attaque récemment ! L'attaque échoue.")
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
            accuracy=True,
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
            print(f"{user.name} a déjà un clone ! L'attaque échoue.")
        else:
            print(f"{user.name} n'a pas assez de PV pour créer un clone ! L'attaque échoue.")

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
            accuracy=True,
            priority=0,
            pp=10,
            flags=["heal"],
            target="User"
        )

        ######## FINIR ########
    def apply_effect(self, user, target, fight):
        # Vérifier si l'utilisateur est sous l'effet de Heal Block
        if getattr(user, 'heal_blocked', False):
            print(f"{user.name} ne peut pas utiliser {self.name} car il est sous l'effet de Heal Block !")
            return
            
        # Soigner 50% des PV max
        heal_amount = user.max_hp // 2
        user.current_hp = min(user.max_hp, user.current_hp + heal_amount)
        
        # Gérer la perte temporaire du type Vol
        if "Flying" in user.types:
            # Marquer que le Pokémon a perdu son type Vol pour ce tour
            user.lost_flying_from_roost = True
            user.original_types = user.types.copy()  # Sauvegarder les types originaux
            user.types = [t for t in user.types if t != "Flying"]  # Retirer temporairement Flying
            
            # Si le Pokémon n'a plus de type après avoir retiré Flying, il devient Normal
            if len(user.types) == 0:
                user.types = ["Normal"]
            
            print(f"{user.name} se repose et récupère {heal_amount} PV ! Il perd temporairement son type Vol.")
        else:
            print(f"{user.name} se repose et récupère {heal_amount} PV !")

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

class WoodHammer(Attack):
    def __init__(self):
        super().__init__(
            name="Wood Hammer",
            type_="Grass",
            category="Physical",
            power=120,
            accuracy=100,
            priority=0,
            pp=15,
            flags=["contact", "protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight, damage_dealt=0):
        # L'utilisateur subit des dégâts de recul à hauteur de 1/3 des dégâts infligés
        if damage_dealt > 0:
            recoil_damage = damage_dealt // 3
            fight.damage_method(user, recoil_damage)
            print(f"{user.name} subit {recoil_damage} PV de dégâts de recul après avoir utilisé Wood Hammer.")

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
            flags=["protect", "reflectable"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        if target.status is None and "Electric" not in target.types:
            target.apply_status("paralyzed")
            print(f"{target.name} est paralysé ! Il aura du mal à attaquer.")
        else:
            print("L'attaque échoue.")

class Taunt(Attack):
    """Attaque qui n'est pas bloquée par les substituts et empêche l'usage d'attaques de statut"""
    def __init__(self):
        super().__init__(
            name="Taunt",
            type_="Dark",
            category="Status",
            power=0,
            accuracy=True,
            priority=0,
            pp=20,
            flags=["protect"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        # Taunt dure 3 tours (comme dans les jeux officiels)
        target.taunted_turns = 3
        print(f"{target.name} est provoqué et ne peut plus utiliser d'attaques de statut pendant 3 tours !")

class Earthquake(Attack):
    def __init__(self):
        super().__init__(
            name="Earthquake",
            type_="Ground",
            category="Physical",
            power=100,
            accuracy=100,
            priority=0,
            pp=10,
            flags=["protect", "mirror", "ground"],
            target="All"
        )

    def apply_effect(self, user, target, fight):
        # Pas d'effet secondaire pour Earthquake
        pass

class PerishSong(Attack):
    """Attaque sonore qui ignore les substituts"""
    def __init__(self):
        super().__init__(
            name="Perish Song",
            type_="Normal",
            category="Status",
            power=0,
            accuracy=True,
            priority=0,
            pp=5,
            flags=["sound"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        print(f"{target.name} entend le Chant Perish ! Il sera K.O. dans 3 tours !")

class Trick(Attack):
    def __init__(self):
        super().__init__(
            name="Trick",
            type_="Psychic",
            category="Status",
            power=0,
            accuracy=True,
            priority=0,
            pp=10,
            flags=["protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        """Échange les objets entre l'utilisateur et la cible. Et ca même si l'un des deux n'a pas d'objet."""
        user_item = user.item
        target_item = target.item
        target.item = user_item
        user.item = target_item

class Hurricane(Attack):
    def __init__(self):
        super().__init__(
            name="Hurricane",
            type_="Flying",
            category="Special",
            power=110,
            accuracy=70,
            priority=0,
            pp=10,
            flags=["protect", "mirror"],
            target="Foe"
        )

    def get_effective_accuracy(self, user, target, fight):
        """Hurricane ne peut pas rater sous la pluie."""
        if fight and fight.weather.get("current") == "Rain":
            return True  # Précision garantie sous la pluie
        return self.accuracy  # Précision normale (70%) sinon

    def apply_effect(self, user, target, fight):
        if random.random() < 0.3:
            target.apply_status("confused")
            print(f"{target.name} est confus !")

class Thunder(Attack):
    def __init__(self):
        super().__init__(
            name="Thunder",
            type_="Electric",
            category="Special",
            power=110,
            accuracy=70,
            priority=0,
            pp=10,
            flags=["protect", "mirror"],
            target="Foe"
        )

    def get_effective_accuracy(self, user, target, fight):
        """Thunder ne peut pas rater sous la pluie, précision réduite au soleil."""
        if fight and fight.weather.get("current") == "Rain":
            return True  # Précision garantie sous la pluie
        elif fight and fight.weather.get("current") == "Sunny":
            return 50  # Précision réduite au soleil
        return self.accuracy  # Précision normale (70%) sinon

    def apply_effect(self, user, target, fight):
        if random.random() < 0.3:
            target.apply_status("paralyzed")
            print(f"{target.name} est paralysé !")

class Blizzard(Attack):
    def __init__(self):
        super().__init__(
            name="Blizzard",
            type_="Ice",
            category="Special",
            power=110,
            accuracy=70,
            priority=0,
            pp=5,
            flags=["protect", "mirror"],
            target="All Foes"
        )

    def get_effective_accuracy(self, user, target, fight):
        """Blizzard ne peut pas rater pendant la grêle."""
        if fight and fight.weather.get("current") in ["Hail", "Snow"]:
            return True  # Précision garantie pendant la grêle/neige
        return self.accuracy  # Précision normale (70%) sinon

    def apply_effect(self, user, target, fight):
        if random.random() < 0.1:
            target.apply_status("frozen")
            print(f"{target.name} est gelé !")

class AerialAce(Attack):
    def __init__(self):
        super().__init__(
            name="Aerial Ace",
            type_="Flying",
            category="Physical",
            power=60,
            accuracy=100,  # Ne rate jamais
            priority=0,
            pp=20,
            flags=["contact", "protect", "mirror"],
            target="Foe"
        )

    def get_effective_accuracy(self, user, target, fight):
        """Aerial Ace ne peut jamais rater."""
        return True

class Scald(Attack):
    def __init__(self):
        super().__init__(
            name="Scald",
            type_="Water",
            category="Special",
            power=80,
            accuracy=100,
            priority=0,
            pp=15,
            flags=["protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        if random.random() < 0.3:
            target.apply_status("burned")
            print(f"{target.name} est brûlé !")
        
class DynamicPunch(Attack):
    def __init__(self):
        super().__init__(
            name="Dynamic Punch",
            type_="Fighting",
            category="Physical",
            power=100,
            accuracy=50,  # Très faible précision
            priority=0,
            pp=5,
            flags=["contact", "protect", "mirror", "punch"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        # 100% de chance de rendre confus si l'attaque touche
        target.apply_status("confused")
        print(f"{target.name} est confus à cause de Dynamic Punch !")

class TeraBlast(Attack):
    def __init__(self):
        super().__init__(
            name="Tera Blast",
            type_="Normal",  # Type par défaut, sera modifié selon le Tera Type
            category="Special",  # Catégorie par défaut, sera modifiée selon les stats
            power=80,
            accuracy=100,
            priority=0,
            pp=5,
            flags=["protect", "mirror"],
            target="Foe"
        )

    def get_effective_type(self, user, target, fight):
        """
        Détermine le type effectif de Tera Blast.
        
        :param user: Le Pokémon qui lance l'attaque.
        :param target: Le Pokémon ciblé.
        :param fight: L'instance de combat.
        :return: Le type effectif de l'attaque.
        """
        if user.tera_activated and user.tera_type:
            # Type Stellar spécial : Tera Blast devient le premier type du Pokémon
            if user.tera_type == "Stellar":
                return user.original_types[0] if hasattr(user, 'original_types') and user.original_types else user.types[0]
            return user.tera_type
        return "Normal"

    def get_effective_category(self, user, target, fight):
        """
        Détermine la catégorie effective de Tera Blast.
        
        :param user: Le Pokémon qui lance l'attaque.
        :param target: Le Pokémon ciblé.
        :param fight: L'instance de combat.
        :return: La catégorie effective ("Physical" ou "Special").
        """
        # Tera Blast devient Physique si l'Attaque > Attaque Spéciale
        if user.stats["Attack"] > user.stats["Sp. Atk"]:
            return "Physical"
        return "Special"

    def apply_before_damage(self, user, target, fight):
        """
        Applique les modifications de type et catégorie avant le calcul des dégâts.
        """
        # Sauvegarder les valeurs originales si pas déjà fait
        if not hasattr(self, '_original_type'):
            self._original_type = self.type
        if not hasattr(self, '_original_category'):
            self._original_category = self.category
        
        # Modifier le type selon le Tera Type
        new_type = self.get_effective_type(user, target, fight)
        if new_type != self.type:
            self.type = new_type
            print(f"Tera Blast devient de type {self.type} !")
        
        # Modifier la catégorie selon les stats
        new_category = self.get_effective_category(user, target, fight)
        if new_category != self.category:
            self.category = new_category
            print(f"Tera Blast devient une attaque {self.category.lower()} !")
    
    def restore_original_properties(self):
        """
        Restaure les propriétés originales de l'attaque après utilisation.
        """
        if hasattr(self, '_original_type'):
            self.type = self._original_type
        if hasattr(self, '_original_category'):
            self.category = self._original_category
    
    def apply_effect(self, user, target, fight):
        # Appliquer les modifications avant les dégâts
        self.apply_before_damage(user, target, fight)
        # Pas d'effet secondaire pour Tera Blast

class ShedTail(Attack):
    def __init__(self):
        super().__init__(
            name="Shed Tail",
            type_="Normal",
            category="Status",
            power=0,
            accuracy=True,
            priority=0,
            pp=10,
            flags=["protect", "mirror"],
            target="User"
        )

    def apply_effect(self, user, target, fight):
        """
        Shed Tail crée un substitute (clone) et force le changement de Pokémon.
        L'utilisateur sacrifie 1/4 de ses PV max pour créer le substitute.
        Le substitute sera transféré au Pokémon qui entre.
        """
        # Vérifier si l'utilisateur a assez de PV
        if user.current_hp <= user.max_hp // 4:
            print(f"{user.name} n'a pas assez de PV pour utiliser Shed Tail !")
            return
        
        # Vérifier si le Pokémon a déjà un substitute
        if user.has_substitute():
            print(f"{user.name} a déjà un clone !")
            return
        
        # Créer le substitute (même mécanique que Substitute)
        substitute_hp = user.max_hp // 4
        fight.damage_method(user, substitute_hp, bypass_substitute=True)  # Le Pokémon sacrifie 1/4 de ses PV
        
        # Stocker le substitute pour le transfert (attribut temporaire sur fight)
        team_id = fight.get_team_id(user)
        if team_id == 1:
            fight.pending_substitute_team1 = substitute_hp
        else:
            fight.pending_substitute_team2 = substitute_hp
        
        print(f"{user.name} crée un clone avec {substitute_hp} PV qui sera transféré !")
        
        # Déterminer quelle équipe possède l'utilisateur
        if team_id is None:
            return
            
        team = fight.team1 if team_id == 1 else fight.team2
        
        # Vérifier s'il y a d'autres Pokémon disponibles
        available_pokemon = [p for p in team if p.current_hp > 0 and p != user]
        
        if not available_pokemon:
            print(f"{user.name} ne peut pas changer car il n'y a pas d'autre Pokémon disponible !")
            return
        
        # Marquer que l'utilisateur doit changer après l'attaque
        user.must_switch_after_attack = True
        user.switch_reason = "Shed Tail"
        print(f"{user.name} doit revenir après avoir utilisé Shed Tail !")

class Spikes(Attack):
    def __init__(self):
        super().__init__(
            name="Spikes",
            type_="Ground",
            category="Status",
            power=0,
            accuracy=True,
            priority=0,
            pp=20,
            flags=["protect", "reflectable"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        """
        Pose des piques qui blessent les Pokémon ennemis à leur entrée.
        Peut être posé jusqu'à 3 fois pour augmenter les dégâts.
        """
        # Déterminer l'équipe adverse
        user_team_id = fight.get_team_id(user)
        opponent_hazards = fight.hazards_team2 if user_team_id == 1 else fight.hazards_team1
        
        if opponent_hazards["Spikes"] < 3:
            opponent_hazards["Spikes"] += 1
            layers = opponent_hazards["Spikes"]
            print(f"{user.name} pose des Spikes ! (Couche {layers}/3)")
        else:
            print(f"Il y a déjà le maximum de Spikes sur le terrain !")

class StealthRock(Attack):
    def __init__(self):
        super().__init__(
            name="Stealth Rock",
            type_="Rock",
            category="Status",
            power=0,
            accuracy=True,
            priority=0,
            pp=20,
            flags=["protect", "reflectable"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        """
        Pose des pierres pointues flottantes qui blessent les Pokémon ennemis à leur entrée.
        Efficacité basée sur le type Rock.
        """
        # Déterminer l'équipe adverse
        user_team_id = fight.get_team_id(user)
        opponent_hazards = fight.hazards_team2 if user_team_id == 1 else fight.hazards_team1
        
        if not opponent_hazards["Stealth Rock"]:
            opponent_hazards["Stealth Rock"] = True
            print(f"{user.name} pose des Piège-de-Roc flottants !")
        else:
            print(f"Il y a déjà des Piège-de-Roc sur le terrain !")

class ToxicSpikes(Attack):
    def __init__(self):
        super().__init__(
            name="Toxic Spikes",
            type_="Poison",
            category="Status",
            power=0,
            accuracy=True,
            priority=0,
            pp=20,
            flags=["protect", "reflectable"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        """
        Pose des piques toxiques qui empoisonnent les Pokémon ennemis à leur entrée.
        1 couche = poison normal, 2 couches = poison grave.
        """
        # Déterminer l'équipe adverse
        user_team_id = fight.get_team_id(user)
        opponent_hazards = fight.hazards_team2 if user_team_id == 1 else fight.hazards_team1
        
        if opponent_hazards["Toxic Spikes"] < 2:
            opponent_hazards["Toxic Spikes"] += 1
            layers = opponent_hazards["Toxic Spikes"]
            effect = "empoisonnement" if layers == 1 else "empoisonnement grave"
            print(f"{user.name} pose des Toxic Spikes ! (Couche {layers}/2 - {effect})")
        else:
            print(f"Il y a déjà le maximum de Toxic Spikes sur le terrain !")

class StickyWeb(Attack):
    def __init__(self):
        super().__init__(
            name="Sticky Web",
            type_="Bug",
            category="Status",
            power=0,
            accuracy=True,
            priority=0,
            pp=20,
            flags=["protect", "reflectable"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        """
        Pose une toile collante qui réduit la vitesse des Pokémon ennemis à leur entrée.
        """
        # Déterminer l'équipe adverse
        user_team_id = fight.get_team_id(user)
        opponent_hazards = fight.hazards_team2 if user_team_id == 1 else fight.hazards_team1
        
        if not opponent_hazards["Sticky Web"]:
            opponent_hazards["Sticky Web"] = True
            print(f"{user.name} tisse une Toile Gluante !")
        else:
            print(f"Il y a déjà une Toile Gluante sur le terrain !")

class RapidSpin(Attack):
    def __init__(self):
        super().__init__(
            name="Rapid Spin",
            type_="Normal",
            category="Physical",
            power=50,
            accuracy=100,
            priority=0,
            pp=40,
            flags=["protect", "mirror", "contact"],
            target="Single"
        )

    def apply_effect(self, user, target, fight):
        """
        Attaque qui supprime tous les Entry Hazards de son côté du terrain.
        Augmente aussi la vitesse de l'utilisateur d'un niveau.
        """
        # Déterminer l'équipe de l'utilisateur
        user_team_id = fight.get_team_id(user)
        user_hazards = fight.hazards_team1 if user_team_id == 1 else fight.hazards_team2
        
        # Vérifier s'il y a des hazards à supprimer
        has_hazards = (user_hazards["Spikes"] > 0 or 
                      user_hazards["Stealth Rock"] or 
                      user_hazards["Toxic Spikes"] > 0 or 
                      user_hazards["Sticky Web"] or 
                      user.leech_seeded_by != None)
        
        if has_hazards:
            # Supprimer tous les hazards
            user_hazards["Spikes"] = 0
            user_hazards["Stealth Rock"] = False
            user_hazards["Toxic Spikes"] = 0
            user_hazards["Sticky Web"] = False
            user.leech_seeded_by = None  # Enlever le Leech Seed si présent
            print(f"{user.name} supprime tous les pièges de son côté avec Rapid Spin !")
        
        # Augmenter la vitesse (depuis la Gen VIII)
        stats_changes = {"Speed": 1}
        success = apply_stat_changes(user, stats_changes, "self", fight)
        if success:
            print(f"{user.name} augmente sa Vitesse !")

class Defog(Attack):
    def __init__(self):
        super().__init__(
            name="Defog",
            type_="Flying",
            category="Status",
            power=0,
            accuracy=True,
            priority=0,
            pp=15,
            flags=[],
            target="Single"
        )

    def apply_effect(self, user, target, fight):
        """
        Supprime TOUS les Entry Hazards des deux côtés du terrain.
        Réduit l'esquive de la cible d'un niveau.
        """
        # Supprimer tous les hazards des deux équipes
        for hazards in [fight.hazards_team1, fight.hazards_team2]:
            hazards["Spikes"] = 0
            hazards["Stealth Rock"] = False
            hazards["Toxic Spikes"] = 0
            hazards["Sticky Web"] = False

        # Enlever le Leech Seed si présent
        if user.leech_seeded_by is not None:
            user.leech_seeded_by = None
        
        print(f"{user.name} dissipe tous les pièges du terrain avec Débrouillard !")
        
        # Réduire l'esquive de la cible
        if target.stats_modifier[7] > -6:  # Evasion est à l'index 7
            target.stats_modifier[7] -= 1
            print(f"L'esquive de {target.name} diminue !")

class MortalSpin(Attack):
    def __init__(self):
        super().__init__(
            name="Mortal Spin",
            type_="Poison",
            category="Physical",
            power=70,
            accuracy=100,
            priority=0,
            pp=10,
            flags=["protect", "mirror", "contact"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight, damage_dealt=0):
        """
        Supprime les Entry Hazards de son côté du terrain (effet qui s'applique toujours).
        Empoisonne la cible si elle n'est pas immunisée ET si l'attaque a infligé des dégâts.
        """
        # Supprimer les hazards de l'utilisateur (cet effet s'applique toujours)
        user_hazards = fight.hazards_team1 if fight.get_team_id(user) == 1 else fight.hazards_team2
        user_hazards["Spikes"] = 0
        user_hazards["Stealth Rock"] = False
        user_hazards["Toxic Spikes"] = 0
        user_hazards["Sticky Web"] = False

        # Enlever le Leech Seed si présent
        if user.leech_seeded_by is not None:
            user.leech_seeded_by = None
        
        print(f"{user.name} supprime tous les pièges de son côté avec Mortal Spin !")
        
        # Empoisonner la cible seulement si l'attaque a infligé des dégâts
        if damage_dealt > 0 and target.status is None and "Poison" not in target.types:
            target.apply_status("poison")
            print(f"{target.name} est empoisonné par Mortal Spin !")

class MagicCoat(Attack):
    def __init__(self):
        super().__init__(
            name="Magic Coat",
            type_="Psychic",
            category="Status",
            power=0,
            accuracy=True,
            priority=4,
            pp=15,
            flags=["protect"],
            target="User"
        )

    def apply_effect(self, user, target, fight):
        """
        Renvoie les attaques de statut à l'adversaire pendant ce tour.
        Même effet que Magic Bounce mais activé par une attaque.
        """
        user.magic_coat_active = True
        user.magic_coat_turns = 1
        print(f"{user.name} se couvre d'un voile magique ! Les attaques de statut seront renvoyées !")

class PsychicNoise(Attack):
    def __init__(self):
        super().__init__(
            name="Psychic Noise",
            type_="Psychic",
            category="Special",
            power=75,
            accuracy=100,
            priority=0,
            pp=10,
            flags=["protect", "mirror", "sound"],  # Ajout du flag "sound"
            target="Foe"  # Une seule cible, pas "All Foes"
        )

    def apply_effect(self, user, target, fight):
        """
        Empêche le Pokémon ciblé d'utiliser des attaques de soin pendant 2 tours.
        Les objets comme les Restes ne soignent plus et les terrains/talents non plus.
        """
        if target.current_hp <= 0:
            return
            
        # Appliquer l'effet Heal Block
        target.heal_blocked = True
        target.heal_blocked_turns = 2  # Durée de l'effet selon les règles officielles
        print(f"{target.name} ne peut plus se soigner pendant 2 tours à cause de Psychic Noise !")

class HealBell(Attack):
    def __init__(self):
        super().__init__(
            name="Heal Bell",
            type_="Normal",
            category="Status",
            power=0,
            accuracy=True,
            priority=0,
            pp=5,
            flags=["heal", "sound"],  # Attaque de soin sonore
            target="All Allies"
        )

    def apply_effect(self, user, target, fight):
        """
        Soigne tous les statuts de l'équipe (comme Aromatherapy).
        Bloquée par Heal Block.
        """
        # Cette vérification sera automatiquement faite par can_use_attack()
        # grâce au flag "heal" et à la vérification dans battle_interface.py
        
        # Déterminer l'équipe de l'utilisateur
        team_id = fight.get_team_id(user)
        team = fight.team1 if team_id == 1 else fight.team2
        
        healed_pokemon = []
        for pokemon in team:
            if pokemon.current_hp > 0 and pokemon.status != "normal":
                pokemon.status = "normal"
                pokemon.status_turns = 0
                healed_pokemon.append(pokemon.name)
        
        if healed_pokemon:
            print(f"Heal Bell soigne les statuts de : {', '.join(healed_pokemon)} !")
        else:
            print(f"Aucun Pokémon de l'équipe n'avait de statut à soigner.")

class PartingShot(Attack):
    def __init__(self):
        super().__init__(
            name="Parting Shot",
            type_="Dark",
            category="Status",
            power=0,
            accuracy=True,
            priority=0,
            pp=20,
            flags=["protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        """
        Réduit l'Attaque et l'Attaque Spéciale de la cible d'un niveau.
        Force l'utilisateur à changer de Pokémon.
        """
        if target.current_hp <= 0:
            return
            
        # Appliquer les changements de stats
        stat_changes = {"Attack": -1, "Sp. Def": -1}
        success = apply_stat_changes(target, stat_changes, "opponent", fight)
        
        if success:
            print(f"{target.name} subit une baisse de son Attaque et de sa Défense Spéciale !")
        
        # Forcer le changement de Pokémon
        user.must_switch_after_attack = True
        user.switch_reason = "Parting Shot"
        print(f"{user.name} doit changer après avoir utilisé Parting Shot !")

class HeavySlam(Attack):
    def __init__(self):
        super().__init__(
            name="Heavy Slam",
            type_="Steel",
            category="Physical",
            power=0,  # La puissance est déterminée par le poids
            accuracy=100,
            priority=0,
            pp=10,
            flags=["contact", "protect", "mirror"],
            target="Foe"
        )
        self.weight_factor = 0.5  # Facteur de poids pour le calcul de la puissance

    def get_power(self, user, target, fight):
        """
        Calcule la puissance de Heavy Slam en fonction du poids des Pokémon.
        Plus l'utilisateur est lourd par rapport à la cible, plus la puissance est élevée.
        """
        user_weight = getattr(user, 'weight', 100)  # Poids par défaut si non défini
        target_weight = getattr(target, 'weight', 100)  # Poids par défaut si non défini
        
        rapport = int((user_weight / target_weight) * 120 * self.weight_factor)
        match rapport:
            case 0:
                return 40
            case 1:
                return 40
            case 2:
                return 60
            case 3:
                return 80
            case 4:
                return 100
            case _:
                return 120
            
class Crunch(Attack):
    def __init__(self):
        super().__init__(
            name="Crunch",
            type_="Dark",
            category="Physical",
            power=80,
            accuracy=100,
            priority=0,
            pp=15,
            flags=["contact", "protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        """
        A 20 % de chance de baisser la Défense de la cible d'un niveau.
        """
        if random.random() < 0.2:
            stat_changes = {"Defense": -1}
            apply_stat_changes(target, stat_changes, "opponent", fight)

class FlareBlitz(Attack):
    def __init__(self):
        super().__init__(
            name="Flare Blitz",
            type_="Fire",
            category="Physical",
            power=120,
            accuracy=100,
            priority=0,
            pp=15,
            flags=["contact", "protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight, damage_dealt=0):
        """
        L'utilisateur subit des dégâts de recul à hauteur de 1/3 des dégâts infligés.
        """
        if damage_dealt > 0:
            recoil_damage = damage_dealt // 3
            fight.damage_method(user, recoil_damage)
            print(f"{user.name} subit {recoil_damage} PV de dégâts de recul après avoir utilisé Flare Blitz.")

class EarthPower(Attack):
    def __init__(self):
        super().__init__(
            name="Earth Power",
            type_="Ground",
            category="Special",
            power=90,
            accuracy=100,
            priority=0,
            pp=10,
            flags=["protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        """
        A 10 % de chance de baisser la Défense Spéciale de la cible d'un niveau.
        """
        if random.random() < 0.1:
            stat_changes = {"Sp. Def": -1}
            apply_stat_changes(target, stat_changes, "opponent", fight)

class PowerGem(Attack):
    def __init__(self):
        super().__init__(
            name="Power Gem",
            type_="Rock",
            category="Special",
            power=80,
            accuracy=100,
            priority=0,
            pp=20,
            flags=["protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        """
        Pas d'effet secondaire pour Power Gem.
        """
        pass

class KowtowCleave(Attack):
    def __init__(self):
        super().__init__(
            name="Kowtow Cleave",
            type_="Dark",
            category="Physical",
            power=85,
            accuracy=True,
            priority=0,
            pp=10,
            flags=["contact", "protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        """
        Pas d'effet secondaire pour Kowtow Cleave.
        """
        pass

class SludgeBomb(Attack):
    def __init__(self):
        super().__init__(
            name="Sludge Bomb",
            type_="Poison",
            category="Special",
            power=90,
            accuracy=100,
            priority=0,
            pp=10,
            flags=["protect", "mirror"],
            target="Foe"
        )
    
    def apply_effect(self, user, target, fight):
        """
        A 30 % de chance de provoquer un empoisonnement de la cible.
        """
        if random.random() < 0.3:
            target.apply_status("poison")
            print(f"{target.name} est empoisonné !")

class DarkPulse(Attack):
    def __init__(self):
        super().__init__(
            name="Dark Pulse",
            type_="Dark",
            category="Special",
            power=80,
            accuracy=100,
            priority=0,
            pp=15,
            flags=["protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        """
        A 20 % de chance de faire flancher la cible.
        """
        if random.random() < 0.2:
            if not target.flinched:
                target.flinched = True

class FocusBlast(Attack):
    def __init__(self):
        super().__init__(
            name="Focus Blast",
            type_="Fighting",
            category="Special",
            power=120,
            accuracy=70,
            priority=0,
            pp=5,
            flags=["protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        """
        A 10 % de chance de baisser la Défense Spéciale de la cible d'un niveau.
        """
        if random.random() < 0.1:
            stat_changes = {"Sp. Def": -1}
            apply_stat_changes(target, stat_changes, "opponent", fight)

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
        """
        A 10 % de chance de geler la cible.
        """
        if random.random() < 0.1:
            target.apply_status("frozen")
            print(f"{target.name} est gelé par Ice Beam !")

class Roar(Attack):
    def __init__(self):
        super().__init__(
            name="Roar",
            type_="Normal",
            category="Status",
            power=0,
            accuracy=True,
            priority=0,
            pp=20,
            flags=["protect", "mirror"],
            target="All Foes"
        )

    def apply_effect(self, user, target, fight):
        """
        Force le Pokémon adverse à changer de Pokémon.
        Ignore les effets de protection comme Protect ou Substitute.
        """
        if target.current_hp <= 0:
            return
            
        # Forcer le changement de Pokémon
        target.must_switch_after_attack = True
        target.switch_reason = "Roar"

class BodyPress(Attack):
    def __init__(self):
        super().__init__(
            name="Body Press",
            type_="Fighting",
            category="Physical",
            power=80,
            accuracy=100,
            priority=0,
            pp=10,
            flags=["contact", "protect", "mirror"],
            target="Foe"
        )

    def get_power(self, user, target, fight):
        """
        La puissance de Body Press est basée sur la Défense de l'utilisateur.
        """
        return int(user.stats["Defense"])  # Puissance basée sur la Défense

class DragonDance(Attack):
    def __init__(self):
        super().__init__(
            name="Dragon Dance",
            type_="Dragon",
            category="Status",
            power=0,
            accuracy=True,
            priority=0,
            pp=20,
            flags=["protect", "mirror"],
            target="User"
        )

    def apply_effect(self, user, target, fight):
        """
        Augmente l'Attaque et la Vitesse de l'utilisateur d'un niveau.
        """
        stat_changes = {"Attack": 1, "Speed": 1}
        success = apply_stat_changes(user, stat_changes, "self", fight)
        
        if success:
            print(f"{user.name} danse pour augmenter son Attaque et sa Vitesse !")

class ExtremeSpeed(Attack):
    def __init__(self):
        super().__init__(
            name="Extreme Speed",
            type_="Normal",
            category="Physical",
            power=80,
            accuracy=100,
            priority=2,  # Priorité élevée
            pp=5,
            flags=["contact", "protect", "mirror"],
            target="Foe"
        )
    def apply_effect(self, user, target, fight):
        """        Pas d'effet secondaire pour Extreme Speed.
        """        
        pass

class Moonblast(Attack):
    def __init__(self):
        super().__init__(
            name="Moonblast",
            type_="Fairy",
            category="Special",
            power=95,
            accuracy=100,
            priority=0,
            pp=10,
            flags=["protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        """
        A 30 % de chance de baisser l'Attaque Spéciale de la cible d'un niveau.
        """
        if random.random() < 0.3:
            stat_changes = {"Sp. Atk": -1}
            apply_stat_changes(target, stat_changes, "opponent", fight)

class ShadowBall(Attack):
    def __init__(self):
        super().__init__(
            name="Shadow Ball",
            type_="Ghost",
            category="Special",
            power=80,
            accuracy=100,
            priority=0,
            pp=15,
            flags=["protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        """
        A 20 % de chance de baisser la Défense Spéciale de la cible d'un niveau.
        """
        if random.random() < 0.2:
            stat_changes = {"Sp. Def": -1}
            apply_stat_changes(target, stat_changes, "opponent", fight)

class VacuumWave(Attack):
    def __init__(self):
        super().__init__(
            name="Vacuum Wave",
            type_="Fighting",
            category="Special",
            power=40,
            accuracy=100,
            priority=1,
            pp=30,
            flags=["protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        """
        Pas d'effet secondaire pour Vacuum Wave.
        """
        pass

class IronHead(Attack):
    def __init__(self):
        super().__init__(
            name="Iron Head",
            type_="Steel",
            category="Physical",
            power=80,
            accuracy=100,
            priority=0,
            pp=15,
            flags=["contact", "protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        """
        A 30 % de chance de faire flancher la cible.
        """
        if random.random() < 0.3:
            if not target.flinched:
                target.flinched = True

class Surf(Attack):
    def __init__(self):
        super().__init__(
            name="Surf",
            type_="Water",
            category="Special",
            power=90,
            accuracy=100,
            priority=0,
            pp=15,
            flags=["protect", "mirror"],
            target="All Foes"
        )

    def apply_effect(self, user, target, fight):
        """
        Pas d'effet secondaire pour Surf.
        """
        pass

class Hex(Attack):
    def __init__(self):
        super().__init__(
            name="Hex",
            type_="Ghost",
            category="Special",
            power=65,
            accuracy=100,
            priority=0,
            pp=10,
            flags=["protect", "mirror"],
            target="Foe"
        )

    def get_power(self, user, target, fight):
        """
        La puissance de Hex est doublée si la cible a un statut.
        """
        if target.status is not None:
            return 130
        else:
            return 65
        
class IceShard(Attack):
    def __init__(self):
        super().__init__(
            name="Ice Shard",
            type_="Ice",
            category="Physical",
            power=40,
            accuracy=100,
            priority=1,  # Priorité élevée
            pp=30,
            flags=["contact", "protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        """
        Pas d'effet secondaire pour Ice Shard.
        """
        pass

class LowKick(Attack): 
    def __init__(self):
        super().__init__(
            name="Low Kick",
            type_="Fighting",
            category="Physical",
            power=0,  # La puissance est déterminée par le poids
            accuracy=100,
            priority=0,
            pp=20,
            flags=["contact", "protect", "mirror"],
            target="Foe"
        )
        self.weight_factor = 0.5  # Facteur de poids pour le calcul de la puissance

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
        
class ChillyReception(Attack):
    def __init__(self):
        super().__init__(
            name="Chilly Reception",
            type_="Ice",
            category="Status",
            power=0,
            accuracy=True,
            priority=0,
            pp=10,
            flags=["mirror"],
            target="User"
        )

    def apply_effect(self, user, target, fight):
        """
        Invoque la neige et fait switcher l'utilisateur.
        """
        fight.set_weather("Snow")

        # Vérifier si l'utilisateur est encore en vie
        if user.current_hp <= 0:
            print(f"{user.name} est K.O. et ne peut pas switcher !")
            return
        
        # Déterminer quelle équipe possède l'utilisateur
        team_id = fight.get_team_id(user)
        if team_id is None:
            return
            
        team = fight.team1 if team_id == 1 else fight.team2
        
        # Vérifier s'il y a d'autres Pokémon disponibles
        available_pokemon = [p for p in team if p.current_hp > 0 and p != user]
        
        if not available_pokemon:
            print(f"{user.name} ne peut pas changer car il n'y a pas d'autre Pokémon disponible !")
            return
        
        # Marquer que le Pokémon doit changer après l'attaque
        user.must_switch_after_attack = True
        user.switch_reason = "Chilly Reception"
        print(f"{user.name} doit revenir après Chilly Reception !")

class Tailwind(Attack):
    def __init__(self):
        super().__init__(
            name="Tailwind",
            type_="Flying",
            category="Status",
            power=0,
            accuracy=True,
            priority=0,
            pp=10,
            flags=[],
            target="User"
        )
    
    def apply_effect(self, user, target, fight):
        """
        Pose le vent arrière pendant 5 tours.
        """
        team_id = fight.get_team_id(user)
        if team_id == 1:
            fight.tailwind_team1 = 5
        else:
            fight.tailwind_team2 = 5

class TripleAxel(Attack):
    def __init__(self):
        super().__init__(
            name="Triple Axel",
            type_="Ice",
            category="Physical",
            power=20,  # Puissance de base par coup
            accuracy=90,
            priority=0,
            pp=10,
            flags=["contact", "protect", "mirror"],
            target="Foe"
        )
        self.hits = 3  # Nombre de coups
        self.multi_hit = True  # Marquer comme attaque multi-coups

    def get_hit_power(self, hit_number):
        """
        Retourne la puissance pour chaque coup.
        Triple Axel : 20, 40, 60 de puissance
        """
        return 20 * hit_number

    def apply_effect(self, user, target, fight):
        """
        Pas d'effet secondaire pour Triple Axel.
        """
        pass

class BulletSeed(Attack):
    def __init__(self):
        super().__init__(
            name="Bullet Seed",
            type_="Grass",
            category="Physical",
            power=25,
            accuracy=100,
            priority=0,
            pp=30,
            flags=["protect", "mirror"],
            target="Foe"
        )
        self.multi_hit = True
        self.min_hits = 2
        self.max_hits = 5

    def get_hit_count(self):
        """
        Détermine le nombre de coups pour les attaques 2-5 hits.
        37.5% pour 2 hits, 37.5% pour 3 hits, 12.5% pour 4 hits, 12.5% pour 5 hits
        """
        import random
        rand = random.random()
        if rand < 0.375:
            return 2
        elif rand < 0.75:
            return 3
        elif rand < 0.875:
            return 4
        else:
            return 5

class RockBlast(Attack):
    def __init__(self):
        super().__init__(
            name="Rock Blast",
            type_="Rock",
            category="Physical",
            power=25,
            accuracy=90,
            priority=0,
            pp=10,
            flags=["protect", "mirror"],
            target="Foe"
        )
        self.multi_hit = True
        self.min_hits = 2
        self.max_hits = 5

    def get_hit_count(self):
        """
        Même distribution que Bullet Seed
        """
        import random
        rand = random.random()
        if rand < 0.375:
            return 2
        elif rand < 0.75:
            return 3
        elif rand < 0.875:
            return 4
        else:
            return 5

class IcicleSpear(Attack):
    def __init__(self):
        super().__init__(
            name="Icicle Spear",
            type_="Ice",
            category="Physical",
            power=25,
            accuracy=100,
            priority=0,
            pp=30,
            flags=["protect", "mirror"],
            target="Foe"
        )
        self.multi_hit = True
        self.min_hits = 2
        self.max_hits = 5

    def get_hit_count(self):
        """
        Même distribution que les autres attaques 2-5 hits
        """
        import random
        rand = random.random()
        if rand < 0.375:
            return 2
        elif rand < 0.75:
            return 3
        elif rand < 0.875:
            return 4
        else:
            return 5

class PopulationBomb(Attack):
    def __init__(self):
        super().__init__(
            name="Population Bomb",
            type_="Normal",
            category="Physical",
            power=20,
            accuracy=100,
            priority=0,
            pp=10,
            flags=["protect", "mirror"],
            target="Foe"
        )
        self.multi_hit = True
        self.min_hits = 10
        self.max_hits = 10  # Toujours 10 coups

class TidyUp(Attack):
    def __init__(self):
        super().__init__(
            name="Tidy Up",
            type_="Normal",
            category="Status",
            power=0,
            accuracy=100,
            priority=0,
            pp=10,
            flags=[""],
            target="User"
        )

    def apply_effect(self, user, target, fight):
        """
        Tidy up nettoie les Entry Hazards et les clones des deux cotés du terrain et augmente l'attaque et la vitesse.
        """
        # Nettoyer tous les Entry Hazards des deux côtés
        for hazards in [fight.hazards_team1, fight.hazards_team2]:
            hazards["Spikes"] = 0
            hazards["Stealth Rock"] = False
            hazards["Toxic Spikes"] = 0
            hazards["Sticky Web"] = False
        
        # Supprimer les substituts des Pokémon actifs des deux équipes
        active_pokemon = [fight.pokemon1, fight.pokemon2]
        for pokemon in active_pokemon:
            if pokemon and hasattr(pokemon, 'substitute_hp') and pokemon.substitute_hp > 0:
                pokemon.substitute_hp = 0
                print(f"Le clone de {pokemon.name} est détruit par Tidy Up !")
        
        print(f"{user.name} nettoie le terrain avec Tidy Up !")
        
        # Augmenter l'Attaque et la Vitesse dans tous les cas
        stats_changes = {"Speed": 1, "Attack": 1}
        success = apply_stat_changes(user, stats_changes, "self", fight)
        if success:
            print(f"{user.name} augmente sa Vitesse et son Attaque !")

class FutureSight(Attack):
    def __init__(self):
        super().__init__(
            name="Future Sight",
            type_="Psychic",
            category="Special",
            power=120,
            accuracy=100,
            priority=0,
            pp=10,
            flags=["protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        """
        Future Sight programme une attaque qui frappera dans 2 tours.
        L'attaque sauvegarde l'Attaque Spéciale de l'utilisateur au moment de l'utilisation.
        """
        # Initialiser la liste des attaques Future Sight si elle n'existe pas
        if not hasattr(fight, 'future_sight_attacks'):
            fight.future_sight_attacks = []
        
        # Vérifier s'il y a déjà un Future Sight programmé pour cette position
        target_position = 1 if target == fight.active1 else 2
        for existing_attack in fight.future_sight_attacks:
            if existing_attack['target_position'] == target_position:
                print(f"Un Future Sight est déjà programmé pour cette position !")
                return
        
        # Programmer l'attaque pour dans 2 tours
        future_attack = {
            'user': user,
            'user_name': user.name,  # Sauvegarder le nom pour les messages
            'user_sp_atk': user.current_stats()['Sp. Atk'],  # Attaque Spé au moment de l'utilisation
            'target_position': target_position,  # Position de la cible (1 ou 2)
            'turns_remaining': 2,
            'attack_power': self.base_power,
            'attack_type': self.type
        }
        
        fight.future_sight_attacks.append(future_attack)
        print(f"{user.name} utilise Future Sight ! L'attaque frappera dans 2 tours !")


class PsychoBoost(Attack):
    def __init__(self):
        super().__init__(
            name="Psycho Boost",
            type_="Psychic",
            category="Special",
            power=140,
            accuracy=90,
            priority=0,
            pp=5,
            flags=["contact"],
            target="Foe"
        )
        
    def apply_effect(self, user, target, fight):
        """Psycho Boost réduit l'Attaque Spéciale de 2 niveaux après utilisation"""
        stat_changes = {"Sp. Atk": -2}
        success = apply_stat_changes(user, stat_changes, "self", fight)
        if success:
            print(f"L'Attaque Spéciale de {user.name} diminue drastiquement !")

class Superpower(Attack):
    def __init__(self):
        super().__init__(
            name="Superpower",
            type_="Fighting",
            category="Physical",
            power=120,
            accuracy=100,
            priority=0,
            pp=5,
            flags=["contact"],
            target="Foe"
        )
        
    def apply_effect(self, user, target, fight):
        """Superpower réduit l'Attaque et la Défense de 1 niveau après utilisation"""
        stat_changes = {"Attack": -1, "Defense": -1}
        success = apply_stat_changes(user, stat_changes, "self", fight)
        if success:
            print(f"L'Attaque et la Défense de {user.name} diminuent !")

class MakeItRain(Attack):
    def __init__(self):
        super().__init__(
            name="Make It Rain",
            type_="Steel",
            category="Special",
            power=120,
            accuracy=100,
            priority=0,
            pp=5,
            flags=[],
            target="All Foes"
        )
        
    def apply_effect(self, user, target, fight):
        """Make It Rain réduit l'Attaque Spéciale de 1 niveau après utilisation"""
        stat_changes = {"Sp. Atk": -1}
        success = apply_stat_changes(user, stat_changes, "self", fight)
        if success:
            print(f"L'Attaque Spéciale de {user.name} diminue !")

class IceSpinner(Attack):
    def __init__(self):
        super().__init__(
            name="Ice Spinner",
            type_="Ice",
            category="Physical",
            power=80,
            accuracy=100,
            priority=0,
            pp=15,
            flags=["contact"],
            target="Foe"
        )
        
    def apply_effect(self, user, target, fight):
        """Ice Spinner supprime les effets de terrain"""
        if fight.field:
            print(f"{user.name} supprime l'effet de terrain avec Ice Spinner !")
            fight.field = None
            fight.field_turn_left = None

class FieryDance(Attack):
    def __init__(self):
        super().__init__(
            name="Fiery Dance",
            type_="Fire",
            category="Special",
            power=80,
            accuracy=100,
            priority=0,
            pp=10,
            flags=[],
            target="Foe"
        )
        
    def apply_effect(self, user, target, fight):
        """50% de chance d'augmenter l'Attaque Spéciale"""
        if random.random() < 0.5:
            stat_changes = {"Sp. Atk": 1}
            success = apply_stat_changes(user, stat_changes, "self", fight)
            if success:
                print(f"L'Attaque Spéciale de {user.name} augmente grâce à Fiery Dance !")

class SludgeWave(Attack):
    def __init__(self):
        super().__init__(
            name="Sludge Wave",
            type_="Poison",
            category="Special",
            power=95,
            accuracy=100,
            priority=0,
            pp=10,
            flags=[],
            target="All"
        )
        
    def apply_effect(self, user, target, fight):
        """10% de chance d'empoisonner"""
        if random.random() < 0.1:
            if target.status is None:
                target.status = "poison"
                print(f"{target.name} est empoisonné par Sludge Wave !")

class CeaselessEdge(Attack):
    def __init__(self):
        super().__init__(
            name="Ceaseless Edge",
            type_="Dark",
            category="Physical",
            power=65,
            accuracy=90,
            priority=0,
            pp=15,
            flags=["contact", "sharp"],
            target="Foe"
        )
        
    def apply_effect(self, user, target, fight):
        """Place une couche de Spikes sur le terrain adverse"""
        defender_team_id = fight.get_team_id(target)
        if defender_team_id == 1:
            hazards = fight.hazards_team1
        else:
            hazards = fight.hazards_team2
            
        if hazards["Spikes"] < 3:
            hazards["Spikes"] += 1
            print(f"{user.name} place des Spikes avec Ceaseless Edge !")

class RazorShell(Attack):
    def __init__(self):
        super().__init__(
            name="Razor Shell",
            type_="Water",
            category="Physical",
            power=75,
            accuracy=95,
            priority=0,
            pp=10,
            flags=["contact", "sharp"],
            target="Foe"
        )
        
    def apply_effect(self, user, target, fight):
        """50% de chance de réduire la Défense"""
        if random.random() < 0.5:
            stat_changes = {"Defense": -1}
            success = apply_stat_changes(target, stat_changes, "opponent", fight)
            if success:
                print(f"La Défense de {target.name} diminue !")

class GunkShot(Attack):
    def __init__(self):
        super().__init__(
            name="Gunk Shot",
            type_="Poison",
            category="Physical",
            power=120,
            accuracy=80,
            priority=0,
            pp=5,
            flags=["contact", "protect", "mirror"],
            target="Foe"
        )
        
    def apply_effect(self, user, target, fight):
        """30% de chance d'empoisonner la cible"""
        if random.random() < 0.3:
            if target.status is None:
                target.status = "poison"
                print(f"{target.name} est empoisonné par Gunk Shot !")

class Struggle(Attack):
    """
    Attaque spéciale utilisée quand un Pokémon n'a plus de PP.
    Inflige des dégâts à l'utilisateur aussi.
    """
    def __init__(self):
        super().__init__(
            name="Struggle",
            type_="Normal",
            category="Physical",
            power=50,
            accuracy=True,  # Ne peut pas rater
            priority=0,
            pp=1,  # PP infini en réalité
            flags=["contact", "protect"],
            target="Foe"
        )
    
    def apply_effect(self, user, target, fight):
        # L'utilisateur perd 1/4 de ses PV max en dégâts de recul
        recoil_damage = max(1, user.max_hp // 4)
        print(f"{user.name} subit {recoil_damage} dégâts de recul de Struggle !")
        fight.damage_method(user, recoil_damage)

# Instance globale de Struggle pour tous les Pokémon
STRUGGLE_ATTACK = Struggle()

class Liquidation(Attack):
    def __init__(self):
        super().__init__(
            name="Liquidation",
            type_="Water",
            category="Physical",
            power=85,
            accuracy=100,
            priority=0,
            pp=10,
            flags=["contact", "protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        """
        A 20% de chance de baisser la Défense de la cible d'un niveau.
        """
        if random.random() < 0.2:
            stat_changes = {"Defense": -1}
            apply_stat_changes(target, stat_changes, "opponent", fight)

class Overheat(Attack):
    def __init__(self):
        super().__init__(
            name="Overheat",
            type_="Fire",
            category="Special",
            power=130,
            accuracy=90,
            priority=0,
            pp=5,
            flags=["protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        """
        Réduit l'Attaque Spéciale de l'utilisateur de 2 niveaux après utilisation.
        """
        stat_changes = {"Sp. Atk": -2}
        success = apply_stat_changes(user, stat_changes, "self", fight)
        if success:
            print(f"L'Attaque Spéciale de {user.name} diminue drastiquement !")

class DracoMeteor(Attack):
    def __init__(self):
        super().__init__(
            name="Draco Meteor",
            type_="Dragon",
            category="Special",
            power=130,
            accuracy=90,
            priority=0,
            pp=5,
            flags=["protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        """
        Réduit l'Attaque Spéciale de l'utilisateur de 2 niveaux après utilisation.
        """
        stat_changes = {"Sp. Atk": -2}
        success = apply_stat_changes(user, stat_changes, "self", fight)
        if success:
            print(f"L'Attaque Spéciale de {user.name} diminue drastiquement !")

class VoltSwitch(Attack):
    def __init__(self):
        super().__init__(
            name="Volt Switch",
            type_="Electric",
            category="Special",
            power=70,
            accuracy=100,
            priority=0,
            pp=20,
            flags=["protect", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        """
        Force l'utilisateur à changer de Pokémon après l'attaque.
        """
        # Déterminer quelle équipe possède l'utilisateur
        team_id = fight.get_team_id(user)
        if team_id is None:
            return
            
        team = fight.team1 if team_id == 1 else fight.team2
        
        # Vérifier s'il y a d'autres Pokémon disponibles
        available_pokemon = [p for p in team if p.current_hp > 0 and p != user]
        
        if not available_pokemon:
            print(f"{user.name} ne peut pas changer car il n'y a pas d'autre Pokémon disponible !")
            return
        
        # Marquer que l'utilisateur doit changer après l'attaque
        user.must_switch_after_attack = True
        user.switch_reason = "Volt Switch"
        print(f"{user.name} doit revenir après avoir utilisé Volt Switch !")


def process_future_sight_attacks(fight):
    """
    Fonction à appeler à la fin de chaque tour pour gérer les attaques Future Sight.
    Cette fonction doit être intégrée dans le système de combat.
    """
    if not hasattr(fight, 'future_sight_attacks'):
        return
    
    # Décrémenter le compteur et exécuter les attaques prêtes
    attacks_to_remove = []
    
    for i, future_attack in enumerate(fight.future_sight_attacks):
        future_attack['turns_remaining'] -= 1
        
        if future_attack['turns_remaining'] == 0:
            # Exécuter l'attaque
            execute_future_sight(future_attack, fight)
            attacks_to_remove.append(i)
    
    # Supprimer les attaques exécutées (en partant de la fin pour éviter les problèmes d'index)
    for i in reversed(attacks_to_remove):
        fight.future_sight_attacks.pop(i)

def execute_future_sight(future_attack, fight):
    """
    Exécute une attaque Future Sight programmée.
    """
    # Déterminer la cible actuelle à cette position
    if future_attack['target_position'] == 1:
        current_target = fight.active1
    else:
        current_target = fight.active2
    
    if current_target.current_hp <= 0:
        print(f"Future Sight de {future_attack['user_name']} rate car il n'y a plus de cible !")
        return
    
    print(f"Future Sight de {future_attack['user_name']} frappe {current_target.name} !")
    
    # Vérifier si l'utilisateur original est encore sur le terrain
    original_user = future_attack['user']
    user_on_field = (original_user == fight.active1 or original_user == fight.active2)
    
    # Calculer les dégâts
    # Attaque Spé de l'utilisateur au moment de l'utilisation
    attack_stat = future_attack['user_sp_atk']
    
    # Défense Spé de la cible actuelle au moment de l'impact
    defense_stat = current_target.current_stats()['Sp. Def']
    
    base_power = future_attack['attack_power']
    attack_type = future_attack['attack_type']
    
    # Créer un objet Attack temporaire pour Future Sight
    from pokemon_attacks import Attack
    temp_attack = Attack("Future Sight", attack_type, "Special", base_power, 100, 0, 10, ["protect", "mirror"], "Foe")
    
    # Formule de dégâts simplifiée pour Future Sight
    import random
    rdm = random.uniform(0.85, 1.0)
    
    # Utiliser le système existant de calcul d'efficacité de type
    from donnees import type_effectiveness, is_stab
    type_eff = type_effectiveness(attack_type, current_target)
    
    # STAB si l'utilisateur est encore sur le terrain
    stab = is_stab(original_user, temp_attack) if user_on_field else 1.0
    
    # Future Sight utilise les objets et talents seulement si l'utilisateur est encore sur le terrain
    if user_on_field:
        # Utiliser le système existant de trigger_talent et trigger_item
        from pokemon_talents import trigger_talent
        from pokemon_items import trigger_item
        
        talent_mod = trigger_talent(original_user, "on_attack", temp_attack, fight)
        item_mod = trigger_item(original_user, "on_attack", temp_attack, fight)
        
        # Valeurs par défaut si None
        if talent_mod is None:
            talent_mod = {"attack": 1.0, "power": 1.0, "accuracy": 1.0, "type": None}
        if item_mod is None:
            item_mod = {"attack": 1.0, "power": 1.0, "accuracy": 1.0}
        
        # Appliquer les modificateurs
        attack_stat *= talent_mod.get("attack", 1.0)
        base_power *= talent_mod.get("power", 1.0) * item_mod.get("power", 1.0)
        
        # Changer le type si le talent le modifie
        if talent_mod.get("type") is not None:
            attack_type = talent_mod["type"]
            type_eff = type_effectiveness(attack_type, current_target)
            temp_attack.type = attack_type
            stab = is_stab(original_user, temp_attack)
    
    # Calcul final des dégâts
    damage = ((22 * base_power * (attack_stat / defense_stat)) / 50 + 2) * type_eff * stab * rdm
    damage = int(damage)
    
    # Appliquer les dégâts (Future Sight ignore les substituts)
    print(f"Future Sight inflige {damage} dégâts !")
    fight.damage_method(current_target, damage, bypass_substitute=True)
    
    if current_target.current_hp <= 0:
        print(f"{current_target.name} est K.O. par Future Sight !")

attack_registry = {
    "Aerial Ace": AerialAce(),
    "Aurora Veil": AuroraVeil(),
    "Behemoth Blade": BehemothBlade(),
    "Body Press": BodyPress(),
    "Bulk Up": BulkUp(),
    "Bullet Seed": BulletSeed(),
    "Blizzard": Blizzard(),
    "Brave Bird": BraveBird(),
    "Calm Mind": CalmMind(),
    "Ceaseless Edge": CeaselessEdge(),
    "Chilly Reception": ChillyReception(),
    "Close Combat": CloseCombat(),
    "Crunch": Crunch(),
    "Dark Pulse": DarkPulse(),
    "Defog": Defog(),
    "Draco Meteor": DracoMeteor(),
    "Dragon Dance": DragonDance(),
    "Dragon Pulse": DragonPulse(),
    "Draining Kiss": DrainingKiss(),
    "Dynamic Punch": DynamicPunch(),
    "Earthquake": Earthquake(),
    "Earth Power": EarthPower(),
    "Electro Shot": ElectroShot(),
    "Encore": Encore(),
    "Extreme Speed": ExtremeSpeed(),
    "Fake Out": FakeOut(),
    "Fiery Dance": FieryDance(),
    "Flamethrower": Flamethrower(),
    "Flare Blitz": FlareBlitz(),
    "Flip Turn": FlipTurn(),
    "Flower Trick": FlowerTrick(),
    "Focus Blast": FocusBlast(),
    "Future Sight": FutureSight(),
    "Grass Knot": GrassKnot(),
    "Gunk Shot": GunkShot(),
    "Heal Bell": HealBell(),
    "Heavy Slam": HeavySlam(),
    "Hex": Hex(),
    "Hurricane": Hurricane(),
    "Hydro Pump": HydroPump(),
    "Hyper Beam": HyperBeam(),
    "Ice Beam": IceBeam(),
    "Ice Shard": IceShard(),
    "Ice Spinner": IceSpinner(),
    "Icicle Spear": IcicleSpear(),
    "Iron Defense": IronDefense(),
    "Iron Head": IronHead(),
    "Knock Off": KnockOff(),
    "Kowtow Cleave": KowtowCleave(),
    "Leaf Blade": LeafBlade(),
    "Leaf Storm": LeafStorm(),
    "Light Screen": LightScreen(),
    "Liquidation": Liquidation(),
    "Low Kick": LowKick(),
    "Magic Coat": MagicCoat(),
    "Make It Rain": MakeItRain(),
    "Moonblast": Moonblast(),
    "Mortal Spin": MortalSpin(),
    "Nasty Plot": NastyPlot(),
    "Nuzzle": Nuzzle(),
    "Overheat": Overheat(),
    "Parting Shot": PartingShot(),
    "Play Rough": PlayRough(),
    "Population Bomb": PopulationBomb(),
    "Power Gem": PowerGem(),
    "Protect": Protect(),
    "Psycho Boost": PsychoBoost(),
    "Psychic": Psychic(),
    "Rain Dance": RainDance(),
    "Rapid Spin": RapidSpin(),
    "Razor Shell": RazorShell(),
    "Recover": Recover(),
    "Reflect": Reflect(),
    "Roar": Roar(),
    "Rock Slide": RockSlide(),
    "Rock Blast": RockBlast(),
    "Roost": Roost(),
    "Sandstorm": Sandstorm(),
    "Scald": Scald(),
    "Shadow Ball": ShadowBall(),
    "Shed Tail": ShedTail(),
    "Shell Smash": ShellSmash(),
    "Shift Gear": ShiftGear(),
    "Sludge Bomb": SludgeBomb(),
    "Sludge Wave": SludgeWave(),
    "Solar Beam": SolarBeam(),
    "Snarl": Snarl(),
    "Spikes": Spikes(),
    "Spore": Spore(),
    "Stealth Rock": StealthRock(),
    "Sticky Web": StickyWeb(),
    "Stone Edge": StoneEdge(),
    "Struggle": STRUGGLE_ATTACK,
    "Substitute": Substitute(),
    "Sucker Punch": SuckerPunch(),
    "Sunny Day": SunnyDay(),
    "Superpower": Superpower(),
    "Surf": Surf(),
    "Swords Dance": SwordsDance(),
    "Tailwind": Tailwind(),
    "Taunt": Taunt(),
    "Tera Blast": TeraBlast(),
    "Thunder": Thunder(),
    "Thunder Wave": ThunderWave(),
    "Tidy Up": TidyUp(),
    "Toxic": Toxic(),
    "Toxic Spikes": ToxicSpikes(),
    "Trick": Trick(),
    "Trick Room": TrickRoom(),
    "Triple Axel": TripleAxel(),
    "U-turn": UTurn(),
    "Vacuum Wave": VacuumWave(),
    "Volt Switch": VoltSwitch(),
    "Wave Crash": WaveCrash(),
    "Will-O-Wisp": WillOWisp(),
    "Wood Hammer": WoodHammer()


}
