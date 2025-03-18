from Controller import Controller

class PassiveController(Controller):
    def take_turn(self):
        if not self.current_target:
            # Les créatures passives tentent toujours de fuir en priorité
            if self.attempt_flee():
                return
            else:
                # Si la fuite échoue, elles deviennent agressives !
                self.current_target = self.choose_target()
        
        if self.current_target and self.current_target.is_alive():
            self.creature.send_attack(self.current_target)