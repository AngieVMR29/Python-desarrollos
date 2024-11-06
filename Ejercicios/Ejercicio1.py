print("Bienvenid@")  # Esta línea imprime el mensaje de bienvenida "Bienvenid@" en la consola.
inverT = int(input("Ingrese la inversión total: "))  # Solicita al usuario que ingrese la inversión total y la convierte en entero.
hipot = int(input("Ingrese el monto de la hipoteca: "))  # Solicita al usuario el monto de la hipoteca y lo convierte en entero.
faltante = inverT - hipot  # Calcula la diferencia entre la inversión total y la hipoteca, y la guarda en la variable `faltante`.
if (hipot < 1000000):  # Verifica si el monto de la hipoteca es menor a 1,000,000.
    inverT = inverT * 50 / 100  # Calcula el 50% de la inversión total.
    print(f"Usted debe invertir {inverT} y el socio debe invertir {inverT}")  # Muestra la inversión necesaria para cada socio si la hipoteca es menor a 1,000,000.
elif (hipot >= 1000000):  # Verifica si la hipoteca es igual o mayor a 1,000,000.
    faltante = faltante * 50 / 100  # Calcula el 50% del monto faltante.
    print(f"Usted debe invertir {inverT + faltante}\n El restante del socio es {faltante}")  # Muestra la inversión del usuario y el aporte del socio si la hipoteca es igual o mayor a 1,000,000.


