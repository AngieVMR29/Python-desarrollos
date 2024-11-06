# Inicialización de la lista de instructores
instructores = []  # Lista que almacenará los nombres de los instructores
seguir = "s"  # Variable que controla si el usuario desea seguir utilizando el menú
# Bucle principal que mantiene el programa en ejecución mientras el jugador quiera seguir interactuando
while seguir == "s" or seguir == "S":
    """
    Bucle principal que muestra un menú de opciones para interactuar con la lista de instructores.
    Dependiendo de la opción elegida, el programa permite insertar, listar, modificar, borrar, 
    buscar u ordenar los instructores en la lista.
    """
    # Muestra el menú de opciones y solicita la opción que el usuario desea ejecutar
    menu = int(input("Ingrese la opción que va a ejecutar \n1. Insertar nombre de instructor \n2.Listar los instructores \n3.Modificar algún instructor \n4.Borrar un elemento de la lista \n5.Buscar instructor \n6.Ordenar la lista de forma ascendente \n"))
    if menu == 1:
        """
        Opción 1: Permite agregar un nuevo instructor a la lista.
        El nombre del instructor se obtiene como entrada del usuario y se agrega a la lista 'instructores'.
        """
        instructores.append(input("Escriba el nombre del instructor que va a agregar \n"))
    elif menu == 2:
        """
        Opción 2: Muestra la lista de instructores con sus respectivas posiciones.
        Utiliza 'enumerate' para obtener tanto el índice como el valor del elemento.
        """
        for i, e in enumerate(instructores):
            print("En la posición ", i, " se encuentra ", e)
    elif menu == 3:
        """
        Opción 3: Permite modificar el nombre de un instructor ya existente.
        Muestra la lista de instructores y solicita la posición del instructor a modificar.
        Luego, reemplaza el nombre del instructor en esa posición.
        """
        for i, e in enumerate(instructores):
            print("En la posición ", i, " se encuentra ", e)
        a = int(input("Ingresa la posición del instructor que deseas modificar\n"))
        instructores[a] = input("Ingrese el nombre del instructor\n")
    elif menu == 4:
        """
        Opción 4: Permite eliminar un instructor de la lista.
        Muestra la lista de instructores y solicita la posición del instructor a borrar.
        Luego, elimina el instructor de esa posición.
        """
        for i, e in enumerate(instructores):
            print("En la posición ", i, " se encuentra ", e)
        p = int(input("Escriba la posicion del instructor que desea borrar: \n")) 
        del instructores[p]
    elif menu == 5:
        """
        Opción 5: Permite buscar un instructor en la lista.
        Convierte todos los nombres de instructores a minúsculas para realizar la búsqueda de forma insensible a mayúsculas/minúsculas.
        Muestra la posición del instructor encontrado.
        """
        Instructores1 = []
        for i in instructores:
            Instructores1.append(i.lower())  # Convierte a minúsculas para comparación
        Elemento = input("Ingrese el nombre del instructor que desea buscar: \n")
        if Elemento.lower() in Instructores1:
            print("El instructor ingresado ", Elemento, " se encuentra en la posición ", Instructores1.index(Elemento.lower()))
        else:
            print("Instructor no encontrado.")
    elif menu == 6:
        """
        Opción 6: Ordena la lista de instructores de forma ascendente.
        La lista de instructores se organiza alfabéticamente y luego se muestra la lista ordenada.
        """
        instructores.sort()
        for i, e in enumerate(instructores):
            print("En la posición ", i, " se encuentra ", e)
    else:
        """
        Si el usuario ingresa una opción que no está en el menú, se muestra un mensaje de error.
        """
        print("Opción invalida")
    # Pregunta si desea seguir interactuando con la lista de instructores
    seguir = input("Escriba s o S para seguir en su lista \n")
