from pokemon import pokemon
import random 
import donnees 
from item import item_effects
from pokemon_talents import trigger_talent
from pokemon_attacks import Attack

class Fight():
    def __init__(self, team1, team2):
        self.team1 = team1  # Liste de 6 pokémon
        self.team2 = team2
        self.active1 = team1[0]  # Pokémon actuellement en combat
        self.active2 = team2[0]

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

        self.check_ability_weather(self.active1)
        self.check_ability_weather(self.active2)
        
        self.active1.init_fight(self)
        self.active2.init_fight(self)
        self.active1.actualize_stats()  # Met à jour les stats du Pokémon actif au cas ou le talent de active2 active celui de 1


        trigger_talent(self.active1, "on_entry", self)
        trigger_talent(self.active2, "on_entry", self)

    
    def is_team_defeated(self, team):
        """
        Vérifie si tous les Pokémon de l'équipe sont K.O.
        """
        return all(p.current_hp <= 0 for p in team)
    
    def auto_switch(self, team_id):
        """
        Sélectionne automatiquement le prochain Pokémon vivant dans l'équipe.
        """
        team = self.team1 if team_id == 1 else self.team2
        for i, p in enumerate(team):
            if p.current_hp > 0:
                self.player_switch(team_id, i)
                return

    def check_battle_end(self):
        """
        Vérifie si le combat est terminé. Retourne True si oui, False sinon.
        Affiche aussi le gagnant.
        """
        if self.is_team_defeated(self.team1):
            print("Tous les Pokémon de l'équipe 1 sont K.O. ! Victoire de l'équipe 2 !")
            return True
        elif self.is_team_defeated(self.team2):
            print("Tous les Pokémon de l'équipe 2 sont K.O. ! Victoire de l'équipe 1 !")
            return True
        return False



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
        self.weather_boost_modifier()

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

        if "Grassy Terrain" == self.field_effects:
            print("Le terrain est herbeux ! Tous les Pokémon regagnent des PV.")
        elif "Electric Terrain" == self.field_effects:
            print("Le terrain est électrique ! Les Pokémon ne peuvent pas dormir.")
        elif "Psychic Terrain" == self.field_effects:
            print("Le terrain est psychique ! Les attaques de priorité sont neutralisées.")
        elif "Misty Terrain" == self.field_effects:
            print("Le terrain est brumeux ! Les attaques de type Dragon sont neutralisées.")
            
    #def attack(pokemon : pokemon, attack : dict, target : pokemon, fight : Fight):
    def attack_power(self, user_pokemon : pokemon, attack : Attack, target_pokemon : pokemon):
        """
        Effectue une attaque d'un Pokémon sur une cible.

        :param pokemon: Instance de la classe Pokemon qui attaque.
        :param attack: Dictionnaire contenant les détails de l'attaque.
        :param target: Instance de la classe Pokemon qui est la cible de l'attaque.
        :return: Dégâts infligés à la cible.

        formule de calcul des dégâts :
        damage = ((22 * base_power * (attack_stat / defense_stat)) / 50 + 2) * burn * screen * weather * FF * critical * item * stab * random * Type1 * Type2 * Berry
        """
        # Le coup critique est déterminé avant car s'il y a un coup critique, on ne prend pas en compte les modificateurs de stats
        base_power = attack.base_power
        attack_stat = user_pokemon.current_stats()['Attack'] if attack.category == 'Physical' else user_pokemon.current_stats()['Sp. Atk']
        defense_stat = target_pokemon.current_stats()['Defense'] if attack.category == 'Physical' else target_pokemon.current_stats()['Sp. Def']
        terrain_boost = attack_terrain_boost(attack, self)  # Modificateur de puissance des attaques en fonction du terrain
        weather_boost = attack_weather_boost(attack, self)  # Modificateur de puissance des attaques en fonction de la météo
        berry = berry_boost(target_pokemon, attack)  # Placeholder pour l'effet de la baie, si applicable
        burn = 0.5 if is_burned(user_pokemon) else 1.0  # Si le Pokémon est brûlé, les dégâts sont réduits de moitié
        rdm = random.uniform(0.85, 1.0)  # Valeur aléatoire entre 0.85 et 1.0
        stab = is_stab(user_pokemon, attack)
        screen = screen_effect(attack, self)  # Effet de l'écran de protection actif
        type_eff = type_effectiveness(attack.type, target_pokemon.types)  # Calcul de l'efficacité du type

        if is_critical_hit(user_pokemon, attack, target_pokemon):
            print(f"{user_pokemon.name} porte un coup critique avec {attack.name} !")
            critical = 1.5  # Coup critique inflige 1.5x les dégâts
            damage = ((22 * base_power * (attack_stat / defense_stat)) / 50 + 2) * burn * screen * type_eff * terrain_boost * weather_boost * critical * stab * rdm * berry
            # A changer car les crits ne prennent pas en compte les modificateurs de stats
        else:
            critical = 1.0
            damage = ((22 * base_power * (attack_stat / defense_stat)) / 50 + 2) * burn * screen * type_eff * terrain_boost * weather_boost * critical * stab * rdm * berry
            
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
                trigger_talent(self.active1, "on_entry", self)

        elif team == 2:
            if self.team2[index].current_hp > 0:
                print(f"{self.active2.name} est remplacé par {self.team2[index].name} !")
                self.active2.reset_stats_nd_status()  # Réinitialiser les stats et les effets de statut du Pokémon actif
                self.active2 = self.team2[index]
                trigger_talent(self.active2, "on_entry", self)          
        
    def reset_stats_nd_status(self, pokemon):
        """
        Réinitialise les stats et les effets de statut d'un Pokémon lorsque le pokémon est switché.
        :param pokemon: Instance de la classe Pokemon à réinitialiser.
        """ 
        pokemon.stats_modifier = [0, 0, 0, 0, 0]
        pokemon.ev_and_acc_modifier = [0, 0]
        if pokemon.is_confused:
            pokemon.is_confused = False
        pokemon.locked_move = None  # Réinitialiser le verrouillage de l'attaque si le Pokémon est switché
        pokemon.leech_seeded_by = None  # Réinitialiser le Leech Seed si le Pokémon est switché

    def player_attack(self, attacker : pokemon, attack : Attack, defender : pokemon):
        """
        Gère l'action "Attaquer" d'un Pokémon sur un autre, en prenant en compte les effets de statut, multi-tours et priorités.
        """

        # Si le Pokémon est confus, on gère la confusion
        if attacker.is_confused:
            if attacker.still_confused:
                if random.random() < 0.33:
                    print(f"{attacker.name} est confus et se blesse lui-même !")
                    damage = confusion_attack(attacker)
                    self.damage_method(attacker, damage)
                    if random() < 0.33: # Le Pokémon ne sera plus confus au prochain tour 1/3 chance
                        attacker.is_confused = False
                    return
            elif attacker.still_confused == False and attacker.is_confused:
                print(f"{attacker.name} n'est plus confus !")
                attacker.is_confused = False

        # Si le Pokémon est en recharge ou charge, on gère cela
        if attacker.charging:
            print(f"{attacker.name} lance la deuxième phase de son attaque chargée !")
            attacker.charging = False
        elif "charge" in attack.flags:
            if attacker.item == "Power Herb":
                print(f"{attacker.name} lance la deuxième phase de son attaque chargée !")
                attacker.charging = False
            else:
                print(f"{attacker.name} charge {attack.name} et attaquera au prochain tour !")
                attacker.charging = True
            return

        # Vérification Précision avec modificateurs
        if not self.calculate_hit_chance(attacker, defender, attack):
            print(f"{attacker.name} rate son attaque !")
            return

        print(f"{attacker.name} utilise {attack.name} !")
        
        # Vérifie si l'objet de choix le verrouille sur une attaque
        if attacker.item and "Choice" in attacker.item:
            if attacker.locked_move and attacker.locked_move != attack.name:
                print(f"{attacker.name} est verrouillé sur {attacker.locked_move} à cause de {attacker.item} et ne peut pas utiliser {attack.name} !")
                return
            attacker.locked_move = attack.name

        # Gérer effet météo - TODO: implémenter via apply_effect des attaques
        # if "weather" in attack.get("effect", {}):
        #     meteo = attack['effect']['weather']['type']
        #     duration = attack['effect']['weather'].get("duration", 5)
        #     self.set_weather(meteo, duration)

        # Attaque sans puissance (statut, terrain...)
        if attack.base_power == 0:
            self.apply_secondary_effects(attacker, defender, attack)
            return

        cancel = trigger_talent(defender, "on_defense", attack, self)
        if cancel == "nullify":
            print(f"{defender.name} n’est pas affecté grâce à son talent !")
            return


        # Calcul des dégâts
        trigger_talent(attacker, "on_attack", attack, self)
        damage = self.attack_power(attacker, attack, defender)
        damage = int(damage)
        print(f"{defender.name} subit {damage} points de dégâts.")
        self.damage_method(defender, damage)

        # Effets secondaires de l'attaque
        self.apply_secondary_effects(attacker, defender, attack)

        if defender.current_hp == 0:
            print(f"{defender.name} est K.O. !")

    def apply_secondary_effects(self, attacker, defender, attack):
        """
        Applique les effets secondaires d'une attaque : statut, flinch, etc.
        """
        # Vérifier si l'attaque a une méthode apply_effect
        if hasattr(attack, 'apply_effect'):
            # Déterminer la cible en fonction du target de l'attaque
            if attack.target == "Foe":
                target = defender
            elif attack.target == "User":
                target = attacker
            else:
                target = defender  # Par défaut
            
            # Appliquer l'effet secondaire
            attack.apply_effect(attacker, target, self)

            

    def compute_priority(self, pokemon, attack = Attack):
        """
        Calcule la priorité effective d'une attaque, en prenant en compte les talents.
        """
        base_priority = attack.priority
        if pokemon.talent == "Prankster" and attack.category == "Status":
            base_priority += 1
        if pokemon.talent == "Gale Wings" and attack.type == "Flying" and pokemon.current_hp == pokemon.max_hp:
            base_priority += 1
        if pokemon.talent == "Triage" and "heal" in attack.flags:
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

        # Déterminer l'ordre d'action
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
                if random.random() < 0.5:
                    first, first_attack, second, second_attack = p1, atk1, p2, atk2
                else:
                    first, first_attack, second, second_attack = p2, atk2, p1, atk1

        # Première attaque
        if self.check_status_before_attack(first):
            self.player_attack(first, first_attack, second)
            
        # Seconde attaque si vivant
        if second.current_hp > 0:
            if self.check_status_before_attack(second):
                self.player_attack(second, second_attack, first)
        
        if second.current_hp == 0:
            print(f"{second.name} est K.O. !")
            defeated_team = self.team1 if second == self.active1 else self.team2
            team_id = 1 if second == self.active1 else 2
            if self.is_team_defeated(defeated_team):
                if self.check_battle_end():
                    return
            else:
                self.auto_switch(team_id)

        if first.current_hp == 0:
            print(f"{first.name} est K.O. !")
            defeated_team = self.team1 if first == self.active1 else self.team2
            team_id = 1 if first == self.active1 else 2
            if self.is_team_defeated(defeated_team):
                if self.check_battle_end():
                    return
            else:
                self.auto_switch(team_id)


        # Effet de Leech Seed à la fin du tour
        for pokemon in [self.active1, self.active2]:
            if pokemon.leech_seeded_by and pokemon.current_hp > 0:
                drained = max(1, pokemon.max_hp // 8)
                pokemon.current_hp = max(0, pokemon.current_hp - drained)
                seeder = pokemon.leech_seeded_by
                if seeder.current_hp > 0:
                    seeder.current_hp = min(seeder.max_hp, seeder.current_hp + drained)
                print(f"{pokemon.name} perd {drained} PV à cause de Graine ! {seeder.name} les récupère.")

        
        self.next_turn()


    ### Savoir la probabilité de toucher une attaque ###
    def calculate_hit_chance(self, attacker, defender, attack):
        """
        Calcule si l'attaque touche en tenant compte de la précision de l'attaque,
        de la précision de l'attaquant et de l'évasion du défenseur.
        """
        base_accuracy = attack.accuracy / 100.0
        effective_accuracy = base_accuracy * attacker.accuracy / defender.evasion
        return random.random() <= effective_accuracy
    
#### appliquer les degats des statuts ####
    def apply_status_damage(self, pokemon):
        """
        Applique les dégâts liés aux statuts persistants : burn, poison, etc.
        """
        if pokemon.status == "burn":
            dmg = int(pokemon.max_hp * 0.0625)
            print(f"{pokemon.name} souffre de sa brûlure ! Il perd {dmg} PV.")
            self.damage_method(pokemon, dmg)
        elif pokemon.status == "poison":
            dmg = int(pokemon.max_hp * 0.125)
            print(f"{pokemon.name} est empoisonné ! Il perd {dmg} PV.")
            self.damage_method(pokemon, dmg)
        elif pokemon.status == "badly_poisoned":
            if not hasattr(pokemon, "toxic_counter"):
                pokemon.toxic_counter = 1
            dmg = int(pokemon.max_hp * 0.0625 * pokemon.toxic_counter)
            print(f"{pokemon.name} est gravement empoisonné ! Il perd {dmg} PV.")
            self.damage_method(pokemon, dmg)
            pokemon.toxic_counter += 1

    def check_status_before_attack(self, attacker: pokemon) -> bool:
        """
        Vérifie si le Pokémon peut agir selon son statut.
        Retourne True s'il peut attaquer, False sinon.
        """
        if attacker.status == "sleep":
            if attacker.sleep_counter > 0:
                print(f"{attacker.name} dort encore ({attacker.sleep_counter} tour(s) restant).")
                attacker.sleep_counter -= 1
                return False
            else:
                print(f"{attacker.name} se réveille !")
                attacker.remove_status()
                return True

        if attacker.status == "freeze":
            if random.random() < 0.2:  # 20% chance de dégeler
                print(f"{attacker.name} dégèle !")
                attacker.remove_status()
                return True
            else:
                print(f"{attacker.name} est gelé et ne peut pas bouger.")
                return False

        if attacker.status == "paralyze":
            if random.random() < 0.25:
                print(f"{attacker.name} est paralysé ! Il ne peut pas attaquer.")
                return False

        if attacker.flinched:
            print(f"{attacker.name} est paralysé par la peur et ne peut pas attaquer.")
            attacker.flinched = False
            return False
        
        return True
    
#### Activer l'item du pokemon ####
    
    def trigger_held_item(self, pokemon):
        """
        Applique l'effet de l'objet tenu si applicable.
        """
        item = pokemon.item
        if not item:
            return

        if item in item_effects:
            item_effects[item](pokemon, self)




#
# Ensemble des fonctions pour gérer la puissance d'une attaque contre un autre pokémon.
# Utilisées dans la méthode attack_power de la classe Fight.
#

def type_effectiveness(attack_type, target_types):
    modifier = 1.0
    for t in target_types:
        modifier *= donnees.type_chart[donnees.POKEMON_TYPES_ID[attack_type]][donnees.POKEMON_TYPES_ID[t]]
    return modifier

#### Gerer le STAB ####
def is_stab(pokemon : pokemon, attack : Attack):
    if attack.type in pokemon.types:
        return 1.5
    else:
        return 1.0

#### Regarder si c'est un coup critique ####
import random

def is_critical_hit(pokemon, attack, target):
    """
    Détermine si une attaque est un coup critique.
    
    :param pokemon: Attaquant (instance de Pokemon)
    :param attack: Instance d'une classe Attack
    :param target: Défenseur (instance de Pokemon)
    :return: True si coup critique, False sinon
    """
    
    # 1. Cas d'un crit garanti (ex: Flower Trick)
    if getattr(attack, "guaranteed_crit", False):
        return True

    # 2. Cas où le talent de la cible bloque les coups critiques
    if target.talent in {"Shell Armor", "Battle Armor"}:
        return False

    # 3. Calcul du niveau de taux critique (crit stage)
    crit_stage = 1  # par défaut

    # Bonus d'attaque : taux critique augmenté
    if hasattr(attack, "critical_chance") and attack.critical_chance > 6.25:
        crit_stage += 1

    # Objet augmentant le taux de crit
    if pokemon.item in {"Scope Lens", "Razor Claw"}:
        crit_stage += 1

    # Talent Super Luck
    if pokemon.talent == "Super Luck":
        crit_stage += 1

    # Bonus personnalisé (ex: Laser Focus, effets custom)
    if hasattr(pokemon, "power") and pokemon.power:
        crit_stage += 2

    # 4. Table officielle des chances critiques
    CRIT_RATES = {
        0: 0.0,
        1: 0.0625,  # 1/16
        2: 0.125,   # 1/8
        3: 0.25,    # 1/4
        4: 0.333,   # 1/3
        5: 0.5,
        6: 1.0
    }

    chance = CRIT_RATES.get(min(crit_stage, 6), 1.0)
    return random.random() < chance

#### Regarder si le terrain booste l'attaque ####
def attack_terrain_boost(attack : Attack, fight : Fight):
    """
    Applique les modificateurs de puissance des attaques en fonction du terrain.
    :param attack: Instance de la classe Attack.
    :param fight: Instance de la classe Fight contenant toutes les informations sur le combat, y compris le terrain actuel.
    :return: Modificateur de puissance des attaques en fonction du terrain.
    """
    match fight.field_effects, attack.type:
        case (["Grassy Terrain"], "Grass"):
            return 1.3
        case (["Electric Terrain"], "Electric"):
            return 1.3
        case (["Psychic Terrain"], "Psychic"):
            return 1.3
        case (["Misty Terrain"], "Dragon"):
            return 0.5
        case _ :
            return 1.0  # Pas de boost si le terrain ne correspond pas à l'attaque ou s'il n'y a pas d'effet de terrain actif
        
#### Regarder si le Pokémon en face tient une baie qui le fait resister à l'attaque ####
def berry_boost(pokemon, attack : Attack):
    """
    Placeholder pour l'effet de la baie, si applicable, si le pokémon tient une baie qui réduit les dégâts de l'attaque si celle-ci est super efficace.
    :param pokemon: Instance de la classe Pokemon qui attaque.
    :param attack: Instance de la classe Attack.
    :return: Modificateur de puissance des attaques en fonction de la baie.
    """

    item = pokemon.item
    if item is None:
        return 1.0
    berry = str.split(item, "_")
    if len(berry) > 1 and berry[1] != "berry":
        return 1.0
    else:
        return 1.0    # sera implémenté plus tard

#### Regarder si la météo booste l'attaque ####
def attack_weather_boost(attack : Attack, fight):
    """
    Applique les modificateurs de puissance des attaques en fonction de la météo.

    :param attack: Instance de la classe Attack.
    :param fight: Instance de la classe Fight contenant toutes les informations sur le combat, y compris la météo actuelle.
    :return: Modificateur de puissance des attaques en fonction de la météo.
    """
    match fight.weather["current"], attack.type:
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

#### Regarder si le Pokémon est brûlé ####
def is_burned(pokemon):
    if pokemon.status != "burn":
        return False
    else:
        return True
    
#### Attaque de confusion ####
def confusion_attack(pokemon : pokemon):
    """
    Gère l'attaque subit lorsqu'un pokémon est confus, il s'agit d'une attaque de type Normal (qui n'est pas affecté par les types ni le stab)
    et qui a 40 de puissance de base. La formule de calcul est donc la suivante :
    ((base_power * (attack_stat / defense_stat)) + 1) 
    """
    damage = int(((40 * (pokemon.current_stats()['Attack'] / pokemon.current_stats()['Defense'])) + 1))
    return damage

def screen_effect(attack : Attack, fight : Fight):
    """
    Applique l'effet de l'écran de protection actif.
    
    :param attack: Instance de la classe Attack.
    :param fight: Instance de la classe Fight contenant les informations sur les écrans actifs.
    :return: Facteur de réduction des dégâts.
    """ 
    if 'light_screen' in fight.screen and attack.category == "Special":
        return 0.5
    elif 'reflect' in fight.screen and attack.category == "Physical":
        return 0.5
    elif 'aurora veil' in fight.screen:
        return 0.5
    else:
        return 1.0