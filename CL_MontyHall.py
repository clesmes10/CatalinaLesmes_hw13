import numpy as np
import matplotlib.pyplot as plt
from random import shuffle

#funcion que retorna la lista dada de forma desordenada mediante shuffle
def sort_doors():
    listagoat = ["goat", "goat", "car"]
    np.random.shuffle(listagoat)
    return listagoat
sortd = sort_doors()

#funcion que retorna un numero aleatorio entre 0 y 2 con random
def choose_door():
    num = [0,1,2]
    numaleatorio = np.random.choice(num)
    return numaleatorio
choosed = choose_door()

#funcion que revisa las puertas para revelar donde hay una cabra
def reveal_door(lista, choice):
    for j in range(len(lista)):
        if(lista[j] == "goat" and j != choice):
            lista[j] = "GOAT_MONTY"
            return lista
revelarpuerta = reveal_door(sortd, choosed)

#funcion para revelar todas las puertas mediante la lista el numero choice y un booleano
def finish_game(lista, choice, change):
    if(change ==False):
        return lista[choice]
    else:
        for i in range(len(lista)):
            if(i!= choice and lista[i] != "GOAT_MONTY"):
                listam = lista[i]
                return  listam



#se simulan muchos escenarios de juego con false y true
listafalsa = []
listaverdadera = []

for k in range(100):
    terminarjuegofalso = finish_game(revelarpuerta, choosed, False)
    listafalsa.append(terminarjuegofalso)
for j in range(100):
    terminarjuegoverdadero = finish_game(revelarpuerta, choosed, True)
    listaverdadera.append(terminarjuegoverdadero)

#calculo de veces que se gana
ganaverdadero = 0.0
ganafalso = 0.0

for i in range(len(listafalsa)):
    if(listafalsa[i] == "car"):
        ganafalso += 1.0

for j in range(len(listaverdadera)):
    if(listaverdadera[j] == "car"):
        ganaverdadero += 1.0
#probabilidad de ganar falso o verdadero

probverdadera = ganaverdadero/len(listaverdadera)
probfalsa = ganafalso/len(listafalsa)

print "la probabilidad verdadera es: ", probverdadera, "y la probabilidad falsa es: ", probfalsa 

    
    



    
