print("Bienvenido al programa")  # Muestra un mensaje de bienvenida.
personas = int(input("Ingrese la cantidad de personas "))  # Solicita al usuario la cantidad de personas y convierte el valor a entero.
peso1 = 0  # Variable para acumular el peso total de los niños.
j = 0  # Contador para la categoría de jóvenes.
k = 0  # Contador para la categoría de niños.
# Itera sobre el número de personas ingresadas por el usuario.
for i in range(personas):
    peso = int(input("Ingrese el peso "))  # Solicita al usuario el peso de la persona actual y lo convierte a entero.
    edad = int(input("Ingrese la edad "))  # Solicita al usuario la edad de la persona actual y la convierte a entero.
    # Verifica si la persona pertenece a la categoría de niños (0 a 12 años).
    if 0 <= edad <= 12:
        k += 1  # Incrementa el contador de niños.
        peso1 += peso  # Suma el peso de la persona a la variable `peso1` que almacena el total de peso de los niños.
    # Verifica si la persona pertenece a la categoría de jóvenes (13 a 29 años).
    elif 13 <= edad <= 29:
        categoria = "Jovenes"  # Asigna la categoría "Jóvenes".
        j += 1  # Incrementa el contador de jóvenes.
    # Verifica si la persona pertenece a la categoría de adultos (30 a 59 años).
    elif 30 <= edad <= 59:
        categoria = "Adultos"  # Asigna la categoría "Adultos".
# Calcula el promedio de peso de los niños.
promedio = peso1 / k  # Divide el peso total de los niños entre la cantidad de niños para obtener el promedio.

   