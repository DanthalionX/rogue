import random

class Controller:
    def __init__(self, creature):
        self.creature = creature
        self.nearby_creatures = []
        self.neutral_nearby_creatures = []
        self.ennemy_nearby_creatures = []
        self.ally_nearby_creatures = []
        self.current_target = None

    def register_enemy(self, creature):
        if not self.creature.is_alive():
            return
        if self.current_target != creature:
            if creature in self.neutral_nearby_creatures:
                self.neutral_nearby_creatures.remove(creature)
                print(f"{self.creature.species} n'est plus indifférent à {creature.species} !")
            if creature not in self.ennemy_nearby_creatures:
                self.ennemy_nearby_creatures.append(creature)
                print(f"{self.creature.species} considère {creature.species} comme une menace !")

    def take_turn(self):
        pass
    
    def attempt_flee(self):
        # Calcul de la chance de fuite basée sur l'agilité et la chance
        flee_chance = self.creature.stats.esquive + self.creature.stats.chance
        success_chance = random.uniform(0, 100)
        
        if success_chance <= flee_chance:
            print(f"{self.creature.species} a réussi à fuir !")
            # Retirer la créature des listes des autres créatures
            for creature in self.nearby_creatures:
                creature.controller.remove_from_nearby(self.creature)
            self.current_target = None
            self.set_nearby_creatures([])
            self.creature.has_fled = True
            return True
        else:
            print(f"{self.creature.species} a échoué dans sa tentative de fuite...")
            return False
        
    def set_nearby_creatures(self, nearby_creatures):
        self.nearby_creatures = [c for c in nearby_creatures if c != self.creature]
        self.neutral_nearby_creatures = [c for c in nearby_creatures if c != self.creature]
        self.ennemy_nearby_creatures = []
        self.ally_nearby_creatures = []

    def remove_from_nearby(self, creature):
        if creature in self.nearby_creatures:
            self.nearby_creatures.remove(creature)
        if creature in self.ennemy_nearby_creatures:
            self.ennemy_nearby_creatures.remove(creature)
        if creature in self.neutral_nearby_creatures:
            self.neutral_nearby_creatures.remove(creature)
        if creature == self.current_target:
            self.current_target = None

    def die(self):
        print(f"{self.species} est mort !")
        for creature in self.controller.nearby_creatures:
            creature.controller.remove_from_nearby(self)