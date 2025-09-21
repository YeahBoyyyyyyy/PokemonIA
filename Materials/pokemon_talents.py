'''
fichier regroupant tous les talents de poke et créant un dictionnaire regroupant tous leurs effets.
'''
import random
from Materials.utilities import MOLD_BREAKER_IGNORED_ABILITIES, NON_DIRECT_PHYSICAL_ATTACK, DIRECT_SPECIAL_ATTACKS, PRINTING_METHOD, print_infos


ON_ATTACK_MOD_DICT = {
    "attack": 1.0,
    "power": 1.0,
    "accuracy": 1.0,
    "type": None
}

class Talent:
    """
    Classe de base pour tous les talents. Les sous-classes peuvent surcharger les méthodes suivantes :
    - on_entry: quand le pokémon entre en combat
    - on_attack: juste avant de lancer une attaque
    - on_defense: quand le pokémon est ciblé par une attaque
    - modify_stat: pour modifier une stat temporairement (ex: vitesse sous le soleil)
    - on_stat_change: quand une tentative de modification de stat est effectuée (pour Clear Body, Competitive, etc.)
    """
    def on_entry(self, poke, fight):
        pass

    def on_exit(self, poke, fight):
        """Appelé quand le Pokémon quitte le terrain (switch ou remplacement)."""
        pass

    def on_attack(self, poke, attack, fight):
        """Appelé juste avant de lancer une attaque.
        
        :param poke: Le Pokémon qui attaque.
        :param attack: L'attaque lancée.
        :param fight: Instance du combat.
        :return: None ou un dict avec des modifications à appliquer à l'attaque. De base : {"attack": 1.0, "power": 1.0, "accuracy": 1.0, "type": None}"""
        return ON_ATTACK_MOD_DICT

    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight=None):
        pass

    def modify_stat(self, poke, fight=None):
        return None
    
    def on_turn_end(self, poke, fight=None):
        pass

    def on_stat_change(self, poke, stat_changes, source, fight=None):
        """
        Appelé quand une tentative de modification de stats est effectuée.
        
        :param poke: Le Pokémon ciblé par la modification
        :param stat_changes: Dict des changements de stats proposés {stat: modification}
        :param source: Source du changement ('self', 'opponent', 'field', etc.)
        :param fight: Instance du combat
        :return: Dict des changements de stats autorisés (peut être modifié)
        """
        return stat_changes

class Prankster(Talent):
    """Talent qui fait en sorte que les attaques de status gagne +1 en priorité. Gain de priorité géré dans fight.py."""
    def prankster(self, poke, attack, fight):
        """Les pokémons de type Dark sont immunisés aux attaques de status venant d'un pokémon avec Prankster."""
        target = fight.active1 if fight.active2 == poke else fight.active2
        if "Dark" in target.types and attack.category == "Status":
            print_infos(f"{target.name} n'est pas affecté par les attaques de status provenant du talent prankskter !")
            return
        else:
            pass
    
class Fluffy(Talent):
    """Talent qui divise par 2 les dégâts des capacités directes mais double les dégâts des attaque de type feu"""
    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight=None):
        total_changes = 1.0
        if (incoming_attack.category == "Physical" and not incoming_attack.name in NON_DIRECT_PHYSICAL_ATTACK) or (incoming_attack.category == "Special" and incoming_attack.name in DIRECT_SPECIAL_ATTACKS):
            total_changes *= 0.5
        if incoming_attack.type == "Fire":
            total_changes *= 2.0
        return total_changes

class FurCoat(Talent):
    """Talent qui double la défense du pokémon."""
    def modify_stat(self, poke, fight=None):
        poke.hidden_modifier["Defense"] *= 2

class WaterAbsorb(Talent):
    """ Talent qui absorbe les attaques de type Eau et soigne le Pokémon."""
    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight = None):
        if incoming_attack.type == "Water":
            healed = int(poke.max_hp * 0.25)
            poke.current_hp = min(poke.current_hp + healed, poke.max_hp)
            print_infos(f"{poke.name} absorbe l'eau et récupère {healed} PV !")
            return 0  # annule les dégâts

class WindRider(Talent):
    """ Si le Pokémon est touché par une capacité de Vent (ou si le Vent Arrière est actif de son coté),
      il ne subit aucun dégât et son attaque augmente d'1 cran."""
    
    def on_entry(self, poke, fight):
        team_id = fight.get_team_id(poke)
        tailwind_side = fight.tailwind_team1 if team_id == 1 else fight.tailwind_team2
        if tailwind_side > 0:
            from pokemon import apply_stat_changes
            stat_changes = {"Attack" : 1}
            success = apply_stat_changes(poke, stat_changes, "self", fight)
            if success:
                print_infos(f"L'attaque de {poke.name} augmente grâce à Wind Rider !")
    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight=None):
        if "wind" in incoming_attack.flags:
            from pokemon import apply_stat_changes
            stat_changes = {"Attack" : 1}
            success = apply_stat_changes(poke, stat_changes, "self", fight)
            if success:
                print_infos(f"L'attaque de {poke.name} augmente grâce à Wind Rider !")
            return 0  # annule les dégâts

class Chlorophyll(Talent):
    """ Talent qui double la vitesse du Pokémon sous le soleil."""
    def modify_stat(self, poke, fight=None):
        if fight:
            if fight.weather["current"] == "Sunny" and fight.weather["previous"] != "Sunny":
                poke.stats["Speed"] = int(poke.stats["Speed"] * 2)
                return "activated"
            elif fight.weather["previous"] == "Sunny" and fight.weather["current"] != "Sunny":
                poke.stats["Speed"] = poke.stats["Speed"] // 2
                return "activated"
        return None
    
