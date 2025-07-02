from pokemon import pokemon
import random 

class Fight():
    def __init__(self, team1, team2):
        self.team1 = team1  # Liste de 6 pokémon
        self.team2 = team2
        self.active1 = team1[0]  # Pokémon actuellement en combat
        self.active2 = team2[0]

        self.check_ability_weather(self.active1)
        self.check_ability_weather(self.active2)
     
        
####### Effets de combats : Terrain, Météo, Murs #######

        ## Météo ##
        self.weather = {"current" : None, "previous" : None}  # Météo actuelle (par exemple : "Ensoleillé", "Pluvieux", etc.) sera un dictionnaire 
        # contenant la météo actuelle et la météo du tour précédent pour savoir si la météo est la même que la précédente
        self.weather_turn_left = None  # Nombre de tours restants pour la météo actuelle, si elle est active
        # Peut juste être un entier puisqu'il n'y a qu'une seule météo active à la fois

        ## Terrain ##
        self.field_effects = None  # Effets de terrain actifs (par exemple : "Champ Electrique", "Champ Herbu", etc.) sera juste une chaine de caractères
        self.field_turn_left = None  # Nombre de tours restants pour le terrain actuel, si il est actif
        # Peut être juste un entier vu que un seul terrain peut être actif à la fois

        ## Murs de protection ##
        self.screen = []  # Écran de protection actif (par exemple : "Mur Lumière", "Protection", etc.)
        self.screen_turn_left = {}  # Nombre de tours restants pour l'écran de protection actif, si il est actif

        self.turn = 0  # Compteur de tours pour suivre le nombre de tours écoulés dans le combat
    
###### Méthodes pour gérer les effets de la météo #######
    def set_weather(self, weather, duration=5):
        """
        Déclenche une météo avec une durée (par défaut 5 tours).
        :param weather: str, nom de la météo ("Sunny", "Rainy", etc.)
        :param duration: int, nombre de tours pendant lesquels la météo est active
        """
        self.weather["previous"] = self.weather["current"]
        self.weather["current"] = weather
        if duration is not None:
            self.weather_turn_left = duration
        else:
            self.weather_turn_left = None  # Infini
        print(f"La météo change : {weather} pendant {duration} tours.")
        

    def apply_weather_effects(self):
        """
        Applique les effets de la météo actuelle sur les Pokémon.
        Et notamment les degats infligés par la tempete de sable et la neige aux Pokémon non-Roche/Acier/Sol et non-Glace.
        """
        match self.weather['current']:
            case "Sandstorm":
                for pokemon in [self.active1, self.active2]:
                    if not any(t in pokemon.types for t in ["Rock", "Steel", "Ground"]):
                        damage = int(pokemon.max_hp * 0.0625)
                        self.damage_method(pokemon, damage)
            case "Snow":
                for pokemon in [self.active1, self.active2]:
                    if "Ice" not in pokemon.types:
                        damage = int(pokemon.max_hp * 0.0625)
                        self.damage_method(pokemon, damage)
            case "Rainy":
                for pokemon in [self.active1, self.active2]:
                    # Si l'un des Pokémons a le talent "Rain Dish", il regagne des PV
                    if pokemon.talent == "Rain Dish":
                        heal_amount = int(pokemon.max_hp * 0.0625) # Régénération de 1/16 des PV max
                        self.damage_method(pokemon, -heal_amount)
                    # Si l'un des Pokémons a le talent "Dry Skin", il perd des PV
                    if talent == "Dry Skin":
                        heal_amount = int(pokemon.max_hp * 0.125)
                        self.damage_method(pokemon, -heal_amount)  # Régénération de 1/8 des PV max
            case "Sunny":
                for pokemon in [self.active1, self.active2]:
                    # Si l'un des Pokémons a le talent "Dry Skin", il perd des PV
                    if pokemon.talent == "Dry Skin":
                        damage = int(pokemon.max_hp * 0.125)
                        self.damage_method(pokemon, damage)
                    
    def weather_boost_modifier(self):
        """
        Applique les changements de stats en fonction de la météo
        """
        for pokemon in [self.active1, self.active2]:
            if self.weather["current"] == "Snow" and self.weather["previous"] != "Snow" and "Ice" in pokemon.types:
                pokemon.stats_modifier[3] += 1
            elif self.weather["previous"] == "Snow" and self.weather["current"] != "Snow" and "Ice" in pokemon.types:
                pokemon.stats_modifier[3] -= 1
            elif self.weather["current"] == "Sandstorm" and self.weather["previous"] and "Rock" in pokemon.types:
                pokemon.stats_modifier[1] += 1
            elif self.weather["previous"] == "Sandstorm" and self.weather["current"] != "Sandstorm" and "Rock" in pokemon.types:
                pokemon.stats_modifier[1] -= 1

    def actualize_weather(self):
        """
        Met à jour la météo : décrémente les tours restants et la retire si elle expire.
        """
        if self.weather_turn_left is not None:
            self.weather_turn_left -= 1
            if self.weather_turn_left <= 0:
                print(f"La météo {self.weather['current']} se dissipe.")
                self.weather['previous'] = self.weather['current']
                self.weather['current'] = None
                self.weather_turn_left = None

    def check_ability_weather(self, pokemon):
        """
        Déclenche une météo si le Pokémon possède un talent météo.
        """
        talent_weather = {
            "Drought": "Sun",
            "Drizzle": "Rain",
            "Sand Stream": "Sandstorm",
            "Snow Warning": "Snow"
        }

        if pokemon.talent in talent_weather:
            self.set_weather(talent_weather[pokemon.talent], duration=None)


