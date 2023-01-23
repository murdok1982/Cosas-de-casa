
"""programa de inteligencia artificial para el juego de Euromillones"""


import random



N1=[50,21,4,19,9]
E1=[3,6]
N2=[44,10,23,26,28]
E2=[10,8]
N3=[20,17,21,42,23]
E3=[2,3]
N4=[23,19,50,44,42]
E4=[2,3]
num=[0,0,0,0,0]
star=[0,0]

print("Bienvenido al juego de Euromillones")
print("Este programa es una inteligencia artificial para el juego de Euromillones")
print("Para jugar, seleccione una opcion")

opcion = int(input("Seleccione una opcion: "))

if opcion == 1:
    num=random.sample(N1+N2+N3+N4,5)
    star=random.sample(E1+E2+E3+E4,2)
    print("Los numeros son: ",num)
    print("Las estrellas son: ",star)
    print("Gracias por jugar")