class SwiftSwim(Talent):
    """Talent qui double la vitesse du Pokémon sous la pluie."""
    def modify_stat(self, poke, fight=None):
        if fight:
            if fight.weather["current"] == "Rain" and fight.weather["previous"] != "Rain":
                poke.stats["Speed"] = int(poke.stats["Speed"] * 2)
                return "activated"
            elif fight.weather["previous"] == "Rain" and fight.weather["current"] != "Rain":
                poke.stats["Speed"] = poke.stats["Speed"] // 2
                return "activated"
        return None

class Overgrow(Talent):
    """ Talent qui booste les attaques de type Plante quand le Pokémon a moins de 1/3 de ses PV."""
    def on_attack(self, poke, attack, fight = None):
        if poke.current_hp < poke.max_hp / 3 and attack.type == "Grass":
            mod_dict = ON_ATTACK_MOD_DICT.copy()
            mod_dict["power"] = 1.5
            return mod_dict

class Blaze(Talent):
    """ Talent qui booste les attaques de type Feu quand le Pokémon a moins de 1/3 de ses PV."""
    def on_attack(self, poke, attack, fight = None):
        if poke.current_hp < poke.max_hp / 3 and attack.type == "Fire":
            mod_dict = ON_ATTACK_MOD_DICT.copy()
            mod_dict["power"] = 1.5
            return mod_dict

class Torrent(Talent):
    """ Talent qui booste les attaques de type Eau quand le Pokémon a moins de 1/3 de ses PV."""
    def on_attack(self, poke, attack, fight):
        if poke.current_hp < poke.max_hp / 3 and attack.type == "Water":
            mod_dict = ON_ATTACK_MOD_DICT.copy()
            mod_dict["power"] = 1.5
            return mod_dict

class Drizzle(Talent):
    """ Talent qui invoque la pluie quand le Pokémon entre en combat."""
    def on_entry(self, poke, fight):
        if fight.weather["current"] != "Rain":
            fight.set_weather("Rain", duration=5)
            print_infos(f"{poke.name} invoque la pluie !")
        return "activated"

class Drought(Talent):
    """ Talent qui invoque le soleil quand le Pokémon entre en combat."""
    def on_entry(self, poke, fight):
        if fight.weather["current"] != "Sunny":
            rounds = 8 if poke.item == "Heat Rock" else 5
            fight.set_weather("Sunny", duration=rounds)
            print_infos(f"{poke.name} invoque le soleil !")
        return "activated"
    
class SnowWarning(Talent):
    """Talent qui invoque la grêle quand le Pokémon entre en combat"""
    def on_entry(self, poke, fight):
        if fight.weather["current"] != "Snow":
            fight.set_weather("Snow", duration=5)
            print_infos(f"{poke.name} invoque la grêle !")
        return "activated"

class Intimidate(Talent):
    """ Talent qui réduit l'attaque de l'adversaire de 1 niveau."""
    def on_entry(self, poke, fight):
        from pokemon import apply_stat_changes
        opponent = fight.active2 if poke == fight.active1 else fight.active1

        # Vérifie que l'adversaire n'est pas déjà KO
        if opponent.current_hp > 0:
            stat_changes = {"Attack": -1}
            success = apply_stat_changes(opponent, stat_changes, "opponent", fight)
            if success:
                print_infos(f"{poke.name} intimide {opponent.name} !")
                return "activated"
        return None

class QuarkDrive(Talent):
    """ Talent qui booste la stat la plus élevée du Pokémon sous le soleil ou dans le terrain électrique."""
    def on_entry(self, poke, fight):
        if fight.weather['current'] == "Electric Terrain":
            self._boost_highest_stat(poke)

class Protosynthesis(Talent):
    """ Talent qui booste la stat la plus élevée du Pokémon sous le soleil ou dans le terrain électrique."""
    def on_entry(self, poke, fight):
        if fight.weather['current'] == "Sunny":
            self._boost_highest_stat(poke)
    
    def _boost_highest_stat(self, poke):
        """Méthode commune pour booster la stat la plus élevée"""
        stat_max = max(poke.stats, key=poke.stats.get)
        if stat_max == "Speed":
            poke.hidden_modifier["Speed"] *= 1.5
        else:
            poke.hidden_modifier[stat_max] *= 1.3

class FlashFire(Talent):
    """ Talent qui absorbe les attaques de type Feu et augmente l'Attaque Spéciale."""
    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight=None):
        if incoming_attack.type == "Fire":
            from pokemon import apply_stat_changes
            apply_stat_changes(poke, {"Sp. Atk": 1}, "self", fight)
            print_infos(f"{poke.name} absorbe le feu et augmente son Attaque Spéciale !")
            return 0  # annule les dégâts

class SapSipper(Talent):
    """ Talent qui absorbe les attaques de type Feu et augmente l'Attaque Spéciale."""
    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight=None):
        if incoming_attack.type == "Grass":
            from pokemon import apply_stat_changes
            apply_stat_changes(poke, {"Attack": 1}, "self", fight)
            print_infos(f"{poke.name} absorbe les attaques de type Plante et augmente son Attaque !")
            return 0  # annule les dégâts

class SpeedBoost(Talent):
    """ Talent qui augmente la Vitesse de 1 niveau à la fin de chaque tour."""
    def on_turn_end(self, poke, fight=None):
        from pokemon import apply_stat_changes
        stat_changes = {"Speed": 1}
        success = apply_stat_changes(poke, stat_changes, "self", fight)
        if success:
            print_infos(f"La vitesse de {poke.name} augmente grâce à Speed Boost !")
            return "activated"
        return None

class ThickFat(Talent):
    """ Talent qui réduit de moitié les dégâts des attaques de type Feu et Glace."""
    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight=None):
        if incoming_attack.type in ["Fire", "Ice"]:
            print_infos(f"{poke.name} réduit de moitié les dégâts grâce à sa graisse !")
            return 0.5
        
class Levitate(Talent):
    """ Talent qui immunise aux capacités de type sol."""
    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight=None):
        if incoming_attack.type == "Ground":
            print_infos(f"{poke.name} est immunisé aux attaques de type Sol grâce à Lévitation !")
            return 0
        return 1.0