###### Méthodes pour gérer les effets de terrain #######
    def add_field_effect(self, effect):
        self.field_effects.append(effect)
        self.field_turn_left = 5  # Classiquement les effets de terrain durent 5 tours, on ignore la Light Clay pour l'instant
    
    def remove_field_effect(self):
        self.field_effects = None  # Supprimer l'effet de terrain
        self.field_turn_left = None  # Réinitialiser le compteur de tours

    def actualize_field_effects(self):
        """
        Met à jour les effets de terrain actifs en décrémentant le nombre de tours restants.
        Supprime les effets de terrain qui ont expiré.
        """
        if self.field_turn_left is not None:
            self.field_turn_left -= 1
            if self.field_turn_left <= 0:
                self.remove_field_effect()
    
    def apply_field_effects(self):
        """
        Applique les effets de terrain actifs sur les Pokémon.
        Par exemple, si le terrain est herbeux, tous les Pokémons sur le terrain regagnent des PV à chaque tour.
        """
        if "Grassy Terrain" == self.field_effects:
            # Regénérer des PV pour les Pokémon de type Plante
            for pokemon in [self.active1, self.active2]:
                damage = -int(pokemon.max_hp * 0.0625)  # Régénération de 1/16 des PV max
                self.damage_method(pokemon, damage)  # Utiliser la méthode de dégâts pour régénérer les PV (dégâts "négatifs")

