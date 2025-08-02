ON_ATTACK_MOD_DICT = {
    "attack": 1.0,
    "power": 1.0,
    "accuracy": 1.0
}

class Item:
    def on_turn_end(self, fight=None):
        """
        This method is called at the end of each turn to apply the item's effect.
        """
        
        pass
    def after_attack(self, poke, fight, attacker, attack):
        """
        This method is called after an attack to apply the item's effect.
        """
        pass

    def before_attack(self, poke, attack, fight=None):
        """
        This method is called before an attack to apply the item's effect (e.g., Focus Sash).
        """
        pass

    def on_attack(self, poke, attack, fight=None):
        """
        This method is called before an attack to apply the item's effect.
        """
        pass
    def on_entry(self, poke, fight=None):
        """
        This method is called when the Pokémon enters the battle to apply the item's effect.
        """
        pass
    def modify_stat(self, poke, fight=None):
        """
        This method is called to modify the Pokémon's stats based on the item's effect.
        """
        return None
    
    def on_defense(self, poke, attack, fight=None):
        """
        This method is called when the Pokémon is attacked to apply the item's effect.
        """
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

class Leftovers(Item):
    def on_turn_end(self, poke, fight=None):
        if poke.current_hp < poke.max_hp:
            if not getattr(poke, 'heal_blocked', False):
                heal = int(poke.max_hp * 0.0625)
                print(f"{poke.name} récupère {heal} PV grâce à ses Restes.")
                poke.current_hp = min(poke.current_hp + heal, poke.max_hp)
            else:
                print(f"{poke.name} ne peut pas bénéficier de ses Restes à cause de Heal Block !")

class SitrusBerry(Item):
    def after_attack(self, poke, fight = None, attacker = None, attack = None):
        if poke.current_hp <= poke.max_hp * 0.5 and poke.current_hp > 0:
            if not getattr(poke, 'heal_blocked', False):
                heal = int(poke.max_hp * 0.25)
                print(f"{poke.name} consomme une Baie Sitrus et récupère {heal} PV !")
                poke.current_hp = min(poke.current_hp + heal, poke.max_hp)
                poke.item = None
            else:
                print(f"{poke.name} ne peut pas utiliser sa Baie Sitrus à cause de Heal Block !")
                # La baie n'est pas consommée si elle ne peut pas être utilisée

class ChoiceBoost(Item):
    def modify_stat(self, poke, fight=None):
        if poke.item == "Choice Band":
            poke.stats["Attack"] = int(poke.stats["Attack"] * 1.5)
        elif poke.item == "Choice Specs":
            poke.stats["Sp. Atk"] = int(poke.stats["Sp. Atk"] * 1.5)
        elif poke.item == "Choice Scarf":
            poke.stats["Speed"] = int(poke.stats["Speed"] * 1.5)

class Eviolite(Item):
    def modify_stat(self, poke, fight=None):
        if not poke.fully_evolved:
            poke.stats["Defense"] = int(poke.stats["Defense"] * 1.5)
            poke.stats["Sp. Def"] = int(poke.stats["Sp. Def"] * 1.5)

class BoosterEnergy(Item):
    def on_entry(self, poke, fight=None):
        if poke.talent == "Quark Drive" or poke.talent == "Protosynthesis":
            stat_max = max(poke.stats, key = poke.stats.get)
            if stat_max == "Speed":
                poke.hidden_modifier[stat_max] *= 1.5
            else:
                poke.hidden_modifier[stat_max] *= 1.3
        poke.item = None

class ChestoBerry(Item):
    def on_turn_end(self, poke, fight=None):
        if poke.status == "sleep":
            print(f"{poke.name} se réveille grâce à sa Baie Chesto !")
            poke.status = None
            poke.item = None
    def before_attack(self, poke, attack, fight=None):
        if poke.status == "sleep":
            print(f"{poke.name} utilise sa Baie Chesto pour se réveiller avant l'attaque !")
            poke.status = None
            poke.item = None

class AssaultVest(Item):
    def modify_stat(self, poke, fight=None):
        poke.stats["Sp. Def"] += int(poke.stats_with_no_modifier["Sp. Def"] * 0.5)
    
class RockyHelmet(Item):
    """
    Rocky Helmet inflige des dégâts à l'attaquant si l'attaque était de contact.    
    Cet effet se déclenche après que le porteur ait subi une attaque de contact.
    """
    def after_attack(self, poke, fight=None, attacker=None, attack=None):
        
        pass

class HeavyDutyBoots(Item):
    """
    Heavy-Duty Boots permet au Pokémon de ne pas subir de dégâts de Pièges d'Entrée.
    Cet effet se déclenche lorsque le Pokémon entre dans le combat.
    """
    def on_entry(self, poke, fight=None):
       
        print(f"{poke.name} porte des Heavy-Duty Boots et ignore les Pièges d'Entrée !")

class FocusSash(Item):
    """
    Focus Sash permet au Pokémon de survivre à une attaque qui le mettrait KO, en restant à 1 PV à la place. Ne fonctionne que si le Pokémon était à pleine santé.
    """
    def on_attack(self, poke, attack, fight=None):
        # La Ceinture Force ne fonctionne que si le Pokémon est à pleine santé
        if poke.current_hp == poke.max_hp:
            poke.focus_sash_ready = True
        else:
            poke.focus_sash_ready = False

        return ON_ATTACK_MOD_DICT    
    
class BlackGlasses(Item):
    """
    Black Glasses augmente la puissance des attaques de type Ténèbres de 20%.
    """
    def on_attack(self, poke, attack, fight=None):
        if attack.type == "Dark":
            print(f"Les Black Glasses de {poke.name} renforcent la puissance de son attaque !")
        return {"attack":1.0,"power": 1.2, "accuracy": 1.0}
    
