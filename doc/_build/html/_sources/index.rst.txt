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
-----

Cette documentation décrit le processus CI/CD (Intégration Continue et Déploiement Continu) mis en place pour ce projet. L'objectif de ce document est de fournir une compréhension claire des outils utilisés.

J'utilise les outils suivants pour le pipeline CI/CD :

- **GitHub Actions** : Pour l'automatisation des workflows.
- **flake8** : Pour le linting du code Python.
- **pytest** : Pour l'exécution des tests unitaires.
- **Docker** : Pour un déploiement facile sur tout type d'architecture.
- **EC2 (AWS)** : Pour hébergé mon app.

Vous pouvez trouver `ici <https://github.com/raltheo/Python-OC-Lettings-FR/blob/master/.github/workflows/docker-publish.yml>`_ la configuration pour le CI/CD.

Dans l'idée le 

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