class Stamina(Talent):
    """ Talent qui augmente la Défense de 1 niveau à chaque fois que le Pokémon subit des dégâts."""
    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight=None):
        if incoming_attack.category in ["Physical", "Special"]:
            from pokemon import apply_stat_changes
            apply_stat_changes(poke, {"Defense": 1}, "self", fight)
            print_infos(f"{poke.name} augmente sa Défense grâce à Endurance !")
        return None

class Sturdy(Talent):
    """ Talent qui permet au Pokémon de survivre à un coup fatal avec 1 PV."""
    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight=None):
        # Si le Pokémon a tous ses PV et que l'attaque pourrait le mettre KO
        if poke.current_hp == poke.max_hp and not poke.sturdy_activated:
            # On ne peut pas vraiment empêcher les dégâts ici, mais on peut marquer le Pokémon
            # pour qu'il garde au moins 1 PV dans la méthode damage_method
            poke.sturdy_activated = True
            print_infos(f"{poke.name} résiste grâce à Fermeté et garde 1 PV !")
            return "activated"  # Indique que le talent a été activé
        return None

class LightMetal(Talent):
    """ Talent qui réduit le poids du Pokémon de moitié."""
    def on_defense(self, poke, fight=None):
        # Réduit le poids de moitié (utilisé pour les attaques basées sur le poids)
        if not hasattr(poke, 'original_weight'):
            poke.original_weight = getattr(poke, 'weight', 100)  # Poids par défaut si non défini
        poke.weight = poke.original_weight / 2
        return 1.0

class PoisonPuppeteer(Talent):
    """ Talent qui rend confus la cible si celle-ci est empoisonnée."""
    def on_attack(self, poke, attack, fight):
        defender = fight.active2 if poke == fight.active1 else fight.active1
        if attack.category in ["Physical", "Special"]:
            if defender.status == "poison":
                defender.is_confused = True
                print_infos(f"{defender.name} devient confus !")
        return ON_ATTACK_MOD_DICT

class CursedBody(Talent):
    """ Talent qui a 30% de chance de désactiver l'attaque qui touche le Pokémon."""
    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight=None):
        attacker = fight.active1 if poke == fight.active2 else fight.active2
        if random.random() < 0.3:  # 30% de chance de désactiver l'attaque
            attacker.disabled_attack = incoming_attack
            print_infos(f"{attacker.name} est entravé et ne peut plus utiliser {incoming_attack.name} !")

class ClearBody(Talent):
    def on_stat_change(self, poke, stat_changes, source, fight=None):
        """Clear Body empêche les réductions de stats imposées par l'adversaire."""
        if source == "opponent":
            # Filtrer les réductions de stats (valeurs négatives)
            filtered_changes = {}
            for stat, change in stat_changes.items():
                if change < 0:
                    print_infos(f"{poke.name} ignore la baisse de {stat} grâce à Clear Body !")
                else:
                    filtered_changes[stat] = change
            return filtered_changes
        return stat_changes

class Competitive(Talent):
    def on_stat_change(self, poke, stat_changes, source, fight=None):
        """Competitive augmente l'Attaque Spéciale de 2 niveaux quand une stat est réduite par l'adversaire."""
        if source == "opponent":
            # Vérifier s'il y a des réductions de stats
            has_reduction = any(change < 0 for change in stat_changes.values())
            if has_reduction:
                print_infos(f"{poke.name} devient compétitif ! Son Attaque Spéciale augmente !")
                # Ajouter le boost d'Attaque Spéciale
                poke.stats_modifier[2] = min(poke.stats_modifier[2] + 2, 6)
                poke.actualize_stats()
        return stat_changes

class Defiant(Talent):
    def on_stat_change(self, poke, stat_changes, source, fight=None):
        """Defiant augmente l'Attaque de 2 niveaux quand une stat est réduite par l'adversaire."""
        if source == "opponent":
            # Vérifier s'il y a des réductions de stats
            has_reduction = any(change < 0 for change in stat_changes.values())
            if has_reduction:
                print_infos(f"{poke.name} devient provocateur ! Son Attaque augmente !")
                # Ajouter le boost d'Attaque
                poke.stats_modifier[0] = min(poke.stats_modifier[0] + 2, 6)
                poke.actualize_stats()
        return stat_changes
    
class NoGuard(Talent):
    """Talent qui garantit que toutes les attaques touchent."""
    def on_attack(self, poke, attack, fight=None):
        # Aucune action spécifique à faire ici, No Guard est passif
        mod_dict = ON_ATTACK_MOD_DICT.copy()
        mod_dict["accuracy"] = True
        return mod_dict

class Sharpness(Talent):
    """Talent qui augmente la puissance des attaques tranchantes."""
    def on_attack(self, poke, attack, fight=None):
        if "sharp" in attack.flags:
            mod_dict = ON_ATTACK_MOD_DICT.copy()
            mod_dict["power"] = 1.5
            return mod_dict
        return ON_ATTACK_MOD_DICT

class GrassySurge(Talent):
    def on_entry(self, poke, fight):
        """Invoque le terrain herbu quand il entre sur le terrain s'il n'est pas déjà actif."""
        if fight.field != "Grassy Terrain":
            fight.set_field("Grassy Terrain")
            print_infos(f"{poke.name} invoque le terrain herbu !")

class RoughSkin(Talent):
    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight=None):
        # Rough Skin ne devrait se déclencher qu'une fois par attaque de contact
        # On utilise un attribut temporaire pour éviter le double déclenchement
        if ((incoming_attack.category == "Physical" and not incoming_attack.name in NON_DIRECT_PHYSICAL_ATTACK) or (incoming_attack.category == "Special" and incoming_attack.name in DIRECT_SPECIAL_ATTACKS)) and \
            attacker_poke and attacker_poke.current_hp > 0:
            # Vérifier si ce n'est pas déjà traité (éviter double activation)
            if not hasattr(attacker_poke, '_rough_skin_triggered'):
                attacker_poke._rough_skin_triggered = True
                dmg = int(poke.max_hp * 0.125)
                fight.damage_method(attacker_poke, dmg)
                print_infos(f"{attacker_poke.name} subit {dmg} points de dégâts à cause de Rough Skin !")
        return 1.0  # Pas de modification des dégâts

