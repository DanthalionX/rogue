from enum import Enum

class Element:
    name = "Élément"

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
    def __init__(self):
        super().__init__()
        self.name = "Physique"

class MentalElement(Element):
    def __init__(self):
        super().__init__()
        self.name = "Mental"

class BluntElement(PhysicalElement):
    def __init__(self):
        super().__init__()
        self.name = "Contondant"
        self.resistance = 5
        self.puissance = 10

class SharpElement(PhysicalElement):
    def __init__(self):
        super().__init__()
        self.name = "Tranchant"
        self.resistance = 3
        self.puissance = 12

class PercingElement(PhysicalElement):
    def __init__(self):
        super().__init__()
        self.name = "Perçant"
        self.resistance = 4
        self.puissance = 11

class FireElement(Element):
    def __init__(self):
        super().__init__()
        self.name = "Feu"
        self.resistance = 2
        self.puissance = 8

class WaterElement(Element):
    def __init__(self):
        super().__init__()
        self.name = "Eau"
        self.resistance = 3
        self.puissance = 7

class AirElement(Element):
    def __init__(self):
        super().__init__()
        self.name = "Air"
        self.resistance = 1
        self.puissance = 5

class EarthElement(Element):
    def __init__(self):
        super().__init__()
        self.name = "Terre"
        self.resistance = 4
        self.puissance = 6

class LightElement(Element):
    def __init__(self):
        super().__init__()
        self.name = "Lumière"
        self.resistance = 3
        self.puissance = 7

class ShadowElement(Element):
    def __init__(self):
        super().__init__()
        self.name = "Ombre"
        self.resistance = 3
        self.puissance = 9
