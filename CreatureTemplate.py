from dataclasses import dataclass
from typing import Optional, List
from Trait import Trait
from Skill import Skill

@dataclass
class CreatureTemplate:
    constitution: Optional[int] = None
    agilite: Optional[int] = None
    erudition: Optional[int] = None
    size: Optional['Size'] = None  # Annotation en string pour éviter les problèmes de circularité
    basic_trait: Optional[Trait] = None
    traits: Optional[List[Trait]] = None
    nb_standard_traits: Optional[int] = None
    skills: Optional[List[Skill]] = None

    def __post_init__(self):
        from Creature import Size  # ✅ Import local dans le post-init
        if self.size and not isinstance(self.size, Size):
            raise TypeError(f"Invalid size type: {type(self.size)}")
