# Inicialización de la lista de instructores y variable de control
instructores = []  # Lista vacía para almacenar los nombres de los instructores
seguir = "s"  # Variable que controla si el usuario quiere continuar
# Bucle principal que permite realizar múltiples operaciones mientras el usuario quiera seguir
while seguir.lower() == "s":
    # Muestra el menú y solicita una opción del usuario
    menu = int(input("Ingrese la opción que va a ejecutar:\n"
                     "1. Insertar nombre de instructor\n"
                     "2. Listar los instructores\n"
                     "3. Modificar algún instructor\n"
                     "4. Borrar un elemento de la lista\n"
                     "5. Buscar instructor\n"
                     "6. Ordenar la lista de forma ascendente\n"))
    # Opción 1: Insertar un nuevo instructor en la lista
    if menu == 1:
        # Solicita el nombre del instructor y lo agrega a la lista
        instructores.append(input("Escriba el nombre del instructor que va a agregar:\n"))
    # Opción 2: Listar todos los instructores con su posición en la lista
    elif menu == 2:
        # Itera sobre la lista e imprime el índice y nombre de cada instructor
        for i, e in enumerate(instructores):
            print("En la posición ", i, " se encuentra ", e)
    # Opción 3: Modificar el nombre de un instructor en una posición específica
    elif menu == 3:
        # Muestra la lista actual con índices para ayudar al usuario
        for i, e in enumerate(instructores):
            print("En la posición ", i, " se encuentra ", e)
        # Solicita la posición a modificar y el nuevo nombre
        a = int(input("Ingresa la posición del instructor que deseas modificar\n"))
        instructores[a] = input("Ingrese el nombre del instructor\n")
    # Opción 4: Borrar un instructor de la lista en una posición específica
    elif menu == 4:
        # Muestra la lista actual con índices para ayudar al usuario
        for i, e in enumerate(instructores):
            print("En la posición ", i, " se encuentra ", e)
        # Solicita la posición del instructor a eliminar
        p = int(input("Escriba la posición del instructor que desea borrar:\n"))
        del instructores[p]  # Elimina el instructor en la posición especificada
    # Opción 5: Buscar un instructor por nombre
    elif menu == 5:
        # Solicita el nombre a buscar y lo convierte a minúsculas para hacer la búsqueda insensible a mayúsculas
        nombre = input("Ingrese el nombre del instructor que desea buscar: ").lower()
        encontrado = False  # Variable para determinar si el nombre fue encontrado
        for nombre1 in instructores:
            if nombre1.lower() == nombre:  # Compara en minúsculas
                encontrado = True
                break
        if encontrado:
            print(f"El instructor {nombre}, fue encontrado en la lista.")
        else:
            print(f"El instructor {nombre}, no fue encontrado en la lista.")
    # Opción 6: Ordenar la lista de instructores alfabéticamente
    elif menu == 6:
        # Ordena la lista y la imprime ordenada
        instructores.sort()
        for i, e in enumerate(instructores):
            print("En la posición ", i, " se encuentra ", e)
    # Mensaje de error en caso de que el usuario ingrese una opción no válida
    else:
        print("Opción inválida")
    # Pregunta al usuario si desea continuar o salir del bucle
    seguir = input("Escriba 's' o 'S' para seguir en su lista:\n")
