
from entities.Archetype_Loader import ArchetypeLoader
from entities.Creature import Creature

def main():
    print("=== Génération d'un Humain ===")
    
    # Création du template basé sur l'archétype "Humain"
    human_template = ArchetypeLoader.load_template("Humain")
    
    # Création de la créature basée sur ce template
    human = Creature.generer_aleatoire(template=human_template)
    
    # Affichage des stats
    human.afficher_stats()

if __name__ == "__main__":
    main()
