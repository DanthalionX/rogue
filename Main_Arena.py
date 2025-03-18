import time
import random
from Controller import Controller
from Creature import Creature

MAX_ROUNDS = 50
TICK_INTERVAL = 0.5

def main():
    creature1 = Creature.generer_aleatoire()
    creature2 = Creature.generer_aleatoire()
    enemies = [creature2]

    controller1 = Controller(creature1, enemies)
    controller2 = Controller(creature2, [creature1])

    print("\n=== DÉBUT DU COMBAT ===\n")
    round_counter = 0
    MAX_ROUNDS = 50

    while creature1.is_alive() and creature2.is_alive() and round_counter < MAX_ROUNDS:
        controller1.update_logic()
        controller2.update_logic()
        round_counter += 1

    print("\n=== FIN DU COMBAT ===\n")
    if creature1.is_alive() and creature2.is_alive():
        print(f"Égalité après {MAX_ROUNDS} rounds.")
    elif creature1.is_alive():
        print(f"{creature1.species} remporte le combat !")
    elif creature2.is_alive():
        print(f"{creature2.species} remporte le combat !")

if __name__ == "__main__":
    main()