class CompoundEyes(Talent):
    """Talent qui augmente la précision des attaques de 30%."""
    def on_attack(self, poke, attack, fight):
        mod_dict = ON_ATTACK_MOD_DICT.copy()
        mod_dict["accuracy"] = 1.3
        return mod_dict

class IceScales(Talent):
    """Talent qui réduit les dégâts des attaques spéciales de 50%."""
    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight=None):
        if incoming_attack and incoming_attack.category == "Special":
            print_infos(f"{poke.name} utilise Ice Scales pour réduire les dégâts !")
            return 0.5  # Réduit les dégâts spéciaux de 50%
        return 1.0  # Pas de modification des dégâts

class VictoryStar(Talent):
    """Talent qui augmente la précision de l'équipe de 10%."""
    def on_attack(self, poke, attack, fight):
        mod_dict = ON_ATTACK_MOD_DICT.copy()
        mod_dict["accuracy"] = 1.1
        return mod_dict

class SandVeil(Talent):
    """Talent qui augmente l'évasion de 20% pendant une tempête de sable."""
    def modify_stat(self, poke, fight=None):
        if fight and fight.weather.get("current") == "Sandstorm":
            poke.evasion = poke.evasion * 1.25
            return "activated"
        return None

class SnowCloak(Talent):
    """Talent qui augmente l'évasion de 20% pendant la grêle."""
    def modify_stat(self, poke, fight=None):
        if fight and fight.weather.get("current") in ["Hail", "Snow"]:
            poke.evasion = poke.evasion_with_no_modifier * 1.25
            return "activated"
        return None

class Static(Talent):
    """Talent qui paralyse l'adversaire si une attaque de contact le touche."""
    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight=None):
        if (incoming_attack.category == "Physical" and not incoming_attack.name in NON_DIRECT_PHYSICAL_ATTACK) or (incoming_attack.category == "Special" and incoming_attack.name in DIRECT_SPECIAL_ATTACKS):
            if random.random() < 0.3:  # 30% de chance de paralyser
                attacker_poke.status = "paralysis"
                print_infos(f"{attacker_poke.name} est paralysé par {poke.name}'s Static !")

class FlameBody(Talent):
    """Talent qui brûle l'adversaire si une attaque de contact le touche."""
    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight=None):
        if (incoming_attack.category == "Physical" and not incoming_attack.name in NON_DIRECT_PHYSICAL_ATTACK) or (incoming_attack.category == "Special" and incoming_attack.name in DIRECT_SPECIAL_ATTACKS):
            if random.random() < 0.3:  # 30% de chance de brûler
                attacker_poke.status = "burn"
                print_infos(f"{attacker_poke.name} est brûlé par {poke.name}'s Flame Body !")

class MagicBounce(Talent):
    """Talent qui renvoie les attaques de statut à l'adversaire."""
    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight=None):
        # Magic Bounce renvoie seulement les attaques de statut avec le flag "reflectable"
        if (incoming_attack and 
            incoming_attack.category == "Status" and 
            "reflectable" in incoming_attack.flags and
            attacker_poke and attacker_poke.current_hp > 0):
            
            print_infos(f"{poke.name} renvoie {incoming_attack.name} à {attacker_poke.name} grâce à Magic Bounce !")
            
            # Vérifier si l'attaquant original a aussi Magic Bounce (éviter boucle infinie)
            if (hasattr(attacker_poke, 'talent') and 
                attacker_poke.talent == "Magic Bounce"):
                print_infos(f"Mais {attacker_poke.name} a aussi Magic Bounce ! L'attaque échoue.")
                return 0  # Annule complètement l'attaque
            
            # Vérifier si l'attaquant a Magic Coat actif
            if getattr(attacker_poke, 'magic_coat_active', False):
                print_infos(f"Mais {attacker_poke.name} a un voile magique actif ! L'attaque échoue.")
                return 0
            
            # Renvoyer l'attaque vers l'attaquant original
            print_infos(f"{incoming_attack.name} est renvoyée vers {attacker_poke.name} !")
            
            # Déterminer la nouvelle cible
            target = attacker_poke if incoming_attack.target == "Foe" else poke
            
            # Appliquer l'effet de l'attaque sur l'attaquant original
            if hasattr(incoming_attack, 'apply_effect'):
                try:
                    incoming_attack.apply_effect(poke, target, fight)
                except Exception as e:
                    print_infos(f"Erreur lors du renvoi de l'attaque : {e}")
            
            return 0  # Annule l'attaque originale sur le Pokémon avec Magic Bounce

class DauntlessShield(Talent):
    """Augmente la Défense de 1 niveau quand le Pokémon entre pour la première sur le terrain."""
    def on_entry(self, poke, fight):
        if not hasattr(poke, "dauntless_shield_activated"):
            from pokemon import apply_stat_changes
            poke.dauntless_shield_activated = True
            apply_stat_changes(poke, {"Defense": 1}, "self", fight)
            print_infos(f"{poke.name} active Egide Inflexible et augmente sa Défense !")
            return "activated"
        
class IntrepidSword(Talent):
    """Augmente l'Attaque de 1 niveau quand le Pokémon entre pour la première sur le terrain."""
    def on_entry(self, poke, fight):
        if not hasattr(poke, "intrepid_sword_activated"):
            from pokemon import apply_stat_changes
            poke.intrepid_sword_activated = True
            apply_stat_changes(poke, {"Attack": 1}, "self", fight)
            print_infos(f"{poke.name} active Epée Intrépide et augmente son Attaque !")
            return "activated"
        
