import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.widgets import Cursor, Slider

#set directory
df = pd.read_excel('Climat.xlsx', 'SI ', engine='openpyxl')
#récupérer les données du fichier excel dans un tableau

days = (df["jour"])
temp = (df["Température"])

#xtab_temp = []
#ytab_temp = []

# graphes mois par mois créer avec les données du fichier excel
plt.figure("Graphes mois par mois")

plt.subplot(6,2,1)
plt.plot(df["Jour"], df["janvier"])
plt.title("Janvier")

plt.subplot(6,2,2)
plt.plot(df["Jour"], df["février"])
plt.title("Février")

plt.subplot(6,2,3)
plt.plot(df["Jour"], df["mars"])
plt.title("Mars")

plt.subplot(6,2,4)
plt.plot(df["Jour"], df["avril"])
plt.title("Avril")

plt.subplot(6,2,5)
plt.plot(df["Jour"], df["mai"])
plt.title("Mai")

plt.subplot(6,2,6)
plt.plot(df["Jour"], df["juin"])
plt.title("Juin")

plt.subplot(6,2,7)
plt.plot(df["Jour"], df["juillet"])
plt.title("Juillet")

plt.subplot(6,2,8)
plt.plot(df["Jour"], df["août"])
plt.title("Aout")

plt.subplot(6,2,9)
plt.plot(df["Jour"], df["septembre"])
plt.title("Septembre")

plt.subplot(6,2,10)
plt.plot(df["Jour"], df["octobre"])
plt.title("Octobre")

plt.subplot(6,2,11)
plt.plot(df["Jour"], df["novembre"])
plt.title("Novembre")

plt.subplot(6,2,12)
plt.plot(df["Jour"], df["décembre"])
plt.title("Décembre")


# graphes à l'année avec un curseur
fig, ax = plt.subplots()
#wallah je tente un truc
#x1 = 16

#for n in range(30):
#    if ((x1 - 15 + n) > 0) & ((x1 - 15 + n) < 365):
#        xtab_temp.append(df["jour"][x1 - 15 + n])
#        ytab_temp.append(df["Température"][x1 - 15 + n])

plt.plot(df["jour"], df["Température"])
#p, = plt.plot(xtab_temp, ytab_temp)
plt.title("Graphe annuel")
cursor = Cursor(ax,
                horizOn=False,
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

#plt.axes([0, 10, 0, 365])

#axSlider = plt.axes([0.1, 0.1, 0.8, 0.05])
#plotSlider = Slider(axSlider, 'Test Slider',
#                    valmin = 15,
#                    valmax = 350,
#                    valstep = 1,
#                    closedmax=True,
#                    )

#def val_update(val):
#    x1 = plotSlider.val
    #global xtab_temp
    #global y
#    xtab_temp.clear()
#    ytab_temp.clear()
#    if ((x1-15) > 0) & ((x1+15) < 365):
#        for n in range(30):
#            xtab_temp.append(days[x1 - 15 + n])
#            ytab_temp.append(temp[x1 - 15 + n])
#    p.set_xdata(xtab_temp[0:29])
#    p.set_ydata(ytab_temp[0:29])
#    plt.draw()
fig.canvas.mpl_connect('button_press_event', onClick)

#plotSlider.on_changed(val_update)
plt.show()