
from dataclasses import dataclass
from typing import Optional, List
from utils import Size
from Trait import *
from skills.Skill import *

@dataclass
class CreatureTemplate:
    species: Optional[str] = None  
    constitution: Optional[int] = None
    agilite: Optional[int] = None
    erudition: Optional[int] = None
    size: Optional[Size] = None
    basic_trait: Optional[Trait] = None
    traits: Optional[List[Trait]] = None
    nb_standard_traits: Optional[int] = None
    skills: Optional[List[Skill]] = None
    locked_traits: Optional[List[Trait]] = None
    locked_skills: Optional[List[Skill]] = None