###### Méthodes pour gérer les screens et la gravité #######
    def add_screen(self, effect):
        self.screen.append(effect)
        self.screen_turn_left[effect] = 5  # Classiquement les effets de terrain durent 5 tours, on ignore la Light Clay pour l'instant
    
    def remove_screen(self, effect):
        if effect in self.screen:
            self.screen.remove(effect)
            del self.screen[effect]  # Supprimer l'effet de terrain et son compteur de tours

    def actualize_field_effects(self):
        """
        Met à jour les effets de terrain actifs en décrémentant le nombre de tours restants.
        Supprime les effets de terrain qui ont expiré.
        """
        for effect in list(self.field_turn_left.keys()):
            self.field_turn_left[effect] -= 1
            if self.field_turn_left[effect] <= 0:
                self.remove_field_effect(effect)

    def damage_method(self, pokemon : pokemon, damage : int):
        """
        Applique les dégâts à un Pokémon.
        :param pokemon: Instance de la classe Pokemon qui subit les dégâts.
        :param damage: Dégâts à infliger.
        """
        pokemon.current_hp -= damage
        if pokemon.current_hp < 0:
            pokemon.current_hp = 0
        elif pokemon.current_hp > pokemon.max_hp:
            pokemon.current_hp = pokemon.max_hp

    ## Printing methods pour debugger
    def print_fight_status(self):
        print(f"Pokémon 1: {self.active1.name} (HP: {self.active1.current_hp}/{self.active1.max_hp})")
        print(f"Pokémon 2: {self.active2.name} (HP: {self.active2.current_hp}/{self.active2.max_hp})")
        print(f"Météo actuelle: {self.weather['current']}")
        print(f"Effets de terrain actifs: {', '.join(self.field_effects) if self.field_effects else 'Aucun'}")
        print(f"Écran de protection actif: {self.screen if self.screen else 'Aucun'}")

    def fight(self):
        print(f"Le combat oppose {self.active1.name} à {self.active2.name} !")

    def next_turn(self):
        """
        Passe au tour suivant du combat.
        Incrémente le compteur de tours et applique les effets de terrain et de météo.
        """
        self.turn += 1
        print(f"Tour {self.turn}:")
        self.actualize_weather()

        self.print_fight_status()
        
        # Appliquer les effets de terrain et de météo
        self.apply_weather_effects()
        for p in [self.active1, self.active2]:
            self.weather_boost_modifier(p)

        if self.weather['current'] == "Sunny":
            print("Le soleil brille ! Les attaques de type Feu sont boostées.")
        elif self.weather['current'] == "Rainy":
            print("Il pleut ! Les attaques de type Eau sont boostées.")
        elif self.weather['current'] == "Sandstorm":
            print("Une tempête de sable souffle ! Les Pokémon du mauvais type subissent des dégâts.")
        elif self.weather['current'] == "Snow":
            print("Il neige ! Les Pokémon du mauvais type subissent des dégâts.")
        
        # Gérer les effets de terrain
        self.apply_field_effects()

        if "Grassy Terrain" in self.field_effects:
            print("Le terrain est herbeux ! Tous les Pokémon regagnent des PV.")
        elif "Electric Terrain" in self.field_effects:
            print("Le terrain est électrique ! Les Pokémon ne peuvent pas dormir.")
        elif "Psychic Terrain" in self.field_effects:
            print("Le terrain est psychique ! Les attaques de priorité sont neutralisées.")
        elif "Misty Terrain" in self.field_effects:
            print("Le terrain est brumeux ! Les attaques de type Dragon sont neutralisées.")
            

    #def attack(pokemon : pokemon, attack : dict, target : pokemon, fight : Fight):
    def attack_power(self, user_pokemon : pokemon, attack : dict, target_pokemon : pokemon):
        """
        Effectue une attaque d'un Pokémon sur une cible.

        :param pokemon: Instance de la classe Pokemon qui attaque.
        :param attack: Dictionnaire contenant les détails de l'attaque.
        :param target: Instance de la classe Pokemon qui est la cible de l'attaque.
        :return: Dégâts infligés à la cible.

        formule de calcul des dégâts :
        damage = ((22 * base_power * (attack_stat / defense_stat)) / 50 + 2) * burn * screen * weather * FF * critical * item * stab * random * Type1 * Type2 * Berry
        """
        critical = 2.0 if is_critical_hit(user_pokemon, attack, target_pokemon) else 1.0  # Si c'est un coup critique, les dégâts sont doublés
        # Le coup critique est déterminé avant car s'il y a un coup critique, on ne prend pas en compte les modificateurs de stats
        base_power = attack['basePower']
        attack_stat = user_pokemon.current_stats()['Attack'] if attack['category'] == 'Physical' else user_pokemon.current_stats()['Sp. Atk']
        defense_stat = target_pokemon.current_stats()['Defense'] if attack['category'] == 'Physical' else target_pokemon.current_stats()['Sp. Def']
        terrain_boost = attack_terrain_boost(attack, self)  # Modificateur de puissance des attaques en fonction du terrain
        weather_boost = attack_weather_boost(attack, self)  # Modificateur de puissance des attaques en fonction de la météo
        berry = berry_boost(target_pokemon, attack)  # Placeholder pour l'effet de la baie, si applicable
        burn = 0.5 if is_burned(user_pokemon) else 1.0  # Si le Pokémon est brûlé, les dégâts sont réduits de moitié
        random = random.uniform(0.85, 1.0)  # Valeur aléatoire entre 0.85 et 1.0
        stab = is_stab(user_pokemon, attack)
        screen = screen_effect(attack, self)  # Effet de l'écran de protection actif

        
        damage = ((22 * base_power * (attack_stat / defense_stat)) / 50 + 2) * burn * screen * terrain_boost * weather_boost * critical * stab * random * berry
            
        return damage
    
    ## PRINTING METHODS POUR DEBUGGER

    def print_wall_effects(self):
        """
        Affiche les effets des murs de protection actifs.
        """
        if self.screen:
            for effet in self.screen:
                if effet == "light_screen":
                    print(f"Mur Lumière actif pendant encore {self.screen_turn_left[effet]} tours.")
                elif effet == "reflect":
                    print(f"Protection active pendant encore {self.screen_turn_left[effet]} tours.")
                elif effet == "aurora_veil":
                    print(f"Voile Aurore actif pendant encore {self.screen_turn_left[effet]} tours.")
        else:
            print("Aucun écran de protection actif.")
    
    def print_weather_effects(self):
        """
        Affiche les effets de la météo actuelle.
        """
        print(f"Météo actuelle : {self.weather['current']} ({self.weather_turn_left} tours restants)")

