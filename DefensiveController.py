from Controller import Controller
import random

class DefensiveController(Controller):
    def register_enemy(self, creature):
        if creature != self.creature and creature not in self.ennemy_nearby_creatures:
            print(f"{self.creature.species} considère {creature.species} comme une menace après avoir été attaqué !")
            self.neutral_nearby_creatures.remove(creature)
            self.ennemy_nearby_creatures.append(creature)

    def take_turn(self):
        if not self.creature.is_alive() or not self.ennemy_nearby_creatures:
            return
        if self.current_target and self.current_target.is_alive():
            # Si une menace est déjà identifiée, elle attaque
            self.creature.send_attack(self.current_target)
        elif self.ennemy_nearby_creatures :
            # Si une menace existe mais pas de cible en cours → choisir la menace la plus faible
            self.current_target = self.choose_target()
            print(f"{self.creature.species} cible {self.current_target.species} en défense !")
        else:
            self.current_target = None

    def choose_target(self):
        target = None
        valid_hostile_targets = [c for c in self.ennemy_nearby_creatures if c.is_alive()]
        if valid_hostile_targets:
            target = random.choice(valid_hostile_targets)
        if target:
            print(f"{self.creature.species} choisit {target.species} comme cible.")
        else:
            print(f"{self.creature.species} n'a trouvé aucune cible valide.")
        return target