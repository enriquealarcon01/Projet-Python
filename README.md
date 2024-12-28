# Projet Music Trend Analyser - Python pour la data science

### Auteurs : Nathan SOARES DE MELO & Enrique ALARCON VILLARROEL

Plan (Brouillon)

## Introduction

Les principaux classements de musique, comme le Billboard 200, semblent toujours être dominés par les mêmes artistes et par les mêmes genres. Est-ce que cela s'explique uniquement par leur notoriété? Il y a-t-il d'autres facteurs qui contribuent à leur succès?

## Problématisation

Comment,à partir des outils abordés en cours, pouvons-nous expliquer la popularité des chansons présentes dans le classement du Billboard 200? Peut-on créer une chanson populaire capable de rivaliser avec les productions des labels discographiques les plus puissants?

### Partie 1: Collecte, manipulation et traitement des données
Objectifs
- Collecter des données pertinentes:
    classement du Billboard 200
    caractéristiques des artistes et des chasons grâce à MusicBrainz
    paroles des chansons à partir de Genius
- Nettoyage des données pour les rendre exploitables
Lien avec le cours: Manipuler


### Partie 2: Analyse descriptive
Objectif: Identifier les tendances générales ainsi que les caractéristiques principales des chansons populaires
A) Une analyse générale des tendances
    - Etude des données générales sur les artistes et les genres dominants dans le classement
    - Communication: visualisation des résultats à partir des graphiques et des histogrammes
Partie du cours: Communiquer (Construire des graphiques avec Python)

B) Analyse approfondie des paroles
    - Effectuer une analyse fréquentielle des paroles pour déterminer les thèmes et les mots récurrents.
Partie du cours: NLP- Nettoyer l'information + analyse fréquentiste

### Partie 3: Modélisation, vers la création d'un véritable hit
Objectif: A partir des informations collectées dans les deux parties précédentes, nous allons essayer de générer une chanson capable d'atteindre le sommet du Billboard 200

A) Préambule: retrouver les expressions et les mots clés
    - Modélisation des collocations ou n-grammes les plus utilisés dans les chansons populaires
B) Tentative: Génération des paroles
    - Nous allons essayer de produire des paroles originales en nous inspirant des tendances
C) Définir l'artiste idéal?
    - Modélisation des caractéristiques d'un artiste fictif idéal pour interpréter notre chanson
    Pour cela on pourra essayer de faire une régression??

## Lien vers le notebook

[Music Trend Analyser](https://github.com/enriquealarcon01/Projet-Python/blob/main/data_retrieve.ipynb)

Conclusion?
Pistes d'amélioration? 
