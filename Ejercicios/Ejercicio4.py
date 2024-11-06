print("Bienvenid@ al programa que calcula el salario semanal de los obreros")  # Imprime el mensaje de bienvenida.
obreros = int(input("Ingrese el número de obreros "))  # Solicita el número de obreros y lo convierte a entero.
# Itera sobre la cantidad de obreros especificada.
for i in range(obreros):
    horas = int(input(f"Ingrese las horas trabajadas del obrero {i+1}: "))  # Solicita las horas trabajadas del obrero actual y las convierte a entero.
    # Verifica si el obrero trabajó 40 horas o menos.
    if horas <= 40:
        salario = 20 * horas  # Calcula el salario base multiplicando las horas por 20.
        print(f"Su salario semanal es {salario}")  # Muestra el salario semanal.
    # Verifica si el obrero trabajó más de 40 horas.
    elif horas > 40:
        horasT = 40  # Define el límite de horas normales como 40.
        salario = 40 * 20  # Calcula el salario base para las primeras 40 horas.
        horaex = horas - 40  # Calcula las horas extra.
        extra = horaex * 25  # Calcula el pago adicional por horas extra (25 por cada hora extra).
        print(f"Su salario semanal es {salario} y el extra es: {extra}")  # Muestra el salario semanal y el pago extra.

