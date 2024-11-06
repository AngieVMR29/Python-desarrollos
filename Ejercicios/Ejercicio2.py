print("Bienvenid@")  # Imprime un mensaje de bienvenida en la consola.
superficie = int(input("Ingrese los metros cuadrados de la superficie "))  # Solicita al usuario ingresar los metros cuadrados y convierte el valor a entero.
if (superficie > 1000000):  # Comprueba si la superficie es mayor a 1,000,000 metros cuadrados.
    pino = superficie * 70 / 100  # Calcula el 70% de la superficie para el área de pino.
    oyamel = superficie * 20 / 100  # Calcula el 20% de la superficie para el área de oyamel.
    cedro = superficie * 10 / 100  # Calcula el 10% de la superficie para el área de cedro.
    print(f"Para pino debe sembrar 70% que es: {pino}")  # Muestra la cantidad de metros cuadrados para sembrar pino.
    print(f"Para oyamel debe sembrar 20% que es: {oyamel}")  # Muestra la cantidad de metros cuadrados para sembrar oyamel.
    print(f"Para cedro debe sembrar 10% que es: {cedro}")  # Muestra la cantidad de metros cuadrados para sembrar cedro.
elif (superficie <= 1000000):  # Verifica si la superficie es igual o menor a 1,000,000 metros cuadrados.
    pino = superficie * 50 / 100  # Calcula el 50% de la superficie para el área de pino.
    oyamel = superficie * 30 / 100  # Calcula el 30% de la superficie para el área de oyamel.
    cedro = superficie * 20 / 100  # Calcula el 20% de la superficie para el área de cedro.
    print(f"Para pino debe sembrar 50% que es: {pino}")  # Muestra la cantidad de metros cuadrados para sembrar pino.
    print(f"Para oyamel debe sembrar 30% que es: {oyamel}")  # Muestra la cantidad de metros cuadrados para sembrar oyamel.
    print(f"Para cedro debe sembrar 20% que es: {cedro}")  # Muestra la cantidad de metros cuadrados para sembrar cedro.

    