###### Actions ######

    def player_switch(self, team: int, index: int):
        """
        Change le Pokémon actif dans l'équipe.
        :param team: 1 ou 2 selon le joueur
        :param index: index du Pokémon dans l'équipe (0 à 5)
        """
        if team == 1:
            if self.team1[index].current_hp > 0:
                print(f"{self.active1.name} est remplacé par {self.team1[index].name} !")
                self.active1.reset_stats_nd_status()  # Réinitialiser les stats et les effets de statut du Pokémon actif
                self.active1 = self.team1[index]
        elif team == 2:
            if self.team2[index].current_hp > 0:
                print(f"{self.active2.name} est remplacé par {self.team2[index].name} !")
                self.active2.reset_stats_nd_status()  # Réinitialiser les stats et les effets de statut du Pokémon actif
                self.active2 = self.team2[index]
        
    def reset_stats_nd_status(self, pokemon):
        """
        Réinitialise les stats et les effets de statut d'un Pokémon.
        :param pokemon: Instance de la classe Pokemon à réinitialiser.
        """ 
        pokemon.stats_modifier = [0, 0, 0, 0, 0]
        pokemon.ev_and_acc_modifier = [0, 0]
        if pokemon.is_confused:
            pokemon.is_confused = False
        
    def player_attack(self, attacker, attack, defender):
        """
        Gère l'action "Attaquer" d'un Pokémon sur un autre, en prenant en compte les effets de statut, multi-tours et priorités.
        """

        # Si le Pokémon est en recharge ou charge, on gère cela
        if attacker.charging:
            print(f"{attacker.name} lance la deuxième phase de son attaque chargée !")
            attacker.charging = False
        elif "charge" in attack.get("flags", []):
            if attacker.item == "Power Herb":
                print(f"{attacker.name} lance la deuxième phase de son attaque chargée !")
                attacker.charging = False
            else:
                print(f"{attacker.name} charge {attack['name']} et attaquera au prochain tour !")
                attacker.charging = True
            return

        # Vérification Précision avec modificateurs
        if not self.calculate_hit_chance(attacker, defender, attack):
            print(f"{attacker.name} rate son attaque !")
            return

        print(f"{attacker.name} utilise {attack['name']} !")

        # Gérer effet météo
        if "weather" in attack.get("effect", {}):
            meteo = attack['effect']['weather']['type']
            duration = attack['effect']['weather'].get("duration", 5)
            self.set_weather(meteo, duration)

        # Attaque sans puissance (statut, terrain...)
        if attack['basePower'] == 0:
            self.apply_secondary_effects(attacker, defender, attack)
            return

        # Calcul des dégâts
        damage = self.attack_power(attacker, attack, defender)
        damage = int(damage)
        print(f"{defender.name} subit {damage} points de dégâts.")
        self.damage_method(defender, damage)

        # Effets secondaires (brûlure, paralysie, etc.)
        self.apply_secondary_effects(attacker, defender, attack)

        if defender.current_hp == 0:
            print(f"{defender.name} est K.O. !")

    def apply_secondary_effects(self, attacker, defender, attack):
        """
        Applique les effets secondaires d'une attaque : statut, flinch, etc.
        """
        if "effect" not in attack:
            return

        for effect_name, effect_data in attack["effect"].items():
            chance = effect_data.get("chance", 100)
            if isinstance(chance, bool) or random.randint(1, 100) <= chance:
                effect_fn = effect_data.get("effect")
                if effect_fn:
                    effect_fn(defender if attack["target"] == "Foe" else attacker, True)
                    print(f"Effet secondaire appliqué : {effect_name} sur {defender.name if attack['target'] == 'Foe' else attacker.name}.")

    def compute_priority(self, pokemon, attack):
        """
        Calcule la priorité effective d'une attaque, en prenant en compte les talents.
        """
        base_priority = attack.get("priority", 0)
        if pokemon.talent == "Prankster" and attack["category"] == "Status":
            base_priority += 1
        if pokemon.talent == "Gale Wings" and attack["type"] == "Flying" and pokemon.current_hp == pokemon.max_hp:
            base_priority += 1
        if pokemon.talent == "Triage" and "heal" in attack.get("flags", []):
            base_priority += 3
        if pokemon.talent == "Stall":
            base_priority -= 6
        if pokemon.talent == "Quick Draw" and random.random() < 0.3:
            base_priority += 7
        return base_priority

    def resolve_turn(self, action1, action2):
        """
        Résout un tour de jeu en fonction des priorités (modifiées par les talents), vitesses, et gère les égalités aléatoirement.
        action = (pokemon, attack_dict)
        """
        p1, atk1 = action1
        p2, atk2 = action2

        prio1 = self.compute_priority(p1, atk1)
        prio2 = self.compute_priority(p2, atk2)

        if prio1 > prio2:
            first, first_attack, second, second_attack = p1, atk1, p2, atk2
        elif prio2 > prio1:
            first, first_attack, second, second_attack = p2, atk2, p1, atk1
        else:
            speed1 = p1.stats['Speed']
            speed2 = p2.stats['Speed']
            if speed1 > speed2:
                first, first_attack, second, second_attack = p1, atk1, p2, atk2
            elif speed2 > speed1:
                first, first_attack, second, second_attack = p2, atk2, p1, atk1
            else:
                # Vitesse égale, ordre aléatoire
                if random.random() < 0.5:
                    first, first_attack, second, second_attack = p1, atk1, p2, atk2
                else:
                    first, first_attack, second, second_attack = p2, atk2, p1, atk1

        self.player_attack(first, first_attack, second)
        if second.current_hp > 0:
            self.player_attack(second, second_attack, first)

        self.next_turn()


    ### Savoir la probabilité de toucher une attaque ###
    def calculate_hit_chance(self, attacker, defender, attack):
        """
        Calcule si l'attaque touche en tenant compte de la précision de l'attaque,
        de la précision de l'attaquant et de l'évasion du défenseur.
        """
        base_accuracy = attack.get("accuracy", 100) / 100.0
        effective_accuracy = base_accuracy * attacker.accuracy / defender.evasion
        return random.random() <= effective_accuracy
    


