# Solicita al usuario ingresar si su tarjeta está personalizada o no
personalizada = int(input("Ingrese 1 si su tarjeta está personalizada o 2 si no esta personalizada: \n"))
# Verifica si la tarjeta está personalizada (opción 1)
if personalizada == 1:
    # Solicita si está realizando un transbordo (cambio de medio de transporte)
    transbordo = int(input("Usted está realizando transbordo, ingrese 1 para sí o 2 para no: \n"))
    # Si está realizando transbordo, muestra el mensaje de éxito
    if transbordo == 1:
        print("¡Transferencia realizada!")
    # Si no está realizando transbordo, verifica el saldo de recarga disponible
    elif transbordo == 2:
        # Solicita el saldo de recarga disponible
        recargaDisponible = int(input("Ingrese la recarga que tiene disponible: \n"))
        # Verifica si la recarga disponible es suficiente para el costo de 2950
        if recargaDisponible > 2950:
            # Calcula y muestra el saldo restante después de descontar el costo
            saldo = recargaDisponible - 2950
            print("El saldo que le queda es ", saldo)
        # Si el saldo es menor que 2950 pero aún positivo, muestra el saldo que falta
        elif recargaDisponible < 2950 and recargaDisponible > 0:
            saldo = recargaDisponible - 2950
            print("No olvide recargar antes de la siguiente subida, usted debe", saldo)
        # Si el saldo es negativo, muestra un mensaje de saldo insuficiente
        elif recargaDisponible < 0:
            print("¡Saldo insuficiente!")
        # Si el valor ingresado es inválido, muestra un mensaje de tarjeta inválida
        else:
            print("¡Tarjeta inválida!")
    # Si la opción de transbordo es inválida, muestra un mensaje de error
    else:
        print("¡Error!")
# Si la tarjeta no está personalizada (opción 2)
elif personalizada == 2:
    # Solicita el saldo de recarga disponible
    recargaDisponible = int(input("Ingrese la recarga que tiene disponible: \n"))
    # Verifica si el saldo es suficiente para el costo de 2950
    if recargaDisponible > 2950:
        saldo = recargaDisponible - 2950
        print("El saldo que le queda es ", saldo)
    # Si el saldo es insuficiente, muestra un mensaje de saldo insuficiente
    elif recargaDisponible < 2950:
        print("¡Saldo insuficiente!")
# Si la opción ingresada no es ni 1 ni 2, muestra un mensaje de tarjeta inválida
else:
    print("¡Tarjeta inválida!")

