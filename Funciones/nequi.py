import random  # Importa la biblioteca random para generar códigos de retiro aleatorios.
continuar = 1  # Inicializa la variable que controla el bucle de transacciones.
print("Usted esta ingresando a nuestros sistemas, por favor indique los siguientes datos: ")
# Solicita al usuario su número de celular y contraseña.
celular = input("Ingrese su número de celular: ")
contraseña = input("Ingrese su contraseña: ")
# Verifica que el número de celular tenga 10 dígitos y la contraseña tenga 4.
if len(celular) == 10 and len(contraseña) == 4:
    print("¡Usted ha ingresado exitosamente!")
    valorI = 4500  # Inicializa el saldo de la cuenta con 4500.
    # Bucle para realizar transacciones mientras el usuario desee continuar.
    while continuar == 1:
        # Muestra el menú de opciones y solicita al usuario que elija un proceso.
        proceso = int(input("Escoja el número que corresponde al proceso que quiere realizar según el siguiente menú:\n 1. Retiro\n 2. Enviar\n 3. Recarga\n 4. Salir\n"))
        # Opción 1: Retiro de dinero.
        if proceso == 1:
            puntodeRetiro = int(input("Ingresa\n 1. Punto físico\n 2. Cajero\n"))
            # Si elige el punto físico y tiene más de 2000 en la cuenta:
            if puntodeRetiro == 1 and valorI > 2000:
                codigodeRetiro = random.randint(0, 999999)  # Genera un código de retiro aleatorio.
                print("Usted escogió punto físico como forma de retiro y su código para retirar es", codigodeRetiro)
                valorR = int(input("Ingrese el valor a retirar: "))
                valorI -= valorR  # Resta el valor retirado del saldo.
                print("Usted retiró", valorR, "el saldo que le queda en la cuenta es de", valorI)
            # Si elige el cajero y tiene más de 2000 en la cuenta:
            elif puntodeRetiro == 2 and valorI > 2000:
                codigodeRetiro = random.randint(0, 999999)  # Genera un código de retiro aleatorio.
                print("Usted escogió cajero como forma de retiro y su código para retirar es", codigodeRetiro)
                valorR = int(input("Ingrese el valor a retirar: "))
                valorI -= valorR  # Resta el valor retirado del saldo.
                print("¡Retiro exitoso! Usted retiró", valorR, "el saldo que le queda en la cuenta es de", valorI)
            # Si elige cualquier método de retiro pero el saldo es insuficiente:
            elif (puntodeRetiro == 1 or puntodeRetiro == 2) and valorI < 2000:
                print("¡No te alcanza!")
            else:
                print("¡Transacción inválida!")
        # Opción 2: Envío de dinero.
        elif proceso == 2:
            numEnvio = input("Ingrese por favor el número al que va a realizar el envío: ")
            valorE = int(input("Ingrese el valor que va a enviar: "))
            # Si tiene suficiente saldo para el envío:
            if valorE < valorI:
                valorI -= valorE  # Resta el valor enviado del saldo.
                print("Usted envió", valorE, "el saldo que le queda en la cuenta es de", valorI)
            else:
                print("Proceso inválido, saldo insuficiente")
        # Opción 3: Recarga de dinero.
        elif proceso == 3:
            valorRec = int(input("Ingrese el valor que va a recargar a su cuenta:\n"))
            print("Usted va a recargar", valorRec)
            seguro = int(input("¿Está seguro? Ingrese el número correspondiente\n 1. Sí\n 2. No\n"))
            # Si confirma la recarga:
            if seguro == 1:
                valorI += valorRec  # Suma el valor recargado al saldo.
                print("¡Recarga exitosa! Usted recargó", valorRec, "el saldo disponible en la cuenta es de", valorI)
            elif seguro == 2:
                print("¡Transacción cancelada!")
            else:
                print("¡Transacción inválida!")
        # Opción 4: Salir del sistema.
        elif proceso == 4:
            print("Usted está por salir del sistema")
            # Pregunta si quiere continuar o salir definitivamente.
            continuar = int(input("Ingrese 1 para continuar realizando transacciones o 2 para salir\n"))
# Si el número de celular o la contraseña no cumplen con el formato:
else:
    print("¡Ups! Tus datos son incorrectos, tienes 3 intentos más.")
    contadorIntentos = 1  # Contador para los intentos fallidos.
    # Permite 3 intentos adicionales.
    while contadorIntentos < 4:
        contadorIntentos += 1
        celular = input("Ingrese su número de celular: ")
        contraseña = input("Ingrese su contraseña: ")
        # Verifica nuevamente si los datos son correctos.
        if len(celular) == 10 and len(contraseña) == 4:
            print("¡Usted ha ingresado exitosamente!")
            break
        else:
            print("¡Ups! Tus datos son incorrectos, intenta nuevamente.")

