
from dataclasses import dataclass
from typing import Optional, List
from Creature import Size
from Trait import Trait
from Skill import Skill

@dataclass
class CreatureTemplate:
    species: Optional[str] = None  # ✅ Ajout de l'attribut species
    constitution: Optional[int] = None
    agilite: Optional[int] = None
    erudition: Optional[int] = None
    size: Optional[Size] = None
    basic_trait: Optional[Trait] = None
    traits: Optional[List[Trait]] = None
    nb_standard_traits: Optional[int] = None
    skills: Optional[List[Skill]] = None
