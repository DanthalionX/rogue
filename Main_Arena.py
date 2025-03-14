import time
import random
from Creature import Creature

MAX_ROUNDS = 50
TICK_INTERVAL = 0.5

def simulate_combat(creature1, creature2):
    print("=== DÉBUT DU COMBAT ===")

    # Affichage des stats des deux créatures au début du combat
    print("\n--- Stats de départ ---")
    print(creature1.afficher_stats())
    print(creature2.afficher_stats())

    rounds = 0

    while rounds < MAX_ROUNDS and creature1.is_alive() and creature2.is_alive():
        rounds += 1

        # Gestion de l'attaque de la créature 1
        creature1.stats.attack_timer += TICK_INTERVAL
        if creature1.stats.attack_timer >= creature1.stats.attack_speed:
            creature1.send_attack(creature2)
            creature1.stats.attack_timer -= creature1.stats.attack_speed

        # Gestion de l'attaque de la créature 2
        creature2.stats.attack_timer += TICK_INTERVAL
        if creature2.stats.attack_timer >= creature2.stats.attack_speed:
            creature2.send_attack(creature1)
            creature2.stats.attack_timer -= creature2.stats.attack_speed

        time.sleep(TICK_INTERVAL)

    # Détermination du gagnant si le combat dure trop longtemps
    if creature1.is_alive() and creature2.is_alive():
        ratio1 = creature1.stats.vie / creature1.stats.vie_max
        ratio2 = creature2.stats.vie / creature2.stats.vie_max

        if ratio1 > ratio2:
            print(f"{creature1.species} gagne par pourcentage de vie restante !")
        elif ratio2 > ratio1:
            print(f"{creature2.species} gagne par pourcentage de vie restante !")
        else:
            print("Match nul !")
    elif creature1.is_alive():
        print(f"{creature1.species} remporte le combat !")
    elif creature2.is_alive():
        print(f"{creature2.species} remporte le combat !")

    # Affichage des stats après le combat
    print("\n--- Stats finales ---")
    print(creature1.afficher_stats())
    print(creature2.afficher_stats())

# Fonction main pour lancer le combat
if __name__ == "__main__":
    creature1 = Creature.generer_aleatoire()
    creature2 = Creature.generer_aleatoire()
    simulate_combat(creature1, creature2)