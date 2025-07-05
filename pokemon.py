import random
import donnees # Données de la table des types et des natures
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

        ## EVs
        self.evs = {
            'HP': 0,
            'Attack': 0,
            'Defense': 0,
            'Sp. Atk': 0,
            'Sp. Def': 0,
            'Speed': 0,
        }

        ## Les stats dans le combat
        self.stats_modifier = [0, 0, 0, 0, 0]  # Modificateurs de stats pour Attack, Defense, Sp. Atk, Sp. Def, Speed
        self.ev_and_acc_modifier = [0, 0]  # Modificateurs d'évasion et de précision 

        self.nature_modifier = donnees.nature_chart[self.nature] if self.nature else [1, 1, 1, 1, 1]
        self.stats = {
                "Attack": int(((2 * self.base_stats['Attack'] + 31 + self.evs['Attack'] // 4) // 2 + 5) * self.nature_modifier[0]),
                "Defense": int(((2 * self.base_stats['Defense'] + 31 + self.evs['Defense'] // 4) // 2 + 5) * self.nature_modifier[1]),
                "Sp. Atk": int(((2 * self.base_stats['Sp. Atk'] + 31 + self.evs['Sp. Atk'] // 4) // 2 + 5) * self.nature_modifier[2]),
                "Sp. Def": int(((2 * self.base_stats['Sp. Def'] + 31 + self.evs['Sp. Def'] // 4) // 2 + 5) * self.nature_modifier[3]),
                "Speed": int(((2 * self.base_stats['Speed'] + 31 + self.evs['Speed'] // 4) // 2 + 5) * self.nature_modifier[4])
            }

        self.accuracy = 1.0  # Précision du Pokémon (par exemple : 1.0 pour 100% de précision)
        self.evasion = 1.0  # Évasion du Pokémon (par exemple : 1.0 pour 100% d'évasion)
            
        ## ATTACKS : Les attaques ne sont pas mises à l'initialisation du Pokémon, mais lorsque l'on modifie le Pokémon pour le combat.
        self.attack1 = None
        self.attack2 = None
        self.attack3 = None
        self.attack4 = None
        
        self.max_hp =  int((2 * self.base_stats['HP'] + 31 + self.evs['HP'] / 4) * 0.5 + 60)   # Points de vie maximum
        self.current_hp = self.max_hp  # Points de vie actuels
        
        self.status = None  # Statut du Pokémon (par exemple : "Brûlé", "Gelé", etc.)
        self.is_confused = False  # Indique si le Pokémon est confus
        self.power = False # Indique si le Pokémon est sous l'effet de puissance (qui booste le taux de crits)
        self.charging = False  # Indique si le Pokémon est en train de charger une attaque (par exemple : "Meteor Beam", "Solar Beam", etc.)
        self.sleep_counter = 0  # Nombre de tours de sommeil restants si le Pokémon est endormi
        self.poison_counter = 0  # Nombre de tours de poison restants si le Pokémon est gravement empoisonné vu que les degats augmentent à chaque tour
        self.protect_turns = 0  # Nombre de tours de protection restants si le Pokémon utilise "Protect" ou "Detect"
        self.still_confused = False  # Indique si le Pokémon est toujours confus au prochain tour
        self.locked_move = None  # Pour gérer Choice Band/Specs/Scarf
        self.fully_evolved = poke['fully_evolved'] if 'fully_evolved' in poke else False  # Indique si le Pokémon est entièrement évolué

    def actualize_stats(self):
        """
        Met à jour les stats du Pokémon en fonction de ses EVs, IVs, nature et modificateurs de stats.
        """
        def calculate_stat(base, ev, nature_mod, stage_mod):
            base_value = (2 * base + 31 + ev // 4) // 2 + 5
            if stage_mod >= 0:
                modifier = 1 + stage_mod / 2
            else:
                modifier = 1 / (1 + abs(stage_mod) / 2)
            return int(base_value * nature_mod * modifier)
        
        def calculate_accuracy_and_evasion(stage_mod):
            """
            Calcule la précision et l'évasion du Pokémon en fonction de ses stats.
            """
            base_value = 1.0
            if stage_mod >= 0:
                modifier = 1 + stage_mod / 2
            else:
                modifier = 1 / (1 + abs(stage_mod) / 3)
            return base_value * modifier

        self.stats = {
            "Attack": calculate_stat(self.base_stats['Attack'], self.evs['Attack'], self.nature_modifier[0], self.stats_modifier[0]),
            "Defense": calculate_stat(self.base_stats['Defense'], self.evs['Defense'], self.nature_modifier[1], self.stats_modifier[1]),
            "Sp. Atk": calculate_stat(self.base_stats['Sp. Atk'], self.evs['Sp. Atk'], self.nature_modifier[2], self.stats_modifier[2]),
            "Sp. Def": calculate_stat(self.base_stats['Sp. Def'], self.evs['Sp. Def'], self.nature_modifier[3], self.stats_modifier[3]),
            "Speed": calculate_stat(self.base_stats['Speed'], self.evs['Speed'], self.nature_modifier[4], self.stats_modifier[4])
        }

        self.evasion = calculate_accuracy_and_evasion(self.ev_and_acc_modifier[0])
        self.accuracy = calculate_accuracy_and_evasion(self.ev_and_acc_modifier[1])
        
    
    def set_nature(self, nature):
        """
        Définit la nature du Pokémon et met à jour les stats en conséquence.
        :param nature: Nature du Pokémon (par exemple : "Hardy", "Lonely", etc.)
        """
        if nature in donnees.nature_chart:
            self.nature = nature
            self.nature_modifier = donnees.nature_chart[nature]
            self.actualize_stats()
        else:
            raise ValueError(f"Nature '{nature}' inconnue.")



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
            self.sleep_counter = random.randint(1, 3)
        if status == "badly_poisoned":
            self.toxic_counter = 1
    
    def remove_status(self):
        self.status = None
    
    ## Printing methods pour debugger
    def print_pokemon_status(self):
        print(f"Nom: {self.name}, HP: {self.current_hp}/{self.max_hp}, Types: {', '.join(self.types)}, Talent: {self.talent}, Nature: {self.nature}")
        print(f"Stats actuelles: {self.current_stats()}")
        print(f"Statut: {self.status if self.status else 'Aucun'}, Confusion: {'Oui' if self.is_confused else 'Non'}")
    
    def print_base_stats(self):
        print(f"Nom: {self.name}")
        print(f"Base Stats: {self.base_stats}")
        print(f"EVs: {self.evs}")
        print(f"Stats: {self.stats}")
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