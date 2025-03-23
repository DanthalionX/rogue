import time
from Creature import Creature
from CreatureTemplate import CreatureTemplate
from skills.Skill import SkillEnum
from Trait import TraitEnum
from Element import ElementEnum

def main():
    # Création d'une créature pyromancienne avec PyromancySkill et BurnSkill
    pyromancer_template = CreatureTemplate(
        skills=[SkillEnum.PYROMANCY.skill_class(), SkillEnum.BURN.skill_class()]
    )
    pyromancer = Creature.generer_aleatoire(pyromancer_template)
    pyromancer.afficher_stats()
    
    # Création d'une créature cible vivante
    target_template = CreatureTemplate(
        basic_trait=TraitEnum.LIVING.trait_class()
    )
    target = Creature.generer_aleatoire(target_template)
    target.afficher_stats()

    pyromancer.cast_skill(SkillEnum.BURN, target)

    # Simulation du combat
    for _ in range(10):
        target.status_effect_manager.update_effects()
        time.sleep(0.5)

    # Affichage après l'effet
    print("=== État de la cible après la brûlure ===")
    target.afficher_stats()

if __name__ == "__main__":
    main()
