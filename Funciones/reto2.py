# Diccionario para almacenar los instructores y su información
instructores2557861 = {}
# Variable para controlar si el usuario desea continuar
seguir = "s"
# Bucle principal del programa que se ejecuta mientras el usuario quiera continuar
while seguir.lower() == "s":
    # Menú de opciones para el usuario
    opcion = int(input("Elija una opción: \n"
                       "1. Añadir/Modificar.\n"
                       "2. Buscar.\n"
                       "3. Borrar.\n"
                       "4. Listar.\n"
                       "5. Salir\n"))
    # Opción 1: Añadir o modificar un instructor
    if opcion == 1:
        inst = input("Ingrese el nombre del instructor: \n")
        if inst in instructores2557861:
            print("El instructor ya se encuentra registrado en la ficha.")
            opcion1 = int(input("Digite 1 si desea modificar el nombre del instructor. \n"
                                "Digite 2 si desea modificar la materia del instructor de la ficha. \n"
                                "Digite 3 si desea modificar el teléfono del instructor. \n"))
            if opcion1 == 1:
                # Modificar el nombre del instructor
                nombre = input("Ingrese el nuevo nombre del instructor. \n")
                instructores2557861[inst]['Nombre'] = nombre
            elif opcion1 == 2:
                # Modificar la materia del instructor
                materia = input("Ingrese la nueva materia del instructor. \n")
                instructores2557861[inst]['Materia'] = materia
            elif opcion1 == 3:
                # Modificar el teléfono del instructor
                telefono = input("Ingrese el nuevo teléfono del instructor. \n")
                instructores2557861[inst]['Telefono'] = telefono
            else:
                print("¡¡ERROR!! Opción no válida.")
        else:
            print("El instructor no se encuentra en el sistema.")
            # Si el instructor no está registrado, agregarlo
            instructores2557861[inst] = {}
            materia = input("Ingrese la nueva materia del instructor. \n")
            instructores2557861[inst]['Materia'] = materia
            telefono = input("Ingrese el nuevo teléfono del instructor. \n")
            instructores2557861[inst]['Telefono'] = telefono
            print("Instructor añadido: ", instructores2557861)
    # Opción 2: Buscar un instructor
    elif opcion == 2:
        inst = input("Ingrese el nombre del instructor que desea buscar: ")
        inst = inst.lower()
        encontrado = False
        # Buscar el instructor en el diccionario
        print("Se encontraron los siguientes resultados:")
        for nombre, datos in instructores2557861.items():
            if nombre.lower().startswith(inst):  # Comparación insensible a mayúsculas/minúsculas
                print(f"{nombre}: Materia: {datos['Materia']}, Teléfono: {datos['Telefono']}")
                encontrado = True
        if not encontrado:
            print("No se encontró ningún instructor con ese nombre.")
    # Opción 3: Borrar un instructor
    elif opcion == 3:
        nombre = input("Ingrese el nombre del instructor que desea borrar: ")
        nombre = nombre.lower()
        if nombre in instructores2557861:
            print(f"Se encontraron los siguientes resultados: \n{instructores2557861}")
            borrar = int(input("Digite 1 para borrar el instructor. \nDigite 2 para cancelar la acción. \n"))
            if borrar == 1:
                del instructores2557861[nombre]
                print(f"El instructor {nombre} ha sido eliminado.")
            elif borrar == 2:
                print("Usted ha cancelado la acción.")
            else:
                print("Opción no válida.")
        else:
            print("El instructor no se encuentra en el sistema.")
    # Opción 4: Listar todos los instructores
    elif opcion == 4:
        if instructores2557861:
            for nombre, datos in instructores2557861.items():
                print(f"Nombre: {nombre}, Materia: {datos['Materia']}, Teléfono: {datos['Telefono']}")
        else:
            print("No hay instructores registrados.")
    # Opción 5: Salir del programa
    elif opcion == 5:
        seguir = input("¿Desea salir? Escriba 's' para continuar o cualquier otra tecla para salir: ")
    else:
        print("¡¡ERROR!! Opción no válida.")
