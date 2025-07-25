'''
fichier regroupant tous les talents de poke et créant un dictionnaire regroupant tous leurs effets.
'''
import random

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


class WaterAbsorb(Talent):
    """ Talent qui absorbe les attaques de type Eau et soigne le Pokémon."""
    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight = None):
        if incoming_attack.get("type") == "Water":
            healed = int(poke.max_hp * 0.25)
            poke.current_hp = min(poke.current_hp + healed, poke.max_hp)
            print(f"{poke.name} absorbe l'eau et récupère {healed} PV !")
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
        fight.set_weather("Rain", duration=5)
        print(f"{poke.name} invoque la pluie !")
        return "activated"

class Drought(Talent):
    """ Talent qui invoque le soleil quand le Pokémon entre en combat."""
    def on_entry(self, poke, fight):
        fight.set_weather("Sunny", duration=5)
        print(f"{poke.name} invoque le soleil !")
        return "activated"

class Intimidate(Talent):
    """ Talent qui réduit l'attaque de l'adversaire de 1 niveau."""
    def on_entry(self, poke, fight):
        opponent = fight.active2 if poke == fight.active1 else fight.active1

        # Vérifie que l'adversaire n'est pas déjà KO
        if opponent.current_hp > 0:
            stat_changes = {"Attack": -1}
            success = apply_stat_changes(opponent, stat_changes, "opponent", fight)
            if success:
                print(f"{poke.name} intimide {opponent.name} !")
                return "activated"
        return None

class QuarkDrive(Talent):
    """ Talent qui booste la stat la plus élevée du Pokémon sous le soleil ou dans le terrain électrique."""
    def on_entry(self, poke, fight):
        if fight.weather['current'] == "Electric Terrain":
            stat_max = max(poke.stats, key = poke.stats.get)
            if stat_max == "Speed":
                poke.hidden_boost["Speed"] *= 1.5
            else:
                poke.hidden_boost[stat_max] *= 1.3

class Protosynthesis(Talent):
    """ Talent qui booste la stat la plus élevée du Pokémon sous le soleil ou dans le terrain électrique."""
    def on_entry(self, poke, fight):
        if fight.weather['current'] == "Electric Terrain":
            stat_max = max(poke.stats, key = poke.stats.get)
            if stat_max == "Speed":
                poke.hidden_boost["Speed"] *= 1.5
            else:
                poke.hidden_boost[stat_max] *= 1.3

class FlashFire(Talent):
    """ Talent qui absorbe les attaques de type Feu et augmente l'Attaque Spéciale."""
    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight=None):
        if incoming_attack.type == "Fire":
            apply_stat_changes(poke, {"Sp. Atk": 1}, "self", fight)
            print(f"{poke.name} absorbe le feu et augmente son Attaque Spéciale !")
            return 0  # annule les dégâts

class ThickFat(Talent):
    """ Talent qui réduit de moitié les dégâts des attaques de type Feu et Glace."""
    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight=None):
        if incoming_attack.type in ["Fire", "Ice"]:
            print(f"{poke.name} réduit de moitié les dégâts grâce à sa graisse !")
            return 0.5

class Stamina(Talent):
    """ Talent qui augmente la Défense de 1 niveau à chaque fois que le Pokémon subit des dégâts."""
    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight=None):
        if incoming_attack.category in ["Physical", "Special"]:
            apply_stat_changes(poke, {"Defense": 1}, "self", fight)
            print(f"{poke.name} augmente sa Défense grâce à Endurance !")
        return None

class Sturdy(Talent):
    """ Talent qui permet au Pokémon de survivre à un coup fatal avec 1 PV."""
    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight=None):
        # Si le Pokémon a tous ses PV et que l'attaque pourrait le mettre KO
        if poke.current_hp == poke.max_hp and not poke.sturdy_activated:
            # On ne peut pas vraiment empêcher les dégâts ici, mais on peut marquer le Pokémon
            # pour qu'il garde au moins 1 PV dans la méthode damage_method
            poke.sturdy_activated = True
            print(f"{poke.name} résiste grâce à Fermeté et garde 1 PV !")
            return "activated"  # Indique que le talent a été activé
        return None

class LightMetal(Talent):
    """ Talent qui réduit le poids du Pokémon de moitié."""
    def modify_stat(self, poke, fight=None):
        # Réduit le poids de moitié (utilisé pour les attaques basées sur le poids)
        if not hasattr(poke, 'original_weight'):
            poke.original_weight = getattr(poke, 'weight', 100)  # Poids par défaut si non défini
        poke.weight = poke.original_weight / 2
        return None

