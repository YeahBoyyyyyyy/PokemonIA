from pokemon import pokemon, apply_stat_changes
import random 
import utilities 
from IA.pokemon_ia import PokemonAI
from colors_utils import Colors as bcolors
from Materials.pokemon_items import trigger_item, item_registry
from Materials.pokemon_talents import trigger_talent
from Materials.pokemon_attacks import Attack, process_future_sight_attacks

class Fight():
    def __init__(self, team1 : list[pokemon], team2 : list[pokemon]):
        self.team1 = team1  # Liste de 6 pokémon
        self.team2 = team2
        self.active1 = team1[0] # Pokémon actuellement en combat
        self.active2 = team2[0]

####### Effets de combats : Terrain, Météo, Murs, Hazards #######

        ## Météo ##
        self.weather = {"current" : None, "previous" : None}  # Météo actuelle (par exemple : "Ensoleillé", "Pluvieux", etc.) sera un dictionnaire 
        # contenant la météo actuelle et la météo du tour précédent pour savoir si la météo est la même que la précédente
        self.weather_turn_left = None  # Nombre de tours restants pour la météo actuelle, si elle est active
        # Peut juste être un entier puisqu'il n'y a qu'une seule météo active à la fois

        ## Terrain ##
        self.field = None  # Effets de terrain actifs (par exemple : "Champ Electrique", "Champ Herbu", etc.) sera juste une chaine de caractères
        self.field_turn_left = None  # Nombre de tours restants pour le terrain actuel, si il est actif
        # Peut être juste un entier vu que un seul terrain peut être actif à la fois

        ## Hazards ##
        self.hazards_team1 = {"Spikes" : 0, "Toxic Spikes" : 0, "Stealth Rock" : False, "Sticky Web" : False}  # Dangers actifs pour l'équipe 1
        self.hazards_team2 = {"Spikes" : 0, "Toxic Spikes" : 0, "Stealth Rock" : False, "Sticky Web" : False}  # Dangers actifs pour l'équipe 2

        ## Murs de protection ##
        self.screen_team1 = []  # Écrans de protection actifs pour l'équipe 1
        self.screen_team2 = []  # Écrans de protection actifs pour l'équipe 2
        self.screen_turn_left_team1 = {}  # Nombre de tours restants pour les écrans de l'équipe 1
        self.screen_turn_left_team2 = {}  # Nombre de tours restants pour les écrans de l'équipe 2

        self.turn = 0  # Compteur de tours pour suivre le nombre de tours écoulés dans le combat

        ## Shed Tail substitute en attente ##
        self.pending_substitute_team1 = 0  # Substitute en attente pour l'équipe 1
        self.pending_substitute_team2 = 0  # Substitute en attente pour l'équipe 2

        ## Tailwind
        self.tailwind_team1 = 0
        self.tailwind_team2 = 0

        ## Trick Room - inverse l'ordre de vitesse
        self.trick_room_active = False
        self.trick_room_turns_left = 0

        ## Talents de ruine actifs ##
        self.ruin_effects_active = {
            "Sword of Ruin": False,
            "Tablets of Ruin": False, 
            "Vessel of Ruin": False,
            "Beads of Ruin": False
        }

        """
        self.check_ability_weather(self.active1)
        self.check_ability_weather(self.active2)
        """

        self.set_fight_attribute()

        trigger_talent(self.active1, "on_entry", self)
        trigger_talent(self.active2, "on_entry", self)
        trigger_item(self.active1, "on_entry", self)
        trigger_item(self.active2, "on_entry", self)
        
        for p in [self.active1, self.active2]:
            p.actualize_stats()  # Met à jour les stats des Pokémon actifs au début du combat

    def get_active_pokemon(self, team_id):
        """
        Récupère le Pokémon actif d'une équipe.
        """
        if team_id == 1:
            return self.active1
        elif team_id == 2:
            return self.active2
        return None
    
    def get_enemy_pokemon(self, team_id):
        """
        Récupère le Pokémon ennemi d'une équipe.
        """
        if team_id == 1:
            return self.active2
        elif team_id == 2:
            return self.active1
        return None

    def set_fight_attribute(self):
        for poke in self.team1 + self.team2:
            poke.init_fight(self)

    ##### Gerer les switch #######
    def handle_switch(self, team_id, forced=False, pokemon_index=None):
        """
        Gère tous les types de changements de Pokémon : automatique, forcé ou par choix.
        
        :param team_id: ID de l'équipe (1 ou 2)
        :param forced: Si True, c'est un changement forcé (KO, U-turn, etc.)
        :param pokemon_index: Index du Pokémon à faire entrer (None = choix automatique/manuel)
        :return: Index du Pokémon qui entre, ou None si impossible
        """
        team = self.team1 if team_id == 1 else self.team2
        current_active = self.active1 if team_id == 1 else self.active2
        team_name = "joueur 1" if team_id == 1 else "joueur 2"
        
        # Vérifier si c'est un changement forcé par U-turn
        is_uturn_switch = (hasattr(current_active, 'must_switch_after_attack') and 
                        current_active.must_switch_after_attack and 
                        current_active.current_hp > 0)
        
        # Obtenir la liste des Pokémon disponibles
        available_pokemon = []
        for i, p in enumerate(team):
            if p.current_hp > 0 and p != current_active:
                available_pokemon.append((i, p))
        
        if not available_pokemon:
            return None  # Aucun Pokémon disponible
        
        # Déterminer l'index du Pokémon à faire entrer
        switch_index = None
        
        if pokemon_index is not None:
            # Index spécifié directement (IA ou choix prédéfini)
            if any(i == pokemon_index for i, _ in available_pokemon):
                switch_index = pokemon_index
            else:
                print(f"ERREUR: Pokémon #{pokemon_index} non disponible !")
                return None
        
        elif team_id == 2:  # IA - choix automatique
            switch_index = available_pokemon[0][0]  # Premier Pokémon disponible
        
        else:  # team_id == 1 - Joueur humain - choix manuel
            switch_index = self._get_player_choice(available_pokemon, team_name, forced, is_uturn_switch)
        
        # Effectuer le changement
        if switch_index is not None:
            self.player_switch(team_id, switch_index)
            return switch_index
        
        return None

    def _get_player_choice(self, available_pokemon, team_name, forced, is_uturn_switch):
        """
        Gère le choix du joueur humain pour le changement de Pokémon.
        """
        # Afficher le message approprié
        if forced and not is_uturn_switch:
            print(f"\n{bcolors.OKYELLOW}Le Pokémon du {team_name} est KO ! Choisissez un remplaçant :{bcolors.RESET}")
        elif is_uturn_switch:
            print(f"\n{bcolors.OKBLUE}Choisissez le Pokémon à faire entrer :{bcolors.RESET}")
        
        # Boucle de choix pour le joueur humain
        while True:
            print("\nPokémon disponibles :")
            for idx, (i, p) in enumerate(available_pokemon):
                print(f"{idx}. {p.name} (HP: {p.current_hp}/{p.max_hp})")
            
            choice = input("Choisissez un Pokémon (numéro) : ").strip()
            
            if choice.isdigit():
                choice_idx = int(choice)
                if 0 <= choice_idx < len(available_pokemon):
                    return available_pokemon[choice_idx][0]
                else:
                    print("Choix invalide.")
            else:
                print("Veuillez entrer un numéro valide.")

    def handle_forced_switches(self):
        """
        Gère les changements forcés après les attaques comme U-turn, Volt Switch, etc.
        """
        for team_id, active_pokemon in [(1, self.active1), (2, self.active2)]:
            if (hasattr(active_pokemon, 'must_switch_after_attack') and 
                active_pokemon.must_switch_after_attack and 
                active_pokemon.current_hp > 0):
                
                team = self.team1 if team_id == 1 else self.team2
                available_pokemon = [p for p in team if p.current_hp > 0 and p != active_pokemon]
                
                if available_pokemon:
                    switch_reason = getattr(active_pokemon, 'switch_reason', 'une attaque')
                    print(f"{active_pokemon.name} revient grâce to {switch_reason} !")
                    self.handle_switch(team_id, forced=False)  # U-turn n'est pas "forced" au sens KO
                
                # Réinitialiser les attributs
                active_pokemon.must_switch_after_attack = False
                if hasattr(active_pokemon, 'switch_reason'):
                    active_pokemon.switch_reason = None

    # Raccourcis pour compatibilité avec l'ancien code
    def auto_switch(self, team_id):
        """Changement automatique pour l'IA."""
        return self.handle_switch(team_id, forced=False)

    def choose_switch_pokemon(self, team_id):
        """Choix manuel de Pokémon pour remplacement KO."""
        return self.handle_switch(team_id, forced=True)

    def choose_uturn_switch_pokemon(self, team_id):
        """Choix manuel après U-turn/Volt Switch."""
        current_pokemon = self.active1 if team_id == 1 else self.active2
        if hasattr(current_pokemon, 'must_switch_after_attack'):
            current_pokemon.must_switch_after_attack = True
        return self.handle_switch(team_id, forced=False)


##### Vérifications fin de combat #######
    def is_team_defeated(self, team):
        """
        Vérifie si tous les Pokémon de l'équipe sont K.O.
        """
        return all(p.current_hp <= 0 for p in team)
    
    def check_battle_end(self):
        """
        Vérifie si le combat est terminé. Retourne True si oui, False sinon.
        Affiche aussi le gagnant.
        """
        if self.is_team_defeated(self.team1):
            if utilities.PRINTING_METHOD:
                print("Tous les Pokémon de l'équipe 1 sont K.O. ! Victoire de l'équipe 2 !")
            return True, 1
        elif self.is_team_defeated(self.team2):
            if utilities.PRINTING_METHOD:
                print("Tous les Pokémon de l'équipe 2 sont K.O. ! Victoire de l'équipe 1 !")
            return True, 2
        return False, None

