from entities.Creature import Creature
from skills.Skill import *
from CreatureTemplate import CreatureTemplate
from entities.Trait import LivingTrait

def main():
    # Création d'une créature vivante aléatoire
    template_living = CreatureTemplate(
        basic_trait=LivingTrait()
    )
    living_creature = Creature.generer_aleatoire(template=template_living)
    
    # Création d'une créature avec compétences Nécromancie, Peur et Confusion
    template_psychomancer = CreatureTemplate(
        skills=[SkillEnum.PSYCHOMANCY.skill_class(), SkillEnum.FEAR.skill_class(), SkillEnum.CONFUSION.skill_class()]
    )
    psychomancer = Creature.generer_aleatoire(template=template_psychomancer)
    
    print(f"Créature Vivante : {living_creature.species}")
    print(f"Psycomancien : {psychomancer.species} avec compétences Fear et Confusion")

    # Le Psycomancien attaque la créature vivante avec la compétence Peur
    psychomancer.cast_skill(SkillEnum.FEAR, living_creature)
    
    # Le Psycomancien attaque la créature vivante avec la compétence Confusion
    psychomancer.cast_skill(SkillEnum.CONFUSION, living_creature)

    living_creature.afficher_stats()
    
    for _ in range(10):
    # ✅ Mise à jour explicite des effets dans le gestionnaire
            living_creature.status_effect_manager.update_effects()

    living_creature.afficher_stats()

if __name__ == "__main__":
    main()
