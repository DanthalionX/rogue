from Controller import Controller
import random

class HostileController(Controller):
    def take_turn(self):
        if not self.creature.is_alive():
            return
        # On ne change pas de cible si il y a une cible déjà définie et qu'elle est en vie
        if not self.current_target or not self.current_target.is_alive():
            self.current_target = self.choose_target()
            self.register_enemy(self.current_target)
        
        if self.current_target and self.current_target.is_alive():
            # Attaque basique → Définit automatiquement la cible comme ennemie
            self.creature.send_attack(self.current_target)
            self.current_target.controller.register_enemy(self.creature)

    def choose_target(self):
        target = None
        valid_hostile_targets = [c for c in self.ennemy_nearby_creatures if c.is_alive()]
        valid_neutral_targets = [c for c in self.neutral_nearby_creatures if c.is_alive()]
        if valid_hostile_targets:
            target = random.choice(valid_hostile_targets)
        elif valid_neutral_targets:
            target = random.choice(valid_neutral_targets)
            self.neutral_nearby_creatures.remove(target)
            self.ennemy_nearby_creatures.append(target)
    
        if target:
            print(f"{self.creature.species} choisit {target.species} comme cible.")
        else:
            print(f"{self.creature.species} n'a trouvé aucune cible valide.")
        return target