
from enum import Enum
from Trait import LivingTrait, UndeadTrait
from Element import ShadowElement, MentalElement

class SkillType(Enum):
    ACTIVE = "ACTIVE"
    PASSIVE = "PASSIVE"
    DOMAIN = "DOMAIN"

class Skill:
    def __init__(self, skill_type: SkillType, is_dodgeable=True):
        self.skill_type = skill_type
        self.skill_level = 1
        self.skill_experience = 0
        self.required_skills = []
        self.is_dodgeable = is_dodgeable
        self.linked_elements = []  # (element, weight)

    def xp_required_for_next_level(self):
        return int(100 * (1.5 ** self.skill_level))

    def raise_skill_xp(self, xp_amount):
        self.skill_experience += xp_amount
        while self.skill_experience >= self.xp_required_for_next_level():
            self.skill_experience -= self.xp_required_for_next_level()
            self.skill_level += 1
            print(f"{self.__class__.__name__} atteint le niveau {self.skill_level} !")

    def decrease_skill_xp(self, xp_amount):
        self.skill_experience -= xp_amount
        if self.skill_experience < 0:
            self.skill_experience = 0

    def calculate_success_chance(self, caster, target):
        total_power = sum(caster.puissances[element] * weight for element, weight in self.linked_elements)
        total_resistance = sum(target.resistances[element] * weight for element, weight in self.linked_elements)
        success_chance = total_power - total_resistance + caster.stats.chance
        return success_chance

    def activate(self, caster, target):
        raise NotImplementedError("La méthode activate doit être implémentée dans la sous-classe.")

# Domaine de compétence : Necromancy
class NecromancySkill(Skill):
    def __init__(self):
        super().__init__(SkillType.DOMAIN)
        self.linked_elements = [(ShadowElement, 1.0)]  # Compétence principale liée à Mental

# Compétence dépendante du domaine de Nécromancie
class RiseUndeadSkill(Skill):
    def __init__(self):
        super().__init__(SkillType.ACTIVE, is_dodgeable=False)
        self.required_skills = [NecromancySkill]
        self.linked_elements = [(ShadowElement, 0.75), (MentalElement, 0.25)]

    def activate(self, caster, target):
        success_chance = self.calculate_success_chance(caster, target)
        if success_chance > 0:
            if any(isinstance(t, LivingTrait) for t in target.traits):
                target.traits = [t for t in target.traits if not isinstance(t, LivingTrait)]
                target.add_trait(UndeadTrait())
                target.stats.vie = target.stats.vie_max
                print(f"{target.species} a été relevé comme mort-vivant par {caster.species} !")
                self.raise_skill_xp(100)  # Gain d'XP en cas de succès
                for req in self.required_skills:
                    for skill in caster.skills:
                        if isinstance(skill, req):
                            skill.raise_skill_xp(10)  # Bonus dans les compétences liées
            else:
                print(f"{target.species} ne peut pas être relevé — Ce n'est pas une créature vivante !")
        else:
            print(f"{caster.species} échoue à relever {target.species} comme mort-vivant !")
            self.raise_skill_xp(10)  # 10% du gain d'XP en cas d'échec
            for req in self.required_skills:
                for skill in caster.skills:
                    if isinstance(skill, req):
                        skill.raise_skill_xp(1)  # 10% du bonus dans les compétences liées

# Compétence dépendante du domaine de Psychomancie
class PsychomancySkill(Skill):
    def __init__(self):
        super().__init__(SkillType.DOMAIN)
        self.linked_elements = [(MentalElement, 1.0)]  

class FearSkill(Skill):
    def __init__(self):
        super().__init__(SkillType.ACTIVE, is_dodgeable=False)
        self.required_skills = [PsychomancySkill]  
        self.linked_elements = [(MentalElement, 1.0)]  

    def activate(self, caster, target):
        success_chance = self.calculate_success_chance(caster, target)

        if success_chance > 0:
            print(f"{target.species} est terrifié par {caster.species} et tente de fuir !")
            self.raise_skill_xp(100)
            for req in self.required_skills:
                for skill in caster.skills:
                    if isinstance(skill, req):
                        skill.raise_skill_xp(10)
        else:
            print(f"{caster.species} échoue à effrayer {target.species} !")
            self.raise_skill_xp(10)

class ConfusionSkill(Skill):
    def __init__(self):
        super().__init__(SkillType.ACTIVE, is_dodgeable=False)
        self.required_skills = [PsychomancySkill]  
        self.linked_elements = [(MentalElement, 0.5), (ShadowElement, 0.5)]  # 50/50 Ombre et Mental

    def activate(self, caster, target):
        success_chance = self.calculate_success_chance(caster, target)
        
        if success_chance > 0:
            print(f"{target.species} est confusé par {caster.species} !")
            self.raise_skill_xp(100)
            for req in self.required_skills:
                for skill in caster.skills:
                    if isinstance(skill, req):
                        skill.raise_skill_xp(10)
        else:
            print(f"{caster.species} échoue à confondre {target.species} !")
            self.raise_skill_xp(10)

# Enum pour gérer les compétences par référence
class SkillEnum(Enum):
    NECROMANCY = NecromancySkill
    PSYCHOMANCY = PsychomancySkill
    RISE_UNDEAD = RiseUndeadSkill
    FEAR = FearSkill
    CONFUSION = ConfusionSkill

    @property
    def skill_class(self):
        return self.value
