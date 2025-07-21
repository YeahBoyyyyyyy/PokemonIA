'''
fichier regroupant tous les talents de poke et créant un dictionnaire regroupant tous leurs effets.
'''

class Talent:
    """
    Classe de base pour tous les talents. Les sous-classes peuvent surcharger les méthodes suivantes :
    - on_entry: quand le pokémon entre en combat
    - on_attack: juste avant de lancer une attaque
    - on_defense: quand le pokémon est ciblé par une attaque
    - modify_stat: pour modifier une stat temporairement (ex: vitesse sous le soleil)
    """
    def on_entry(self, poke, fight):
        pass

    def on_attack(self, poke, attack, fight):
        pass

    def on_defense(self, poke, incoming_attack, fight):
        pass

    def modify_stat(self, poke, fight = None):
        return None


class WaterAbsorb(Talent):
    def on_defense(self, poke, incoming_attack, fight = None):
        if incoming_attack.get("type") == "Water":
            healed = int(poke.max_hp * 0.25)
            poke.current_hp = min(poke.current_hp + healed, poke.max_hp)
            print(f"{poke.name} absorbe l'eau et récupère {healed} PV !")
            return 0  # annule les dégâts


class Chlorophyll(Talent):
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
    def on_attack(self, poke, attack, fight = None):
        if poke.current_hp < poke.max_hp / 3 and attack.type == "Grass":
            return 1.5


class Blaze(Talent):
    def on_attack(self, poke, attack, fight = None):
        if poke.current_hp < poke.max_hp / 3 and attack.type == "Fire":
            return 1.5 


class Torrent(Talent):
    def on_attack(self, poke, attack, fight):
        if poke.current_hp < poke.max_hp / 3 and attack.type == "Water":
            return 1.5

class Drizzle(Talent):
    def on_entry(self, poke, fight):
        fight.set_weather("Rain", duration=5)
        print(f"{poke.name} invoque la pluie !")
        return "activated"

class Drought(Talent):
    def on_entry(self, poke, fight):
        fight.set_weather("Sunny", duration=5)
        print(f"{poke.name} invoque le soleil !")
        return "activated"

class Intimidate(Talent):
    def on_entry(self, poke, fight):
        opponent = fight.active2 if poke == fight.active1 else fight.active1

        # Vérifie que l'adversaire n'est pas déjà KO
        if opponent.current_hp > 0:
            opponent.stats_modifier[0] = max(opponent.stats_modifier[0] - 1, -6)
            opponent.actualize_stats()
            print(f"{poke.name} intimide {opponent.name} ! Son Attaque baisse.")
            return "activated"
        return None

class QuarkDrive(Talent):
    def on_entry(self, poke, fight):
        if fight.weather['current'] == "Electric Terrain":
            stat_max = max(poke.stats, key = poke.stats.get)
            if stat_max == "Speed":
                poke.hidden_boost["Speed"] *= 1.5
            else:
                poke.hidden_boost[stat_max] *= 1.3

class Protosynthesis(Talent):
    def on_entry(self, poke, fight):
        if fight.weather['current'] == "Electric Terrain":
            stat_max = max(poke.stats, key = poke.stats.get)
            if stat_max == "Speed":
                poke.hidden_boost["Speed"] *= 1.5
            else:
                poke.hidden_boost[stat_max] *= 1.3

class FlashFire(Talent):
    def on_defense(self, poke, incoming_attack, fight=None):
        if incoming_attack.type == "Fire":
            poke.stats_modifier[2] += 1
            poke.actualize_stats()
            print(f"{poke.name} absorbe le feu et augmente son Attaque Spéciale !")
            return 0  # annule les dégâts

class ThickFat(Talent):
    def on_defense(self, poke, incoming_attack, fight=None):
        if incoming_attack.type in ["Fire", "Ice"]:
            print(f"{poke.name} réduit de moitié les dégâts grâce à sa graisse !")
            return 0.5

class Stamina(Talent):
    def on_defense(self, poke, incoming_attack, fight=None):
        if incoming_attack.category in ["Physical", "Special"]:
            poke.stats_modifier[1] = min(poke.stats_modifier[1] + 1, 6)
            poke.actualize_stats()
            print(f"{poke.name} augmente sa Défense grâce à Endurance !")
        return None

class Sturdy(Talent):
    def on_defense(self, poke, incoming_attack, fight=None):
        # Si le Pokémon a tous ses PV et que l'attaque pourrait le mettre KO
        if poke.current_hp == poke.max_hp and not poke.sturdy_activated:
            # On ne peut pas vraiment empêcher les dégâts ici, mais on peut marquer le Pokémon
            # pour qu'il garde au moins 1 PV dans la méthode damage_method
            poke.sturdy_activated = True
            print(f"{poke.name} résiste grâce à Fermeté et garde 1 PV !")
            return "activated"  # Indique que le talent a été activé
        return None

class LightMetal(Talent):
    def modify_stat(self, poke, fight=None):
        # Réduit le poids de moitié (utilisé pour les attaques basées sur le poids)
        if not hasattr(poke, 'original_weight'):
            poke.original_weight = getattr(poke, 'weight', 100)  # Poids par défaut si non défini
        poke.weight = poke.original_weight / 2
        return None

class PoisonPuppeteer(Talent):
    def on_defense(self, poke, incoming_attack, fight=None):
        # Trouve l'attaquant (celui qui n'est pas poke)
        if fight:
            attacker = fight.active1 if poke == fight.active2 else fight.active2
            if incoming_attack.category in ["Physical", "Special"] and not attacker.status:
                attacker.apply_status("poison")
                print(f"{attacker.name} est empoisonné par Emprise Toxique de {poke.name} !")
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
}


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