class SwordOfRuin(Talent):
    """Diminue de manière discrète la Défense de tous les Pokémon sur le terrain (ne possédant pas le talent) de 25%."""
    
    def on_entry(self, poke, fight):
        """Applique l'effet de Sword of Ruin quand le Pokémon entre."""
        fight.ruin_effects_active["Sword of Ruin"] = True
        fight.apply_ruin_effects()
        print_infos(f"{poke.name} active Sword of Ruin !")
        return "activated"

class TabletsOfRuin(Talent):
    """Diminue de manière discrète l'Attaque de tous les Pokémon sur le terrain (ne possédant pas le talent) de 25%."""
    
    def on_entry(self, poke, fight):
        """Applique l'effet de Tablets of Ruin quand le Pokémon entre."""
        fight.ruin_effects_active["Tablets of Ruin"] = True
        fight.apply_ruin_effects()
        print_infos(f"{poke.name} active Tablets of Ruin !")
        return "activated"

class VesselOfRuin(Talent):
    """Diminue de manière discrète l'Attaque Spéciale de tous les Pokémon sur le terrain (ne possédant pas le talent) de 25%."""
    
    def on_entry(self, poke, fight):
        """Applique l'effet de Vessel of Ruin quand le Pokémon entre."""
        fight.ruin_effects_active["Vessel of Ruin"] = True
        fight.apply_ruin_effects()
        print_infos(f"{poke.name} active Vessel of Ruin !")
        return "activated"

class BeadsOfRuin(Talent):
    """Diminue de manière discrète la Défense Spéciale de tous les Pokémon sur le terrain (ne possédant pas le talent) de 25%."""
    
    def on_entry(self, poke, fight):
        """Applique l'effet de Beads of Ruin quand le Pokémon entre."""
        fight.ruin_effects_active["Beads of Ruin"] = True
        fight.apply_ruin_effects()
        print_infos(f"{poke.name} active Beads of Ruin !")
        return "activated"
    
class ToxicDebris(Talent):
    """Talent qui place des Débris Toxiques sur le terrain quand le Pokémon est touché par une attaque physique."""
    
    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight=None):
        # Éviter la double activation en vérifiant si le talent s'est déjà déclenché ce tour
        if hasattr(poke, '_toxic_debris_triggered'):
            return None
            
        # Se déclenche seulement si c'est une attaque physique qui inflige des dégâts
        if incoming_attack and incoming_attack.category == "Physical":
            # Marquer que le talent s'est déclenché pour éviter la double activation
            poke._toxic_debris_triggered = True
            
            user_team_id = fight.get_team_id(poke)
            opponent_hazards = fight.hazards_team2 if user_team_id == 1 else fight.hazards_team1

            if opponent_hazards["Toxic Spikes"] < 2:
                opponent_hazards["Toxic Spikes"] += 1
                layers = opponent_hazards["Toxic Spikes"]
                effect = "empoisonnement" if layers == 1 else "empoisonnement grave"
                print_infos(f"{poke.name} pose des Toxic Spikes ! (Couche {layers}/2 - {effect})")
                return "activated"
            else:
                print_infos(f"Il y a déjà le maximum de Toxic Spikes sur le terrain !")
        return None

class SupremeOverlord(Talent):
    """Talent qui augmente de 10% l'attaque et l'attaque spéciale pour chaque Pokémon allié KO"""
    def on_entry(self, poke, fight):
        user_team_id = fight.get_team_id(poke)
        team = fight.team1 if user_team_id == 1 else fight.team2
        num_kos = sum(1 for p in team if p.current_hp <= 0)

        if num_kos > 0:
            boost = 1 + 0.1 * num_kos
            poke.hidden_modifier["Attack"] *= boost
            poke.hidden_modifier["Sp. Atk"] *= boost
            print_infos(f"{poke.name} active Supreme Overlord et augmente son Attaque et Attaque Spéciale de {boost:.1f}x !")
            poke.actualize_stats()
            return "activated"
        return None
    
class Multiscale(Talent):
    """Talent qui réduit les dégâts subis par le Pokémon de 50% quand il est à plein PV."""
    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight=None):
        if poke.current_hp == poke.max_hp:
            print_infos(f"{poke.name} réduit les dégâts grâce à Multiscale !")
            return 0.5  # Réduit les dégâts de moitié
        return 1.0  # Pas de réduction si pas à plein PV

class BadDreams(Talent):
    """Talent qui inflige 1/8 des PV max de chaque pokemon adverses endormis."""
    def on_turn_end(self, poke, fight):
        opponent = fight.active2 if poke == fight.active1 else fight.active1
        if opponent.status == "sleep":
            damage = int(opponent.max_hp * 0.125)
            fight.damage_method(opponent, damage)
            print_infos(f"{opponent.name} subit {damage} points de dégâts à cause de Bad Dreams !")

class GoodAsGold(Talent):
    """Talent qui rend le Pokémon immunisé aux attaques de statut provenant d'autres pokémon que lui-même."""
    def on_defense(self, poke, incoming_attack, attacker_poke, fight=None):
        if incoming_attack.category == "Status" and attacker_poke != poke:
            print_infos(f"{poke.name} est immunisé aux attaques de statut grâce à Good as Gold !")
            return 0  # Annule l'attaque de statut
        return None  # Pas d'effet sur les autres types d'attaques

class Regenerator(Talent):
    """Talent qui permet au Pokémon de récupérer 1/3 de ses PV max quand il quitte le terrain."""
    def on_exit(self, poke, fight):
        """Se déclenche quand le Pokémon quitte le terrain (switch ou KO d'un autre Pokémon)."""
        if poke.current_hp > 0 and poke.current_hp < poke.max_hp:
            healed = int(poke.max_hp / 3)  # 1/3 des PV max
            old_hp = poke.current_hp
            poke.current_hp = min(poke.current_hp + healed, poke.max_hp)
            actual_healed = poke.current_hp - old_hp
            print_infos(f"{poke.name} récupère {actual_healed} PV grâce à Regenerator !")
            return "activated"
        return None

