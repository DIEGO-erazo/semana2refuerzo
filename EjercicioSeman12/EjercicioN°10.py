usuario1 = input("Ingrese su nombre de usuario: ")
contraseña1 = input("Ingrese su contraseña: ")

usuario2 = "diego"
contraseña2 = "123"


def validar_usuario(usuario, contraseña):
    if usuario == usuario2 and contraseña == contraseña2:
        print("Acceso Permitido , ", usuario)
    else:
        print("Acceso Denegado.")


validar_usuario(usuario1, contraseña1)
