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
    
    def attempt_flee(self):
        # Calcul de la chance de fuite basée sur l'agilité et la chance
        flee_chance = self.creature.stats.esquive + self.creature.stats.chance
        success_chance = random.uniform(0, 100)
        
        if success_chance <= flee_chance:
            print(f"{self.creature.species} a réussi à fuir !")
            # Retirer la créature des listes d'ennemis des autres créatures
            for other in self.nearby_creatures:
                if self.creature in other.controller.ennemy_nearby_creatures:
                    other.controller.ennemy_nearby_creatures.remove(self.creature)
            # Retirer de la liste des créatures proches
            self.nearby_creatures.clear()
            return True
        else:
            print(f"{self.creature.species} a échoué dans sa tentative de fuite...")
            return False