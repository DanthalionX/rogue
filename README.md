
# Rogue - A Rogue-like Game

## Introduction

`Rogue` est un jeu de type rogue-like où le joueur explore un monde peuplé de créatures et de mécanismes magiques. Le projet inclut des mécaniques de combat complexes, de nécromancie, et de compétences évolutives.

## Fonctionnalités Principales

### 1. Mécanique de Combat
- Le jeu repose sur un système de **combat au tour par tour** entre créatures.  
- Chaque créature possède des statistiques de base (constitution, agilité, érudition) et des statistiques dérivées (esquive, précision, vie, énergie, etc.).  
- Les créatures ont des **résistances physiques, mentales et élémentaires** ainsi que des **puissances** associées aux éléments.  
  - Les résistances mentales sont basées sur l'érudition de la créature.  
  - Les résistances physiques et élémentaires sont calculées en fonction de la constitution de la créature.  

### 2. Nécromancie et Réanimation
- La compétence **`RiseUndeadSkill`** permet de **relever une créature morte** et de la transformer en **mort-vivant**. La créature vivante doit être **morte** pour être transformée.
- La compétence **`RiseUndeadSkill`** dépend du domaine de nécromancie (`NecromancySkill`) et influe sur la créature cible en vérifiant ses résistances élémentaires (ombre et mental).  
- Une fois transformée en mort-vivant, la créature a le **nécromancien** comme maître, mais elle peut toujours l'attaquer.  
- **Note** : Le **nécromancien** peut utiliser la compétence `RiseUndeadSkill` pour relever des créatures mortes et les garder sous son contrôle.

### 3. Système de Compétences
- Les compétences sont classées en trois types :  
  - **ACTIVE** : Compétences qui nécessitent d'être activées (ex : `RiseUndeadSkill`).  
  - **PASSIVE** : Compétences toujours actives sans action directe (ex : `NecromancySkill`).  
  - **DOMAIN** : Compétences liées à un domaine spécifique (ex : `NecromancySkill`).  
- **Compétences existantes** :  
  - **`RiseUndeadSkill`** : Implémentée et utilisée pour transformer une créature vivante en mort-vivant.  
  - **Autres compétences à venir** : D'autres compétences seront ajoutées, telles que des compétences offensives, des attaques mentales, et des compétences liées aux éléments.

### 4. Traits de Créatures
- Les **traits basiques** (basic traits) représentent la **nature même** de la créature et sont toujours présents. Un trait basique est **unique** et **obligatoire** pour chaque créature.
- Exemples de traits basiques : **`LivingTrait`**, **`UndeadTrait`**.
- Certains traits peuvent être **incompatibles** ou **interdépendants**. Par exemple, une créature ne peut pas avoir à la fois les traits **`RidableTrait`** et **`EtherealTrait`**.

### 5. Système de Statistiques Dynamiques
- Les créatures possèdent des **statistiques dynamiques** calculées à partir de leurs statistiques de base. Ces statistiques incluent :  
  - **Esquive** : Calculée à partir de l'agilité et de la taille de la créature.  
  - **Précision** : Basée sur l'agilité.  
  - **Vie** et **Énergie** : Dépendantes de la constitution et de l'érudition de la créature.  
  - **Vitesse d'attaque** : Basée sur l'agilité.  
  - **Chance** : Une statistique aléatoire influençant la probabilité de réussir des actions.

## Instructions d'Installation et d'Exécution

1. Clonez ou téléchargez le dépôt :
```
git clone https://github.com/DanthalionX/rogue.git
```
2. Installez les dépendances nécessaires (si applicables).  
3. Lancez le jeu avec Python :
```
python Main_Arena.py
```

## Exemple de Gameplay

Le joueur contrôle un **nécromancien** qui peut attaquer une créature vivante et tenter de la relever comme un mort-vivant. Voici un exemple de combat où une créature est relevée après sa mort.

## Architecture du Code

Le projet est structuré comme suit :
- **Main_Arena.py** : Simulation de combat entre créatures.
- **Main_Undead_Rising.py** : Scénario de nécromancie avec `RiseUndeadSkill`.
- **Creature.py** : Contient la classe `Creature` et ses statistiques.
- **CreatureTemplate.py** : Classe `CreatureTemplate` pour la génération de créatures avec des contraintes spécifiques.
- **Trait.py** : Définition des traits (ex : `LivingTrait`, `UndeadTrait`).
- **Skill.py** : Gestion des compétences (ex : `NecromancySkill`, `RiseUndeadSkill`).
- **Element.py** : Définition des éléments et affinités élémentaires.
- **DerivedStats.py** : Contient les statistiques dérivées pour chaque créature (esquive, précision, résistances, etc.).

## Contributions

Les contributions sont bienvenues ! Si vous souhaitez contribuer à ce projet, vous pouvez :
- Forker le dépôt et envoyer une pull request avec vos changements.
- Ouvrir une issue pour signaler des bugs ou suggérer des fonctionnalités.
