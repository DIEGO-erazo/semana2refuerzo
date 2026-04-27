import random

secreto = random.randint(1, 50)
intentos = []
acertó = False

while not acertó:
    tiro = int(input("Adivina el número: "))
    intentos.append(tiro)
    if tiro == secreto:
        print("¡Acertaste!")
        acertó = True
    elif tiro < secreto:
        print("Es mayor")
    else:
        print("Es menor")

for i in intentos:
    print(f"Intentaste con: {i}")