def is_stab(pokemon : pokemon, attack : dict):
    if attack['type'] in pokemon.types:
        return 1.5

def is_critical_hit(pokemon, attack, target):
    """Détermine si une attaque est un coup critique.
    :param pokemon: Instance de la classe Pokemon qui attaque. Pour connaitre son item, son talent
    :param attack: Dictionnaire contenant les détails de l'attaque. Si elle a un effet de coup critique, on le prend en compte
    :param target: Instance de la classe Pokemon qui est la cible de l'attaque. Si son talent annule les coups critiques
    :return: True si c'est un coup critique, False sinon.
    Implémentation de Air Veinard après (une attauqe qui empeche les crits)
    """
    nb_of_boost = 1

    if 'critical' in attack['effect']:
        if attack['effect']['critical']['chance'] == 100:
            nb_of_boost += 100
        elif attack['effect']['critical']['chance'] > 0:
            nb_of_boost += 1
    if pokemon.item == "Scope Lens" or pokemon.item == "Razor Claw":
        nb_of_boost += 1  # 12.5% de chance d'avoir un coup critique avec la lentille de visée
    if pokemon.talent == "Super Luck":
        nb_of_boost += 1  # 12.5% de chance d'avoir un coup critique avec le talent Super Luck
    if target.status == "poisoned" and pokemon.talent == "Poison Touch":
        nb_of_boost += 1
    if pokemon.power:
        nb_of_boost += 2
    if target.talent == "Battle Armor" or target.talent == "Shell Armor":
        nb_of_boost = 1  # Si la cible a le talent Battle Armor ou Shell Armor, elle ne subit pas de coups critiques
    
    return random.random() < 0.0625*nb_of_boost  # retourne True si le coup est critique, False sinon. 0.0625 est la probabilité de coup critique de base (1/16)

