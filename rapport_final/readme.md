# RAPPORT FINAL STICB545

## Introduction

Ce readme est un support à la compréhension des scripts utilisés dans le cadre de mon rapport final. Les scripts sont listés et accompagnés d'une courte explication quant à leur utilité.

## Exploiter des bases de données externes

- Script *api.py* : permet de récolter quelques infos de base de données open data de la ville de bruxelles

## Explorer le corpus en surface

- Script *simple_txt_exploration.py* permet, à partir d'un dossier contenant tous les rapports en version .txt, de calculer le nombre de fois ou "cimetière" apparait par année. Peut facilement être modifié pour afficher les informations par décennie, ou encore par fichier. Les données sont contenues dans un dictionnaire, et un graphe les représentant est généré.

- Script *plot_nombre_bulletins.py* permet de visualiser l'évolution du nombre de fichiers de bulletin par année

- Script *nltk_script.py* récupère les 400 mots les plus fréquents dans le corpus après un traitement via nltk (tokenisation + suppression des mots-vides)

- Script *wordcloud_filtering.py* et *wordcloud.sh* : permettent de générer des wordclouds pour les années choisies

## Explorer le corpus à l'aide d'outils plus complexes : 

- *word2vec_explore.py* utilise un modèle word2vec généré grâce à la librairie gensim pour explorer les rapports entre différents mots liés à la thématique étudiée.

- *sentiment.py* est utilisé pour analyser les aspects de subjectivité et de polarité de quelques phrases argumentatives du corpus
