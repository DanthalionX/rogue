from utils import generer_nom_aleatoire
from enum import Enum
from Element import *
import random

class TraitType(Enum):
    BASIC = "BASIC"
    STANDARD = "STANDARD"

class Trait:
    def __init__(self, trait_type: TraitType):
        self.nom_trait = "Trait générique"
        self.trait_type = trait_type
        self.required_traits = []
        self.incompatible_traits = []

# Définition de l'énumération des traits
class TraitEnum(Enum):
    FLYING = "FlyingTrait"
    UNDEAD = "UndeadTrait"
    RIDABLE = "RidableTrait"
    TAMABLE = "TamableTrait"
    LIVING = "LivingTrait"
    NAMED = "NamedTrait"
    ELEMENT_AFFINITY = "ElementAffinityTrait"

    @property
    def trait_class(self):
        return globals()[self.value]
    
    def get_instance(self):
        return self.trait_class()

class FlyingTrait(Trait):
    def __init__(self):
        super().__init__(TraitType.STANDARD)
        self.nom_trait = "Volant"
        self.can_fly = True
        self.flight_speed = 10

class UndeadTrait(Trait):
    def __init__(self, master=None):
        super().__init__(TraitType.BASIC)
        self.nom_trait = "Mort-vivant"
        self.master = master

class RidableTrait(Trait):
    def __init__(self):
        super().__init__(TraitType.STANDARD)
        self.nom_trait = "Monture"
        self.is_ridable = True
        self.carry_weight = 50

class TamableTrait(Trait):
    def __init__(self):
        super().__init__(TraitType.STANDARD)
        self.nom_trait = "Apprivoisable"
        self.is_tamable = True

class LivingTrait(Trait):
    def __init__(self):
        super().__init__(TraitType.BASIC)
        self.nom_trait = "Vivant"
        self.is_living = True

class NamedTrait(Trait):
    def __init__(self):
        super().__init__(TraitType.STANDARD)
        self.nom_trait = "Nommé"
        self.name = generer_nom_aleatoire()

class ElementAffinityTrait(Trait):
    def __init__(self):
        super().__init__(TraitType.STANDARD)
        element = random.choice(list(ElementEnum)).element_class()  
        self.nom_trait = f"Affinité {element.nom}"
        self.element_affinity_modifiers = element
