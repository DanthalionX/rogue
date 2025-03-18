from random import choice

class Controller:
    def __init__(self, creature, enemies):
        self.creature = creature
        self.enemies = enemies

    def choose_target(self):
        # Sélectionne l'ennemi avec le plus bas pourcentage de vie restante
        targets = [enemy for enemy in self.enemies if enemy.is_alive()]
        if not targets:
            return None
        return min(targets, key=lambda t: t.stats.vie / t.stats.vie_max)

    def choose_attack(self, target):
        # Sélectionne l'élément qui infligera le plus de dégâts à la cible
        best_element = self.creature.choose_best_attack(target)
        if best_element:
            self.creature.send_attack(target)
        else:
            # Sélectionne une compétence utilisable
            usable_skills = [skill for skill in self.creature.skills if skill.can_activate(self.creature, target)]
            if usable_skills:
                best_skill = max(usable_skills, key=lambda s: s.calculate_success_chance(self.creature, target))
                best_skill.activate(self.creature, target)

    def update_logic(self):
        if self.creature.is_alive() and self.creature.stats.attack_timer >= self.creature.stats.attack_speed:
            target = self.choose_target()
            if target:
                self.choose_attack(target)
            self.creature.stats.attack_timer = 0
        else:
            self.creature.stats.attack_timer += 1