class WonderSkin(Talent):
    """Talent qui fait que le pokemon a 50% de chance de faire échouer les capacités de statut dont il est la cible."""
    def on_defense(self, poke, incoming_attack, attacker_poke, fight=None):
        if incoming_attack.category == "Status" and incoming_attack.target != "User" and attacker_poke != poke and random.random() < 0.5:
            print_infos(f"{poke.name} fait échouer l'attaque de statut adverse grâce à Peau Miracle")

class InnerFocus(Talent):
    """Talent qui empêche le pokémon d'être flinch (étourdi) par une attaque. 
    Géré dans fight.check_status_before_attack() juste le nom nous interesse."""

class IceFace(Talent):
    """Talent qui permet au Pokémon de résister à la première attaque physique qu'il subit et le transforme en bekeglacon tete degel.
    On suppose que personne ne sera assez bête pour utiliser Ice Face sur un autre pokémon que Eiscue."""
    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight=None):
        if incoming_attack.category == "Physical" and poke.ice_face_active and poke.name == "Eiscue-Ice-Face":
            from Materials.utilities import transform_pokemon
            # Activer l'effet Ice Face
            poke.ice_face_active = False
            print_infos(f"{poke.name} utilise Ice Face pour résister à l'attaque physique !")
            transform_pokemon(poke, "Eiscue-No-Ice-Face")
            return 0

class SheerForce(Talent):
    """Talent qui augmente la puissance des attaques avec un effet secondaire de 30% mais annule l'effet secondaire."""
    def on_attack(self, poke, attack, fight=None):
        mod_dict = ON_ATTACK_MOD_DICT.copy()
        if "secondary_effect" in attack.flags:
            mod_dict["power"] = 1.3
            print_infos(f"{poke.name} utilise Sheer Force pour augmenter la puissance de {attack.name} !")
        return mod_dict

class Contrary(Talent):
    """Talent qui inverse tous les chagements de stats subits par le Pokémon."""
    def on_stat_change(self, poke, stat_changes, source, fight=None):
        for stat, change in stat_changes.items():
            stat_changes[stat] = -change
        return stat_changes

class Protean(Talent):
    """Talent qui change le type du Pokémon en celui de la première attaque qu'il lance."""
    def on_attack(self, poke, attack, fight=None):
        if poke.first_attack:
            poke.types = [attack.type] # Pas besoin de sauvegarder les anciens types, cela est déjà fait dans pokemon.py à l'__init__
            poke.protean_active = True  # Indique que Protean a été activé
            print_infos(f"{poke.name} change son type en {attack.type} grâce à Protean !")
            return ON_ATTACK_MOD_DICT  # Pas de modification des dégâts par défaut

class Libero(Talent):
    """Talent qui change le type du Pokémon en celui de la première attaque qu'il lance, similaire à Protean."""
    def on_attack(self, poke, attack, fight=None):
        if poke.first_attack:
            poke.types = [attack.type]  # Change le type du Pokémon
            poke.libero_active = True  # Indique que Libero a été activé
            print_infos(f"{poke.name} change son type en {attack.type} grâce à Libero !")
        return ON_ATTACK_MOD_DICT  # Pas de modification des dégâts par défaut

class Technician(Talent):
    """Talent qui augmente la puissance des attaques de 60 de puissance ou moins de 50%."""
    def on_attack(self, poke, attack, fight=None):
        if attack.base_power <= 60:
            mod_dict = ON_ATTACK_MOD_DICT.copy()
            mod_dict["power"] = 1.5
            print_infos(f"{poke.name} utilise Technician pour augmenter la puissance de {attack.name} !")
            return mod_dict
        return ON_ATTACK_MOD_DICT  # Pas de modification si l'attaque est trop puissante

class Infiltrator(Talent):
    """Les attaques de ce Pokémon ignorent les clones et les Protection, Mur Lumière,
    Rune Protect, Brume et Voile Aurore de l'adversaire."""

class MoldBreaker(Talent):
    """Ignore les talents défensifs adverses lors de l'attaque (implémentation minimale: flag)."""
    def on_entry(self, poke, fight):
        poke.mold_breaker_active = True
        return "activated"
    def on_exit(self, poke, fight):
        if hasattr(poke, 'mold_breaker_active'):
            poke.mold_breaker_active = False

class SandStream(Talent):
    """Déclenche la Tempête de Sable à l'entrée sur le terrain (5 tours)."""
    def on_entry(self, poke, fight):
        if fight.weather["current"] != "Sandstorm":
            fight.set_weather("Sandstorm", duration=5)
            print_infos(f"{poke.name} invoque une tempête de sable !")
        return "activated"

class Moxie(Talent):
    """Augmente l'Attaque d'un niveau après avoir mis K.O un adversaire."""
    def on_attack(self, poke, attack, fight=None):
        # Le boost est géré juste après un KO dans fight via un flag sur l'attaquant.
        return ON_ATTACK_MOD_DICT
    def modify_stat(self, poke, fight=None):
        if hasattr(poke, 'pending_moxie'):
            if poke.pending_moxie:
                from pokemon import apply_stat_changes
                apply_stat_changes(poke, {"Attack": 1}, "self", fight)
                print_infos(f"{poke.name} augmente son Attaque grâce à Moxie !")
                poke.pending_moxie = False  # Réinitialiser le flag
                return "activated"

class ChillingNeigh(Talent):
    """Augmente l'Attaque après un kill."""
    def on_attack(self, poke, attack, fight=None):
        # Le boost est géré juste après un KO dans fight via un flag sur l'attaquant.
        return ON_ATTACK_MOD_DICT
    def modify_stat(self, poke, fight=None):
        if hasattr(poke, 'pending_chilling_neigh'):
            if poke.pending_chilling_neigh:
                from pokemon import apply_stat_changes
                apply_stat_changes(poke, {"Attack": 1}, "self", fight)
                print_infos(f"{poke.name} augmente son Attaque grâce à Chilling Neigh !")
                poke.pending_chilling_neigh = False  # Réinitialiser le flag
                return "activated"
        
