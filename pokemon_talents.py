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
            return "nullify"  # annule les dégâts


class Chlorophyll(Talent):
    def modify_stat(self, poke, fight=None):
        if fight:
            if fight.weather["current"] == "Sunny" and fight.weather["previous"] != "Sunny":
                poke.stats["Speed"] = int(poke.stats["Speed"] * 2)
            elif fight.weather["previous"] == "Sunny" and fight.weather["current"] != "Sunny":
                poke.stats["Speed"] = poke.stats["Speed"] // 2
        return


class Overgrow(Talent):
    def on_attack(self, poke, attack, fight = None):
        if poke.current_hp < poke.max_hp / 3 and attack['type'] == "Grass":
            attack['basePower'] = int(attack['basePower'] * 1.5)


class Blaze(Talent):
    def on_attack(self, poke, attack, fight = None):
        if poke.current_hp < poke.max_hp / 3 and attack['type'] == "Fire":
            attack['basePower'] = int(attack['basePower'] * 1.5)


class Torrent(Talent):
    def on_attack(self, poke, attack, fight):
        if poke.current_hp < poke.max_hp / 3 and attack['type'] == "Water":
            attack['basePower'] = int(attack['basePower'] * 1.5)


class Drought(Talent):
    def on_entry(self, poke, fight):
        fight.set_weather("Sunny", duration = 5)
        print(f"{poke.name} invoque le soleil !")

class Intimidate(Talent):
    def on_entry(self, poke, fight):
        opponent = fight.active2 if poke == fight.active1 else fight.active1

        # Vérifie que l'adversaire n'est pas déjà KO
        if opponent.current_hp > 0:
            opponent.stats_modifier[0] = max(opponent.stats_modifier[0] - 1, -6)
            opponent.actualize_stats()
            print(f"{poke.name} intimide {opponent.name} ! Son Attaque baisse.")

class QuarkDrive(Talent):
    def on_entry(self, poke, fight):
        if fight.weather['current'] == "Electric Terrain":
            stat_max = max(poke.stats, key = poke.stats.get)
            if stat_max == "Speed":
                poke.stats["Speed"] = int(poke.stats["Speed"] * 1.5)
            else:
                poke.stats[stat_max] = int(poke.stats[stat_max] * 1.3)

class Paleosynthesis(Talent):
    def on_entry(self, poke, fight):
        if fight.weather['current'] == "Electric Terrain":
            stat_max = max(poke.stats, key = poke.stats.get)
            if stat_max == "Speed":
                poke.stats["Speed"] = int(poke.stats["Speed"] * 1.5)
            else:
                poke.stats[stat_max] = int(poke.stats[stat_max] * 1.3)

class FlashFire(Talent):
    def on_defense(self, poke, incoming_attack, fight=None):
        if incoming_attack.type == "Fire":
            poke.stats_modifier[2] += 1
            poke.actualize_stats()
            print(f"{poke.name} absorbe le feu et augmente son Attaque Spéciale !")
            return "nullify"  # annule les dégâts




# Registre des talents
talent_registry = {
    "Water Absorb": WaterAbsorb(),
    "Intimidate": Intimidate(),
    "Chlorophyll": Chlorophyll(),
    "Overgrow": Overgrow(),
    "Blaze": Blaze(),
    "Torrent": Torrent(),
    "Drought": Drought(),
    "Quark Drive": QuarkDrive(),
    "Paleosynthesis": Paleosynthesis(),
    "Flash Fire": FlashFire(),
}


def trigger_talent(poke, event_name, *args):
    """
    Déclenche l'effet du talent en fonction de l'événement.

    :param poke: Le Pokémon utilisant le talent.
    :param event_name: Le nom de l'événement qui déclenche l'effet du talent.
    :param args: Arguments supplémentaires à mettre dans cet ordre"""
    talent = talent_registry.get(poke.talent)
    if talent and hasattr(talent, event_name):
        print(f"[TALENT] {poke.name} active {poke.talent} -> {event_name}")
        return getattr(talent, event_name)(poke, *args)
    return None
