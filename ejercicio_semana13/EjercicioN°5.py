correcta = "1234"
intentos = []
while True:
    pass_input = input("Contraseña: ")
    if pass_input == correcta:
        print("Acceso concedido")
        break
    else:
        intentos.append("Fallido")
        if pass_input != correcta:
            print("Incorrecta")

for i in range(len(intentos)):
    print(f"Intento número {i + 1} fue incorrecto")
