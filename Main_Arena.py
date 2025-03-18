import time
from HostileController import HostileController
from DefensiveController import DefensiveController
from Creature import Creature

MAX_ROUNDS = 50
TICK_INTERVAL = 0.5

def main():
    creature1 = Creature.generer_aleatoire()
    creature2 = Creature.generer_aleatoire()
    creature3 = Creature.generer_aleatoire()
    creature4 = Creature.generer_aleatoire()

    creatures = [creature1, creature2,creature3, creature4]

    creature1.controller = HostileController(creature1, creatures)
    creature2.controller = DefensiveController(creature2, creatures)
    creature3.controller = DefensiveController(creature2, creatures)
    creature4.controller = DefensiveController(creature2, creatures)

    print("=== DÉBUT DU COMBAT ===")

    while sum(creature.is_alive() for creature in creatures) > 1:
        for creature in creatures:
            if creature.is_alive():
                creature.controller.take_turn()
            time.sleep(0.5)

    print("=== FIN DU COMBAT ===")

    if creature1.is_alive() and creature2.is_alive():
        print(f"Égalité après {MAX_ROUNDS} rounds.")
    elif creature1.is_alive():
        print(f"{creature1.species} remporte le combat !")
    elif creature2.is_alive():
        print(f"{creature2.species} remporte le combat !")

if __name__ == "__main__":
    main()
