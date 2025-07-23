class Item:
    def on_turn_end(self, fight=None):
        """
        This method is called at the end of each turn to apply the item's effect.
        """
        pass
    def after_attack(self, poke, fight=None):
        """
        This method is called after an attack to apply the item's effect.
        """
        pass

    def before_attack(self, poke, attack, fight=None):
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
    


class Leftovers(Item):
    def on_turn_end(self, poke, fight=None):
        if poke.current_hp < poke.max_hp:
            heal = int(poke.max_hp * 0.0625)
            print(f"{poke.name} récupère {heal} PV grâce à ses Restes.")
            poke.current_hp = min(poke.current_hp + heal, poke.max_hp)

class SitrusBerry(Item):
    def after_attack(self, poke, fight=None):
        if poke.current_hp <= poke.max_hp * 0.5:
            heal = int(poke.max_hp * 0.25)
            print(f"{poke.name} consomme une Baie Sitrus et récupère {heal} PV !")
            poke.current_hp = min(poke.current_hp + heal, poke.max_hp)
            poke.item = None

class ChoiceBoost(Item):
    def modify_stat(self, poke, fight=None):
        if poke.item == "Choice Band":
            poke.stats["Attack"] += int(poke.stats_with_no_modifier["Attack"] * 0.5)
        elif poke.item == "Choice Specs":
            poke.stats["Sp. Atk"] += int(poke.stats_with_no_modifier["Sp. Atk"] * 0.5)
        elif poke.item == "Choice Scarf":
            poke.stats["Speed"] += int(poke.stats_with_no_modifier["Speed"] * 0.5)

class Eviolite(Item):
    def modify_stat(self, poke, fight=None):
        if not poke.fully_evolved:
            poke.stats["Defense"] += int(poke.stats_with_no_modifier["Defense"] * 0.5)
            poke.stats["Sp. Def"] += int(poke.stats_with_no_modifier["Sp. Def"] * 0.5)

class EnergyBooster(Item):
    def on_entry(self, poke, fight=None):
        if poke.talent == "Quark Drive" or poke.talent == "Protosynthesis":
            stat_max = max(poke.stats, key = poke.stats.get)
            if stat_max == "Speed":
                poke.hidden_boost[stat_max] *= 1.5
            else:
                poke.hidden_boost[stat_max] *= 1.3
        poke.item = None

class AssaultVest(Item):
    def modify_stat(self, poke, fight=None):
        if poke.fully_evolved:
            poke.stats["Sp. Def"] += int(poke.stats_with_no_modifier["Sp. Def"] * 0.5)
            poke.item = None

item_registry = {
    "Leftovers": Leftovers(),
    "Sitrus Berry": SitrusBerry(),
    "Choice Band": ChoiceBoost(),
    "Choice Specs": ChoiceBoost(),
    "Choice Scarf": ChoiceBoost(),
    "Eviolite": Eviolite(),
    "Energy Booster": EnergyBooster(),
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