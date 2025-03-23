from Controller import Controller
import random

class PassiveController(Controller):
    def take_turn(self):
        if not self.creature.is_alive() or not self.ennemy_nearby_creatures:
            return
        if not self.current_target:
            # Les créatures passives tentent toujours de fuir en priorité
            if self.attempt_flee():
                return
            else:
                # Si la fuite échoue, elles deviennent agressives contre leurs aggresseurs !
                self.current_target = self.choose_target()
        
        if self.current_target and self.current_target.is_alive():
            self.creature.send_attack(self.current_target)

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