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
            accuracy=True,
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

class Aerial_Ace(Attack):
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

class Shock_Wave(Attack):
    def __init__(self):
        super().__init__(
            name="Shock Wave",
            type_="Electric",
            category="Special",
            power=60,
            accuracy=100,  # Ne rate jamais
            priority=0,
            pp=20,
            flags=["protect", "mirror"],
            target="Foe"
        )

    def get_effective_accuracy(self, user, target, fight):
        """Shock Wave ne peut jamais rater."""
        return True

class Dynamic_Punch(Attack):
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
                      user_hazards["Sticky Web"])
        
        if has_hazards:
            # Supprimer tous les hazards
            user_hazards["Spikes"] = 0
            user_hazards["Stealth Rock"] = False
            user_hazards["Toxic Spikes"] = 0
            user_hazards["Sticky Web"] = False
            print(f"{user.name} supprime tous les pièges de son côté avec Rapid Spin !")
        
        # Augmenter la vitesse (depuis la Gen VIII)
        if user.stats_modifier[5] < 6:  # Speed est à l'index 5
            user.stats_modifier[5] += 1
            print(f"La vitesse de {user.name} augmente !")

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
            flags=["protect", "reflectable", "mirror"],
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
        
        print(f"{user.name} dissipe tous les pièges du terrain avec Débrouillard !")
        
        # Réduire l'esquive de la cible
        if target.stats_modifier[7] > -6:  # Evasion est à l'index 7
            target.stats_modifier[7] -= 1
            print(f"L'esquive de {target.name} diminue !")

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
            flags=["protect", "reflectable", "mirror"],
            target="Foe"
        )

    def apply_effect(self, user, target, fight):
        """
        Paralyse la cible. Test parfait pour Magic Bounce !
        """
        if target.current_hp <= 0:
            return
            
        # Immunité type (Électrique immunisé à la paralysie)
        if "Electric" in target.types:
            print(f"{target.name} est immunisé à la paralysie car il est de type Électrique !")
            return
            
        if target.status == "normal":
            target.status = "paralysis"
            print(f"{target.name} est paralysé !")
        else:
            print(f"{target.name} a déjà un statut et ne peut pas être paralysé !")

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