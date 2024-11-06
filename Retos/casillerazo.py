# Inicialización de variables globales
seguir = "Si"  # Variable que controla si el jugador desea seguir jugando
apostar = 0  # Variable para almacenar el valor apostado (no se usa en el flujo principal)
valorglobal = 10000  # Valor inicial para apostar
# Importa randint para generar números aleatorios
from random import randint
# Función que simula el lanzamiento de una moneda
def lanzarmoneda():
    nombreJugador = input("Ingrese su nombre: \n")  # Solicita el nombre del jugador
    Moneda = randint(1, 2)  # Genera un número aleatorio, 1 para cara y 2 para sello
    return (nombreJugador, Moneda)
# Función que solicita la elección del jugador y el valor a apostar
def jugar():
    # Solicita que el jugador elija entre cara (1) o sello (2)
    eleccion = int(input("Escoja 1 para cara o 2 para sello\n"))
    # Solicita el valor que el jugador desea apostar
    apostado = int(input("Ingrese valor a apostar\n"))
    return (eleccion, apostado)
# Función para procesar la ganancia del jugador
def ganar(valorglobal, apos):
    apostar = apos * 2  # El jugador gana el doble de lo apostado
    valorglobal = valorglobal + apostar  # Se actualiza el valor global
    print("Su ganancia es de ", apos, " y el valor para apostar que le queda es de ", valorglobal)
# Función para procesar la pérdida del jugador
def perder(valorglobal, apos):
    valorglobal = valorglobal - apos  # Se descuenta lo apostado en caso de perder
    print("Su perdida es de ", apos, " y el valor para apostar que le queda es de ", valorglobal)
# Bucle principal del juego
while seguir == "Si" or seguir == "si" or seguir == "sI" or seguir == "SI":
    # Lanza la moneda y obtiene el nombre del jugador y el resultado de la moneda
    nombreJugador, moneda = lanzarmoneda()
    # Obtiene la elección y la cantidad apostada
    eleccion, apo = jugar()
    # Condiciones de ganancia y pérdida basadas en los resultados
    if moneda == 1 and eleccion == 1:
        print("Salió cara y usted escogió cara ¡Ganaste,", nombreJugador, "!")
        ganar(valorglobal, apo)
        seguir = input("¿Desea seguir jugando?\n")  # Pregunta si desea seguir jugando
    elif moneda == 2 and eleccion == 2:
        print("Salió sello y usted escogió sello ¡Ganaste,", nombreJugador, "!")
        ganar(valorglobal, apo)
        seguir = input("¿Desea seguir jugando?\n")
    elif moneda == 1 and eleccion == 2:
        print("Salió cara y usted escogió sello ¡Perdiste, ", nombreJugador, " !")
        perder(valorglobal, apo)
        seguir = input("¿Desea seguir jugando?\n")
    elif moneda == 2 and eleccion == 1:
        print("Salió sello y usted escogió cara ¡Perdiste, ", nombreJugador, "!")
        perder(valorglobal, apo)
        seguir = input("¿Desea seguir jugando?\n")
    elif moneda != 2 or eleccion != 1:
        print("Digitaste una opción invalida")
    else:
        print("Datos incorrectos")
