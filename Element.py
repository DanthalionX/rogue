from enum import Enum

class Element:
    nom = "Élément"

    def __init__(self):
        self.resistance = 0
        self.puissance = 0

# Ajout de l'énumération ElementEnum
class ElementEnum(Enum):
    FIRE = "FireElement"
    WATER = "WaterElement"
    AIR = "AirElement"
    EARTH = "EarthElement"
    LIGHT = "LightElement"
    SHADOW = "ShadowElement"

    @property
    def element_class(self):
        return globals()[self.value]

class PhysicalElement(Element):
    pass

class MentalElement(Element):
    pass

class BluntElement(PhysicalElement):
    def __init__(self):
        super().__init__()
        self.nom = "Contondant"
        self.resistance = 5
        self.puissance = 10

class SharpElement(PhysicalElement):
    def __init__(self):
        super().__init__()
        self.nom = "Tranchant"
        self.resistance = 3
        self.puissance = 12

class PercingElement(PhysicalElement):
    def __init__(self):
        super().__init__()
        self.nom = "Perçant"
        self.resistance = 4
        self.puissance = 11

class FireElement(Element):
    def __init__(self):
        super().__init__()
        self.nom = "Feu"
        self.resistance = 2
        self.puissance = 8

class WaterElement(Element):
    def __init__(self):
        super().__init__()
        self.nom = "Eau"
        self.resistance = 3
        self.puissance = 7

class AirElement(Element):
    def __init__(self):
        super().__init__()
        self.nom = "Air"
        self.resistance = 1
        self.puissance = 5

class EarthElement(Element):
    def __init__(self):
        super().__init__()
        self.nom = "Terre"
        self.resistance = 4
        self.puissance = 6

class LightElement(Element):
    def __init__(self):
        super().__init__()
        self.nom = "Lumière"
        self.resistance = 3
        self.puissance = 7

class ShadowElement(Element):
    def __init__(self):
        super().__init__()
        self.nom = "Ombre"
        self.resistance = 3
        self.puissance = 9
