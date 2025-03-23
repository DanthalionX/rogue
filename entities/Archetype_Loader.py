
import json
from entities.CreatureTemplate import CreatureTemplate
from entities.Trait import TraitEnum
from skills.Skill import SkillEnum

class ArchetypeLoader:
    @staticmethod
    def load_template(*archetypes):
        # Charger les archétypes depuis le fichier JSON
        with open('data_species.json', 'r') as file:
            species_data = json.load(file)

        combined_stats = {
            "constitution": 0,
            "agilite": 0,
            "erudition": 0,
            "traits": set(),
            "skills": set(),
            "size": None,
            "species": None,  
            "basic_trait": None,
            "locked_traits": set(),
            "locked_skills": set()
        }

        for archetype in archetypes:
            data = next((item for item in species_data if item.get("name") == archetype), None)
            if data:
                combined_stats["constitution"] += data.get("constitution", 0)
                combined_stats["agilite"] += data.get("agilite", 0)
                combined_stats["erudition"] += data.get("erudition", 0)
                combined_stats["species"] = data.get("name", None)  

                if "size" in data:
                    from entities.Creature import Size
                    combined_stats["size"] = Size[data["size"]]

                if "basic_trait" in data:
                    trait_enum = getattr(TraitEnum, data["basic_trait"], None)
                    if trait_enum:
                        combined_stats["basic_trait"] = trait_enum.trait_class()

                # ✅ Lecture des traits
                for trait in data.get("traits", []):
                    trait_enum = getattr(TraitEnum, trait, None)
                    if trait_enum:
                        combined_stats["traits"].add(trait_enum.trait_class())

                # ✅ Lecture des locked_traits
                for trait in data.get("locked_traits", []):
                    trait_enum = getattr(TraitEnum, trait, None)
                    if trait_enum:
                        combined_stats["locked_traits"].add(trait_enum.trait_class())

                # ✅ Lecture des skills
                for skill in data.get("skills", []):
                    skill_enum = getattr(SkillEnum, skill, None)
                    if skill_enum:
                        combined_stats["skills"].add(skill_enum.skill_class())

                # ✅ Lecture des locked_skills
                for skill in data.get("locked_skills", []):
                    skill_enum = getattr(SkillEnum, skill, None)
                    if skill_enum:
                        combined_stats["locked_skills"].add(skill_enum.skill_class())

        template = CreatureTemplate(
            constitution=combined_stats["constitution"],
            agilite=combined_stats["agilite"],
            erudition=combined_stats["erudition"],
            size=combined_stats["size"],
            species=combined_stats["species"],
            basic_trait=combined_stats["basic_trait"],
            traits=list(combined_stats["traits"]),
            skills=list(combined_stats["skills"]),
            locked_traits = list(combined_stats["locked_traits"]),
            locked_skills = list(combined_stats["locked_skills"])
        )

        return template