class GrimNeigh(Talent):
    """Augmente l'Attaque Spéciale après un kill."""
    def on_attack(self, poke, attack, fight=None):
        # Le boost est géré juste après un KO dans fight via un flag sur l'attaquant.
        return ON_ATTACK_MOD_DICT
    def modify_stat(self, poke, fight=None):
        if hasattr(poke, "pending_grim_neigh"):
            if poke.pending_grim_neigh:
                from pokemon import apply_stat_changes
                apply_stat_changes(poke, {"Sp. Atk": 1}, "self", fight)
                print_infos(f"{poke.name} augmente son Attaque Spéciale grâce à Grim Neigh !")
                poke.pending_grim_neigh = False  # Réinitialiser le flag
                return "activated"

class Steadfast(Talent):
    """Augmente la vitesse de 1 niveau quand le Pokémon est flinch par une attaque."""
    def on_attack(self, poke, attack, fight):
        if poke.flinched:
            from pokemon import apply_stat_changes
            stat_changes = {"Speed": 1}
            success = apply_stat_changes(poke, stat_changes, "self", fight)
            if success:
                print_infos(f"La vitesse de {poke.name} augmente de 1 niveau à cause du flinch!")

class LiquidOoze(Talent):
    """Ce Pokémon blesse ceux qui lui drainent des PVs pour se soigner proportionnellement à ce qu'ils auraient dû récupérer."""

class MagicGuard(Talent):
    """Ce Pokémon ne peut subir des dégâts que par des attaques directes. 
    L'utilisation de Clonage, de Malédiction, de Cognobidon, de Balance, le recul de Lutte, 
    et les dégâts de confusion sont considérés comme des dégâts directs. Ce Pokémon n'est pas affecté 
    par les dégâts de Picots, Pics Toxik, et Piège de Roc lorsqu'il arrive sur le terrain. 
    Il est également immunisé aux dégâts du climat, des capacités piégeant les Pokémon sur le terrain 
    comme Vortex Magma, et des contrecoups des capacités ou de l'Orbe Vie."""

class GaleWings(Talent):
    """Les attaques de type Flying de l'utilisateur gagne 1 de priorité"""

class Guts(Talent):
    """Si ce Pokémon a un problème de statut, son attaque est multipliée 
    par 1,5 (augmentée de 50%). Il ignore la réduction de l'Attaque causée par la brûlure."""
    
    def on_attack(self, poke, attack, fight=None):
        if poke.status:
            mod_dict = ON_ATTACK_MOD_DICT.copy()
            mod_dict["attack"] = 1.5
            print_infos(f"{poke.name} augmente son attaque grâce à Guts !")
            return mod_dict
        return ON_ATTACK_MOD_DICT  # Pas de modification si pas de problème de statut

class ThermalExchange(Talent):
    """Lorsque le Pokémon est touché par une capacité de type Feu, son attaque augmente d'1 cran. Il ne peut pas être brûlé."""
    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight=None):
        if incoming_attack.type == "Fire":
            from pokemon import apply_stat_changes
            apply_stat_changes(poke, {"Attack": 1}, "opponent")
            print_infos(f"L'attaque de {poke.name} augmente grâce à Thermal Exchange !")

class Analytic(Talent):
    """Si ce Pokémon agit le dernier pendant un tour, la puissance de son attaque est multipliée par 1,3 (augmentée de 30%)."""
    def on_attack(self, poke, attack, fight=None):
        team_id = fight.get_team_id(poke)
        opponent = fight.active2 if team_id == 1 else fight.active1
        if opponent.has_attacked_or_switched:
            mod_dict = ON_ATTACK_MOD_DICT.copy()
            mod_dict["power"] = 1.3
            print_infos(f"La puissance de {attack.name} est augmentée grâce à Analytic !")
            return mod_dict
        return ON_ATTACK_MOD_DICT
        
class ShadowTag(Talent):
    """Talent qui empêche les Pokémon adverses de fuir ou de se retirer du combat."""
    def on_entry(self, poke, fight):
        opponent = fight.active2 if poke == fight.active1 else fight.active1

        # Vérifier si l'adversaire est immunisé (par exemple, type Ghost ou talent Shadow Tag)
        if "Ghost" in opponent.types or getattr(opponent, 'talent', None) == "Shadow Tag":
            print_infos(f"{opponent.name} est immunisé à Shadow Tag !")
            return None

        # Empêcher l'adversaire de fuir ou de switcher
        opponent.cannot_switch = True
        print_infos(f"{poke.name} active Shadow Tag ! {opponent.name} ne peut pas fuir ou être remplacé.")
        return "activated"

    def on_exit(self, poke, fight):
        """Désactive l'effet de Shadow Tag lorsque le Pokémon quitte le terrain."""
        opponent = fight.active2 if poke == fight.active1 else fight.active1
        if hasattr(opponent, 'cannot_switch'):
            opponent.cannot_switch = False
            print_infos(f"{poke.name} quitte le terrain. {opponent.name} peut à nouveau fuir ou être remplacé.")

class MotorDrive(Talent):
    """Talent qui augmente la Vitesse de 1 niveau lorsqu'il est touché par une attaque de type Électrik. 
    Il est immunisé aux attaques de type Électrik."""
    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight=None):
        if incoming_attack.type == "Electric":
            from pokemon import apply_stat_changes
            apply_stat_changes(poke, {"Speed": 1}, "self", fight)
            print(f"La vitesse de {poke.name} augmente grâce à Motor Drive !")
            return 0  # Annule les dégâts de l'attaque électrique
        return 1.0  # Pas de modification des dégâts pour les autres types d'attaques

