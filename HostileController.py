from Controller import Controller

class HostileController(Controller):
    def __init__(self, creature, nearby_creatures):
        super().__init__(creature, nearby_creatures)

    def take_turn(self):
        # On ne change pas de cible si il y a une cible déjà définie et qu'elle est en vie
        if not self.current_target or not self.current_target.is_alive():
            self.current_target = self.choose_target()
            self.register_enemy(self.current_target)
        
        if self.current_target and self.current_target.is_alive():
            # Attaque basique → Définit automatiquement la cible comme ennemie
            self.creature.send_attack(self.current_target)
            self.current_target.controller.register_enemy(self.creature)
