
from Creature import Creature
from CreatureTemplate import CreatureTemplate

class Main:
    @staticmethod
    def run():
        template = CreatureTemplate()
        creature = Creature.generer_aleatoire(template)
        print(creature.afficher_stats())

if __name__ == "__main__":
    Main.run()