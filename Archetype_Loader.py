
import json
from CreatureTemplate import CreatureTemplate
from Trait import TraitEnum
from Skill import SkillEnum

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
            "species": None,  # ✅ Ajout de species
            "basic_trait": None
        }

        for archetype in archetypes:
            data = next((item for item in species_data if item.get("name") == archetype), None)
            if data:
                combined_stats["constitution"] += data.get("constitution", 0)
                combined_stats["agilite"] += data.get("agilite", 0)
                combined_stats["erudition"] += data.get("erudition", 0)

                combined_stats["species"] = data.get("name", None)  # ✅ Ajout du nom de l'espèce

                if "size" in data:
                    from Creature import Size
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

                # ✅ Lecture des skills
                for skill in data.get("skills", []):
                    skill_enum = getattr(SkillEnum, skill, None)
                    if skill_enum:
                        combined_stats["skills"].add(skill_enum.skill_class())

        # ✅ Correction : Ajout du champ species dans le template
        template = CreatureTemplate(
            constitution=combined_stats["constitution"],
            agilite=combined_stats["agilite"],
            erudition=combined_stats["erudition"],
            size=combined_stats["size"],
            species=combined_stats["species"],  # ✅ Nouvel attribut
            basic_trait=combined_stats["basic_trait"],
            traits=list(combined_stats["traits"]),
            skills=list(combined_stats["skills"])
        )

        return template
