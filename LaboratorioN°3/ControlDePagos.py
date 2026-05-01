def sistema_control_pagos():
    continuar = "si"

    # REQUISITO 1: Uso de while para retir el proceso si es necesario 
    while continuar.lower().strip() == "si":
        print("\n--- SISTEMA DE CONTROL DE PAGOS (Diego Erazo) ---")
        try:
            num_cuotas = int(input("Cantidad de cuotas a procesar: "))

            # REQUISITO 2: Uso de for
            for i in range(1, num_cuotas + 1):
                print(f"\n--- Cuota #{i} ---")
                monto = float(input("Monto de la cuota ($): "))
                dias_retraso = int(input("Días de retraso: "))

                # REQUISITO 3: Uso de if para validar mora
                if dias_retraso > 0:
                    # AQUÍ ESTÁ LA CORRECCIÓN: 5% multiplicado por los días
                    recargo = (monto * 0.05) * dias_retraso
                    print(
                        f"Recargo (5% por cada uno de los {dias_retraso} días): ${recargo:.2f}"
                    )
                else:
                    recargo = 0
                    print("Pago a tiempo. Sin recargos.")

                total = monto + recargo

                # REQUISITO 4: Uso de select case / match
                print("Estado (1. Completo | 2. Pendiente | 3. Convenio)")
                opcion = input("Seleccione opción: ")
                match opcion:
                    case "1":
                        estado = "COMPLETO"
                    case "2":
                        estado = "PENDIENTE"
                    case "3":
                        estado = "CONVENIO"
                    case _:
                        estado = "DESCONOCIDO"

                print(f"Resumen: {estado} | Total a pagar: ${total:.2f}")

        except ValueError:
            print("Error: Por favor, ingrese valores numéricos.")

        continuar = input("\n¿Desea procesar otro lote? (si/no): ")

    print("Programa finalizado.")


if __name__ == "__main__":
    sistema_control_pagos()
