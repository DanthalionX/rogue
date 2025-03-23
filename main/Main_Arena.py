import time
from HostileController import HostileController
from DefensiveController import DefensiveController
from PassiveController import PassiveController
from entities.Creature import Creature

MAX_ROUNDS = 50
TICK_INTERVAL = 0.5

def main():
    creature1 = Creature.generer_aleatoire(controller_class=HostileController)
    creature2 = Creature.generer_aleatoire(controller_class=PassiveController)
    creature3 = Creature.generer_aleatoire(controller_class=PassiveController)
    creature4 = Creature.generer_aleatoire(controller_class=PassiveController)

    # Remplir la liste des créatures voisines après la création de toutes les créatures
    creatures = [creature1, creature2,creature3, creature4]
    for creature in creatures:
        creature.controller.set_nearby_creatures(creatures)
        #print(f"{creature.species}  → NEAR:[{[c.species for c in creature.controller.nearby_creatures]}] HOSTILES:[{[c.species for c in creature.controller.ennemy_nearby_creatures]}] NEUTRALS:[{[c.species for c in creature.controller.neutral_nearby_creatures]}]")

    print("=== DÉBUT DU COMBAT ===")

    round_count = 0
    while sum(creature.is_alive() and not creature.has_fled for creature in creatures) > 1:
        round_count += 1

        for creature in creatures:
            if creature.is_alive() and not creature.has_fled:
                creature.controller.take_turn()
            time.sleep(0.5)
            
        remaining_creatures = [creature for creature in creatures if creature.is_alive() and not creature.has_fled]
        if len(remaining_creatures) <= 1:
            print("=== FIN DU COMBAT ===")
            if remaining_creatures:
                print(f"{remaining_creatures[0].species} remporte la victoire avec {remaining_creatures[0].stats.vie:.2f} points de vie !")
            else:
                print("Toutes les créatures sont mortes ou ont fui !")
            break
        if all(isinstance(creature.controller, PassiveController) for creature in remaining_creatures):
            print("=== FIN DU COMBAT : Toutes les créatures restantes sont passives ===")
            break

if __name__ == "__main__":
    main()
