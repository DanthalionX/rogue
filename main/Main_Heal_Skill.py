import time
from Creature import Creature
from CreatureTemplate import CreatureTemplate
from skills.Skill import SkillEnum
from Trait import TraitEnum
from Element import ElementEnum

def main():
    # Création d'une créature healer avec holymancy et heal
    healer_template = CreatureTemplate(
        skills=[SkillEnum.HOLYMANCY.skill_class(), SkillEnum.HEAL.skill_class()]
    )
    healer = Creature.generer_aleatoire(healer_template)
    healer.afficher_stats()
    
    # Création d'une créature cible vivante
    target_template = CreatureTemplate(
        basic_trait=TraitEnum.LIVING.trait_class()
    )
    target = Creature.generer_aleatoire(target_template)
    target.stats.vie=1
    target.afficher_stats()

    healer.cast_skill(SkillEnum.HEAL, target)

    # Simulation du combat
    for _ in range(10):
        target.status_effect_manager.update_effects()
        time.sleep(0.5)

    # Affichage après l'effet
    print("=== État de la cible après le soin ===")
    target.afficher_stats()

if __name__ == "__main__":
    main()