###### Méthodes pour gérer les effets de la météo #######
    def set_weather(self, weather, duration=5):
        """
        Déclenche une météo avec une durée (par défaut 5 tours).

        :param weather: str, nom de la météo ("Sunny", "Rain", etc.)
        :param duration: int, nombre de tours pendant lesquels la météo est active
        :return: Change la météo
        """
        self.weather["previous"] = self.weather["current"]
        self.weather["current"] = weather
        if duration is not None:
            self.weather_turn_left = duration
        else:
            self.weather_turn_left = None  # Infini
        
        for p in [self.active1, self.active2]:
            trigger_talent(p, "modify_stat", self)
        self.weather_boost_modifier()
        
        if utilities.PRINTING_METHOD:
            print(f"La météo change : {weather} pendant {duration} tours.")

    def apply_weather_effects(self):
        """
        Applique les effets de la météo actuelle sur les Pokémon.
        Et notamment les degats infligés par la tempete de sable et la neige aux Pokémon non-Roche/Acier/Sol et non-Glace.
        """
        weather = self.weather['current']
        if not weather:
            return
            
        active_pokemon = [self.active1, self.active2]
        
        if weather == "Sandstorm":
            immune_types = {"Rock", "Steel", "Ground"}
            immune_talents = {"Sand Veil", "Overcoat", "Magic Guard"}
            for pokemon in active_pokemon:
                if not any(t in immune_types for t in pokemon.types) or pokemon.talent in immune_talents:
                    damage = int(pokemon.max_hp * 0.0625)
                    self.damage_method(pokemon, damage, True)
        elif weather == "Snow":
            for pokemon in active_pokemon:
                if pokemon.talent == "Ice Body" and not getattr(pokemon, 'heal_blocked', False):
                    heal_amount = int(pokemon.max_hp * 0.0625)
                    self.damage_method(pokemon, -heal_amount, True)
                elif "Ice" not in pokemon.types or pokemon.talent == "Magic Guard":
                    damage = int(pokemon.max_hp * 0.0625)
                    self.damage_method(pokemon, damage, True)
        elif weather == "Rain":
            for pokemon in active_pokemon:
                self._apply_rain_effects(pokemon)
        elif weather == "Sunny":
            for pokemon in active_pokemon:
                if pokemon.talent == "Dry Skin":
                    damage = int(pokemon.max_hp * 0.125)
                    self.damage_method(pokemon, damage, True)
    
    def _apply_rain_effects(self, pokemon):
        """Applique les effets spécifiques de la pluie sur un Pokémon"""
        if pokemon.talent == "Rain Dish" and not getattr(pokemon, 'heal_blocked', False):
            heal_amount = int(pokemon.max_hp * 0.0625)
            self.damage_method(pokemon, -heal_amount, True)
        elif pokemon.talent == "Rain Dish" and getattr(pokemon, 'heal_blocked', False):
            print(f"{pokemon.name} ne peut pas bénéficier de Rain Dish à cause de Heal Block !")
        
        if pokemon.talent == "Dry Skin" and not getattr(pokemon, 'heal_blocked', False):
            heal_amount = int(pokemon.max_hp * 0.125)
            self.damage_method(pokemon, -heal_amount, True)
        elif pokemon.talent == "Dry Skin" and getattr(pokemon, 'heal_blocked', False):
            print(f"{pokemon.name} ne peut pas bénéficier de Dry Skin à cause de Heal Block !")
                    
    def weather_boost_modifier(self):
        """
        Applique les changements de stats en fonction de la météo
        """
        for pokemon in [self.active1, self.active2]:
            if self.weather["current"] == "Snow" and self.weather["previous"] != "Snow" and "Ice" in pokemon.types:
                pokemon.hidden_modifier["Sp. Def"] *= 1.5
            elif self.weather["previous"] == "Snow" and self.weather["current"] != "Snow" and "Ice" in pokemon.types:
                pokemon.hidden_modifier["Sp. Def"] /= 1.5
            elif self.weather["current"] == "Sandstorm" and self.weather["previous"] and "Rock" in pokemon.types:
                pokemon.hidden_modifier["Defense"] *= 1.5
            elif self.weather["previous"] == "Sandstorm" and self.weather["current"] != "Sandstorm" and "Rock" in pokemon.types:
                pokemon.hidden_modifier["Defense"] /= 1.5

    def weather_update(self):
        """
        Met à jour la météo : décrémente les tours restants et la retire si elle expire.
        """
        if self.weather_turn_left is not None:
            self.weather_turn_left -= 1
            self.weather['previous'] = self.weather['current']
            if self.weather_turn_left <= 0:
                if utilities.PRINTING_METHOD:
                    print(f"La météo {self.weather['current']} se dissipe.")
                self.weather['current'] = None
                self.weather_turn_left = None
        else:
            self.weather['previous'] = self.weather['current']
            self.weather['current'] = None
            
###### Méthodes pour gérer les effets de terrain #######
    def set_field(self, effect):
        self.field = effect
        self.field_turn_left = 5  
    
    def remove_field_effect(self):
        self.field = None  # Supprimer l'effet de terrain
        self.field_turn_left = None  # Réinitialiser le compteur de tours

    def actualize_field(self):
        """
        Met à jour les effets de terrain actifs en décrémentant le nombre de tours restants.
        Supprime les effets de terrain qui ont expiré.
        """
        if self.field_turn_left is not None:
            self.field_turn_left -= 1
            if self.field_turn_left <= 0:
                self.remove_field_effect()
    
    def apply_field(self):
        """
        Applique les effets de terrain actifs sur les Pokémon.
        Par exemple, si le terrain est herbeux, tous les Pokémons sur le terrain regagnent des PV à chaque tour.
        """
        if "Grassy Terrain" == self.field:
            # Regénérer des PV pour tous les Pokémon (bypass substitute car la guérison affecte directement le Pokémon)
            for pokemon in [self.active1, self.active2]:
                if not getattr(pokemon, 'heal_blocked', False):
                    heal_amount = int(pokemon.max_hp * 0.0625)  # Régénération de 1/16 des PV max
                    pokemon.current_hp = min(pokemon.max_hp, pokemon.current_hp + heal_amount)
                    if utilities.PRINTING_METHOD:
                        print(f"{pokemon.name} regagne {heal_amount} PV grâce au terrain herbeux !")
                else:
                    if utilities.PRINTING_METHOD:
                        print(f"{pokemon.name} ne peut pas bénéficier du terrain herbeux à cause de Heal Block !")

