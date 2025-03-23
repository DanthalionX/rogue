import time
from entities.Creature import Creature, Size
from CreatureTemplate import CreatureTemplate
from entities.Trait import LivingTrait
from skills.Skill import SkillEnum

MAX_ROUNDS = 50
TICK_INTERVAL = 0.5

def main():
    # Création d'une créature vivante via le template
    template_living = CreatureTemplate(
        size=Size.M,
        basic_trait=LivingTrait()
    )
    living_creature = Creature.generer_aleatoire(template=template_living)

    # Création d'un nécromancien avec la compétence RiseUndeadSkill
    template_necromancer = CreatureTemplate(
        size=Size.M,
        basic_trait=None,
        skills=[SkillEnum.NECROMANCY.skill_class(), SkillEnum.RISE_UNDEAD.skill_class()]
    )
    necromancer = Creature.generer_aleatoire(template=template_necromancer)

    print("\n--- DÉBUT DU COMBAT ---\n")
    print(living_creature.afficher_stats())
    print(necromancer.afficher_stats())

    rounds = 0
    while rounds < MAX_ROUNDS and living_creature.is_alive():
        rounds += 1

        # Le nécromancien attaque la créature vivante
        necromancer.stats.attack_timer += TICK_INTERVAL
        if necromancer.stats.attack_timer >= necromancer.stats.attack_speed:
            necromancer.send_attack(living_creature)
            necromancer.stats.attack_timer -= necromancer.stats.attack_speed
        
        time.sleep(TICK_INTERVAL)

    print("\n--- FIN DU COMBAT ---\n")
    
    if not living_creature.is_alive():
        print(f"{living_creature.species} est mort !")
        print(f"Tentative de lancer RiseUndeadSkill par {necromancer.species}")

        # Correction : Passer la classe du skill via l'énumération
        necromancer.cast_skill(SkillEnum.RISE_UNDEAD, living_creature)

        print("\n--- STATS APRÈS RÉANIMATION ---")
        print(living_creature.afficher_stats())
    else:
        print(f"{living_creature.species} a survécu !")

if __name__ == "__main__":
    main()
