import random  # Importa la librería random para generar números aleatorios, como códigos de retiro
continuar = 1  # Variable que se utiliza para controlar el ciclo de las transacciones
print("Usted está ingresando a nuestros sistemas, por favor indique los siguientes datos: ")  # Mensaje de bienvenida
celular = input("Ingrese su número de celular: ")  # Solicita al usuario ingresar su número de celular
contraseña = input("Ingrese su contraseña: ")  # Solicita al usuario ingresar su contraseña
# Verificación de que el celular tiene 10 dígitos y la contraseña 4 caracteres
if len(celular) == 10 and len(contraseña) == 4:
    print("¡Usted ha ingresado exitosamente!")  # Mensaje si las credenciales son correctas
    valorI = 4500  # Saldo inicial de la cuenta
    while continuar == 1:  # Ciclo principal para realizar múltiples transacciones
        proceso = int(input("Escoja el número que corresponde al proceso que quiere realizar según el siguiente menú: \n 1. Saca \n 2. Envia \n 3. Recarga \n 4. Salir\n"))
        # Solicita al usuario elegir un proceso entre las opciones disponibles
        # Opción para realizar un retiro
        if proceso == 1:
            puntodeRetiro = int(input("Ingresa \n 1.Punto físico \n 2. Cajero\n"))  # Solicita el tipo de retiro (punto físico o cajero)
            if puntodeRetiro == 1 and valorI > 2000:  # Verifica si el saldo es suficiente para el retiro en punto físico
                codigodeRetiro = random.randint(100000, 999999)  # Genera un código aleatorio de 6 dígitos para el retiro
                print("Usted escogió punto físico como forma de retiro y su código para retirar es ", codigodeRetiro)
                valorR = int(input("Ingrese el valor a retirar"))  # Solicita el valor a retirar
                valorI = valorI - valorR  # Actualiza el saldo después del retiro
                print("Usted retiró ", valorR, " el saldo que le queda en la cuenta es de ", valorI)  # Muestra el saldo restante
            elif puntodeRetiro == 2 and valorI > 2000:  # Verifica si el saldo es suficiente para el retiro en cajero
                codigodeRetiro = random.randint(100000, 999999)  # Genera un código aleatorio de 6 dígitos para el retiro
                print("Usted escogió cajero como forma de retiro y su código para retirar es ", codigodeRetiro)
                valorR = int(input("Ingrese el valor a retirar"))  # Solicita el valor a retirar
                valorI = valorI - valorR  # Actualiza el saldo después del retiro
                print("¡Retiro exitoso! Usted retiró ", valorR, " el saldo que le queda en la cuenta es de ", valorI)  # Muestra el saldo restante
            elif (puntodeRetiro == 1 or puntodeRetiro == 2) and valorI < 2000:  # Verifica si el saldo es insuficiente
                print("¡No te alcanza!")  # Mensaje cuando el saldo no es suficiente
            else:
                print("¡Transacción inválida!")  # Mensaje si la opción de retiro es inválida
        # Opción para enviar dinero
        elif proceso == 2:
            numEnvio = input("Ingrese por favor el número al que va a realizar el envío: ")  # Solicita el número de destino para el envío
            valorE = int(input("Ingrese el valor que va a enviar: "))  # Solicita el valor que se va a enviar
            if valorE < valorI:  # Verifica si el saldo es suficiente para el envío
                valorI = valorI - valorE  # Actualiza el saldo después del envío
                print("Usted envió ", valorE, " el saldo que le queda en la cuenta es de ", valorI)  # Muestra el saldo restante
            elif valorE > valorI:  # Si el valor a enviar es mayor al saldo disponible
                print("Proceso inválido, saldo insuficiente")  # Mensaje si el saldo es insuficiente
        # Opción para recargar saldo
        elif proceso == 3:
            valorRec = int(input("Ingrese el valor que va a recargar a su cuenta: \n"))  # Solicita el valor de la recarga
            print("Usted va a recargar ", valorRec)  # Muestra el valor de la recarga
            seguro = int(input("¿Está seguro? Ingrese el número correspondiente\n 1.Si \n 2.No \n"))  # Pide confirmación
            if seguro == 1:  # Si el usuario confirma la recarga
                valorI = valorI + valorRec  # Actualiza el saldo con la recarga
                print("¡Recarga exitosa! Usted recargó ", valorRec, " el saldo disponible en la cuenta es de ", valorI)  # Muestra el saldo actualizado
            elif seguro == 2:  # Si el usuario cancela la recarga
                print("¡Transacción cancelada!")  # Mensaje de cancelación
            else:
                print("¡Transacción inválida!")  # Mensaje si la opción de confirmación es inválida
        # Opción para salir del sistema
        elif proceso == 4:
            print("Usted está por salir del sistema")  # Mensaje de salida
            continuar = int(input("Ingresa 1.Para continuar realizando transacciones o 2. Para salir \n"))  # Pregunta si el usuario desea seguir o salir
# Si las credenciales de celular o contraseña son incorrectas
elif len(celular) != 10 and len(contraseña) != 4:
    print("¡Upps! Tus datos son incorrectos, tienes 3 intentos más.")  # Mensaje de error inicial
    contadorIntentos = 1  # Inicializa el contador de intentos
    while contadorIntentos < 4:  # Permite hasta 3 intentos
        contadorIntentos = contadorIntentos + 1  # Incrementa el contador de intentos
        celular = input("Ingrese su número de celular: ")  # Solicita nuevamente el celular
        contraseña = input("Ingrese su contraseña: ")  # Solicita nuevamente la contraseña
        if len(celular) == 10 and len(contraseña) == 4:  # Verifica si las credenciales son correctas
            print("¡Usted ha ingresado exitosamente!")  # Si las credenciales son correctas, muestra mensaje de éxito
        elif len(celular) != 10 and len(contraseña) != 4:  # Si las credenciales siguen siendo incorrectas
            print("¡Upps! Tus datos son incorrectos, intenta nuevamente.")  # Muestra el mensaje de error
