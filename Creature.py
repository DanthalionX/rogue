
from Element import *
from Trait import *
from Skill import *
from DerivedStats import *
from CreatureTemplate import *
from utils import generer_nom_espece
from enum import Enum
from StatusEffectManager import StatusEffectManager

import random

class Size(Enum):
    XS = 3
    S = 4
    M = 5
    L = 6
    XL = 7

class BaseStats:
    def __init__(self, constitution: int, agilite: int, erudition: int):
        self.constitution = constitution
        self.agilite = agilite
        self.erudition = erudition

class Creature(BaseStats, DerivedStats):
    def __init__(self, species, constitution, agilite, erudition, size, basic_trait, *additional_traits):
        self.species = species
        self.constitution = constitution
        self.agilite = agilite
        self.erudition = erudition
        self.size = size
        self.status_effect_manager = StatusEffectManager(self)  # Initialize the effect manager


        # Initialisation des résistances et puissances
        self.resistances = {}
        self.puissances = {}

        # Initialisation des traits et compétences
        self.traits = [basic_trait] + list(additional_traits)
        self.skills = []

        # Initialisation des statistiques dynamiques
        self.stats = DerivedStats(self, size)
        self.stats.initialiser_resistances_et_puissances()

    @classmethod
    def generer_aleatoire(cls, template=None):
        from utils import generer_nom_espece
        from Trait import TraitEnum, TraitType

        constitution = template.constitution if template and template.constitution is not None else random.randint(5, 20)
        agilite = template.agilite if template and template.agilite is not None else random.randint(5, 20)
        erudition = template.erudition if template and template.erudition is not None else random.randint(5, 20)
        size = template.size if template and template.size is not None else random.choice(list(Size))
        species = template.species if template and template.species is not None else generer_nom_espece()

        # Sélection d'un trait BASIC obligatoire
        if template and template.basic_trait:
            basic_trait = template.basic_trait
        else:
            basic_trait_enum = random.choice([t for t in TraitEnum if t.trait_class().trait_type == TraitType.BASIC])
            basic_trait = basic_trait_enum.trait_class()

        # Compléter automatiquement les traits standards
        existing_traits = template.traits if template and template.traits else []
        nb_standard_traits = template.nb_standard_traits if template and template.nb_standard_traits is not None else random.randint(0, 5)

        while len(existing_traits) < nb_standard_traits:
            trait_enum = random.choice([t for t in TraitEnum if t.trait_class().trait_type == TraitType.STANDARD])
            trait_class = trait_enum.trait_class
            trait_instance = trait_class()
            if all(not isinstance(t, trait_class) for t in existing_traits):
                existing_traits.append(trait_instance)

        # Gestion des compétences
        existing_skills = template.skills if template and template.skills else []

        # Création de la créature
        creature = cls(
            species,
            constitution,
            agilite,
            erudition,
            size,
            basic_trait,
            *existing_traits
        )

        # Ajout des compétences à la créature
        creature.skills.extend(existing_skills)

        return creature
    
    def afficher_stats(self):
        named_trait = next((trait for trait in self.traits if isinstance(trait, NamedTrait)), None)
        display_name = f"{self.species} {self.size.name} ({named_trait.creature_name})" if named_trait else self.species

        stats = f"""
        {display_name} - {self.size.name} - HP : {self.stats.vie:.2f}/{self.stats.vie_max:.2f}, EP : {self.stats.endurance:.2f}/{self.stats.endurance_max:.2f}, MP : {self.stats.mana:.2f}/{self.stats.mana_max:.2f},
        Traits : {', '.join([trait.name for trait in self.traits]) or 'Aucun'}
        Statistiques : CON:{self.constitution} AGI:{self.agilite} ERU:{self.erudition} -> Esquive : {self.stats.esquive:.2f}, Précision : {self.stats.accuracy:.2f}, Rapidité : {self.stats.attack_speed:.2f}
        Compétences : {', '.join([skill.name for skill in self.skills]) or 'Aucune'}
        Résistances : {', '.join(f"{element().name}: {value:.2f}" for element, value in self.resistances.items())}
        Puissances : {', '.join(f"{element().name}: {value:.2f}" for element, value in self.puissances.items())}
        Effets actifs : {', '.join([f"{effect.name}({effect.duration:.2f})" for effect in self.status_effect_manager.active_effects]) or 'Aucun'}
        """
        print(stats)
    
    def add_trait(self, trait):
        # Vérification des doublons
        if any(isinstance(t, type(trait)) for t in self.traits):
            return
        
        # Vérification des dépendances
        for req in trait.required_traits:
            if not any(isinstance(t, req) for t in self.traits):
                self.add_trait(req())

        # Ajout du trait
        self.traits.append(trait)

    def add_skill(self, skill):
        if any(isinstance(s, type(skill)) for s in self.skills):
            return
        
        # Vérification des dépendances
        for req in skill.required_skills:
            if not any(isinstance(s, req) for s in self.skills):
                print(f"Impossible d'ajouter {skill.__class__.__name__} — Dépendance manquante ({req.__name__})")
                return
    
        self.skills.append(skill)

    def send_attack(self, target):
        if self.stats.endurance < 2:
            print(f"{self.species} est trop fatigué pour attaquer !")
            return
        self.stats.endurance -= 2
        # Vérification de la chance de l'attaquant (1% par point de chance)
        if random.randint(1, 100) <= self.stats.chance:
            print(f"{self.species} réussit une attaque critique grâce à sa chance !")
        elif random.randint(1, 100) <= target.stats.chance:
            print(f"{target.species} réussit une esquive critique !")
            return
        else:
            # Comparaison entre la précision de l'attaquant et l'esquive de la cible
            if random.randint(1, 100) <= target.stats.esquive - self.stats.accuracy:
                print(f"{target.species} esquive l'attaque de {self.species} !")
                return

        # Sélection du meilleur élément d'attaque basé sur la puissance et la faiblesse de la cible
        best_element = max(self.puissances, key=lambda element: self.puissances[element] - target.resistances[element])
        damage = self.puissances[best_element] - target.resistances[best_element]

        if damage > 0:
            target.stats.vie -= damage
            print(f"{self.species} inflige {damage:.2f} points de dégâts ({best_element.__name__}) à {target.species} !")
        else:
            print(f"{self.species} ne parvient pas à percer la résistance de {target.species} !")
        
    def cast_skill(self, skill_enum, target):
        skill_type = skill_enum.skill_class
        for skill in self.skills:
            if isinstance(skill, skill_type):
                if self.stats.mana < skill.mana_cost or self.stats.endurance < skill.endurance_cost:
                    print(f"{self.species} n'a pas assez de ressources pour utiliser {skill_enum.name}")
                    return
                print(f"{self.species} → Lance {skill.name} à {target.species}")
                self.stats.mana -= skill.mana_cost
                self.stats.endurance -= skill.endurance_cost
                skill.activate(self, target)
                effect = skill.get_effect()
                if effect:
                    print(f"{self.species} → Tente d'appliquer {effect.name} à {target.species}")
                    target.status_effect_manager.apply_effect(effect)
                return
        print(f"{self.species} n'a pas la compétence {skill_enum.name}")

    def is_alive(self):
        return self.stats.vie > 0

    def choose_best_attack(self, target):
        best_element = None
        best_score = float('-inf')

        for element, power in self.puissances.items():
            resistance = target.resistances.get(element, 0)
            score = power - resistance
            if score > best_score:
                best_score = score
                best_element = element

        return best_element    
    
    def add_status_effect(self, effect):
        self.status_effect_manager.apply_effect(effect)

    def update_status_effects(self):
        self.status_effect_manager.update_effects()

    def remove_status_effect(self, effect):
        self.status_effect_manager.remove_effect(effect)
