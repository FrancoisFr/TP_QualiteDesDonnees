# TP_QualiteDesDonnees

Ce travail à été effectué sous pyCharm.

Pour répondre aux besoin du TP, 2 fichiers différent ont été créer.

Le fichier mat1.py permet d'utiliser le jeu de donnée de la première feuille ( le premier dans le fichier) afin de fournir un graphe regroupant les températures de chaque jour de l'année dans une fenêtre, ainsi qu'un graphe pour chaque mois dans une seconde fenêtre.

![Alt text](https://github.com/FrancoisFr/TP_QualiteDesDonnees/blob/main/fichier/GrapheAnnuel.PNG?raw=true)

![Alt text](https://github.com/FrancoisFr/TP_QualiteDesDonnees/blob/main/fichier/GrapheMoisParMois.PNG?raw=true)


Sur le graphe annuel, un curseur rouge est mis en place, prenant en compte la position x du curseur dans le graphe qui représente le jour dans l'année. À partir de ce curseur, un clique sur le graphe permet d'ouvrir une troisième fenêtre qui contiendra les températures des 30 jours autour du curseur.

![Alt text](https://github.com/FrancoisFr/TP_QualiteDesDonnees/blob/main/fichier/Graphe30Jours.PNG?raw=true)


Le fichier mat2.py appelle les données contenu dans la seconde feuille, avec un jeu de donnée contenant des erreurs.

Afin de corriger celles-ci, nous vérifions dans le programme chaque variable, celle ne correspondant pas aux types d'entrée attendu sont remplacé dans un premier temps par une valeur nulle.

Une fois cela fait, chaque valeur nulle est remplacé par la valeur médiane des températures du mois. Cela nous permet d'obtenir les graphes suivants:

![Alt text](https://github.com/FrancoisFr/TP_QualiteDesDonnees/blob/main/fichier/GrapheMoisParMoisErreur.PNG?raw=true)

Ce qui donne en graphe annuel:

![Alt text](https://github.com/FrancoisFr/TP_QualiteDesDonnees/blob/main/fichier/GrapheAnnuelErreur.PNG?raw=true)

Enfin, de la même manière en cliquant sur le graphe on en obtient un nouveau graphe avec 15 jours avant et après le curseur:

![Alt text](https://github.com/FrancoisFr/TP_QualiteDesDonnees/blob/main/fichier/Graphe30JoursErreur.PNG?raw=true)