class PoisonPuppeteer(Talent):
    """ Talent qui rend confus la cible si celle-ci est empoisonnée."""
    def on_attack(self, poke, attack, fight):
        defender = fight.active2 if poke == fight.active1 else fight.active1
        if attack.category in ["Physical", "Special"]:
            if defender.status == "poison":
                defender.is_confused = True
                print(f"{defender.name} devient confus !")
        return ON_ATTACK_MOD_DICT

class CursedBody(Talent):
    """ Talent qui a 30% de chance de désactiver l'attaque qui touche le Pokémon."""
    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight=None):
        attacker = fight.active1 if poke == fight.active2 else fight.active2
        if random() < 0.3:  # 30% de chance de désactiver l'attaque
            attacker.disabled_attack = incoming_attack
            print(f"{attacker.name} est entravé et ne peut plus utiliser {incoming_attack.name} !")

class ClearBody(Talent):
    def on_stat_change(self, poke, stat_changes, source, fight=None):
        """Clear Body empêche les réductions de stats imposées par l'adversaire."""
        if source == "opponent":
            # Filtrer les réductions de stats (valeurs négatives)
            filtered_changes = {}
            for stat, change in stat_changes.items():
                if change < 0:
                    print(f"{poke.name} ignore la baisse de {stat} grâce à Clear Body !")
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
                print(f"{poke.name} devient compétitif ! Son Attaque Spéciale augmente !")
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
                print(f"{poke.name} devient provocateur ! Son Attaque augmente !")
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
            print(f"{poke.name} invoque le terrain herbu !")

class RoughSkin(Talent):
    def on_defense(self, poke, incoming_attack, attacker_poke=None, fight=None):
        # Rough Skin ne devrait se déclencher qu'une fois par attaque de contact
        # On utilise un attribut temporaire pour éviter le double déclenchement
        if (incoming_attack and "contact" in incoming_attack.flags and 
            attacker_poke and attacker_poke.current_hp > 0):
            # Vérifier si ce n'est pas déjà traité (éviter double activation)
            if not hasattr(attacker_poke, '_rough_skin_triggered'):
                attacker_poke._rough_skin_triggered = True
                dmg = int(poke.max_hp * 0.125)
                fight.damage_method(attacker_poke, dmg)
                print(f"{attacker_poke.name} subit {dmg} points de dégâts à cause de Rough Skin !")
        return 1.0  # Pas de modification des dégâts

def apply_stat_changes(target_poke, stat_changes, source="unknown", fight=None):
    """
    Applique des modifications de statistiques en gérant les talents qui peuvent les intercepter.
    
    :param target_poke: Le Pokémon dont les stats vont être modifiées
    :param stat_changes: Dict des modifications {stat_name: change_value}
    :param source: L'origine de la modification ("opponent", "self", "field", etc.)
    :param fight: L'instance de combat
    :return: True si des modifications ont été appliquées, False sinon
    """
    if not stat_changes:
        return False
    
    # Convertir les noms de stats en indices si nécessaire
    stat_mapping = {
        "Attack": 0,
        "Defense": 1,
        "Sp. Atk": 2,
        "Sp. Def": 3,
        "Speed": 4
    }
    
    # Déclencher l'événement on_stat_change pour le Pokémon ciblé
    final_changes = trigger_talent(target_poke, "on_stat_change", stat_changes, source, fight)
    if final_changes is None:
        final_changes = stat_changes
    
    # Appliquer les modifications finales
    changes_applied = False
    for stat, change in final_changes.items():
        if change != 0:
            if isinstance(stat, str) and stat in stat_mapping:
                stat_index = stat_mapping[stat]
            elif isinstance(stat, int):
                stat_index = stat
            else:
                continue
                
            # Appliquer la modification avec les limites (-6 à +6)
            old_value = target_poke.stats_modifier[stat_index]
            target_poke.stats_modifier[stat_index] = max(-6, min(6, old_value + change))
            
            if target_poke.stats_modifier[stat_index] != old_value:
                changes_applied = True
    
    if changes_applied:
        target_poke.actualize_stats()
    
    return changes_applied


def trigger_talent(poke, event_name, *args):
    """
    Déclenche l'effet du talent en fonction de l'événement.

    :param poke: Le Pokémon utilisant le talent.
    :param event_name: Le nom de l'événement qui déclenche l'effet du talent.
    :param args: Arguments supplémentaires à mettre dans cet ordre"""
    talent = talent_registry.get(poke.talent)
    if talent and hasattr(talent, event_name):
        # Vérifier si la méthode du talent diffère de la méthode de base (qui ne fait rien)
        talent_method = getattr(talent, event_name)
        base_method = getattr(Talent, event_name)
        
        # Si la méthode a été surchargée (différente de la classe de base)
        if talent_method.__func__ != base_method:
            result = talent_method(poke, *args)
            # Afficher le message seulement si le talent a effectivement fait quelque chose
            if result is not None:
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
}