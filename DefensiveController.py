from Controller import Controller

class DefensiveController(Controller):
    def __init__(self, creature, nearby_creatures):
        super().__init__(creature, nearby_creatures)

    def register_enemy(self, creature):
        if creature != self.creature and creature not in self.ennemy_nearby_creatures:
            print(f"{self.creature.species} considère {creature.species} comme une menace après avoir été attaqué !")
            self.ennemy_nearby_creatures.append(creature)

    def take_turn(self):
        if self.current_target and self.current_target.is_alive():
            # Si une menace est déjà identifiée, elle attaque
            self.creature.send_attack(self.current_target)
        elif self.ennemy_nearby_creatures:
            # Si une menace existe mais pas de cible en cours → choisir la menace la plus faible
            self.current_target = self.choose_target()
            print(f"{self.creature.species} cible {self.current_target.species} en défense !")
        else:
            self.current_target = None
