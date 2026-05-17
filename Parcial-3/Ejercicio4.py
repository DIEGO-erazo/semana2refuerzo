for registro in range(1, 51):
    if registro % 3 == 0:
        continue

    if registro == 42:
        print("Brecha de seguridad detectada. Proceso detenido.")
        break

    print(f"Procesando registro ID: {registro}")