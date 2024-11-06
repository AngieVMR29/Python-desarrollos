# Función para sumar
def sumar(n1, n2):
    print("Este es el método sumar")
    resultado = n1 + n2  # Cambié 'sumar' por 'resultado' para evitar el conflicto de nombres
    return resultado
# Función para restar
def restar(n1, n2):
    resultado = n1 - n2
    print("La resta entre el número 1 y el número 2 es ", resultado)
# Función para multiplicar
def multiplicar(n1, n2):
    resultado = n1 * n2
    return resultado
# Función para dividir
def dividir(n1, n2):
    if n2 != 0:  # Verifica si el divisor no es cero
        resultado = n1 / n2
        print("El resultado de la división es ", resultado)
    else:
        print("No se puede dividir entre cero")
# Función para calcular el promedio
def promedio(num1, num2):
    suma = sumar(num1, num2)  # Usamos la función sumar para obtener el resultado
    promedio = suma / 2  # Calculamos el promedio
    print("El promedio de los números es ", promedio)
# Función para sumar varios números
def sumarp():
    suma = 0
    seguir = "si"
    while seguir.lower() == "si":
        numero = int(input("Ingrese un número: "))
        suma += numero  # Sumar el número ingresado
        seguir = input("Para seguir ingrese 'si', de lo contrario 'no': ")
    return suma
# Menú de opciones
print("Menú de opciones:")
num1 = int(input("Ingrese el número 1: \n"))
num2 = int(input("Ingrese el número 2: \n"))
op = input("Ingrese la opción según la operación a realizar: \n 1. Suma \n 2. Resta \n 3. Multiplicación \n 4. División \n 5. Promedio\n")
if op == "1":
    resultado = sumar(num1, num2)  # Llamamos a la función sumar y guardamos el resultado
    print(f"La suma entre {num1} y {num2} es {resultado}")
elif op == "2":
    restar(num1, num2)
elif op == "3":
    resultado = multiplicar(num1, num2)
    print(f"La multiplicación entre {num1} y {num2} es {resultado}")
elif op == "4":
    dividir(num1, num2)
elif op == "5":
    promedio(num1, num2)
else:
    print("Opción no válida.")

