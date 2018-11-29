

# Kleines Skript, welches die Parameter p,q für quadratische Funktionen ausrechnet
# Es soll nur positive p,q und ganzzahlige Nullstellen geben
# um den Schüler*Innen Kummer mit Vorzeichen und unganzzahligen Nullstellen zu ersparen. 

import math
from math import sqrt
count = 0

# setze p und q zwischen 1 und 10

for p in range(1,10):
    for q in range(1,10):

# berechne die Determinante
        det = ((p*p)/4)-q 

# nur wenn diese > 0 gibt es Nullstellen
#
        if (det) > 0:
            x1= -p/2 + sqrt(det)
            x2= -p/2 - sqrt(det)
            rdet = x1
# rdet ist die Testvariable, es sollen nur ganze Zahlen als x1, x2 rauskommen
        else:
# rdet wird auf 0.5 gesetzt, wenn es keine Nullstellen gibt, dann wird nichts ausgegeben
            rdet = 0.5

        inNumber = rdet
        inNumberint = int(inNumber)
        
# caste rdet als int, bleibt es gleich? dann ist
# x1 eine ganze Zahl, und x2 auch eine.
# Gib p und q sowie die Nullstellen aus 

        if inNumber == inNumberint:
            print ('P:', p)
            print ('Q:', q)
            print ('X1:', x1)
            print ('X2:', x2)
            print ("---")
            count = count + 1

# Wie viele haben wir? 
print ('Anzahl: ', count)
