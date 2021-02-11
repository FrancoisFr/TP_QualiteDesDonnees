import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.widgets import Cursor

#set directory
df2 = pd.read_excel('Savukoski_kirkonkyla.xlsx', 'Temp', engine='openpyxl')
#récupérer les données du fichier excel dans un tableau

days = df2["Jour"]
temp = []
temp_max = []


# graphe mois par mois sur les températures minimales
i = 1
j = 0
mois = ""
plt.figure("Mois de l'année Temp_Min")
while i < 13:
    #défini le mois
    if i == 1:
        mois = "janvier"
        j = 31
    elif i == 2:
        mois = "février"
        j = 28
    elif i == 3:
        mois = "mars"
        j = 31
    elif i == 4:
        mois = "avril"
        j = 30
    elif i == 5:
        mois = "mai"
        j = 31
    elif i == 6:
        mois = "juin"
        j = 30
    elif i == 7:
        mois = "juillet"
        j = 31
    elif i == 8:
        mois = "août"
        j = 31
    elif i == 9:
        mois = "septembre"
        j = 30
    elif i == 10:
        mois = "octobre"
        j = 31
    elif i == 11:
        mois = "novembre"
        j = 30
    elif i == 12:
        mois = "décembre"
        j = 31

    cnt = 0
    # detection des valeurs fausses
    for row in df2[mois]:
        if (type(row) != float) & (type(row) != int):
            df2.loc[cnt, mois] = np.nan
        cnt += 1

    # calcul de la median du mois et remplacement des valeurs manquantes par la median
    median = df2[mois][1:j].median()
    df2[mois].fillna(median, inplace=True)

    plt.subplot(6,2,i)
    plt.plot(df2["jour"], df2[mois])
    plt.title(mois)
    i += 1
    for n in range(j):
        temp.append(df2[mois][n])

plt.show()


#graphe mois par mois sur les températures maximal
i = 1
j = 0
mois = ""
plt.figure("Mois de l'année Temp_Max")
while i < 13:
    #défini le mois
    if i == 1:
        mois = "janvier"
        j = 31
    elif i == 2:
        mois = "février"
        j = 28
    elif i == 3:
        mois = "mars"
        j = 31
    elif i == 4:
        mois = "avril"
        j = 30
    elif i == 5:
        mois = "mai"
        j = 31
    elif i == 6:
        mois = "juin"
        j = 30
    elif i == 7:
        mois = "juillet"
        j = 31
    elif i == 8:
        mois = "août"
        j = 31
    elif i == 9:
        mois = "septembre"
        j = 30
    elif i == 10:
        mois = "octobre"
        j = 31
    elif i == 11:
        mois = "novembre"
        j = 30
    elif i == 12:
        mois = "décembre"
        j = 31

    cnt = 0
    # detection des valeurs fausses
    for row in df2[mois + "_max"]:
        if (type(row) != float) & (type(row) != int):
            df2.loc[cnt, mois + "_max"] = np.nan
        cnt += 1

    # calcul de la median du mois et remplacement des valeurs manquantes par la median
    median = df2[mois + "_max"][1:j].median()
    df2[mois].fillna(median, inplace=True)

    plt.subplot(6,2,i)
    plt.plot(df2["jour" + "_max"], df2[mois + "_max"])
    plt.title(mois + "_max")
    i += 1
    for n in range(j):
        temp_max.append(df2[mois + "_max"][n])

plt.show()


fig, ax = plt.subplots()
plt.title("Graphe annuel température min")
plt.plot(days, temp)
cursor = Cursor(ax,
                horizOn=True,
                vertOn=True,
                color='red',
                linewidth=2.0)

# fonction pour afficher un graphe contenant 30 jours de données centrée sur le curseur
def onClick(event):
    xtab_temp = []
    ytab_temp = []
    x1 = event.xdata
    x2 = round(x1)
    for n in range(30):
        xtab_temp.append(days[x2-15+n])
        ytab_temp.append(temp[x2-15+n])
    plt.figure()
    plt.plot(xtab_temp, ytab_temp)
    plt.show()

fig.canvas.mpl_connect('button_press_event', onClick)
plt.show()

fig2, ax = plt.subplots()
plt.title("Graphe annuel température min")
plt.plot(days, temp_max)
cursor = Cursor(ax,
                horizOn=True,
                vertOn=True,
                color='red',
                linewidth=2.0)

# fonction pour afficher un graphe contenant 30 jours de données centrée sur le curseur

fig2.canvas.mpl_connect('button_press_event', onClick)
plt.show()


#print(df2["mars"][0:32].isnull())