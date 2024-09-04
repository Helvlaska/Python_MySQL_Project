# Python MySQL Project: Dead Town - Zombie Survival

## Description

Projet de jeu pour l'apprentissage de Python et MySQL. Jeu de farm et de craft afin d'améliorer son refuge et survivre le plus de jours possible.

## Fonctionnalités

- **Système d'inscription et de connexion** : Les joueurs peuvent s'inscrire et se connecter avec un pseudo et un mot de passe.
- **Gestion du personnage** : Chaque utilisateur a un personnage unique qui peut collecter des objets et améliorer son refuge.
- **Inventaire évolutif** : Le joueur commence avec une petite capacité d'inventaire, qui peut être augmentée en trouvant ou en fabriquant un sac à dos.
- **Exploration et collecte** : Le joueur peut explorer différents lieux pour trouver des armes, des munitions, de la nourriture, et des matériaux.
- **Amélioration du refuge** : Le refuge peut être amélioré avec des matériaux collectés pour mieux résister aux attaques de zombies.
- **Cycle jour/nuit** : Le jeu intègre un cycle jour/nuit affectant la difficulté des combats et l'exploration.
- **Zombies variés** : Différents types de zombies apparaissent au fur et à mesure que le jeu progresse, chacun avec des niveaux de puissance évolutifs.

## Prérequis

- **Python 3.x** : Le langage de programmation utilisé pour le jeu.
- **MySQL** : Base de données utilisée pour gérer les utilisateurs et les données du jeu.
- **MySQL Connector pour Python** : Bibliothèque nécessaire pour connecter Python à MySQL.

## Installation

1. Clonez ce dépôt GitHub dans votre répertoire local :
   
	    git clone https://github.com/username/Python_MySQL_Project.git

2. Accédez au répertoire du projet :

	    cd Python_MySQL_Project

3. Créez et activez un environnement virtuel :

	    python -m venv venv

  - Sur Windows :

        venv\Scripts\activate
    
  - Sur Mac :
  
        source venv/bin/activate  

4. Installez les dépendances requises :

	    pip install -r requirements.txt

5. Configurez votre base de données MySQL :

	Créez une base de données appelée databasetest ou utilisez une autre base de données en modifiant le fichier de configuration.
	Mettez à jour les paramètres de connexion à la base de données dans main.py si nécessaire.
	Exécutez le script principal pour démarrer le jeu :

        python main.py 