###### Méthodes pour gérer les screens et la gravité #######
    def add_screen(self, effect, team_id, turn_duration=5):
        if team_id == 1:
            self.screen_team1.append(effect)
            self.screen_turn_left_team1[effect] = turn_duration 
        elif team_id == 2:
            self.screen_team2.append(effect)
            self.screen_turn_left_team2[effect] = turn_duration

    def remove_screen(self, effect, team_id):
        if team_id == 1 and effect in self.screen_team1:
            self.screen_team1.remove(effect)
            del self.screen_turn_left_team1[effect]  # Supprimer l'effet de terrain et son compteur de tours
        elif team_id == 2 and effect in self.screen_team2:
            self.screen_team2.remove(effect)
            del self.screen_turn_left_team2[effect]
    
    def get_team_id(self, pokemon):
        """Retourne l'ID de l'équipe d'un Pokémon (1 ou 2)"""
        if pokemon in self.team1:
            return 1
        elif pokemon in self.team2:
            return 2
        else:
            return None
    
    def update_screens(self):
        """Met à jour les écrans de protection en décrémentant le nombre de tours restants"""
        # Équipe 1
        for effect in list(self.screen_turn_left_team1.keys()):
            self.screen_turn_left_team1[effect] -= 1
            if self.screen_turn_left_team1[effect] <= 0:
                self.remove_screen(effect, 1)
                if utilities.PRINTING_METHOD:
                    print(f"L'écran {effect} de l'équipe 1 a expiré.")
        
        # Équipe 2
        for effect in list(self.screen_turn_left_team2.keys()):
            self.screen_turn_left_team2[effect] -= 1
            if self.screen_turn_left_team2[effect] <= 0:
                self.remove_screen(effect, 2)
                if utilities.PRINTING_METHOD:
                    print(f"L'écran {effect} de l'équipe 2 a expiré.")

    def tailwind_update(self):
        self.tailwind_team1 = max(self.tailwind_team1 - 1, 0)
        self.tailwind_team2 = max(self.tailwind_team2 - 1, 0)

    def set_trick_room(self, duration=5):
        """
        Active ou désactive Trick Room.
        Si Trick Room est déjà actif, le désactive.
        Sinon, l'active pour la durée spécifiée.
        
        :param duration: Nombre de tours pendant lesquels Trick Room est actif (défaut: 5)
        """
        if self.trick_room_active:
            if utilities.PRINTING_METHOD:
                print("Trick Room se dissipe !")
            self.trick_room_active = False
            self.trick_room_turns_left = 0
        else:
            if utilities.PRINTING_METHOD:
                print("Les dimensions se tordent ! Trick Room est activé !")
            self.trick_room_active = True
            self.trick_room_turns_left = duration

    def trick_room_update(self):
        """
        Met à jour Trick Room : décrémente les tours restants et le désactive si expiré.
        """
        if self.trick_room_active and self.trick_room_turns_left > 0:
            self.trick_room_turns_left -= 1
            if self.trick_room_turns_left <= 0:
                if utilities.PRINTING_METHOD:
                    print("Trick Room se dissipe !")
                self.trick_room_active = False

    def damage_method(self, pokemon : pokemon, damage : int, bypass_substitute=False, is_draining=False):
        """
        Applique les dégâts à un Pokémon.

        :param pokemon: Instance de la classe Pokemon qui subit les dégâts.
        :param damage: Dégâts à infliger.
        :param bypass_substitute: Si True, ignore le clone (pour les attaques authentic).
        :param is_draining: Si True, l'attaque draine des PV (mais pas du clone selon les règles officielles).
        :return: Les dégâts réellement infligés. 0 si l'attaque drainante touche un clone.
        """
        actual_damage = damage
        
        # Si le Pokémon a un clone et l'attaque ne l'ignore pas, le clone intercepte les dégâts
        if pokemon.has_substitute() and not bypass_substitute:
            pokemon.substitute_hp -= damage
            if pokemon.substitute_hp <= 0:
                actual_damage = pokemon.substitute_hp + damage  # Dégâts effectivement absorbés par le clone
                pokemon.substitute_hp = 0
                if utilities.PRINTING_METHOD:
                    print(f"Le clone de {pokemon.name} est détruit !")
                # Les dégâts en surplus ne sont pas transférés au Pokémon
            else:
                if utilities.PRINTING_METHOD:
                    print(f"Le clone de {pokemon.name} absorbe {damage} dégâts ! ({pokemon.substitute_hp} PV restants)")
            
            # Règle officielle : les attaques drainantes ne peuvent pas drainer des PV d'un clone
            if is_draining:
                if utilities.PRINTING_METHOD:
                    print(f"L'attaque drainante ne peut pas récupérer de PV du clone !")
                return 0  # Aucun PV récupéré pour l'attaquant
            
            return actual_damage  # Retourner les dégâts infligés au clone pour les autres cas
        
        # Sinon, appliquer les dégâts normalement
        pokemon.current_hp -= damage

        # Incrémenter le compteur Rage Fist si le Pokémon est touché directement
        if damage > 0 and hasattr(pokemon, 'nb_of_hit'):
            pokemon.nb_of_hit += 1
        
        # Vérification du talent Sturdy
        if hasattr(pokemon, 'sturdy_activated') and pokemon.sturdy_activated and pokemon.current_hp <= 0:
            pokemon.current_hp = 1
            pokemon.sturdy_activated = False
            if utilities.PRINTING_METHOD:
                print(f"{pokemon.name} survit avec 1 PV grâce à Fermeté !")
        # Vérification de la Ceinture Force (Focus Sash)
        elif (pokemon.current_hp <= 0 and pokemon.item == "Focus Sash" and 
              hasattr(pokemon, 'focus_sash_ready') and pokemon.focus_sash_ready):
            pokemon.current_hp = 1
            pokemon.focus_sash_ready = False
            pokemon.item = None  # La Ceinture Force est consommée
            if utilities.PRINTING_METHOD:
                print(f"{pokemon.name} survit grâce à sa Ceinture Force ! Il reste à 1 PV.")
        elif pokemon.current_hp < 0:
            pokemon.current_hp = 0
        elif pokemon.current_hp > pokemon.max_hp:
            pokemon.current_hp = pokemon.max_hp
        
        # Si le Pokémon est KO, supprimer ses effets de ruine
        if pokemon.current_hp <= 0:
            self.remove_ruin_effects(pokemon)
            # Gestion Moxie: identifier l'attaquant potentiel (l'autre actif)
            attacker = None
            if pokemon == self.active1:
                attacker = self.active2
            elif pokemon == self.active2:
                attacker = self.active1
            if attacker and getattr(attacker, 'talent', None) == 'Moxie':
                try:
                    from pokemon import apply_stat_changes
                    if attacker.current_hp > 0:  # Toujours vivant
                        changed = apply_stat_changes(attacker, {"Attack": 1}, "self", self)
                        if changed:
                            print(f"L'Attaque de {attacker.name} augmente grâce à Moxie !")
                except Exception as e:
                    print(f"Erreur application Moxie: {e}")
            
        return actual_damage

    ## Printing methods pour debugger
    def print_fight_status(self):
        if utilities.PRINTING_METHOD:
            print(f"{bcolors.BOLD}====================Tour {self.turn + 1}===================={bcolors.RESET}")
            display_pokemon(self.active1)
            if self.active1.has_substitute():
                print(f"   Clone: {self.active1.substitute_hp} PV")
            display_pokemon(self.active2)
            if self.active2.has_substitute():
                print(f"   Clone: {self.active2.substitute_hp} PV")
            display_wall(self)
            # Afficher les effets de terrain s'il y en a
            if self.field and self.field_turn_left:
                print(f"Effet de terrain actif: {self.field} ({self.field_turn_left} tours restants)")
            
            # Afficher Trick Room s'il est actif
            if self.trick_room_active:
                print(f"{bcolors.OKMAGENTA}Trick Room actif ! ({self.trick_room_turns_left} tours restants){bcolors.RESET}")
            
            print(f"{bcolors.RESET}", end="")
            display_hazards(self)
            display_weather(self)
            print(f"1:{self.active1.protect_turns} / 2:{self.active2.protect_turns}")

    def print_fight(self):
        if utilities.PRINTING_METHOD:
            print(f"{bcolors.BG_WHITE}{bcolors.BOLD}{bcolors.BLACK}Le combat oppose {self.active1.name} à {self.active2.name} !{bcolors.RESET}{bcolors.UNBOLD}{bcolors.BG_DEFAULT}")

    def next_turn(self, ia1, ia2):
        """
        Passe au tour suivant du combat.
        Incrémente le compteur de tours et applique les effets de terrain et de météo.
        """
        
        # Appliquer les effets de fin de tour AVANT d'incrémenter le tour
        # Effet de Leech Seed à la fin du tour
        for pokemon in [self.active1, self.active2]:
            if pokemon.leech_seeded_by and pokemon.current_hp > 0:
                drained = max(1, pokemon.max_hp // 8)
                pokemon.current_hp = max(0, pokemon.current_hp - drained)
                seeder = pokemon.leech_seeded_by
                if seeder.current_hp > 0:
                    if seeder.item == "Big Root":
                        actual_healing = int(drained * 1.3)
                    if pokemon.talent == "Liquid Ooze":
                        seeder.current_hp -= actual_healing
                        if utilities.PRINTING_METHOD:
                            print(f"{pokemon.name} inflige {actual_healing} PV de dégâts à {seeder.name} avec Liquid Ooze !")
                    else:
                        seeder.current_hp += actual_healing
                        if utilities.PRINTING_METHOD:
                            print(f"{pokemon.name} perd {drained} PV à cause de Graine ! {seeder.name} les récupère.")
                        seeder.current_hp = min(seeder.max_hp, seeder.current_hp + drained)
                
        
        # Vérifier les Pokémon K.O. avant les effets de fin de tour car les Leftovers ne peuvent pas resurrecter un Pokémon K.O.
        if self.active1.current_hp <= 0:
            self.new_handle_ko_replacement(self.active1, ia1)
        
        if self.active2.current_hp <= 0:
            self.new_handle_ko_replacement(self.active2, ia2)

        for p in [self.active1, self.active2]:
            self.apply_status_damage(p)  # Appliquer les dégâts liés aux statuts persistants
            if p.current_hp > 0:
                trigger_item(p, "on_turn_end", self)  # Appliquer les effets des objets à la fin du tour
                trigger_talent(p, "on_turn_end", self)  # Appliquer les effets des talents à la fin du tour
            if p.flinched:
                p.flinched = False  # Réinitialiser le statut de flinch à la fin du tour

        self.turn += 1
        self.weather_update()
        
        # Appliquer les effets de terrain et de météo
        self.apply_weather_effects()
        self.weather_boost_modifier()

        if self.weather['current'] == "Sunny":
            if utilities.PRINTING_METHOD:
                print(f"{bcolors.OKRED}Le soleil brille ! Les attaques de type Feu sont boostées.{bcolors.RESET}")
        elif self.weather['current'] == "Rain":
            if utilities.PRINTING_METHOD:
                print(f"{bcolors.OKBLUE}Il pleut ! Les attaques de type Eau sont boostées.{bcolors.RESET}")
        elif self.weather['current'] == "Sandstorm":
            if utilities.PRINTING_METHOD:
                print(f"{bcolors.OKYELLOW}Une tempête de sable souffle ! Les Pokémon du mauvais type subissent des dégâts.{bcolors.RESET}")
        elif self.weather['current'] == "Snow":
            if utilities.PRINTING_METHOD:
                print(f"{bcolors.OKCYAN}Il neige ! Les Pokémon du mauvais type subissent des dégâts.{bcolors.RESET}")

        # Gérer les effets de terrain
        self.apply_field()
        self.actualize_field()  # Décrémenter le compteur du terrain
        
        # Gérer les écrans de protection
        self.update_screens()
        
        # Gérer tailwind
        self.tailwind_update()
        
        # Gérer Trick Room
        self.trick_room_update()

        for p in [self.active1, self.active2]:
            trigger_talent(p, "modify_stat", self)
            
            # Décrémenter les effets de durée limitée
            if p.taunted_turns > 0:
                p.taunted_turns -= 1
                if p.taunted_turns == 0:
                    if utilities.PRINTING_METHOD:
                        print(f"L'effet de Taunt sur {p.name} se dissipe !")
            
            if p.encored_turns > 0:
                p.encored_turns -= 1
                if p.encored_turns == 0:
                    if utilities.PRINTING_METHOD:
                        print(f"L'effet d'Encore sur {p.name} se dissipe !")
                    p.encored_attack = None
            
            p.has_attacked_or_switched = False

            # Restaurer le type Vol perdu par Roost à la fin du tour
            if hasattr(p, 'lost_flying_from_roost') and p.lost_flying_from_roost:
                if hasattr(p, 'original_types'):
                    p.types = p.original_types.copy()  # Restaurer les types originaux
                p.lost_flying_from_roost = False
                if utilities.PRINTING_METHOD:
                    print(f"{p.name} récupère son type Vol !")

            if hasattr(p, 'original_weight'):
                self.weight = self.original_weight  # Restaure le poids original si modifié

        # Traiter les attaques Future Sight programmées
        process_future_sight_attacks(self)
        
###### Actions ######

    def player_switch(self, team: int, index: int):
        """
        Change le Pokémon actif dans l'équipe.
        :param team: 1 ou 2 selon le joueur
        :param index: index du Pokémon dans l'équipe (0 à 5)
        """
        if team == 1:
            if self.team1[index].current_hp > 0:
                if utilities.PRINTING_METHOD:
                    print(f"{self.active1.name} est remplacé par {self.team1[index].name} !")
                
                # Déclencher on_exit pour le Pokémon qui sort (Regenerator, etc.)
                trigger_talent(self.active1, "on_exit", self)
                
                # Supprimer les effets de ruine du Pokémon qui sort
                self.remove_ruin_effects(self.active1)
                
                self.active1.reset_stats_nd_status()  # Réinitialiser les stats et les effets de statut du Pokémon actif
                self.active1 = self.team1[index]
                # self.active1.init_fight(self)  # Initialiser l'attribut fight
                
                # Appliquer le substitute de Shed Tail si en attente
                if hasattr(self, 'pending_substitute_team1') and self.pending_substitute_team1 > 0:
                    self.active1.substitute_hp = self.pending_substitute_team1
                    if utilities.PRINTING_METHOD:
                        print(f"{self.active1.name} hérite du clone avec {self.pending_substitute_team1} PV !")
                    self.pending_substitute_team1 = 0  # Reset

                self.active1.has_attacked_or_switched = True

                trigger_item(self.active1, "on_entry", self)
                trigger_talent(self.active1, "on_entry", self)
                self.on_entry_hazards(self.active1)
                

        elif team == 2:
            if self.team2[index].current_hp > 0:
                if utilities.PRINTING_METHOD:
                    print(f"{self.active2.name} est remplacé par {self.team2[index].name} !")
                
                # Déclencher on_exit pour le Pokémon qui sort (Regenerator, etc.)
                trigger_talent(self.active2, "on_exit", self)
                
                # Supprimer les effets de ruine du Pokémon qui sort
                self.remove_ruin_effects(self.active2)
                
                self.active2.reset_stats_nd_status()  # Réinitialiser les stats et les effets de statut du Pokémon actif
                self.active2 = self.team2[index]
                # self.active2.init_fight(self)  # Initialiser l'attribut fight

                # Appliquer le substitut de Shed Tail si en attente
                if hasattr(self, 'pending_substitute_team2') and self.pending_substitute_team2 > 0:
                    self.active2.substitute_hp = self.pending_substitute_team2
                    if utilities.PRINTING_METHOD:
                        print(f"{self.active2.name} hérite du clone avec {self.pending_substitute_team2} PV !")
                    self.pending_substitute_team2 = 0  # Reset
                
                self.active2.has_attacked_or_switched = True

                trigger_item(self.active2, "on_entry", self)
                trigger_talent(self.active2, "on_entry", self)
                self.on_entry_hazards(self.active2)       

    def player_attack(self, attacker : pokemon, attack : Attack, defender : pokemon, defender_attack : Attack = None):
        """
        Gère l'action "Attaquer" d'un Pokémon sur un autre, en prenant en compte les effets de statut, multi-tours et priorités.
        """
        from Materials.pokemon_attacks import Struggle
    
        # --- Sleep Talk handling ---
        if attack.name == "Sleep Talk":
            # Only usable if the user is actually asleep
            if attacker.status != "sleep":
                if utilities.PRINTING_METHOD:
                    print(f"{attacker.name} n'est pas endormi : Sleep Talk échoue ! + nombre pp Sleep Talk: {attacker.get_attack_pp(attack)}")
                    pp_cost = 1
                    # Vérifier si l'adversaire a le talent Pressure (augmente la consommation de PP)
                    if hasattr(defender, 'talent') and defender.talent == "Pressure":
                        pp_cost = 2
                        if utilities.PRINTING_METHOD:
                            print(f"{defender.name}'s Pressure increases PP consumption!")
                    # Consommer les PP
                    booleen_inutile = attacker.use_pp(attack, pp_cost)
                return
            candidate_attacks = [attacker.attack1, attacker.attack2, attacker.attack3, attacker.attack4]
            # Filter: existing, not Sleep Talk itself, not charging moves, has PP > 0
            usable_for_sleep_talk = [a for a in candidate_attacks if a and a.name != "Sleep Talk" and "charge" not in a.flags and attacker.get_attack_pp(a) > 0]
            if not usable_for_sleep_talk:
                if utilities.PRINTING_METHOD:
                    print(f"{attacker.name} n'a aucune capacité utilisable via Sleep Talk !")
                    # Consommation des PP (sauf pour Struggle qui a des PP infinis)
                pp_cost = 1
                # Vérifier si l'adversaire a le talent Pressure (augmente la consommation de PP)
                if hasattr(defender, 'talent') and defender.talent == "Pressure":
                    pp_cost = 2
                    if utilities.PRINTING_METHOD:
                        print(f"{defender.name}'s Pressure increases PP consumption!")
                 # Consommer les PP
                if not attacker.use_pp(attack, pp_cost):
                    if utilities.PRINTING_METHOD:
                        print(f"ERREUR: {attacker.name} n'a pas assez de PP pour {attack.name} !")
                    attack = Struggle()  # Passer à Struggle si pas assez de PP
                return
            else:
                attack = random.choice(usable_for_sleep_talk)

        if attack.name != "Glaive Rush" and hasattr(attacker, "glaive_rush"):
            attacker.glaive_rush = False

        if defender.current_hp <= 0:
            if utilities.PRINTING_METHOD:
                print(f"{defender.name} est K.O. et ne peut pas être attaqué !")
            return

        # Si le Pokémon doit se recharger, il ne peut pas attaquer
        if attacker.must_recharge:
            if utilities.PRINTING_METHOD:
                print(f"{attacker.name} se repose et ne peut pas attaquer ce tour-ci.")
            attacker.must_recharge = False  # Réinitialiser après le tour de repos
            return

        # Gestion de l'effet Encore : force l'utilisation d'une attaque spécifique
        if attacker.encored_turns > 0 and attacker.encored_attack:
            if attack != attacker.encored_attack:
                if utilities.PRINTING_METHOD:
                    print(f"{attacker.name} est sous l'effet d'Encore et doit utiliser {attacker.encored_attack.name} !")
                attack = attacker.encored_attack  # Force l'utilisation de l'attaque encodée
            # Décrémenter le compteur d'Encore
            attacker.encored_turns -= 1
            if attacker.encored_turns == 0:
                if utilities.PRINTING_METHOD:
                    print(f"L'effet d'Encore sur {attacker.name} se dissipe !")
                attacker.encored_attack = None

        # Gestion de l'effet Taunt : empêche l'utilisation d'attaques de statut
        if attacker.is_taunted() and attack.category == "Status":
            if utilities.PRINTING_METHOD:
                print(f"{attacker.name} est provoqué et ne peut pas utiliser {attack.name} !")
            return  # L'attaque échoue
        
        if attacker.item == "Assault Vest" and attack.category == "Status":
            if utilities.PRINTING_METHOD:
                print(f"{attacker.name} ne peut pas utiliser d'attaque de Statut à cause de la Veste de Combat !")
            return

        # Si le Pokémon est confus, on gère la confusion
        if attacker.is_confused:
            if attacker.still_confused:
                if random.random() < 0.33:
                    if utilities.PRINTING_METHOD:
                        print(f"{attacker.name} est confus et se blesse lui-même !")
                    damage = confusion_attack(attacker)
                    self.damage_method(attacker, damage, True)
                    if random() < 0.33: # Le Pokémon ne sera plus confus au prochain tour 1/3 chance
                        attacker.is_confused = False
                    return
            elif attacker.still_confused == False and attacker.is_confused:
                if utilities.PRINTING_METHOD:
                    print(f"{attacker.name} n'est plus confus !")
                attacker.is_confused = False

        # Si le Pokémon est en recharge ou charge, on gère cela
        charging_result = None
        if attacker.charging:
            if attacker.charging_attack == attack:
                if utilities.PRINTING_METHOD:
                    print(f"{attacker.name} lance la deuxième phase de {attack.name} !")
                # Laisser l'attaque gérer la logique de fin de charge via apply_effect
                if hasattr(attack, 'apply_effect'):
                    charging_result = attack.apply_effect(attacker, defender, self)
            else:
                if utilities.PRINTING_METHOD:
                    print(f"{attacker.name} est en train de charger {attacker.charging_attack.name} et ne peut pas utiliser {attack.name} !")
                return
        elif "charge" in attack.flags:
            # Gestion moderne des attaques à charge avec apply_effect
            if hasattr(attack, 'apply_effect'):
                charging_result = attack.apply_effect(attacker, defender, self)
                if charging_result == "charging":
                    # L'attaque est en cours de charge
                    return
                # Si charging_result == "attack", continuer normalement
            else:
                # Gestion classique des attaques à charge (fallback)
                if attacker.item == "Power Herb":
                    if utilities.PRINTING_METHOD:
                        print(f"{attacker.name} utilise Power Herb et lance immédiatement {attack.name} !")
                    attacker.item = None  # Power Herb est consommé
                else:
                    if utilities.PRINTING_METHOD:
                        print(f"{attacker.name} charge {attack.name} et attaquera au prochain tour !")
                    attacker.charging = True
                    attacker.charging_attack = attack
                    return

        on_attack_mod = trigger_talent(attacker, "on_attack", attack, self)
        on_item_mod = trigger_item(attacker, "on_attack", attack, self)
        talent_mod_dict = trigger_talent(attacker, "on_attack", attack, self)

        if on_item_mod is None:
            on_item_mod = {"attack": 1.0, "power": 1.0, "accuracy" : 1.0}

        if on_attack_mod is None:
            on_attack_mod = {"attack": 1.0, "power": 1.0, "accuracy": 1.0, "type": None}

        if talent_mod_dict is None:
            talent_mod_dict = {"attack": 1.0, "power": 1.0, "accuracy": 1.0, "type": None}
        
        
        # Vérification Précision avec modificateurs
        if not self.calculate_hit_chance(attacker, defender, attack, talent_mod_dict, on_item_mod):
            if utilities.PRINTING_METHOD:
                print(f"{attacker.name} rate son attaque !")
            if attack.name in ["High Jump Kick", "Supercell Slam"]:
                attacker.current_hp //= 2
            return

        # --- Choice item lock logic (before announcing the move) ---
        if attacker.item and "Choice" in attacker.item and attack.name != "Struggle":
            # If the currently locked move has no PP left, release the lock
            if attacker.locked_attack and attacker.get_attack_pp(attacker.locked_attack) == 0:
                attacker.locked_attack = None
            if attacker.locked_attack and attacker.locked_attack != attack:
                if utilities.PRINTING_METHOD:
                    print(f"{attacker.name} est verrouillé sur {attacker.locked_attack.name} à cause de {attacker.item} !")
                attack = attacker.locked_attack
            if not attacker.locked_attack:
                attacker.locked_attack = attack

        if utilities.PRINTING_METHOD:
            print(f"{attacker.name} utilise {attack.name} !")

        # Consommation des PP (sauf pour Struggle qui a des PP infinis)
        if attack.name != "Struggle":
            pp_cost = 1
            # Vérifier si l'adversaire a le talent Pressure (augmente la consommation de PP)
            if hasattr(defender, 'talent') and defender.talent == "Pressure":
                pp_cost = 2
                if utilities.PRINTING_METHOD:
                    print(f"{defender.name}'s Pressure increases PP consumption!")
            
            # Consommer les PP
            if not attacker.use_pp(attack, pp_cost):
                if utilities.PRINTING_METHOD:
                    print(f"ERREUR: {attacker.name} n'a pas assez de PP pour {attack.name} !")
                attack = Struggle()  # Passer à Struggle si pas assez de PP
    
        if defender.protect:
            if utilities.PRINTING_METHOD:
                print(f"{bcolors.LIGHT_BLUE}{defender.name} se protège !{bcolors.RESET}")
            return

        # Verification attaques qui se lancent que au tour d'entrée du pokemon
        if hasattr(attack, 'on_condition_attack'):
            if not attack.on_condition_attack(attacker, defender, defender_attack, self):
                return

        # Vérification des talents défensifs seulement si l'attaque cible l'adversaire
        if attack.target == "Foe" or attack.target == "All Foes":
            multiplier = trigger_talent(defender, "on_defense", attack, attacker, self)
            if multiplier == 0:
                if utilities.PRINTING_METHOD:
                    print(f"{defender.name} n'est pas affecté grâce à son talent !")
                return 
            # Déclencher les objets on_defense pour le défenseur (ex: Covert Cloak)
            trigger_item(defender, "on_defense", attack, self)
        else:
            multiplier = 1.0  # Pas de modificateur défensif si l'attaque ne cible pas l'adversaire
        if multiplier == 0:
            if utilities.PRINTING_METHOD:
                print(f"{defender.name} n’est pas affecté grâce à son talent !")
            return 
        
        # Déclencher les objets before_attack pour le défenseur (ex: Focus Sash)
        trigger_item(defender, "before_attack", attack, self)
        
        # Calcul des dégâts (gestion spéciale pour les attaques multi-coups)
        dmg = self.handle_multi_hit_attack(attacker, attack, defender, on_attack_mod, on_item_mod, multiplier)
        health_before = defender.current_hp  # Pour les effets secondaires
        if dmg and not (hasattr(attack, 'multi_hit') and attack.multi_hit):
            # Pour les attaques normales, appliquer les dégâts ici
            # Pour les multi-coups, les dégâts sont déjà appliqués dans handle_multi_hit_attack
            self.apply_damage(dmg, defender, attack, attacker)
        if not health_before == None and defender.current_hp < health_before:
            if health_before - dmg < 0:
                dmg = health_before  # Si les dégâts dépassent les PV restants, ajuster au nombre de dégâts pour atteindre 0 PV

        # Effets secondaires de l'attaque (seulement si pas déjà appelé pour les attaques à charge)
        if charging_result != "attack":
            self.apply_secondary_effects(attacker, defender, attack, dmg if dmg else 0)

        # Restaurer les propriétés originales des attaques modifiables (comme Tera Blast)
        if hasattr(attack, 'restore_original_properties'):
            attack.restore_original_properties()

        # Enregistrer la dernière attaque utilisée (pour Encore et autres effets)
        attacker.last_used_attack = attack

        if not attacker.protect:
            attacker.protect_turns = 0  # Réinitialiser les tours de protection à chaque tour

        attacker.first_attack = False  # Réinitialiser le premier tour d'attaque
        attacker.has_attacked_or_switched = True

        # Nettoyer les attributs temporaires pour éviter les doubles activations de talents
        if hasattr(attacker, '_rough_skin_triggered'):
            delattr(attacker, '_rough_skin_triggered')
        if hasattr(defender, '_toxic_debris_triggered'):
            delattr(defender, '_toxic_debris_triggered')

    def apply_secondary_effects(self, attacker, defender, attack, damage_dealt=0):
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
            
            # Vérifier si l'attaque est bloquée par le substitut
            if self.is_blocked_by_substitute(attack, target):
                if utilities.PRINTING_METHOD:
                    print(f"{target.name} a un clone qui bloque {attack.name} !")
                return
            
            # Vérifier si les effets secondaires sont bloqués par Covert Cloak
            # Le Covert Cloak ne bloque que les effets qui ciblent le porteur de la cape
            if (attack.target == "Foe" and 
                "secondary_effect" in attack.flags and 
                target == defender and  # L'effet cible bien le défenseur
                hasattr(target, 'covert_cloak_protection') and 
                target.covert_cloak_protection):
                if utilities.PRINTING_METHOD:
                    print(f"Les effets secondaires de {attack.name} sont bloqués par le Covert Cloak de {target.name} !")
                # Réinitialiser la protection
                target.covert_cloak_protection = False
                return
            
            # Appliquer l'effet secondaire
            # Pour les attaques d'état pur, transmettre toujours damage_dealt
            # Pour les attaques de dégâts, ne transmettre damage_dealt que si > 0
            should_pass_damage = (attack.category == "Status" or damage_dealt > 0)
            
            # Essayer d'abord avec le paramètre damage_dealt, sinon utiliser l'ancienne signature
            try:
                if should_pass_damage:
                    attack.apply_effect(attacker, target, self, damage_dealt)
                else:
                    # Ne pas appliquer les effets secondaires des attaques de dégâts qui font 0 dégâts
                    if utilities.PRINTING_METHOD:
                        print(f"Les effets secondaires de {attack.name} ne s'appliquent pas car l'attaque n'a pas infligé de dégâts.")
                    return
            except TypeError:
                # Ancienne signature sans damage_dealt
                if should_pass_damage:
                    attack.apply_effect(attacker, target, self)
                else:
                    if utilities.PRINTING_METHOD:
                        print(f"Les effets secondaires de {attack.name} ne s'appliquent pas car l'attaque n'a pas infligé de dégâts.")
                    return

    def is_blocked_by_substitute(self, attack, target):
        """
        Détermine si une attaque est bloquée par un substitut selon les règles officielles.
        
        :param attack: L'attaque à vérifier
        :param target: La cible de l'attaque
        :return: True si l'attaque est bloquée, False sinon
        """
        # Les attaques qui ciblent l'utilisateur ne sont jamais bloquées
        if attack.target == "User":
            return False
            
        # Si la cible n'a pas de substitut, pas de blocage
        if not target.has_substitute():
            return False
            
        # Les attaques authentiques ignorent les substituts
        if "authentic" in attack.flags:
            return False
            
        # Les attaques sonores ignorent les substituts
        if "sound" in attack.flags:
            return False
            
        # Attaques qui ne sont JAMAIS bloquées par les substituts
        never_blocked = [
            "Perish Song", "Taunt", "Disable", "Encore", "Torment", "Spite", 
            "Haze", "Boost", "Snatch", "Skill Swap", "Transform", "Whirlwind", 
            "Roar", "Mean Look", "Spider Web", "Block", "Heal Block", "Embargo", 
            "Psych Up", "Heart Swap"
        ]
        
        if attack.name in never_blocked:
            return False
            
        # Les attaques de dégâts ne sont pas bloquées ici (gérées par damage_method)
        if attack.category != "Status":
            return False
            
        # Toutes les autres attaques de statut sont bloquées
        return True

    def handle_multi_hit_attack(self, attacker: pokemon, attack: Attack, defender: pokemon, talent_mod = None, item_mod = None, multiplier = None):
        """
        Gère les attaques multi-coups comme Triple Axel, Bullet Seed, etc.
        
        :param attacker: Le Pokémon qui attaque
        :param attack: L'attaque multi-coups
        :param defender: Le Pokémon qui défend
        :param talent_mod: Modificateurs de talent pour l'attaque (précision, puissance, etc.)
        :param multiplier: Multiplicateur de dégâts
        :return: Dégâts totaux infligés
        """
        from damage_calc import damage_calc

        if not hasattr(attack, 'multi_hit') or not attack.multi_hit:
            # Ce n'est pas une attaque multi-coups, utiliser la méthode normale
            return damage_calc(attacker, attack, defender, self)[0]
        
        total_damage = 0
        hit_count = 0
        
        # Déterminer le nombre de coups
        if hasattr(attack, 'hits'):
            # Attaques avec un nombre fixe de coups (comme Triple Axel)
            max_hits = attack.hits
            hit_count = max_hits
        elif hasattr(attack, 'get_hit_count'):
            # Attaques avec un nombre variable de coups (comme Bullet Seed)
            hit_count = attack.get_hit_count()
        else:
            # Fallback : 2-5 coups aléatoires - optimisation: éviter l'import dans la boucle
            rand_val = random.random()
            if rand_val < 0.375:
                hit_count = 2
            elif rand_val < 0.75:
                hit_count = 3
            elif rand_val < 0.875:
                hit_count = 4
            else:
                hit_count = 5
        
        if utilities.PRINTING_METHOD:
            print(f"{attacker.name} utilise {attack.name} ! L'attaque va frapper {hit_count} fois !")
        
        # Sauver la puissance originale AVANT la boucle pour éviter les problèmes de persistance
        original_base_power = attack.base_power
        
        # Effectuer chaque coup
        for hit in range(1, hit_count + 1):
            # Vérifier si le défenseur est encore en vie
            if defender.current_hp <= 0:
                if utilities.PRINTING_METHOD:
                    print(f"{defender.name} est K.O. ! L'attaque s'arrête.")
                break
            
            # Vérifier la précision pour chaque coup avec les modificateurs de talents
            if not self.calculate_hit_chance(attacker, defender, attack, talent_mod, item_mod):
                if utilities.PRINTING_METHOD:
                    print(f"Le coup {hit} rate !")
                break  # Si un coup rate, l'attaque s'arrête
            
            # Calculer la puissance pour ce coup spécifique
            if hasattr(attack, 'get_hit_power'):
                # Pour des attaques comme Triple Axel (20, 40, 60)
                attack.base_power = attack.get_hit_power(hit)
            else:
                # Utiliser la puissance originale pour les attaques à puissance fixe
                attack.base_power = original_base_power
            
            # Calculer les dégâts pour ce coup
            damage = damage_calc(attacker, attack, defender, self)[0]
            
            if damage and damage > 0:
                if utilities.PRINTING_METHOD:
                    print(f"Coup {hit} : ", end="")
                self.apply_damage(damage, defender, attack, attacker)
                total_damage += damage
                
                # Vérifier les talents qui se déclenchent à chaque coup
                trigger_talent(defender, "after_hit", attack, attacker, self)
                trigger_talent(attacker, "after_dealing_damage", attack, defender, self)
        
        # Restaurer la puissance originale APRÈS la boucle complète
        attack.base_power = original_base_power
        
        if utilities.PRINTING_METHOD:
            print(f"{attack.name} a infligé {total_damage} dégâts au total sur {hit} coup(s) !")
        return total_damage

    def apply_damage(self, damage:int, defender:pokemon, attack:Attack, attacker:pokemon = None):
        """Applique les dégâts à un Pokémon et gère les effets de statut.
        
        :param damage: Dégâts à infliger.
        :param defender: Instance de la classe Pokemon qui subit les dégâts.
        :param attack: Instance de la classe Attack qui est utilisée.
        :param attacker: Instance de la classe Pokemon qui attaque (pour Rocky Helmet).
        """
        # Afficher et appliquer les dégâts
        if utilities.PRINTING_METHOD:
            print(f"{bcolors.DARK_RED}{defender.name} subit {damage} points de dégâts.{bcolors.RESET}")
        # Vérifier si l'attaque ignore les substituts
        if "authentic" in attack.flags or attacker.talent == "Infiltrator":
            bypass_substitute = True
        else:
            bypass_substitute = False
        self.damage_method(defender, damage, bypass_substitute)
        
        # Effet Rocky Helmet : si le défenseur porte Rocky Helmet et l'attaque est de contact
        if (defender.item == "Rocky Helmet" and 
            attacker and 
            attacker.current_hp > 0 and  # L'attaquant doit être vivant
            "contact" in attack.flags and 
            not defender.has_substitute()):  # Rocky Helmet ne fonctionne pas à travers un substitute
            
            # Rocky Helmet inflige 1/6 des PV max de l'attaquant
            helmet_damage = max(1, attacker.max_hp // 6)
            if utilities.PRINTING_METHOD:
                print(f"{bcolors.OKRED}{attacker.name} subit {helmet_damage} dégâts à cause du Rocky Helmet de {defender.name} !{bcolors.RESET}")
            self.damage_method(attacker, helmet_damage, bypass_substitute=True)

    def compute_priority(self, pokemon, attack = Attack):
        """
        Calcule la priorité effective d'une attaque, en prenant en compte les talents.
        """
        if hasattr(attack, "get_priority"):
            base_priority = attack.get_priority(self)
        else:
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
        first, first_attack, second, second_attack = self.get_turn_order(action1, action2)
        # Update des protects
        protect_update(first, first_attack)
        protect_update(second, second_attack)

        # Première attaque
        if self.check_status_before_attack(first):
            self.player_attack(first, first_attack, second, second_attack)
        
        for p in [self.active1, self.active2]:
            trigger_item(p, "after_attack", self, first, first_attack)  # Appliquer les effets des objets après l'attaque

        # Gérer les changements forcés après la première attaque (U-turn, Volt Switch, etc.)   
        self.handle_forced_switches()        

        # Seconde attaque si vivant
        if second.current_hp > 0:
            if self.check_status_before_attack(second):
                self.player_attack(second, second_attack, first, first_attack)
        
        for p in [self.active1, self.active2]:
            trigger_item(p, "after_attack", self, second, second_attack)  # Appliquer les effets des objets après l'attaque

        # Gérer les changements forcés après la deuxième attaque (U-turn, Volt Switch, etc.)
        self.handle_forced_switches()

        self.next_turn()

    def check_magic_coat_reflection(self, attacker, defender, attack):
        """
        Vérifie si Magic Coat est actif et renvoie l'attaque si nécessaire.
        Retourne True si l'attaque a été renvoyée, False sinon.
        """
        if (getattr(defender, 'magic_coat_active', False) and
            attack.category == "Status" and 
            "reflectable" in attack.flags):
            
            if utilities.PRINTING_METHOD:
                print(f"Le voile magique de {defender.name} renvoie {attack.name} à {attacker.name} !")
            
            # Vérifier si l'attaquant a une protection
            has_protection = (
                (hasattr(attacker, 'talent') and attacker.talent == "Magic Bounce") or
                getattr(attacker, 'magic_coat_active', False)
            )
            
            if has_protection:
                if utilities.PRINTING_METHOD:
                    print(f"Mais {attacker.name} est aussi protégé ! L'attaque échoue.")
                return True
            
            # Renvoyer l'attaque vers l'attaquant
            target = attacker if attack.target == "Foe" else defender
            
            if hasattr(attack, 'apply_effect'):
                try:
                    attack.apply_effect(defender, target, self)
                    if utilities.PRINTING_METHOD:
                        print(f"{attack.name} a été renvoyée avec succès !")
                except Exception as e:
                    if utilities.PRINTING_METHOD:
                        print(f"Erreur lors du renvoi de l'attaque : {e}")
            
            return True  # L'attaque a été renvoyée
        
        return False  # Pas de renvoi

    def manage_temporary_status(self, pokemon):
        """
        Gère les statuts temporaires comme Magic Coat, Focus Energy, etc.
        """
        # Magic Coat (dure 1 tour)
        if hasattr(pokemon, 'magic_coat_active') and pokemon.magic_coat_active:
            if hasattr(pokemon, 'magic_coat_turns'):
                pokemon.magic_coat_turns -= 1
                if pokemon.magic_coat_turns <= 0:
                    pokemon.magic_coat_active = False
                    delattr(pokemon, 'magic_coat_turns')
                    if utilities.PRINTING_METHOD:
                        print(f"Le voile magique de {pokemon.name} disparaît.")
        
        # Ajouter d'autres statuts temporaires ici si nécessaire...

    def manage_temporary_status(self, pokemon):
        """
        Gère les statuts temporaires comme Magic Coat qui durent un certain nombre de tours.
        """
        # Gérer Magic Coat
        if getattr(pokemon, 'magic_coat_active', False):
            magic_coat_turns = getattr(pokemon, 'magic_coat_turns', 0)
            if magic_coat_turns <= 1:
                pokemon.magic_coat_active = False
                pokemon.magic_coat_turns = 0
                if utilities.PRINTING_METHOD:
                    print(f"L'effet du voile magique de {pokemon.name} se dissipe !")
            else:
                pokemon.magic_coat_turns -= 1
        
        # Gérer Heal Block (Psychic Noise)
        if getattr(pokemon, 'heal_blocked', False):
            heal_blocked_turns = getattr(pokemon, 'heal_blocked_turns', 0)
            if heal_blocked_turns <= 1:
                pokemon.heal_blocked = False
                pokemon.heal_blocked_turns = 0
                if utilities.PRINTING_METHOD:
                    print(f"{pokemon.name} peut à nouveau se soigner !")
            else:
                pokemon.heal_blocked_turns -= 1
                if utilities.PRINTING_METHOD:
                    print(f"{pokemon.name} ne peut toujours pas se soigner ({pokemon.heal_blocked_turns} tours restants)")

        # Ici on peut ajouter d'autres statuts temporaires si nécessaire
        # ex: Focus Energy, Taunt, etc.

    def remove_ruin_effects(self, departing_pokemon):
        """Supprime les effets de ruine quand un Pokémon avec un talent de ruine quitte le combat."""
        ruin_talents = ["Sword of Ruin", "Tablets of Ruin", "Vessel of Ruin", "Beads of Ruin"]
        
        if departing_pokemon.talent in ruin_talents:
            # Désactiver l'effet correspondant
            self.ruin_effects_active[departing_pokemon.talent] = False
            
            # Vérifier s'il y a encore un autre Pokémon avec le même talent
            still_active = False
            for pokemon in [self.active1, self.active2]:
                if pokemon and pokemon != departing_pokemon and pokemon.current_hp > 0 and pokemon.talent == departing_pokemon.talent:
                    still_active = True
                    break
            
            # Si aucun autre Pokémon n'a ce talent, réappliquer tous les effets actifs
            if not still_active:
                # Réappliquer tous les effets actifs (ce qui va automatiquement 
                # réinitialiser les hidden_modifier appropriés)
                self.apply_ruin_effects()
                if utilities.PRINTING_METHOD:
                    print(f"Les effets de {departing_pokemon.talent} ont été supprimés.")

    def apply_ruin_effects(self):
        """
        Applique les effets des talents de ruine à tous les Pokémon actifs.
        Cette méthode doit être appelée quand un Pokémon avec un talent de ruine entre sur le terrain.
        """
        ruin_talents = ["Sword of Ruin", "Tablets of Ruin", "Vessel of Ruin", "Beads of Ruin"]
        
        # Vérifier si un talent de ruine est actif sur le terrain
        for pokemon in [self.active1, self.active2]:
            if pokemon.current_hp > 0 and pokemon.talent in ruin_talents:
                self.ruin_effects_active[pokemon.talent] = True
        
        # Appliquer les effets de ruine à tous les Pokémon qui n'ont pas ce talent
        for pokemon in [self.active1, self.active2]:
            if pokemon.current_hp > 0:
                self.apply_individual_ruin_effects(pokemon)
    
    def apply_individual_ruin_effects(self, pokemon):
        """
        Applique les effets de ruine individuels à un Pokémon spécifique en utilisant hidden_modifier.
        """
        stat_map = {
            "Sword of Ruin": "Defense",
            "Tablets of Ruin": "Attack", 
            "Vessel of Ruin": "Sp. Atk",
            "Beads of Ruin": "Sp. Def"
        }
        
        # Réinitialiser les hidden_modifier pour les stats de ruine
        for stat in stat_map.values():
            pokemon.hidden_modifier[stat] = 1.0
        
        # Appliquer les effets de ruine actifs
        for ruin_talent, active in self.ruin_effects_active.items():
            if active and ruin_talent in stat_map:
                affected_stat = stat_map[ruin_talent]
                
                # Ne pas affecter les Pokémon avec le même talent
                if pokemon.talent != ruin_talent:
                    pokemon.hidden_modifier[affected_stat] = 0.75
                    if utilities.PRINTING_METHOD:
                        print(f"{ruin_talent} réduit {affected_stat} de {pokemon.name} de 25%")
        
        # Actualiser les stats avec les nouveaux modificateurs
        pokemon.actualize_stats()

    ### Savoir la probabilité de toucher une attaque ###
    def calculate_hit_chance(self, attacker, defender, attack, talent_mod, item_mod):
        """
        Calcule si l'attaque touche en tenant compte de la précision de l'attaque,
        de la précision de l'attaquant et de l'évasion du défenseur.

        :param attacker: Instance de la classe Pokemon qui attaque.
        :param defender: Instance de la classe Pokemon qui défend.
        :param attack: Instance de la classe Attack qui est utilisée.
        :param talent_mod: Modificateur de talent pour l'attaque.
        :return: True si l'attaque touche, False sinon.
        """
        # Vérifier les talents qui garantissent la précision (comme No Guard)
        if isinstance(talent_mod["accuracy"], bool) and talent_mod["accuracy"] == True:
            return True 
        
        # Utiliser la précision effective de l'attaque (conditions météo, etc.)
        effective_accuracy = attack.get_effective_accuracy(attacker, defender, self) if hasattr(attack, 'get_effective_accuracy') else attack.accuracy
        
        # Si l'attaque garantit la précision dans certaines conditions
        if effective_accuracy == True:
            return True

        if hasattr(defender, 'glaive_rush') and defender.glaive_rush:
            return True

        # Calcul normal de précision
        base_accuracy = effective_accuracy / 100.0 * talent_mod["accuracy"] * item_mod["accuracy"]
        final_accuracy = base_accuracy * attacker.accuracy / defender.evasion
        final_accuracy_percent = min(final_accuracy * 100, 100)  # Limiter à 100% pour l'affichage1
        return random.random() <= final_accuracy
    
#### appliquer les degats des statuts ####
    def apply_status_damage(self, pokemon):
        """
        Applique les dégâts liés aux statuts persistants : burn, poison, etc.
        """
        if pokemon.status == "burn":
            dmg = int(pokemon.max_hp * 0.0625)
            if utilities.PRINTING_METHOD:
                print(f"{pokemon.name} souffre de sa brûlure ! Il perd {dmg} PV.")
            self.damage_method(pokemon, dmg, True)
        elif pokemon.status == "poison":
            if pokemon.talent == "Poison Heal":
                if utilities.PRINTING_METHOD:
                    print(f"{pokemon.name} regagne {dmg} PV grâce à Poison Heal ! ")
                dmg = -int(pokemon.max_hp * 0.125)
            else:
                dmg = int(pokemon.max_hp * 0.125)
                if utilities.PRINTING_METHOD:
                    print(f"{pokemon.name} est empoisonné ! Il perd {dmg} PV.")
            self.damage_method(pokemon, dmg, True)
        elif pokemon.status == "badly_poisoned":
            if not hasattr(pokemon, "toxic_counter"):
                pokemon.toxic_counter = 1
            if pokemon.talent == "Poison Heal":
                if utilities.PRINTING_METHOD:
                    print(f"{pokemon.name} regagne {dmg} PV grâce à Poison Heal ! ")
                dmg = -int(pokemon.max_hp * 0.125)
            else:
                dmg = int(pokemon.max_hp * 0.0625 * pokemon.toxic_counter)
                if utilities.PRINTING_METHOD:
                    print(f"{pokemon.name} est gravement empoisonné ! Il perd {dmg} PV.")
            self.damage_method(pokemon, dmg)
            pokemon.toxic_counter += 1

    def check_status_before_attack(self, attacker: pokemon, attack: Attack, attacker_before: pokemon = None) -> bool:
        """
        Vérifie si le Pokémon peut agir selon son statut.
        Retourne True s'il peut attaquer, False sinon.

        :param attacker: Le Pokémon qui attaque.

        :param attack: Instance de l'attaque utilisée par attacker.

        :param attacker_before: Instance du pokémon qui a possiblement attaqué avant, 
        ce paramètre est surtout utilisé pour savoir si le talent de ce pokémon est Mold Breaker dans ce cas on ignore le possible Inner focus de attacker. Le paramètre de merde en gros
        """
        if attacker.status == "sleep":
            match attacker.sleep_counter:
                case 3:
                    if utilities.PRINTING_METHOD:
                        print(f"{attacker.name} se réveille !")
                    attacker.remove_status()
                    return True
                case 2:
                    if random.random() < 0.5:
                        if utilities.PRINTING_METHOD:
                            print(f"{attacker.name} se réveille !")
                        attacker.remove_status()
                        return True
                    else:
                        if utilities.PRINTING_METHOD:
                            print(f"{attacker.name} tape sa meilleur sieste.")
                        attacker.sleep_counter += 1
                        if attack.name != "Sleep Talk":
                            return True
                        return False
                case 1:
                    if random.random() < 0.5:
                        if utilities.PRINTING_METHOD:
                            print(f"{attacker.name} se réveille !")
                        attacker.remove_status()
                        return True
                    else:
                        if utilities.PRINTING_METHOD:
                            print(f"{attacker.name} dort encore.")
                        attacker.sleep_counter += 1
                        if attack.name != "Sleep Talk":
                            return True
                        return False
                case 0:
                    if utilities.PRINTING_METHOD:
                        print(f"{attacker.name} dort profondément.")
                    attacker.sleep_counter += 1
                    if attack.name != "Sleep Talk":
                        return True
                    return False
                case _:
                    raise ValueError(f"Invalid sleep counter value: {attacker.sleep_counter}")
                
        if attacker.status == "frozen":
            if random.random() < 0.2:  # 20% chance de dégeler
                if utilities.PRINTING_METHOD:
                    print(f"{attacker.name} dégèle !")
                attacker.remove_status()
                return True
            else:
                if utilities.PRINTING_METHOD:
                    print(f"{attacker.name} est gelé et ne peut pas bouger.")
                return False

        if attacker.status == "paralyzed":
            if random.random() < 0.25:
                if utilities.PRINTING_METHOD:
                    print(f"{attacker.name} est paralysé ! Il ne peut pas attaquer.")
                return False

        if attacker.flinched:
            if attacker_before and attacker_before.talent == "Mold Breaker":
                return False  # Dans tous les cas avec Mold Breaker il y a flinch même si le poke a Inner Focus
            if attacker.talent == "Inner Focus":
                if utilities.PRINTING_METHOD:
                    print(f"Inner Focus de {attacker.name} l'empêche d'être flinch !")
            else:
                if utilities.PRINTING_METHOD:
                    print(f"{attacker.name} est flinch et ne peut pas attaquer !")
                attacker.flinched = False
                return False
        
        return True

    def on_entry_hazards(self, pokemon):
        """
        Applique les effets des pièges d'entrée (Spikes, Stealth Rock, etc.) sur un Pokémon à son entrée dans le combat.
        
        :param pokemon: Instance de la classe Pokemon qui entre dans le combat.
        :param fight: Instance de la classe Fight contenant les informations sur les pièges d'entrée.
        """
        team = self.get_team_id(pokemon)
        # IMPORTANT : Les hazards affectent l'équipe OPPOSÉE à celle qui les a posés
        match team:
            case 1:
                hazards = self.hazards_team1  # L'équipe 1 subit les hazards posés par l'équipe 2
            case 2:
                hazards = self.hazards_team2  # L'équipe 2 subit les hazards posés par l'équipe 1
            case _:
                raise ValueError("Invalid team ID")
        
        if pokemon.has_substitute():
            if utilities.PRINTING_METHOD:
                print(f"{pokemon.name} a un clone qui bloque les pièges d'entrée !")
            return
        
        if pokemon.item == "Heavy-Duty Boots":
            if utilities.PRINTING_METHOD:
                print(f"{pokemon.name} porte des Heavy-Duty Boots et ignore les pièges d'entrée !")
            return

        # Vérifier les pièges d'entrée
        if hazards["Spikes"] > 0 and "Flying" not in pokemon.types and pokemon.talent != "Levitate":
            damage = int(pokemon.max_hp * 0.0625 * hazards["Spikes"])  # 1/16 par couche de Spikes
            if utilities.PRINTING_METHOD:

                print(f"{pokemon.name} subit {damage} points de dégâts à cause des Spikes !")
            self.damage_method(pokemon, damage)

        if hazards["Stealth Rock"]:
            rock_damage = int(pokemon.max_hp * 0.125)  # 1/8 des PV max
            type_eff = type_effectiveness("Rock", pokemon)
            total_damage = int(rock_damage * type_eff)
            if utilities.PRINTING_METHOD:
                print(f"{pokemon.name} subit {total_damage} points de dégâts à cause des Piège de Roc !")
            self.damage_method(pokemon, total_damage)

        if hazards["Toxic Spikes"] > 0:
            if "Poison" in pokemon.types or "Steel" in pokemon.types:
                if "Poison" in pokemon.types:
                    hazards["Toxic Spikes"] = 0  # Neutralisé par les Pokémon Poison
                    if utilities.PRINTING_METHOD:
                        print(f"{pokemon.name} absorbe les Toxic Spikes !")
                else:
                    if utilities.PRINTING_METHOD:
                        print(f"{pokemon.name} est immunisé contre les Toxic Spikes !")
            elif "Flying" in pokemon.types or pokemon.talent == "Levitate":
                pass  # Ignoré par Flying et Levitate
            else:
                if hazards["Toxic Spikes"] == 1:
                    pokemon.apply_status("poison")
                    if utilities.PRINTING_METHOD:
                        print(f"{pokemon.name} est empoisonné par les Toxic Spikes !")
                elif hazards["Toxic Spikes"] >= 2:
                    pokemon.apply_status("badly_poisoned")
                    if utilities.PRINTING_METHOD:
                        print(f"{pokemon.name} est gravement empoisonné par les Toxic Spikes !")

        if hazards["Sticky Web"]:
            if pokemon.talent != "Levitate" and "Flying" not in pokemon.types:
                stat_change = {"Speed": -1}  # Réduit la vitesse de 1 stage
                pokemon.apply_stat_change(stat_change)
            else:
                if utilities.PRINTING_METHOD:
                    print(f"{pokemon.name} évite Sticky Web grâce à son type/talent !")

    def get_turn_order(self, action1, action2):
        
        p1, atk1 = action1
        p2, atk2 = action2

        prio1 = self.compute_priority(p1, atk1)
        prio2 = self.compute_priority(p2, atk2)

        first, first_attack, second, second_attack = None, None, None, None

        # Déterminer l'ordre d'action
        if prio1 > prio2:
            first, first_attack, second, second_attack = p1, atk1, p2, atk2
        elif prio2 > prio1:
            first, first_attack, second, second_attack = p2, atk2, p1, atk1
        else:
            # Même priorité : départager par la vitesse
            speed1 = p1.current_stats()['Speed']
            speed2 = p2.current_stats()['Speed']
            
            # Trick Room inverse l'ordre de vitesse (les plus lents vont en premier)
            if self.trick_room_active:
                if speed1 < speed2:  # Inversé : plus lent en premier
                    first, first_attack, second, second_attack = p1, atk1, p2, atk2
                elif speed2 < speed1:  # Inversé : plus lent en premier
                    first, first_attack, second, second_attack = p2, atk2, p1, atk1
                else:
                    # Vitesses égales : aléatoire
                    if random.random() < 0.5:
                        first, first_attack, second, second_attack = p1, atk1, p2, atk2
                    else:
                        first, first_attack, second, second_attack = p2, atk2, p1, atk1
            else:
                # Ordre normal : plus rapide en premier
                if speed1 > speed2:
                    first, first_attack, second, second_attack = p1, atk1, p2, atk2
                elif speed2 > speed1:
                    first, first_attack, second, second_attack = p2, atk2, p1, atk1
                else:
                    # Vitesses égales : aléatoire
                    if random.random() < 0.5:
                        first, first_attack, second, second_attack = p1, atk1, p2, atk2
                    else:
                        first, first_attack, second, second_attack = p2, atk2, p1, atk1
    
        return (first, first_attack, second, second_attack)
    
    def new_get_turn_order(self, pokemon1, attack1, pokemon2, attack2):
        """
        Nouvelle méthode pour obtenir l'ordre des attaques en tenant compte des actions de type ('type_action', int, tera_used).
        """
        prio1 = self.compute_priority(pokemon1, attack1)
        prio2 = self.compute_priority(pokemon2, attack2)

        if prio1 > prio2:
            return (pokemon1, attack1, pokemon2, attack2)
        elif prio2 > prio1:
            return (pokemon2, attack2, pokemon1, attack1)
        else:
            # Même priorité : départager par la vitesse
            speed1 = pokemon1.current_stats()["Speed"]
            speed2 = pokemon2.current_stats()["Speed"]
            
            if self.trick_room_active:
                if speed1 < speed2:
                    return (pokemon1, attack1, pokemon2, attack2)
                elif speed2 < speed1:
                    return (pokemon2, attack2, pokemon1, attack1)
                else:
                    # Vitesses égales : random pour tout décider
                    if random.random() < 0.5:
                        return (pokemon1, attack1, pokemon2, attack2)
                    else:
                        return (pokemon2, attack2, pokemon1, attack1)
            else:
                if speed1 > speed2:
                    return (pokemon1, attack1, pokemon2, attack2)
                elif speed2 > speed1:
                    return (pokemon2, attack2, pokemon1, attack1)
                else:
                    # Vitesses égales : random pour tout décider
                    if random.random() < 0.5:
                        return (pokemon1, attack1, pokemon2, attack2)
                    else:
                        return (pokemon2, attack2, pokemon1, attack1)
                    
    def new_handle_ko_replacement(self, ko_pokemon, ai):
        """
        Gère le remplacement immédiat d'un Pokémon K.O.
        """
        if ko_pokemon == self.active1:
            team_id = 1
            team = self.team1
        elif ko_pokemon == self.active2:
            team_id = 2
            team = self.team2
        else:
            return  # Pokémon pas actif, pas besoin de remplacement
        
        if utilities.PRINTING_METHOD:
            print(f"{ko_pokemon.name} est K.O. !")
        
        if self.is_team_defeated(team):
            if utilities.PRINTING_METHOD:
                print(f"Tous les Pokémon de l'équipe {team_id} sont K.O. ! Victoire de l'équipe {3-team_id} !")
            return
        else:
            if utilities.PRINTING_METHOD:
                print(f"Remplacement nécessaire pour l'équipe {team_id}")
            switch_in_pokemon_id = ai.choose_switch_in(self)
            if switch_in_pokemon_id is not None:
                self.new_handle_switch(team_id, switch_in_pokemon_id)
            else:
                if utilities.PRINTING_METHOD:
                    print(f"ERREUR: L'IA n'a pas pu choisir de Pokémon de remplacement !")

    def new_handle_switch(self, team_id, pokemon_index):
        """
        Gère tous les types de changements de Pokémon : automatique, forcé ou par choix causé par une attaque.
        
        :param team_id: ID de l'équipe (1 ou 2)
        :param pokemon_index: Index du Pokémon à faire entrer
        :return: Index du Pokémon qui entre, ou None si impossible
        """
        # Effectuer le changement
        self.player_switch(team_id, pokemon_index)

    
    def new_forced_switch_method(self, ia1 : PokemonAI, ia2 : PokemonAI):
        """
        Nouvelle méthode de switch pour les instances de PokemonAI. Et qui va être utilisée dans new_battle_manager.py.
        Et qui va gérer les switchs décidés par les IA ou ceux faits par les attaques en remplaçant handle_forced_switch() et en 
        appelant notamment choose_switch_in() de la classe PokemonAI.

        :param ia1: Instance de PokemonAI qui est le joueur de l'équipe 1.
        :param ia2: Instance de PokemonAI qui est le joueur de l'équipe 2.
        """

        for team_id, active_pokemon in [(1, self.active1), (2, self.active2)]:
            if (hasattr(active_pokemon, 'must_switch_after_attack') and 
                active_pokemon.must_switch_after_attack and 
                active_pokemon.current_hp > 0):
                
                if team_id == 1:
                    switch_in_pokemon_id = ia1.choose_switch_in(self)
                else:
                    switch_in_pokemon_id = ia2.choose_switch_in(self)

                if switch_in_pokemon_id:
                    switch_reason = getattr(active_pokemon, 'switch_reason', 'une attaque')
                    if utilities.PRINTING_METHOD:
                        print(f"{active_pokemon.name} revient grâce à {switch_reason} !")
                    self.new_handle_switch(team_id, switch_in_pokemon_id)  # U-turn n'est pas "forced" au sens KO
                
                # Réinitialiser les attributs
                active_pokemon.must_switch_after_attack = False
                if hasattr(active_pokemon, 'switch_reason'):
                    active_pokemon.switch_reason = None

    def new_resolve_turn(self, poke1_action : tuple[PokemonAI,(Attack, int, bool)], poke2_action : tuple[PokemonAI,(Attack, int, bool)]):
        """
        Nouvelle méthode resolve_turn pour prendre en charge des actions du type ('type_action', int, tera_used)
        """
        
        ai1, action1 = poke1_action
        ai2, action2 = poke2_action

        # DEBUG : Afficher les actions reçues
        if utilities.PRINTING_METHOD:
            print(f"DEBUG - Action1 reçue: {action1}")
            print(f"DEBUG - Action2 reçue: {action2}")
            print(f"DEBUG - Pokémon actuel team1: {self.active1.name}")
            print(f"DEBUG - Pokémon actuel team2: {self.active2.name}")

        # CORRECTION : Associer correctement les IA à leurs Pokémon
        if ai1.team_id == 1:
            pokemon1, action1_type, action1_value, action1_tera_used = self.active1, *action1
        else:
            pokemon1, action1_type, action1_value, action1_tera_used = self.active2, *action1
            
        if ai2.team_id == 2:
            pokemon2, action2_type, action2_value, action2_tera_used = self.active2, *action2
        else:
            pokemon2, action2_type, action2_value, action2_tera_used = self.active1, *action2

        # Prendre en charge les différents cas facilement
        # On gère d'abord le cas du double switch
        if action1_type == "switch" and action2_type == "switch":
            first, second = None, None
            pokemon1_speed, pokemon2_speed = pokemon1.current_stats()["Speed"], pokemon2.current_stats()["Speed"]
            if pokemon1_speed > pokemon2_speed:
                first, second = pokemon1, pokemon2
                first_switch_in, second_switch_in = action1_value, action2_value
            elif pokemon1_speed < pokemon2_speed:
                first, second = pokemon2, pokemon1
                first_switch_in, second_switch_in = action2_value, action1_value
            else:
                if random.random() < 0.5:
                    first, second = pokemon1, pokemon2
                    first_switch_in, second_switch_in = action1_value, action2_value
                else:
                    first, second = pokemon2, pokemon1
                    first_switch_in, second_switch_in = action2_value, action1_value

            first_team_id, second_team_id = self.get_team_id(first), self.get_team_id(second)
            
            # Gérer les switch.
            self.player_switch(first_team_id, first_switch_in)
            self.player_switch(second_team_id, second_switch_in)

        # Ensuite le cas ou les deux attaquent
        elif action1_type in ["attack", "terastallize"] and action2_type in ["attack", "terastallize"]:

            first, first_attack, second, second_attack = self.new_get_turn_order(pokemon1, action1_value, pokemon2, action2_value)

            # APRÈS new_get_turn_order()
            if utilities.PRINTING_METHOD:
                print(f"DEBUG - APRÈS new_get_turn_order:")
                print(f"  first: {first.name} va utiliser {first_attack.name}")
                print(f"  second: {second.name} va utiliser {second_attack.name}")
            
            # Vérifier les possibles téracristallisations qui se font avant les attaques des 2 pokémons
            if action1_type == "terastallize" and pokemon1 in [first, second]:
                pokemon1.terastallize(pokemon1.tera_type)
            if action2_type == "terastallize" and pokemon2 in [first, second]:
                pokemon2.terastallize(pokemon2.tera_type)

            # Update des protects
            protect_update(first, first_attack)
            protect_update(second, second_attack)

            # Première attaque
            if self.check_status_before_attack(first, first_attack, second):
                self.player_attack(first, first_attack, second, second_attack)
            
            for p in [self.active1, self.active2]:
                trigger_item(p, "after_attack", self, first, first_attack)

            # Vérifier les K.O. après la première attaque
            if second.current_hp <= 0:
                # Déterminer quelle IA contrôle le Pokémon K.O.
                ko_ai = ai1 if second == self.active1 else ai2
                self.new_handle_ko_replacement(second, ko_ai)
                # Vérifier si le combat est terminé
                if self.check_battle_end():
                    return

            # Gérer les changements forcés après la première attaque   
            self.new_forced_switch_method(ai1, ai2)    
            
            # Seconde attaque si vivant et pas remplacé
            if second.current_hp > 0:
                if self.check_status_before_attack(second, second_attack, first):
                    self.player_attack(second, second_attack, first, first_attack)
                
                for p in [self.active1, self.active2]:
                    trigger_item(p, "after_attack", self, second, second_attack)

                # Vérifier les K.O. après la deuxième attaque
                if first.current_hp <= 0:
                    # Déterminer quelle IA contrôle le Pokémon K.O.
                    ko_ai = ai1 if first == self.active1 else ai2
                    self.new_handle_ko_replacement(first, ko_ai)
                    # Vérifier si le combat est terminé
                    if self.check_battle_end():
                        return

            # Gérer les changements forcés après la deuxième attaque
            self.new_forced_switch_method(ai1, ai2)
            
        # Enfin le dernier cas possible est obligatoirement qu'un des deux joueurs switch et l'autre attaque.
        else:
            switcher, switch_in_id, attacker, attack_id = None, None, None, None
            switcher_ai, attacker_ai = None, None
            
            if action1_type == "switch":
                switcher, switch_in_id = pokemon1, action1_value
                attacker, attack_id = pokemon2, action2_value
                switcher_ai, attacker_ai = ai1, ai2
            else:
                switcher, switch_in_id = pokemon2, action2_value
                attacker, attack_id = pokemon1, action1_value
                switcher_ai, attacker_ai = ai2, ai1

            # Effectuer le switch avec la nouvelle méthode
            self.new_handle_switch(self.get_team_id(switcher), switch_in_id)
            
            new_in_pokemon = self.active1 if switcher == pokemon1 else self.active2

            # Vérifier si l'attaquant peut attaquer
            if self.check_status_before_attack(attacker, attack_id):
                self.player_attack(attacker, attack_id, new_in_pokemon)

                # Vérifier les K.O. après l'attaque
                if new_in_pokemon.current_hp <= 0:
                    # Le Pokémon qui vient d'entrer est K.O.
                    self.new_handle_ko_replacement(new_in_pokemon, switcher_ai)
                    # Vérifier si le combat est terminé
                    if self.check_battle_end():
                        return

            # Gérer les changements forcés après l'attaque
            self.new_forced_switch_method(ai1, ai2)

        self.next_turn(ai1, ai2)  # Passer au tour suivant

# Ensemble des fonctions pour gérer la puissance d'une attaque contre un autre pokémon.
# Utilisées dans la méthode attack_power de la classe Fight.

def type_effectiveness(attack_type, target):
    """
    Calcule l'efficacité du type en tenant compte de la Téracristalisation.
    
    :param attack_type: Type de l'attaque
    :param target: Pokémon cible (instance, pas liste de types)
    :return: Multiplicateur d'efficacité
    """
    target_types = target.types
        
    modifier = 1.0
    for t in target_types:
        modifier *= utilities.type_chart[utilities.POKEMON_TYPES_ID[attack_type]][utilities.POKEMON_TYPES_ID[t]]
    return modifier
    
#### Attaque de confusion ####
def confusion_attack(pokemon : pokemon):
    """
    Gère l'attaque subit lorsqu'un pokémon est confus, il s'agit d'une attaque de type Normal (qui n'est pas affecté par les types ni le stab)
    et qui a 40 de puissance de base. La formule de calcul est donc la suivante :
    ((base_power * (attack_stat / defense_stat)) + 1) 
    """
    damage = int(((40 * (pokemon.current_stats()['Attack'] / pokemon.current_stats()['Defense'])) + 1))
    return damage

def protect_update(pokemon : pokemon, attack : Attack):
    """
    Met à jour l'état de protection d'un Pokémon. Sert uniquement le tour après une protection pour annuler le protect si le pokémon attaque.

    :param pokemon: Instance de la classe Pokemon qui utilise la protection.
    :param attack: Instance de la classe Attack qui est utilisée.
    """
    if not "protection" in attack.flags:
        pokemon.protect = False
        pokemon.protect_turns = 0

from colors_utils import Colors

# Affichage des Pokémon
def display_pokemon(poke : pokemon):
    ratio = poke.current_hp / poke.max_hp
    color = Colors.color_hp(ratio)
    color_team = Colors.TEAM1 if poke.fight.get_team_id(poke) == 1 else Colors.TEAM2
    if utilities.PRINTING_METHOD:
        print(f"{Colors.BOLD}{color_team}{poke.name}{Colors.RESET} (HP: {color}{poke.current_hp}/{poke.max_hp}{Colors.RESET}) - {poke.status} - {poke.item if poke.item else 'Aucun objet'}")

def display_weather(fight : Fight):
    weath = fight.weather["current"]
    color = Colors.color_weather(weath)
    if utilities.PRINTING_METHOD:
        print(f"{color}Météo actuelle: {weath} pendant encore {fight.weather_turn_left} tours{Colors.RESET}" if weath else "Aucune météo active")

def display_wall(fight : Fight):
    color = Colors.WALL
    color2 = Colors.WALL_TITLE
    if utilities.PRINTING_METHOD:
        print(f"{Colors.TEAM1}Écrans équipe 1: {color2}{fight.screen_team1 if fight.screen_team1 else 'Aucun'}{Colors.RESET}")
        print(f"{color}", end="")
    if fight.screen_team1 != []:
        for screen in fight.screen_team1:
            if utilities.PRINTING_METHOD:
                print(f"Écran actif: {screen} ({fight.screen_turn_left_team1[screen]} tours restants)")
    if utilities.PRINTING_METHOD:    
        print(f"{color2}", end="")
        print(f"{Colors.TEAM2}Écrans équipe 2: {color2}{fight.screen_team2 if fight.screen_team2 else 'Aucun'}{Colors.RESET}")
        print(f"{color}", end="")
    if fight.screen_team2 != []:
        for screen in fight.screen_team2:
            if utilities.PRINTING_METHOD:
                print(f"Écran actif: {screen} ({fight.screen_turn_left_team2[screen]} tours restants)")

def display_hazards(fight : Fight):
    spike = Colors.SPIKES
    tspike = Colors.TOXIC_SPIKES
    sticky = Colors.STICKY_WEB
    rocks = Colors.STEALTH_ROCK
    if utilities.PRINTING_METHOD:
        print(f"{Colors.TEAM1}Equipe 1: {rocks}Piège de Roc: {fight.hazards_team1['Stealth Rock']}, {spike}Spikes: {fight.hazards_team1['Spikes']}/3, {tspike}Toxic Spikes: {fight.hazards_team1['Toxic Spikes']}/2, {sticky}Sticky Web: {fight.hazards_team1['Sticky Web']} {Colors.RESET}")
        print(f"{Colors.TEAM2}Equipe 2: {rocks}Piège de Roc: {fight.hazards_team2['Stealth Rock']}, {spike}Spikes: {fight.hazards_team2['Spikes']}/3, {tspike}Toxic Spikes: {fight.hazards_team2['Toxic Spikes']}/2, {sticky}Sticky Web: {fight.hazards_team2['Sticky Web']} {Colors.RESET}")


# Affichage du menu
def display_menu():
    if utilities.PRINTING_METHOD:
        print(Colors.TEAM1 + "Choisissez une action pour le joueur 1 :" + Colors.RESET)
        print(Colors.menu_option(1, "Attaquer"))
        print(Colors.menu_option(2, "Changer de Pokémon"))
        print(Colors.menu_option(3, "Voir les stats d'un Pokémon"))
        print(Colors.menu_option(4, "Quitter le combat") + Colors.RESET)