def attack_terrain_boost(attack, fight : Fight):
    """
    Applique les mdoficateurs de puissance des attaques en fonction du terrein.
    :param attack: Dictionnaire contenant les détails de l'attaque.
    :param fight: Instance de la classe Fight contenant toutes les informations sur le combat, y compris le terrain actuel.
    :return: Modificateur de puissance des attaques en fonction du terrain.
    """
    match fight.field_effects, attack['type']:
        case (["Grassy Terrain"], "Grass"):
            return 1.3
        case (["Electric Terrain"], "Electric"):
            return 1.3
        case (["Psychic Terrain"], "Psychic"):
            return 1.3
        case (["Misty Terrain"], "Dragon"):
            return 0.5
        
def berry_boost(pokemon, attack):
    """
    Placeholder pour l'effet de la baie, si applicable, si le pokémon tient une baie qui reduit les dégâts de l'attaque si celle ce est super efficace.
    :param pokemon: Instance de la classe Pokemon qui attaque.
    :param attack: Dictionnaire contenant les détails de l'attaque.
    :return: Modificateur de puissance des attaques en fonction de la baie.
    """

    item = pokemon.item
    if item is None:
        return 1.0
    berry = str.split(item, "_")
    if berry[1] != "berry":
        return 1.0
    else:
        return 1.0    # sera implémenté plus tard

def attack_weather_boost(attack, fight):
    """
    Applique les modificateurs de puissance des attaques en fonction de la météo.

    :param attack: Dictionnaire contenant les détails de l'attaque.
    :param fight: Instance de la classe Fight contenant toutes les informations sur le combat, y compris la météo actuelle.
    :return: Modificateur de puissance des attaques en fonction de la météo.
    """
    match fight.weather["current"], attack['type']:
        case ("Sunny", "Fire"):
            return 1.5
        case ("Rainy", "Water"):
            return 1.5
        case ("Sunny", "Water"):
            return 0.5
        case ("Rainy", "Fire"):
            return 0.5
        case _:
            return 1.0  # Pas de boost si la météo ne correspond pas à l'attaque

    
def is_burned(pokemon):
    if pokemon.status != "burn":
        return False
    else:
        return True

def screen_effect(attack, fight : Fight):
    """
    Applique l'effet de l'écran de protection actif.
    
    :param attack: Dictionnaire contenant les détails de l'attaque.
    :param screen: Écran de protection actif (par exemple : "Mur Lumière", "reflect", "aurora veil").
    :return: Facteur de réduction des dégâts.
    """
    if fight.screen == "light_screen" and attack['category'] == "Special":
        return 0.5
    elif fight.screen == "reflect" and attack['category'] == "Physical":
        return 0.5
    elif fight.screen == "aurora veil":
        return 0.5
    else:
        return 1.0