.. p13 documentation master file, created by
   sphinx-quickstart on Tue Jun 25 14:42:54 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to p13's documentation!
===============================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

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


