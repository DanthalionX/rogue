
from Creature import Creature, CreatureTemplate, Size
from Skill import SkillEnum
import time

def main():
    # Crée une cible avec beaucoup de points de vie
    target_1 = CreatureTemplate(size=Size.XL)
    target_1 = Creature.generer_aleatoire(target_1)
    target_1.stats.vie_max = 10000
    target_1.stats.vie = 10000

    target_2 = CreatureTemplate(size=Size.XL)
    target_2 = Creature.generer_aleatoire(target_2)
    target_2.stats.vie_max = 10000
    target_2.stats.vie = 10000

    # Attaquant 1 : Attaque physique jusqu'à l'épuisement de l'endurance
    attacker_1 = CreatureTemplate(size=Size.M)
    attacker_1 = Creature.generer_aleatoire(attacker_1)
    print("=== COMBAT 1 ===")
    print("Attaquant 1 :")
    attacker_1.afficher_stats()
    print("Cible 1 :")
    target_1.afficher_stats()

    round_counter = 0
    while attacker_1.stats.endurance >= 2 and target_1.is_alive():
        attacker_1.send_attack(target_1)
        time.sleep(0.5)
        round_counter += 1
    attacker_1.send_attack(target_1)

    print(f"Combat terminé après {round_counter} rounds.")
    print("État final de l'attaquant 1 :")
    attacker_1.afficher_stats()
    print("État final de la cible 1 :")
    target_1.afficher_stats()

    # Attaquant 2 : Utilise uniquement des attaques mentales jusqu'à l'épuisement du mana
    attacker_2 = CreatureTemplate(size=Size.M, skills=[SkillEnum.PSYCHOMANCY.skill_class(),SkillEnum.FEAR.skill_class(), SkillEnum.CONFUSION.skill_class()])
    attacker_2 = Creature.generer_aleatoire(attacker_2)
    print("=== COMBAT 2 ===")
    print("Attaquant 2 :")
    attacker_2.afficher_stats()
    print("Cible 2 :")
    target_2.afficher_stats()

    round_counter = 0
    while (attacker_2.stats.mana >= SkillEnum.FEAR.skill_class().mana_cost or
           attacker_2.stats.mana >= SkillEnum.CONFUSION.skill_class().mana_cost) and target_2.is_alive():
        if attacker_2.stats.mana >= SkillEnum.FEAR.skill_class().mana_cost:
            attacker_2.cast_skill(SkillEnum.FEAR, target_2)
        elif attacker_2.stats.mana >= SkillEnum.CONFUSION.skill_class().mana_cost:
            attacker_2.cast_skill(SkillEnum.CONFUSION, target_2)
        time.sleep(0.5)
        round_counter += 1
    attacker_2.cast_skill(SkillEnum.CONFUSION, target_2)

    print(f"Combat terminé après {round_counter} rounds.")
    print("État final de l'attaquant 2 :")
    attacker_2.afficher_stats()
    print("État final de la cible 2 :")
    target_2.afficher_stats()

if __name__ == "__main__":
    main()
