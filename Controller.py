
import random

class Controller:

    def __init__(self, creature, nearby_creatures):
        self.creature = creature
        self.nearby_creatures = [c for c in nearby_creatures if c != self.creature]
        self.neutral_nearby_creatures = [c for c in nearby_creatures if c != self.creature]
        self.ally_nearby_creatures = []
        self.ennemy_nearby_creatures = []
        self.current_target = None

    def choose_target(self):
        # IA agressive → Cible la créature avec le moins de résistances
        target = None
        if [c for c in self.ennemy_nearby_creatures if c.is_alive()]:
            target = random.choice([c for c in self.ennemy_nearby_creatures if c.is_alive()])
            print(f"{self.creature.species} cible {target.species} !")
        elif [c for c in self.neutral_nearby_creatures if c.is_alive()]:
            target = random.choice([c for c in self.neutral_nearby_creatures if c.is_alive()])
            print(f"{self.creature.species} cible {target.species} !")
        else:
            print(f'Aucune cible potentielle pour {self.creature.species}')
        return target

    def take_turn(self):
        # On ne change pas de cible si il y a une cible déjà définie et qu'elle est en vie
        if not self.current_target or not self.current_target.is_alive():
            self.current_target = self.choose_target()
            self.register_enemy(self.current_target)
        
        if self.current_target and self.current_target.is_alive():
            # Attaque basique → Définit automatiquement la cible comme ennemie
            self.creature.send_attack(self.current_target)
            self.current_target.controller.register_enemy(self.creature)

    def register_enemy(self, creature):
        if creature in self.neutral_nearby_creatures:
            self.neutral_nearby_creatures.remove(creature)
            print(f"{self.creature.species} n'est plus indifférent à {creature.species} !")
        if creature not in self.ennemy_nearby_creatures:
            self.ennemy_nearby_creatures.append(creature)
            print(f"{self.creature.species} considère {creature.species} comme une menace !")
