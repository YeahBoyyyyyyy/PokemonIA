import random
import utilities # Données de la table des types et des natures
import sys
sys.path.append("C:/Users/natha/OneDrive/Desktop/Travail/IA Combats pokémons/PokemonIA/Materials")
from Materials.pokemon_items import trigger_item
from Materials.pokemon_talents import trigger_talent
'''
Véritable Intelligence Artificielle pour faire des combats pokémon : On va ici implémenenter toutes les particularités d'un combat pokémon,
c'est-à-dire : les pokémons avec leurs stats, talents, attaques, les 6 pokémons de l'équipe, les effets des attaques, les changements de stats, 
les changements de terrain, les changements de statut, les changements de météo. 
On va pour cela créer un réseau de neuronesprenant en entrée tous ces paramètres.
'''

    
class pokemon():
    def __init__(self, poke: dict): 
        ## Données de base du Pokémon
        self.name = poke['name']  # Nom du Pokémon
        self.talent = poke['abilities'][0]  # Talent du Pokémon le premier est mis par défaut
        self.types = poke['types']  # Types du Pokémon 
        self.item = None  # Objet tenu par le Pokémon (par exemple : Baie, etc.)
        self.nature = None  # Nature du Pokémon (par exemple : "Hardy", "Lonely", etc.)

        ## BASE STATS
        stats = poke['stats']

        self.base_stats = {
            'HP': stats['HP'],
            'Attack': stats['Attack'],
            'Defense': stats['Defense'],
            'Sp. Atk': stats['Sp. Atk'],
            'Sp. Def': stats['Sp. Def'],
            'Speed': stats['Speed'],
        }

        ## IVs - Optimisation: utilisation d'un dict avec valeurs par défaut
        self.ivs = {stat: 31 for stat in self.base_stats.keys()}

        ## EVs - Optimisation: utilisation d'un dict avec valeurs par défaut
        self.evs = {stat: 0 for stat in self.base_stats.keys()}

        ## Les stats dans le combat
        self.stats_modifier = [0, 0, 0, 0, 0]  # Modificateurs de stats pour Attack, Defense, Sp. Atk, Sp. Def, Speed
        self.ev_and_acc_modifier = [0, 0]  # Modificateurs d'évasion et de précision 

        self.hidden_modifier = {"Attack": 1, "Defense": 1, "Sp. Atk": 1, "Sp. Def": 1, "Speed": 1}

        self.max_hp =  int((2 * self.base_stats['HP'] + self.ivs["HP"] + self.evs['HP'] / 4) * 0.5 + 60)   # Points de vie maximum
        self.current_hp = self.max_hp  # Points de vie actuels

        # Cache pour les calculs de stats
        self._stats_cache = {}
        self._stats_dirty = True  # Flag pour savoir si le cache doit être recalculé

        self.nature_modifier = utilities.nature_chart[self.nature] if self.nature else [1, 1, 1, 1, 1]
        self._calculate_initial_stats()
        
        self.accuracy = 1.0  # Précision du Pokémon (par exemple : 1.0 pour 100% de précision)
        self.evasion = 1.0  # Évasion du Pokémon (par exemple : 1.0 pour 100% d'évasion)

        self.accuracy_with_no_modifier = 1.0  # Précision du Pokémon sans modificateurs
        self.evasion_with_no_modifier = 1.0  # Évasion du Pokémon sans modificateurs
        
        ## ATTACKS : Les attaques ne sont pas mises à l'initialisation du Pokémon, mais lorsque l'on modifie le Pokémon pour le combat.
        self.attack1 = None
        self.attack2 = None
        self.attack3 = None
        self.attack4 = None
        
        ## PP SYSTEM : Points de Pouvoir pour chaque attaque
        self.pp1 = 0  # PP actuels pour attack1
        self.pp2 = 0  # PP actuels pour attack2
        self.pp3 = 0  # PP actuels pour attack3
        self.pp4 = 0  # PP actuels pour attack4
        self.max_pp1 = 0  # PP maximum pour attack1
        self.max_pp2 = 0  # PP maximum pour attack2
        self.max_pp3 = 0  # PP maximum pour attack3
        self.max_pp4 = 0  # PP maximum pour attack4
        
        # Système de clones (Substitute)
        self.substitute_hp = 0  # PV du clone

        self.status = None  # Statut du Pokémon (par exemple : "Brûlé", "Gelé", etc.)
        self.is_confused = False  # Indique si le Pokémon est confus
        self.power = False # Indique si le Pokémon est sous l'effet de puissance (qui booste le taux de crits)
        self.charging = False  # Indique si le Pokémon est en train de charger une attaque (par exemple : "Meteor Beam", "Solar Beam", etc.)
        self.charging_attack = None  # Indique quelle attaque est en cours de chargement
        self.must_recharge = False  # Indique si le Pokémon doit récupérer après une attaque de recharge (comme Hyper Beam)
        self.sleep_counter = None  # Nombre de tours de sommeil du Pokémon endormi
        self.toxic_counter = 1  # Compteur pour le poison grave (Toxic) - commence à 1
        self.protect_turns = 0  # Nombre de tours de protection restants si le Pokémon utilise "Protect" ou "Detect"
        self.still_confused = False  # Indique si le Pokémon est toujours confus au prochain tour
        self.locked_attack = None  # Pour gérer Choice Band/Specs/Scarf (stocke l'objet Attack)
        self.fully_evolved = poke['fully_evolved'] if 'fully_evolved' in poke else False  # Indique si le Pokémon est entièrement évolué
        self.flinched = False  # Indique si le Pokémon a été flinché (par exemple : par une attaque comme "Bite" ou "Stomp")
        self.protect = False  # Indique si le Pokémon a utilisé "Protect" ou "Detect" ce tour-ci
        self.protect_turns = 0  # Nombre de tours de protection restants si le Pokémon utilise "Protect" ou "Detect"
        self.leech_seeded_by = None  # Indique si le Pokémon a été "Leech Seeded" par un autre Pokémon
        self.first_attack = True  # Indique si c'est le premier tour du Pokémon dans le combat
        self.disabled_attacks = None  # Indique si les attaques sont désactivées (pour "Disable")
        self.disabled_turns = 0  # Nombre de tours restants sous l'effet de "Disable"
        self.encored_attack = None  # Indique si le Pokémon est sous l'effet de "Encore" et quelle attaque il doit utiliser
        self.encored_turns = 0  # Nombre de tours restants sous l'effet de "Encore"
        self.taunted_turns = 0  # Nombre de tours restants sous l'effet de "Taunt"
        self.last_used_attack = None  # Dernière attaque utilisée par le Pokémon, pour les effets de certaines attaques ou talents
        
        # Attributs pour U-turn et autres attaques de changement forcé
        self.must_switch_after_attack = False  # Indique si le Pokémon doit changer après son attaque (U-turn, Volt Switch, etc.)
        self.switch_reason = None  # Raison du changement forcé ("U-Turn", "Volt Switch", etc.)
        
        # Attributs pour les talents
        self.sturdy_activated = False  # Pour le talent Sturdy (Fermeté)
        self.weight = poke.get('weight', 100.0)  # Poids du Pokémon en kg depuis les données

        # Téracristalisation
        self.tera_type = random.choice(self.types)  # Type de la Téracristalisation
        self.tera_activated = False  # Indique si le Pokémon a été Téracristalisé

    def _calculate_initial_stats(self):
        """Calcule les stats initiales sans modificateurs"""
        self.stats = {}
        self.stats_with_no_modifier = {}
        
        stat_names = ["Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]
        for i, stat in enumerate(stat_names):
            base_value = int(((2 * self.base_stats[stat] + self.ivs[stat] + self.evs[stat] // 4) * 0.5 + 5) * self.nature_modifier[i])
            self.stats[stat] = base_value
            self.stats_with_no_modifier[stat] = base_value

    def has_substitute(self):
        """Retourne True si le Pokémon a un clone actif"""
        return self.substitute_hp > 0

    def is_taunted(self):
        """Retourne True si le Pokémon est sous l'effet de Taunt"""
        return self.taunted_turns > 0

    def terastallize(self, tera_type):
        """
        Téracristallise le Pokémon avec le type spécifié.
        
        :param tera_type: Le type Tera (ex: "Fire", "Water", "Stellar", etc.)
        """
        if self.tera_activated:
            print(f"{self.name} est déjà téracristallisé !")
            return False
            
        self.tera_type = tera_type
        self.tera_activated = True
        self.original_types = self.types.copy()  # Sauvegarder les types originaux
        
        # Le type Stellar garde tous les types et ajoute des bonus spéciaux
        if tera_type != "Stellar":
            self.types = [tera_type]  # Remplacer par le type Tera uniquement
        
        print(f"{self.name} téracristallise en type {tera_type} !")
        return True

    def get_effective_types_for_defense(self):
        """
        Retourne les types effectifs pour le calcul de l'efficacité des attaques reçues.
        """
        if self.tera_activated and self.tera_type != "Stellar":
            return [self.tera_type]
        return self.types

    def is_tera_stab(self, attack_type):
        """
        Détermine si une attaque bénéficie du STAB Tera.
        
        :param attack_type: Type de l'attaque
        :return: Multiplicateur STAB (1.0, 1.5, ou 2.0)
        """
        if not self.tera_activated:
            # STAB normal si pas téracristallisé
            return 1.5 if attack_type in self.types else 1.0
            
        if self.tera_type == "Stellar":
            # Type Stellar : STAB 2.0x pour tous les types une fois chacun
            if hasattr(self, '_stellar_used_types'):
                if attack_type in self._stellar_used_types:
                    return 1.5 if attack_type in self.original_types else 1.0
            else:
                self._stellar_used_types = set()
            
            if attack_type not in self._stellar_used_types:
                self._stellar_used_types.add(attack_type)
                return 2.0
                
            return 1.5 if attack_type in self.original_types else 1.0
        else:
            # Type Tera normal
            if attack_type == self.tera_type:
                # Si le type Tera correspond à un type original : 2.0x
                if attack_type in self.original_types:
                    return 2.0
                # Sinon : 1.5x
                return 1.5
            # STAB adaptatif : garde 1.5x sur les types originaux
            elif attack_type in self.original_types:
                return 1.5
            
            return 1.0

    def actualize_stats(self):
        
        self.stats = {
            "Attack": int(self.calculate_stat(self.base_stats['Attack'],self.ivs['Attack'], self.evs['Attack'], self.nature_modifier[0], self.stats_modifier[0]) * self.hidden_modifier["Attack"]),
            "Defense": int(self.calculate_stat(self.base_stats['Defense'], self.ivs['Defense'], self.evs['Defense'], self.nature_modifier[1], self.stats_modifier[1]) * self.hidden_modifier["Defense"]),
            "Sp. Atk": int(self.calculate_stat(self.base_stats['Sp. Atk'], self.ivs['Sp. Atk'], self.evs['Sp. Atk'], self.nature_modifier[2], self.stats_modifier[2]) * self.hidden_modifier["Sp. Atk"]),
            "Sp. Def": int(self.calculate_stat(self.base_stats['Sp. Def'], self.ivs['Sp. Def'], self.evs['Sp. Def'], self.nature_modifier[3], self.stats_modifier[3]) * self.hidden_modifier["Sp. Def"]),
            "Speed": int(self.calculate_stat(self.base_stats['Speed'], self.ivs['Speed'], self.evs['Speed'], self.nature_modifier[4], self.stats_modifier[4]) * self.hidden_modifier["Speed"] * tailwind_mod(self, self.fight)),
        }

        self.evasion = self.calculate_accuracy_and_evasion(self.ev_and_acc_modifier[0])
        self.accuracy = self.calculate_accuracy_and_evasion(self.ev_and_acc_modifier[1])

        # Vérifier si self.fight existe avant de déclencher les événements
        fight_instance = getattr(self, 'fight', None)
        trigger_item(self, "modify_stat", fight_instance)
        trigger_talent(self, "modify_stat", fight_instance)

    def recalculate_all_stats(self):
        """
        Recalcule toutes les stats du Pokémon, y compris les HP max, après modification des EVs/IVs/nature.
        Utile après avoir modifié les EVs ou la nature d'un Pokémon.
        """
        # Mettre à jour le modificateur de nature
        self.nature_modifier = utilities.nature_chart[self.nature] if self.nature else [1, 1, 1, 1, 1]
        
        # Recalculer les HP max
        old_max_hp = self.max_hp
        self.max_hp = int((2 * self.base_stats['HP'] + self.ivs["HP"] + self.evs['HP'] / 4) * 0.5 + 60)
        
        # Si c'est la première fois ou si le Pokémon est à pleine santé, mettre les HP actuels au max
        if old_max_hp == 0 or self.current_hp == old_max_hp:
            self.current_hp = self.max_hp
        
        # Recalculer les autres stats
        self.stats = {
            "Attack": int(((2 * self.base_stats['Attack'] + self.ivs["Attack"] + self.evs['Attack'] // 4) * 0.5 + 5) * self.nature_modifier[0]),
            "Defense": int(((2 * self.base_stats['Defense'] + self.ivs["Defense"] + self.evs['Defense'] // 4) * 0.5 + 5) * self.nature_modifier[1]),
            "Sp. Atk": int(((2 * self.base_stats['Sp. Atk'] + self.ivs["Sp. Atk"] + self.evs['Sp. Atk'] // 4) * 0.5 + 5) * self.nature_modifier[2]),
            "Sp. Def": int(((2 * self.base_stats['Sp. Def'] + self.ivs["Sp. Def"] + self.evs['Sp. Def'] // 4) * 0.5 + 5) * self.nature_modifier[3]),
            "Speed": int(((2 * self.base_stats['Speed'] + self.ivs["Speed"] + self.evs['Speed'] // 4) * 0.5 + 5) * self.nature_modifier[4])
        }
        
        # Recalculer les stats sans modificateurs
        self.stats_with_no_modifier = {
            "Attack": int(((2 * self.base_stats['Attack'] + self.ivs["Attack"] + self.evs['Attack'] // 4) * 0.5 + 5) * self.nature_modifier[0]),
            "Defense": int(((2 * self.base_stats['Defense'] + self.ivs["Defense"] + self.evs['Defense'] // 4) * 0.5 + 5) * self.nature_modifier[1]),
            "Sp. Atk": int(((2 * self.base_stats['Sp. Atk'] + self.ivs["Sp. Atk"] + self.evs['Sp. Atk'] // 4) * 0.5 + 5) * self.nature_modifier[2]),
            "Sp. Def": int(((2 * self.base_stats['Sp. Def'] + self.ivs["Sp. Def"] + self.evs['Sp. Def'] // 4) * 0.5 + 5) * self.nature_modifier[3]),
            "Speed": int(((2 * self.base_stats['Speed'] + self.ivs["Speed"] + self.evs['Speed'] // 4) * 0.5 + 5) * self.nature_modifier[4])
        }

    def current_stats(self):
        """
        Retourne les stats actuelles du Pokémon, en tenant compte des modificateurs.
        """
        return {
            'HP': self.current_hp,
            'Attack': self.stats['Attack'],
            'Defense': self.stats['Defense'],
            'Sp. Atk': self.stats['Sp. Atk'],
            'Sp. Def': self.stats['Sp. Def'],
            'Speed': self.stats['Speed']
        }
    
    def apply_status(self, status):
        self.status = status
        if status == "sleep":
            self.sleep_counter = 0
        if status == "badly_poisoned":
            self.toxic_counter = 1
    
    def remove_status(self):
        self.status = None
    
    def reset_stats_nd_status(self):
        """
        Réinitialise les stats et les effets de statut d'un Pokémon lorsque le pokémon est switché.
        """
        self.stats_modifier = [0, 0, 0, 0, 0]
        self.ev_and_acc_modifier = [0, 0]
        
        # Réinitialiser les modificateurs cachés (pour les talents de ruine, etc.)
        self.hidden_modifier = {"Attack": 1, "Defense": 1, "Sp. Atk": 1, "Sp. Def": 1, "Speed": 1}
        
        if self.is_confused:
            self.is_confused = False
        self.sturdy_activated = False
        self.flinched = False
        self.protect = False
        self.protect_turns = 0
        self.charging = False
        self.charging_attack = None  # L'attaque en cours de charge
        self.must_recharge = False  # Indique si le Pokémon doit se recharger
        self.power = False
        self.first_attack = True
        self.locked_attack = None  # Réinitialise le verrouillage des objets Choice
        self.encored_attack = None
        self.encored_turns = 0
        self.taunted_turns = 0
        self.last_used_attack = None
        self.disabled_attacks = None  # Réinitialise les attaques désactivées
        
        # Nettoyer les effets de Roost lors du changement
        if hasattr(self, 'lost_flying_from_roost') and self.lost_flying_from_roost:
            if hasattr(self, 'original_types'):
                self.types = self.original_types.copy()  # Restaurer les types originaux
                delattr(self, 'original_types')
            self.lost_flying_from_roost = False
        self.disabled_turns = 0  # Réinitialise le nombre de tours restants
        self.leech_seeded_by = None
        self.substitute_hp = 0
        self.actualize_stats()
    
    ## Printing methods pour debugger
    def print_pokemon_status(self):
        print(f"Nom: {self.name}, HP: {self.current_hp}/{self.max_hp}, Types: {', '.join(self.types)}, Talent: {self.talent}, Nature: {self.nature}")
        print(f"Stats actuelles: {self.current_stats()}")
        print(f"Statut: {self.status if self.status else 'Aucun'}, Confusion: {'Oui' if self.is_confused else 'Non'}")
    
    def print_base_stats(self):
        print(f"Base Stats: {self.base_stats}")
        print(f"EVs: {self.evs}")
        print(f"Nature Modifier: {self.nature_modifier}")
    
    def print_modifiers(self):
        """
        Affiche les modificateurs de stats actuels du Pokémon de façon lisible.
        """
        stat_labels = [
            "Attaque",
            "Défense",
            "Attaque Spéciale",
            "Défense Spéciale",
            "Vitesse",
            "Précision",
            "Évasion"
        ]

        for label, mod in zip(stat_labels, self.stats_modifier + self.ev_and_acc_modifier):
            signe = "+" if mod >= 0 else "-"
            print(f" En {label} : {signe} {abs(mod)}")

    def print_all(self):
        """
        Affiche toutes les informations du Pokémon de manière lisible.
        """
        self.print_pokemon_status()
        self.print_base_stats()
        self.print_modifiers()
        print(f"PV max: {self.max_hp}, PV actuels: {self.current_hp}")
        print(f"Attaques : {self.attack1}, {self.attack2}, {self.attack3}, {self.attack4}")
        print(f"Objet : {self.item}")
        print(f"Évolué : {'Oui' if self.fully_evolved else 'Non'}")
        print(f"En charge : {'Oui' if self.charging else 'Non'}")
        print(f"En protection : {'Oui' if self.protect_turns > 0 else 'Non'}")

    def print_item(self):
        """
        Affiche l'objet tenu par le Pokémon.
        """
        if self.item:
            print(f"{self.name} tient un {self.item}.")
        else:
            print(f"{self.name} ne tient pas d'objet.")

    def init_fight(self, fight):
        self.fight = fight  # ← Ajout important
        self.charging = False  # Booléen pour indiquer si le Pokémon charge
        self.charging_attack = None  # L'attaque en cours de charge
        self.must_recharge = False  # Indique si le Pokémon doit se recharger
        self.actualize_stats()

    def calculate_stat(self, base, iv, ev, nature, modifier):
        """
        Calcule une statistique hors PV selon les formules officielles de Pokémon.
        
        :param base: La base de la statistique
        :param ev: Les EV investis dans cette statistique
        :param nature: Le multiplicateur de la nature (0.9, 1.0 ou 1.1)
        :return: La statistique calculée
        """
        base_value = (2 * base + iv + ev // 4) * 0.5 + 5
        if modifier >= 0:
            modifier = 1 + modifier / 2
        else:
            modifier = 1 / (1 + abs(modifier) / 2)
        return base_value * nature * modifier

    def calculate_accuracy_and_evasion(self, stage_mod):
        """
        Calcule la précision et l'évasion du Pokémon en fonction de ses stats.
        """
        base_value = 1.0
        if stage_mod >= 0:
            modifier = 1 + stage_mod / 2
        else:
            modifier = 1 / (1 + abs(stage_mod) / 3)
        return base_value * modifier

    # ========== SYSTÈME DE PP ==========
    
    def set_attack(self, slot, attack):
        """
        Définit une attaque dans un slot spécifique et initialise ses PP.
        
        :param slot: Numéro du slot (1-4)
        :param attack: L'attaque à assigner
        """
        if slot == 1:
            self.attack1 = attack
            self.max_pp1 = attack.pp if attack else 0
            self.pp1 = self.max_pp1
        elif slot == 2:
            self.attack2 = attack
            self.max_pp2 = attack.pp if attack else 0
            self.pp2 = self.max_pp2
        elif slot == 3:
            self.attack3 = attack
            self.max_pp3 = attack.pp if attack else 0
            self.pp3 = self.max_pp3
        elif slot == 4:
            self.attack4 = attack
            self.max_pp4 = attack.pp if attack else 0
            self.pp4 = self.max_pp4
    
    def get_attack_pp(self, attack):
        """
        Récupère les PP actuels d'une attaque spécifique.
        
        :param attack: L'attaque dont on veut connaître les PP
        :return: PP actuels ou 0 si l'attaque n'est pas trouvée
        """
        if attack == self.attack1:
            return self.pp1
        elif attack == self.attack2:
            return self.pp2
        elif attack == self.attack3:
            return self.pp3
        elif attack == self.attack4:
            return self.pp4
        return 0
    
    def use_pp(self, attack, amount=1):
        """
        Consomme des PP pour une attaque donnée.
        
        :param attack: L'attaque utilisée
        :param amount: Nombre de PP à consommer (défaut: 1)
        :return: True si les PP ont été consommés, False si pas assez de PP
        """
        current_pp = self.get_attack_pp(attack)
        if current_pp < amount:
            return False
        
        if attack == self.attack1:
            self.pp1 = max(0, self.pp1 - amount)
        elif attack == self.attack2:
            self.pp2 = max(0, self.pp2 - amount)
        elif attack == self.attack3:
            self.pp3 = max(0, self.pp3 - amount)
        elif attack == self.attack4:
            self.pp4 = max(0, self.pp4 - amount)
        
        return True
    
    def restore_pp(self, attack, amount):
        """
        Restaure des PP pour une attaque donnée.
        
        :param attack: L'attaque à restaurer
        :param amount: Nombre de PP à restaurer
        """
        if attack == self.attack1:
            self.pp1 = min(self.max_pp1, self.pp1 + amount)
        elif attack == self.attack2:
            self.pp2 = min(self.max_pp2, self.pp2 + amount)
        elif attack == self.attack3:
            self.pp3 = min(self.max_pp3, self.pp3 + amount)
        elif attack == self.attack4:
            self.pp4 = min(self.max_pp4, self.pp4 + amount)
    
    def has_usable_attack(self):
        """
        Vérifie si le Pokémon a au moins une attaque avec des PP disponibles.
        
        :return: True si au moins une attaque a des PP > 0
        """
        return (self.pp1 > 0 and self.attack1 is not None) or \
               (self.pp2 > 0 and self.attack2 is not None) or \
               (self.pp3 > 0 and self.attack3 is not None) or \
               (self.pp4 > 0 and self.attack4 is not None)
    
    def get_usable_attacks(self):
        """
        Retourne la liste des attaques utilisables (avec PP > 0).
        
        :return: Liste des attaques utilisables
        """
        usable = []
        if self.attack1 and self.pp1 > 0:
            usable.append(self.attack1)
        if self.attack2 and self.pp2 > 0:
            usable.append(self.attack2)
        if self.attack3 and self.pp3 > 0:
            usable.append(self.attack3)
        if self.attack4 and self.pp4 > 0:
            usable.append(self.attack4)
        return usable
    
    def restore_all_pp(self):
        """
        Restaure tous les PP au maximum (pour les soins au Centre Pokémon).
        """
        self.pp1 = self.max_pp1
        self.pp2 = self.max_pp2
        self.pp3 = self.max_pp3
        self.pp4 = self.max_pp4
    
def tailwind_mod(poke, fight):
    team_id = fight.get_team_id(poke)
    tailwind_side = fight.tailwind_team1 if team_id == 1 else fight.tailwind_team2

    if tailwind_side != 0:
        return 2.0
    else:
        return 1.0
    
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
    talent_changes = trigger_talent(target_poke, "on_stat_change", stat_changes, source, fight)
    item_changes = trigger_item(target_poke, "on_stat_change", talent_changes, source, fight) # Surtout pour la White Herb
    final_changes = item_changes
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
