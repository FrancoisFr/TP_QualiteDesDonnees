# TP_QualiteDesDonnees

Ce travail à été effectué sous pyCharm.
Pour répondre aux besoin du TP, 2 fichiers différents ont été créé.

<b>Contexte :</b>

Nous avons reçu deux jeux de données météorologique (Climat.xlsx et Savukoski_kyrkonkyla.xlsx).
L'objectif de ce TP est de comparer les deux jeux de données afin de trouver de quel endroit provient le jeux de données Climat.xlsx de manière approximative.

Pour ce faire nous allons mettre en oeuvre un environnement de traitement graphique avec les deux jeux de données afin d'analyser les courbes qui en ressorte.

<b>Mise en oeuvre :</b>
Au début de chaque fichier nous retrouverons les bibliothèques suivantes:


![Alt text](https://github.com/FrancoisFr/TP_QualiteDesDonnees/blob/main/fichier/Figure1.PNG?raw=true)


<b>Climat.xlsx : </b>
Le fichier mat1.py permet d'utiliser le jeu de donnée de la première feuille ( le premier dans le fichier) afin de fournir un graphe regroupant les températures de chaque jour de l'année dans une fenêtre, ainsi qu'un graphe pour chaque mois dans une seconde fenêtre.


![Alt text](https://github.com/FrancoisFr/TP_QualiteDesDonnees/blob/main/fichier/GrapheAnnuel.PNG?raw=true)

Sur le graphe annuel, un curseur rouge est mis en place, prenant en compte la position x du curseur dans le graphe qui représente le jour dans l'année. À partir de ce curseur, un clique sur le graphe permet d'ouvrir une troisième fenêtre qui contiendra les températures des 30 jours autour du curseur.

![Alt text](https://github.com/FrancoisFr/TP_QualiteDesDonnees/blob/main/fichier/GrapheMoisParMois.PNG?raw=true)



![Alt text](https://github.com/FrancoisFr/TP_QualiteDesDonnees/blob/main/fichier/Graphe30Jours.PNG?raw=true)

Afin d'obtenir ces différents graphes, nous avons utilisé matplotlib et panda de la manières suivante:

![Alt text](https://github.com/FrancoisFr/TP_QualiteDesDonnees/blob/main/fichier/CodeGrapheAnnee.PNG?raw=true)

![Alt text](https://github.com/FrancoisFr/TP_QualiteDesDonnees/blob/main/fichier/CodeMoisParMois.PNG?raw=true)

![Alt text](https://github.com/FrancoisFr/TP_QualiteDesDonnees/blob/main/fichier/CodeGraphe30Jours.PNG?raw=true)

![Alt text](https://github.com/FrancoisFr/TP_QualiteDesDonnees/blob/main/fichier/CodeAppelleFonction.PNG?raw=true)

Le fichier mat2.py appelle les données contenu dans la seconde feuille, avec un jeu de donnée contenant des erreurs.

Afin de corriger celles-ci, nous vérifions dans le programme chaque variable, celle ne correspondant pas aux types d'entrée attendu sont remplacé dans un premier temps par une valeur nulle.


![Alt text](https://github.com/FrancoisFr/TP_QualiteDesDonnees/blob/main/fichier/CodeMoisParMoisErreur.PNG?raw=true)

![Alt text](https://github.com/FrancoisFr/TP_QualiteDesDonnees/blob/main/fichier/CodeCorrectionErreur.PNG?raw=true)

Une fois cela fait, chaque valeur nulle est remplacé par la valeur médiane des températures du mois. Cela nous permet d'obtenir les graphes suivants:


![Alt text](https://github.com/FrancoisFr/TP_QualiteDesDonnees/blob/main/fichier/GrapheMoisParMoisErreur.PNG?raw=true)




Ce qui donne en graphe annuel:

![Alt text](https://github.com/FrancoisFr/TP_QualiteDesDonnees/blob/main/fichier/GrapheAnnuelErreur.PNG?raw=true)

Enfin, de la même manière en cliquant sur le graphe on en obtient un nouveau graphe avec 15 jours avant et après le curseur:

![Alt text](https://github.com/FrancoisFr/TP_QualiteDesDonnees/blob/main/fichier/Graphe30JoursErreur.PNG?raw=true)

<b>Savukoski_kyrkonkyla.xlsx : </b>

Le fichier Savukoski_graph.py tous comme le fichier mat2.py va nous permettre de corriger les erreurs ou les manques au sein du jeux de données que l'on nous a fournis en faisant en sorte de les remplacer par une valeur médiane.
Ce fichier va nous permettre aussi d'afficher de manière graphique les valeurs du jeux de données en fonction du mois de l'année ou alors de l'année dans son ensemble.

Sur l'image suivante nous avons les graphiques des 12 mois de l'année en fonction de la T° moyenne de la journée au niveau de la sonde Savukoski_kyrkonkyla.
Cela va nous permettre de faire une comparaison plus précise des valeurs par mois entre les données opendate et les données de la sonde Savukoski_kyrkonkyla.
![Alt text](https://github.com/FrancoisFr/TP_QualiteDesDonnees/blob/main/fichier/GraphesMoisParMoisMoyenne.png?raw=true)

Sur cette image nous avons le graphique annuel de la sonde Savukoski_kyrkonkyla en fonction de la T° moyenne.
Cette image tous comme celle des graphiques mensuels va nous permettre de comparer la courbe à celle de Climat.xlsx
![Alt text](https://github.com/FrancoisFr/TP_QualiteDesDonnees/blob/main/fichier/GrapheAnnuelMoyenne.png?raw=true)


<b>Conclusion : </b>
  
  Nous pouvons en conclure que le climat de Savukoski_kyrkonkyla.xlsx est un climat subartic.
  Or le climat de Climat.xlsx se trouve être un climat plutôt continental. 
  Nous pouvons donc en conclure que Climat.xlsx se trouve plus au sud que Savukoski_kyrkonkyla.xlsx bien que la distance entre les deux ne doit pas être très grande.
  
  Nous pensons donc que la capital européene la plus proche de Climat.xlsx se trouve être la capital de la Finlande Helsinki.