class OrichalcumPulse(Talent):
    """Talent qui augmente l'attaque de 1.33 sous le soleil et invoque le soleil à l'entrée."""
    def on_entry(self, poke, fight):
        if fight.weather["current"] != "Sunny":
            rounds = 8 if poke.item == "Heat Rock" else 5
            fight.set_weather("Sunny", duration=rounds)
            print(f"{poke.name} invoque le soleil !")
        return "activated"
    
    def on_attack(self, poke, attack, fight=None):
        if fight and fight.weather.get("current") == "Sunny":
            mod_dict = ON_ATTACK_MOD_DICT.copy()
            mod_dict["attack"] = 1.33
            print(f"L'attaque de {poke.name} est augmentée grâce à Orichalcum Pulse !")
            return mod_dict
        return ON_ATTACK_MOD_DICT

class Justified(Talent):
    """Augmente l'Attaque d'un niveau lorsqu'il est touché par une attaque de type Ténèbres."""
    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight=None):
        if incoming_attack.type == "Dark":
            from pokemon import apply_stat_changes
            apply_stat_changes(poke, {"Attack": 1}, "self", fight)
            print(f"L'attaque de {poke.name} augmente grâce à Justified !")
            return "activated"
        return None

def trigger_talent(poke, event_name, *args):
    """
    Déclenche l'effet du talent en fonction de l'événement.

    :param poke: Le Pokémon utilisant le talent.
    :param event_name: Le nom de l'événement qui déclenche l'effet du talent.
    :param args: Arguments supplémentaires à mettre dans cet ordre"""
    talent = talent_registry.get(poke.talent)
    if talent and hasattr(talent, event_name):
            # Gestion Mold Breaker : si l'événement est défensif et que l'attaquant possède Mold Breaker
        if event_name == "on_defense" and len(args) >= 2:
            incoming_attack = args[0]
            attacker = args[1]
            if hasattr(attacker, 'talent') and attacker.talent == "Mold Breaker" and poke.talent in MOLD_BREAKER_IGNORED_ABILITIES:
                # Ignorer l'effet défensif
                print(f"[Mold Breaker] {attacker.name} ignore le talent {poke.talent} de {poke.name} !")
                return None
        # Vérifier si la méthode du talent diffère de la méthode de base (qui ne fait rien)
        talent_method = getattr(talent, event_name)
        base_method = getattr(Talent, event_name)
        
        # Si la méthode a été surchargée (différente de la classe de base)
        if talent_method.__func__ != base_method:
            result = talent_method(poke, *args)
            # Afficher le message seulement si le talent a effectivement fait quelque chose
            if result is not None:
                from Materials.utilities import PRINTING_METHOD
                if PRINTING_METHOD:
                    print(f"[TALENT] {poke.name} active {poke.talent} -> {event_name}")
            return result
    return None

# Registre des talents
talent_registry = {
    "Water Absorb": WaterAbsorb(),
    "Intimidate": Intimidate(),
    "Chlorophyll": Chlorophyll(),
    "Overgrow": Overgrow(),
    "Blaze": Blaze(),
    "Torrent": Torrent(),
    "Drizzle": Drizzle(),
    "Drought": Drought(),
    "Quark Drive": QuarkDrive(),
    "Protosynthesis": Protosynthesis(),
    "Flash Fire": FlashFire(),
    "Thick Fat": ThickFat(),
    "Stamina": Stamina(),
    "Sturdy": Sturdy(),
    "Light Metal": LightMetal(),
    "Poison Puppeteer": PoisonPuppeteer(),
    "Clear Body": ClearBody(),
    "Competitive": Competitive(),
    "Defiant": Defiant(),
    "No Guard": NoGuard(),
    "Cursed Body": CursedBody(),
    "Sharpness": Sharpness(),
    "Grassy Surge": GrassySurge(),
    "Rough Skin": RoughSkin(),
    "Compound Eyes": CompoundEyes(),
    "Victory Star": VictoryStar(),
    "Sand Veil": SandVeil(),
    "Snow Cloak": SnowCloak(),
    "Static": Static(),
    "Flame Body": FlameBody(),
    "Magic Bounce": MagicBounce(),
    "Dauntless Shield": DauntlessShield(),
    "Intrepid Sword": IntrepidSword(),
    "Sword of Ruin": SwordOfRuin(),
    "Tablets of Ruin": TabletsOfRuin(),
    "Vessel of Ruin": VesselOfRuin(),
    "Beads of Ruin": BeadsOfRuin(),
    "Supreme Overlord": SupremeOverlord(),
    "Toxic Debris": ToxicDebris(),
    "Multiscale": Multiscale(),
    "Bad Dreams": BadDreams(),
    "Good as Gold": GoodAsGold(),
    "Regenerator": Regenerator(),
    "Prankster": Prankster(),
    "Snow Warning": SnowWarning(),
    "Levitate": Levitate(),
    "Wonder Skin": WonderSkin(),
    "Inner Focus": InnerFocus(),
    "Ice Face": IceFace(),
    "Sheer Force": SheerForce(),
    "Contrary": Contrary(),
    "Libero": Libero(),
    "Protean": Protean(),
    "Technician": Technician(),
    "Infiltrator": Infiltrator(),
    "Wind Rider": WindRider(),
    "Guts": Guts(),
    "Sap Sipper": SapSipper(),
    "Thermal Exchange": ThermalExchange(),
    "Analytic": Analytic(),
    "Gale Wings": GaleWings(),
    "Mold Breaker": MoldBreaker(),
    "Sand Stream": SandStream(),
    "Moxie": Moxie(),
    "Ice Scales": IceScales(),
    "Fluffy": Fluffy(),
    "Fur Coat": FurCoat(),
    "Shadow Tag": ShadowTag(),
    "Speed Boost": SpeedBoost(),
    "Motor Drive": MotorDrive(),
    "Orichalcum Pulse": OrichalcumPulse(),
    "Chilling Neigh": ChillingNeigh(),
    "Grim Neigh": GrimNeigh(),
    "Justified": Justified(),
}