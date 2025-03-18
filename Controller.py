import random

class Controller:
    def __init__(self, creature, nearby_creatures):
        self.creature = creature
        self.nearby_creatures = [c for c in nearby_creatures if c != creature]
        self.neutral_nearby_creatures = self.nearby_creatures.copy()
        self.ennemy_nearby_creatures = []
        self.ally_nearby_creatures = []
        self.current_target = None

    def register_enemy(self, creature):
        if self.current_target != creature:
            if creature in self.neutral_nearby_creatures:
                self.neutral_nearby_creatures.remove(creature)
                print(f"{self.creature.species} n'est plus indifférent à {creature.species} !")
            if creature not in self.ennemy_nearby_creatures:
                self.ennemy_nearby_creatures.append(creature)
                print(f"{self.creature.species} considère {creature.species} comme une menace !")

    def choose_target(self):
        target = None
        valid_hostile_targets = [c for c in self.ennemy_nearby_creatures if c.is_alive()]
        valid_neutral_targets = [c for c in self.neutral_nearby_creatures if c.is_alive()]
        if valid_hostile_targets:
            target = random.choice(valid_hostile_targets)
        elif valid_neutral_targets:
            target = random.choice(valid_neutral_targets)
            self.ennemy_nearby_creatures.append(target)
        return target

    def take_turn(self):
        pass