class LifeOrb(Item):
    """
    Life Orb augmente la puissance des attaques de 30%, mais inflige 10% de dégâts au Pokémon après chaque attaque.
    """
    def on_attack(self, poke, attack, fight=None):
        return {"attack": 1.3, "power": 1.0, "accuracy":1.0}
    
    def after_attack(self, poke, fight, attacker=None, attack=None):
        if attacker == poke and attack.category != "Status":
            if poke.current_hp > 0:
                damage = int(poke.max_hp * 0.1)
                print(f"{poke.name} subit {damage} PV de dégâts à cause de la Life Orb !")
                poke.current_hp = max(poke.current_hp - damage, 0)

class ToxicOrb(Item):
    """
    Empoisonne gravement le porteur à la fin du tour
    """
    def on_turn_end(self, poke, fight=None):
        if poke.status is None:
            print(f"{poke.name} est empoisonné gravement par sa Toxic Orb !")
            poke.apply_status("badly_poisoned")

class WideLens(Item):
    """
    Wide Lens augmente la précision des attaques de 10%.
    """
    def on_attack(self, poke, attack, fight=None):
        return {"attack": 1.0, "power": 1.0, "accuracy": 1.1}

class AirBalloon(Item):
    """
    Air Balloon permet au Pokémon de léviter et d'être immunisé aux attaques de type Sol.
    Se brise si le Pokémon subit des dégâts.
    """
    def on_entry(self, poke, fight=None):
        print(f"{poke.name} flotte grâce à son Air Balloon !")
        poke.air_balloon_active = True
        
    def on_defense(self, poke, attack, fight=None):
        # Immunité aux attaques de type Sol si le ballon est actif
        if getattr(poke, 'air_balloon_active', True) and attack.type == "Ground":
            print(f"{poke.name} évite l'attaque grâce à son Air Balloon !")
            return {"attack": 0.0, "power": 0.0, "accuracy": 1.0}
        return None
        
    def after_attack(self, poke, fight=None, attacker=None, attack=None):
        # Le ballon se brise si le Pokémon subit des dégâts
        if (getattr(poke, 'air_balloon_active', True) and attack.type != "Ground" and attack.category != "Status" and not poke.protect and attacker != poke):
            self.destroy_balloon(poke)
    
    def on_entry(self, poke, fight=None):
        team_id = fight.get_team_id(poke)
        if team_id == 1:
            if fight.hazards_team1["Stealth Rock"]:
                self.destroy_balloon(poke)
        elif team_id == 2:
            if fight.hazards_team2["Stealth Rock"]:
                self.destroy_balloon(poke)

    def destroy_balloon(self, poke):
        """
        Détruit l'Air Balloon du Pokémon.
        """
        print(f"L'Air Balloon de {poke.name} éclate !")
        poke.air_balloon_active = False
        poke.item = None

class WhiteHerb(Item):
    """
    White Herb restaure les stats du Pokémon si elles ont été baissées.
    """
    def on_stat_change(self, poke, stat_changes, source, fight=None):
        # Vérifie s'il y a des stats qui baissent
        has_negative_changes = any(change < 0 for change in stat_changes.values())
        
        if has_negative_changes:
            print(f"{poke.name} utilise sa White Herb !")
            # Annule toutes les baisses de stats
            for stat in stat_changes:
                if stat_changes[stat] < 0:
                    stat_changes[stat] = 0
            # Consomme l'objet une seule fois
            poke.item = None
        
        return stat_changes

class SoulDew(Item):
    """
    La Soul Dew augmente la puissance des capacités de type psy ou dragon lorsque tenu par latias ou latios.
    """
    def on_attack(self, poke, attack, fight=None):
        if poke.name == "Latias" or poke.name == "Latios":
            if attack.type == "Psychic" or attack.type == "Dragon":
                return {"attack": 1.0, "power": 1.2, "accuracy": 1.0}    
        return ON_ATTACK_MOD_DICT

item_registry = {
    "Leftovers": Leftovers(),
    "Sitrus Berry": SitrusBerry(),
    "Chesto Berry": ChestoBerry(),
    "Choice Band": ChoiceBoost(),
    "Choice Specs": ChoiceBoost(),
    "Choice Scarf": ChoiceBoost(),
    "Eviolite": Eviolite(),
    "Booster Energy": BoosterEnergy(),
    "Assault Vest": AssaultVest(),
    "Rocky Helmet": RockyHelmet(),
    "Heavy-Duty Boots": HeavyDutyBoots(),
    "Focus Sash": FocusSash(),
    "Black Glasses": BlackGlasses(),
    "Life Orb": LifeOrb(),
    "Toxic Orb": ToxicOrb(),
    "Wide Lens": WideLens(),
    "Air Balloon": AirBalloon(),
    "White Herb": WhiteHerb(),
    "Soul Dew": SoulDew(),
}

def trigger_item(poke, event, *args):
    """    
    Déclenche l'effet de l'objet en fonction de l'événement.

    :param poke: Le Pokémon utilisant l'objet.
    :param event: Le nom de l'événement end_turn, after_attack, before_attack, on_entry, modify_stat.
    :param args: Arguments supplémentaires en fonction de l'événement
    """
    item = item_registry.get(poke.item)
    if item and hasattr(item, event):
        # Vérifier si la méthode de l'objet diffère de la méthode de base (qui ne fait rien)
        item_method = getattr(item, event)
        base_method = getattr(Item, event)
        
        # Si la méthode a été surchargée (différente de la classe de base)
        if item_method.__func__ != base_method:
            print(f"[ITEM] {poke.name} uses {poke.item} -> {event}")
            return item_method(poke, *args)
    return None