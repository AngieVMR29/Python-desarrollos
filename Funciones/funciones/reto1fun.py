# Lista para almacenar los instructores
instructores = []
# Variable para controlar si el ciclo continúa o no
seguir = "s"
# Función para agregar un instructor a la lista
def agregar():
    # Se pide al usuario que ingrese el nombre del instructor a agregar
    instructores.append(input("Escriba el nombre del instructor que va a agregar: \n"))
# Función para listar todos los instructores registrados
def listar():
    # Recorre la lista de instructores y muestra la posición y el nombre de cada uno
    for i, e in enumerate(instructores):
        print(f"En la posición {i} se encuentra {e}")
# Función para modificar el nombre de un instructor
def modificar():
    # Muestra la lista de instructores con sus posiciones
    for i, e in enumerate(instructores):
        print(f"En la posición {i} se encuentra {e}")
    # Pide al usuario que ingrese la posición del instructor a modificar
    a = int(input("Ingresa la posición del instructor que deseas modificar: \n"))
    # Modifica el nombre del instructor en la posición seleccionada
    instructores[a] = input("Ingrese el nuevo nombre del instructor: \n")
# Función para borrar un instructor de la lista
def borrar():
    # Muestra la lista de instructores con sus posiciones
    for i, e in enumerate(instructores):
        print(f"En la posición {i} se encuentra {e}")
    # Pide al usuario que ingrese la posición del instructor a borrar
    p = int(input("Escriba la posición del instructor que desea borrar: \n"))
    # Elimina el instructor de la lista en la posición indicada
    del instructores[p]
# Función para buscar un instructor por nombre
def buscar():
    # Pide al usuario que ingrese el nombre del instructor a buscar
    nombre = input("Ingrese el nombre del instructor que desea buscar: ")
    nombre = nombre.lower()  # Convierte el nombre a minúsculas para hacer la búsqueda insensible al caso
    encontrado = False
    # Recorre la lista de instructores y busca el nombre
    for nombre1 in instructores:
        if nombre1.lower() == nombre:  # Compara el nombre en minúsculas
            encontrado = True
            break
    # Informa al usuario si el instructor fue encontrado o no
    if encontrado:
        print(f"El instructor {nombre} fue encontrado en la lista.")
    else:
        print(f"El instructor {nombre} no fue encontrado en la lista.")
# Función para organizar la lista de instructores en orden ascendente
def organizar():
    # Ordena la lista de instructores alfabéticamente
    instructores.sort()
    # Muestra la lista organizada
    for i, e in enumerate(instructores):
        print(f"En la posición {i} se encuentra {e}")
# Ciclo principal para interactuar con el usuario
while seguir.lower() == "s":
    # Menú para seleccionar la acción a realizar
    menu = int(input("Ingrese la opción que va a ejecutar: \n"
                     "1. Insertar nombre de instructor \n"
                     "2. Listar los instructores \n"
                     "3. Modificar algún instructor \n"
                     "4. Borrar un instructor \n"
                     "5. Buscar instructor \n"
                     "6. Ordenar la lista de forma ascendente \n"))
    
    # Ejecuta la acción según la opción seleccionada
    if menu == 1:
        agregar()  # Agregar un instructor
    elif menu == 2:
        listar()  # Listar instructores
    elif menu == 3:
        modificar()  # Modificar un instructor
    elif menu == 4:
        borrar()  # Borrar un instructor
    elif menu == 5:
        buscar()  # Buscar un instructor
    elif menu == 6:
        organizar()  # Organizar la lista de instructores
    else:
        print("Opción inválida.")  # Si la opción no es válida, se muestra un mensaje de error
    # Pregunta si el usuario quiere seguir interactuando con el programa
    seguir = input("Escriba 's' o 'S' para seguir en su lista, cualquier otra tecla para salir: ")
