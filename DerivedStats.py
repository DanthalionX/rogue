from Element import *

class DerivedStats:
    def __init__(self, creature, size):
        self.creature = creature
        self.size = size

        # Esquive basée sur l'agilité et la taille
        self.esquive = round(self.creature.agilite * (10 / self.size.value), 2)

        # Précision basée sur l'agilité
        self.accuracy = round(self.creature.agilite * 1.2, 2)

        # Points de vie max basés sur la constitution
        self.vie_max = round(self.creature.constitution * 5, 2)
        self.vie = self.vie_max

        # Énergie max basée sur l'érudition
        self.energie_max = round(self.creature.erudition * 5, 2)
        self.energie = self.energie_max

        # Vitesse d'attaque basée sur l'agilité
        self.attack_speed = round(max(0.5, (self.creature.agilite / 20) * 2.0), 2)

        # Chance par défaut à 1%
        self.chance = 1

        # Accumulateur de ticks pour l'attaque
        self.attack_timer = 0

    def initialiser_resistances_et_puissances(self):
        # Résistances physiques
        self.creature.resistances[BluntElement] = round(self.creature.constitution * 0.5, 2)
        self.creature.resistances[SharpElement] = round(self.creature.constitution * 0.4, 2)
        self.creature.resistances[PercingElement] = round(self.creature.constitution * 0.45, 2)

        # Résistances élémentaires
        self.creature.resistances[FireElement] = round(self.creature.constitution * 0.35, 2)
        self.creature.resistances[WaterElement] = round(self.creature.constitution * 0.4, 2)
        self.creature.resistances[AirElement] = round(self.creature.constitution * 0.3, 2)
        self.creature.resistances[EarthElement] = round(self.creature.constitution * 0.45, 2)
        self.creature.resistances[LightElement] = round(self.creature.constitution * 0.4, 2)
        self.creature.resistances[ShadowElement] = round(self.creature.constitution * 0.35, 2)

        # Résistances mentales
        self.creature.resistances[MentalElement] = round(self.creature.erudition * 0.5, 2)

        # Puissances physiques
        self.creature.puissances[BluntElement] = round(self.creature.constitution * 0.75, 2)
        self.creature.puissances[SharpElement] = round(self.creature.agilite * 0.9, 2)
        self.creature.puissances[PercingElement] = round(self.creature.agilite * 0.85, 2)

        # Puissances élémentaires
        self.creature.puissances[FireElement] = round(self.creature.erudition * 1.0, 2)
        self.creature.puissances[WaterElement] = round(self.creature.erudition * 0.95, 2)
        self.creature.puissances[AirElement] = round(self.creature.erudition * 0.85, 2)
        self.creature.puissances[EarthElement] = round(self.creature.erudition * 0.9, 2)
        self.creature.puissances[LightElement] = round(self.creature.erudition * 0.95, 2)
        self.creature.puissances[ShadowElement] = round(self.creature.erudition * 1.0, 2)

        # Puissance mentale
        self.creature.puissances[MentalElement] = round(self.creature.erudition * 1.1, 2)
