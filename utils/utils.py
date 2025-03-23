
import random
from enum import Enum

def generer_nom_aleatoire():
    prefixes = ["Ka", "Ze", "Lu", "Xa", "Ar", "Lo", "Fa", "Vi", "Ne", "Sa"]
    suffixes = ["ron", "rex", "lia", "thor", "dus", "zar", "men", "tha", "lok", "nir"]
    return random.choice(prefixes) + random.choice(suffixes)

def generer_nom_espece():
    racines = ["Draco", "Felix", "Canis", "Aquila", "Panthera", "Equus", "Lupus", "Serpentis", "Tigris", "Ursus"]
    suffixes = ["us", "a", "is", "on", "ium", "ix", "ora", "an", "or", "en"]
    connecteurs = ["-", "'", " "]

    nom = random.choice(racines) + random.choice(suffixes)
    if random.random() < 0.5:
        nom += random.choice(connecteurs) + random.choice(racines).lower() + random.choice(suffixes)
    if random.random() < 0.3:
        nom = nom[::-1].capitalize()
    return nom

class Size(Enum):
    XS = 3
    S = 4
    M = 5
    L = 6
    XL = 7