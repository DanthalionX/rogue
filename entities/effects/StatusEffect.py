from Element import *
from enum import Enum

# Enum for Status Effects
class StatusEffectEnum(Enum):
    FEAR = 'FearEffect'
    CONFUSION = 'ConfusionEffect'
    BURNING = 'BurningEffect'

    @property
    def effect_class(self):
        return globals()[self.value]  # Dynamically return the effect class

# Base class for all status effects
class StatusEffect:
    name = "Status"
    def __init__(self, base_duration: float, base_activation_rate: float, elements=None):
        self.base_duration = base_duration
        self.duration = base_duration  # La durée actuelle démarre sur la durée de base
        self.base_activation_rate = base_activation_rate
        self.tick_counter = 0
        self.elements = elements if elements else []

    def apply_effect(self, creature):
        """Applique l'effet une seule fois lors de l'activation initiale."""
        if self.duration <= 0:
            print(f"{self.__class__.__name__} échoue à cause de la résistance élevée de {creature.species}.")
            return

    def update_effect(self, creature):
        self.tick_counter += 1

        # Si le compteur atteint le seuil d'activation
        if self.tick_counter >= self.base_activation_rate:
            self.tick_counter = 0

            self.duration -= 1
            # Si l'effet est actif, on consomme la durée
            if self.duration > 0:
                #print(f"{creature.species} → {self.name} reste {self.duration:.2f} ticks")

                # Si l'effet a une action continue, on l'exécute ici (exemple : BurningEffect)
                self.on_activation(creature)

            # Si la durée est épuisée → on supprime l'effet
            if self.duration <= 0:
                self.remove_effect(creature)

    def on_activation(self, creature):
        """Effet continu déclenché à chaque activation (exemple : brûlure)."""
        pass

    def remove_effect(self, creature):
        """Supprime l'effet."""
        pass

    def alter_duration(self, factor: float):
        """Altère la durée de l'effet en fonction du facteur fourni."""
        self.duration = max(0, self.base_duration * factor)

# Fear Effect (affects Mental)
class FearEffect(StatusEffect):
    def __init__(self, base_duration=3.0):
        super().__init__(base_duration, base_activation_rate=1, elements=[MentalElement])
        self.name = "Peur"

    def apply_effect(self, creature):
        # Effet initial → Réduction de la précision
        creature.stats.accuracy -= 5
        print(f"... {creature.species} est terrifié ! Précision réduite de 5.")

    def on_activation(self, creature):
        # Effet passif → On ne fait rien lors de l'activation
        pass

    def remove_effect(self, creature):
        # On restaure la précision à la fin de l'effet
        creature.stats.accuracy += 5
        print(f"... {creature.species} n'est plus terrifié ! Précision restaurée.")

# Confusion Effect (affects Shadow and Mental)
class ConfusionEffect(StatusEffect):
    def __init__(self, base_duration=3.0):
        super().__init__(base_duration, base_activation_rate=1, elements=[MentalElement, ShadowElement])
        self.name = "Confusion"

    def apply_effect(self, creature):
        # Effet initial → Réduction de l'agilité
        creature.agilite -= 3
        print(f"... {creature.species} est confus ! Agilité réduite de 3.")

    def on_activation(self, creature):
        # Pas d'effet continu → On ne fait rien
        pass

    def remove_effect(self, creature):
        creature.agilite += 3
        print(f"... {creature.species} n'est plus confus ! Agilité restaurée.")

class BurningEffect(StatusEffect):
    def __init__(self, base_duration=3.0):
        super().__init__(base_duration, base_activation_rate=2, elements=[FireElement])
        self.name = "Brûlure"

    def apply_effect(self, creature):
        # Appliquer une première fois lors de l'application de l'effet
        creature.stats.vie -= 5
        print(f"... {creature.species} est en feu ! Perte de 5 points de vie.")

    def on_activation(self, creature):
        # Effet continu → Dégâts supplémentaires à chaque activation
        creature.stats.vie -= 2
        print(f"... {creature.species} brûle ! Perte de 2 points de vie.")

    def remove_effect(self, creature):
        print(f"... {creature.species} n'est plus en feu !")

class HealingEffect(StatusEffect):
    def __init__(self, base_duration=3.0):
        super().__init__(base_duration, base_activation_rate=2, elements=[LightElement])
        self.name = "Regeneration vie"

    def apply_effect(self, creature):
        # Appliquer une première fois lors de l'application de l'effet
        creature.stats.vie += 5
        print(f"... {creature.species} se regenere ! Gain de 5 points de vie.")

    def on_activation(self, creature):
        # Effet continu → Dégâts supplémentaires à chaque activation
        creature.stats.vie += 2
        print(f"... {creature.species} se regenere ! Gain de 2 points de vie.")

    def remove_effect(self, creature):
        print(f"... {creature.species} ne se regenere plus!")