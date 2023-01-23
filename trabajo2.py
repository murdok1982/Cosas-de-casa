#condicional if
numeroIf = 5
if numeroIf > 0:
    print("La variable es positiva")
elif numeroIf < 0:
    print("La variable es negativa")
else:
    print("La variable es 0")

#bucle while
numeroWhile = 0
while numeroWhile < 3:
    numeroWhile += 1
    print(numeroWhile)

#bucle do-while
numeroDoWhile = 0
while True:
    numeroDoWhile += 1
    print(numeroDoWhile)
    if numeroDoWhile >= 3:
        break

#bucle for
for numeroFor in range(0,4):
    print(numeroFor)

#Switch case
estacion = "otoño"

def switch_estacion(estacion):
    switcher = {
        "verano": "Es verano",
        "otoño": "Es otoño",
        "invierno": "Es invierno",
        "primavera": "Es primavera"
    }
    return switcher.get(estacion, "Estación no válida")

print(switch_estacion(estacion))
