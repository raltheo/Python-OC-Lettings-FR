.. p13 documentation master file, created by
   sphinx-quickstart on Tue Jun 25 14:42:54 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to p13's documentation!
===============================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Description du projet
=====================
Le site web Orange County Lettings est une application web de gestion de locations et de profils utilisateurs. Il permet de visualiser et de gérer des profils et des locations au sein du comté d'Orange.

Instructions sur l'installation du projet
========================================
Prérequis
---------
- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

macOS / Linux
-------------
1. Cloner le repository :
   ::

       cd /path/to/put/project/in
       git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git

2. Créer l'environnement virtuel :
   ::

       cd /path/to/Python-OC-Lettings-FR
       python -m venv venv
       apt-get install python3-venv  # Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu

3. Activer l'environnement virtuel :
   ::

       source venv/bin/activate

4. Confirmer que la commande python exécute l'interpréteur Python dans l'environnement virtuel :
   ::

       which python

5. Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure :
   ::

       python --version

6. Confirmer que la commande pip exécute l'exécutable pip dans l'environnement virtuel :
   ::

       which pip

7. Pour désactiver l'environnement :
   ::

       deactivate

Windows
-------
Utiliser PowerShell, comme ci-dessus sauf :
1. Pour activer l'environnement virtuel :
   ::

       .\venv\Scripts\Activate.ps1

2. Remplacer ``which <my-command>`` par :
   ::

       (Get-Command <my-command>).Path


Guide de démarrage rapide
=========================
1. Exécuter le site :
   ::

       cd /path/to/Python-OC-Lettings-FR
       source venv/bin/activate
       pip install --requirement requirements.txt
       python manage.py runserver

2. Aller sur http://localhost:8000 dans un navigateur.
3. Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).


Technologies et langages de programmation
=========================================
- Python 3.6 ou supérieur
- Django
- SQLite
- Git


Structure de la base de données et modèles de données
=====================================================
La base de données utilise SQLite et contient les tables suivantes :

- **Address** : stocke les informations d'adresse.
- **Letting** : stocke les informations de locations associées à des adresses.
- **Profile** : stocke les informations de profils utilisateurs.


Interfaces de programmation
===========================
- Les vues Django pour gérer les requêtes HTTP.
- Les modèles Django pour interagir avec la base de données.


Guide d'utilisation
===================
Cas d'utilisation
-----------------
1. **Consulter les profils** :

   - Aller sur http://localhost:8000/profiles/
   - Voir la liste des profils disponibles.
   
2. **Consulter les locations** :

   - Aller sur http://localhost:8000/lettings/
   - Voir la liste des locations disponibles.

3. **Panel d'administration** :

   - Aller sur http://localhost:8000/admin
   - Se connecter avec l'utilisateur root, mot de passe ``root``.


Procédures de déploiement et de gestion de l'application
========================================================
1. **Déploiement** :
   - Suivre les étapes de configuration et d'installation ci-dessus.
   - Utiliser un serveur web tel que Gunicorn pour le déploiement en production.
   - Configurer un serveur web (Apache, Nginx) pour servir l'application.

2. **Gestion** :
   - Utiliser les commandes Django pour la gestion de la base de données et des migrations.
   - Exécuter les tests unitaires :
     ::

         cd /path/to/Python-OC-Lettings-FR
         source venv/bin/activate
         pytest

   - Linting du code :
     ::

         cd /path/to/Python-OC-Lettings-FR
         source venv/bin/activate
         flake8

3. **Base de données** :

   - Ouvrir une session shell sqlite3 :
     ::

         cd /path/to/Python-OC-Lettings-FR
         sqlite3

   - Se connecter à la base de données :
     ::

         .open oc-lettings-site.sqlite3

   - Afficher les tables dans la base de données :
     ::

         .tables

   - Quitter la session :
     ::

         .quit


4. **Mise à jour de l'application** :

   - Pour mettre à jour les dépendances :
     ::

         pip install --upgrade -r requirements.txt

CI/CD
=====

Cette documentation décrit le processus CI/CD (Intégration Continue et Déploiement Continu) mis en place pour ce projet. L'objectif de ce document est de fournir une compréhension claire des outils utilisés.

Outils Utilisés
"""""""""""""""

J'utilise les outils suivants pour le pipeline CI/CD :

- **GitHub Actions** : Pour l'automatisation des workflows.
- **flake8** : Pour le linting du code Python.
- **pytest** : Pour l'exécution des tests unitaires.
- **Docker** : Pour un déploiement facile sur tout type d'architecture.
- **EC2 (AWS)** : Pour hébergé mon app.

Configuration CI/CD
"""""""""""""""""""

Vous pouvez trouver `ici <https://github.com/raltheo/Python-OC-Lettings-FR/blob/master/.github/workflows/docker-publish.yml>`_ la configuration pour le CI/CD.


Variable environnement Github Actions
"""""""""""""""""""""""""""""""""""""

J'utilise des variables d'environnement pour gérer les informations sensibles et les configurations spécifiques. Ces variables permettent de configurer le workflow GitHub Actions sans exposer de données sensibles dans le code source.

Pour définir des variables d'environnement dans GitHub Actions, suivez ces étapes :

1. Accédez au dépôt GitHub de votre projet.
2. Cliquez sur l'onglet "Settings".
3. Dans le menu de gauche, sélectionnez "Secrets and variables".
4. Cliquez sur "Actions".
5. Cliquez sur "New repository secret" pour ajouter une nouvelle variable d'environnement.

Voici quelques variables que j'ai utilisé :

**DOCKER_USERNAME** : Nom d'utilisateur pour se connecter au registre Docker.
**DOCKER_PASSWORD** : Mot de passe pour se connecter au registre Docker.
**EC2_HOST** : L'adresse IP de mon vps.
**EC2_KEY** : Clé privé ssh pour se connecter au vps.

Processus CI/CD
"""""""""""""""

1. **Linting et Tests Unitaires :**

   - Pour chaque commit, GitHub Actions exécute flake8 pour vérifier la qualité du code.
   - Ensuite, pytest est utilisé pour lancer les tests unitaires.

2. **Construction de l'Image Docker :**

   - Une fois les tests passés avec succès, une image Docker est construite à partir du Dockerfile.
   - Cette image est ensuite poussée vers Docker Hub.

3. **Déploiement sur EC2 :**

   - Après la construction et la publication de l'image Docker, le déploiement sur une instance EC2 est déclenché (connexion ssh et execution de commandes).
   - L'application est déployée en utilisant l'image Docker construite.

Conclusion
""""""""""

Ce processus CI/CD permet d'assurer que chaque modification du code est vérifiée et testée automatiquement avant d'être déployée en production. Cela contribue à améliorer la qualité du code et à réduire les risques d'erreurs lors du déploiement.


