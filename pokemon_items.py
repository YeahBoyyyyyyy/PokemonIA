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
            if not getattr(poke, 'heal_blocked', False):
                heal = int(poke.max_hp * 0.0625)
                print(f"{poke.name} récupère {heal} PV grâce à ses Restes.")
                poke.current_hp = min(poke.current_hp + heal, poke.max_hp)
            else:
                print(f"{poke.name} ne peut pas bénéficier de ses Restes à cause de Heal Block !")

class SitrusBerry(Item):
    def after_attack(self, poke, fight=None):
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
    def after_attack(self, poke, fight=None):
        """
        Rocky Helmet inflige des dégâts à l'attaquant si l'attaque était de contact.
        Cet effet se déclenche après que le porteur ait subi une attaque de contact.
        """
        pass

class HeavyDutyBoots(Item):
    def on_entry(self, poke, fight=None):
        """
        Heavy-Duty Boots permet au Pokémon de ne pas subir de dégâts de Pièges d'Entrée.
        Cet effet se déclenche lorsque le Pokémon entre dans le combat.
        """
        print(f"{poke.name} porte des Heavy-Duty Boots et ignore les Pièges d'Entrée !")

item_registry = {
    "Leftovers": Leftovers(),
    "Sitrus Berry": SitrusBerry(),
    "Chesto Berry": ChestoBerry(),
    "Choice Band": ChoiceBoost(),
    "Choice Specs": ChoiceBoost(),
    "Choice Scarf": ChoiceBoost(),
    "Eviolite": Eviolite(),
    "Energy Booster": EnergyBooster(),
    "Assault Vest": AssaultVest(),
    "Rocky Helmet": RockyHelmet(),
    "Heavy-Duty Boots": HeavyDutyBoots(),
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