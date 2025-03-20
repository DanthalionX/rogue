
class StatusEffectManager:
    def __init__(self, creature):
        self.creature = creature
        self.active_effects = []

    def apply_effect(self, effect):
        # Vérification pour éviter les doublons
        for active_effect in self.active_effects:
            if type(active_effect) == type(effect):
                print(f"> {self.creature.species} est déjà affecté par {effect.__class__.__name__}.")
                return
        
        # Vérification de la résistance → Ajustement de la durée
        if effect.elements:
            for element in effect.elements:
                resistance = self.creature.resistances.get(element, 0)
                factor = max(0.1, 1.0 - (resistance / 100))  # Minimum de 10% de durée
                effect.alter_duration(factor)

        # ✅ Si la durée après ajustement est > 0 → On applique
        if effect.duration > 0:
            self.active_effects.append(effect)
            effect.apply_effect(self.creature)
            print(f"> {self.creature.species} est maintenant sous l'effet de {effect.__class__.__name__} pour {effect.duration:.2f} ticks.")
        else:
            print(f"> L'effet {effect.__class__.__name__} a été annulé à cause de la résistance élevée de {self.creature.species}.")

    def update_effects(self):
        for effect in self.active_effects:
            effect.update_effect(self.creature)

        # On retire les effets expirés
        self.active_effects = [effect for effect in self.active_effects if effect.duration > 0]

    def remove_effect(self, effect):
        if effect in self.active_effects:
            self.active_effects.remove(effect)
            effect.remove_effect(self.creature)

    def remove_all_effects(self):
        for effect in self.active_effects:
            effect.remove_effect(self.creature)
        self.active_effects.clear()
