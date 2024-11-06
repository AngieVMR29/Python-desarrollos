# Diccionario para almacenar la información de los instructores
instructores2557861 = {}
# Variable para controlar si el ciclo continúa o no
seguir = "s"
# Función para modificar o agregar información de un instructor
def modificar():
    # Pide al usuario el nombre del instructor que quiere modificar o agregar
    inst = input("Ingrese el nombre del instructor: \n")
    # Verifica si el instructor ya está registrado
    if inst in instructores2557861:
        print("El instructor ya se encuentra registrado en la ficha.")
        # Ofrece opciones para modificar el nombre, materia o teléfono del instructor
        opcion1 = int(input("Digite 1 si desea modificar nombre del instructor. \nDigite 2 si desea modificar la materia del instructor. \nDigite 3 si desea modificar el teléfono del instructor. \n"))
        if opcion1 == 1:
            # Modifica el nombre del instructor
            nombre = input("Ingrese el nuevo nombre del instructor. \n")
            instructores2557861['Nombre'] = nombre
        elif opcion1 == 2:
            # Modifica la materia del instructor
            materia = input("Ingrese la nueva materia del instructor. \n")
            instructores2557861[inst]['Materia'] = materia
        elif opcion1 == 3:
            # Modifica el teléfono del instructor
            telefono = int(input("Ingrese el nuevo teléfono del instructor. \n"))
            instructores2557861[inst]['Teléfono'] = telefono
        else:
            print("¡¡ERROR!! Opción no válida.")
    else:
        # Si el instructor no está registrado, se agrega uno nuevo
        print("El instructor no se encuentra en el sistema.")
        instructores2557861[inst] = {}
        materia = input("Ingrese la nueva materia del instructor. \n")
        instructores2557861[inst]['Materia'] = materia
        telefono = int(input("Ingrese el nuevo teléfono del instructor. \n"))
        instructores2557861[inst]['Telefono'] = telefono
        print(instructores2557861)
    return instructores2557861
# Función para buscar un instructor por nombre
def buscar():
    # Pide el nombre del instructor a buscar
    inst = input("Ingrese el nombre del instructor que desea buscar: ")
    inst = inst.lower()  # Convierte a minúsculas para hacer la búsqueda insensible al caso
    print("Se encontraron los siguientes resultados:")
    
    # Busca e imprime los datos de los instructores que coinciden con el nombre
    for inst, datos in instructores2557861.items():
        if inst.startswith(inst):  # Busca si el nombre empieza con lo que el usuario ingresó
            print(inst)
            print(f"Materia: {instructores2557861[inst]['Materia']} \nNúmero de teléfono: {instructores2557861[inst]['Telefono']}")
        else:
            print("No se encontró ningún instructor con ese nombre.")
    return instructores2557861
# Función para borrar un instructor
def borrar():
    # Pide el nombre del instructor a borrar
    nombre = input("Ingrese el nombre del instructor que desea borrar: ")
    nombre = nombre.lower()  # Convierte a minúsculas para comparar sin importar el caso
    if nombre in instructores2557861:
        # Si el instructor se encuentra en el diccionario, se muestran los datos
        print("Se encontraron los siguientes resultados: ")
        print(instructores2557861)
        # Pide al usuario confirmar la eliminación
        borrar = int(input("Digite 1 para borrar el instructor. \nDigite 2 para cancelar la acción. \n"))
        if borrar == 1:
            # Elimina el instructor
            del instructores2557861[nombre]
            print(f"El instructor {nombre} ha sido eliminado.")
            print(instructores2557861)
        elif borrar == 2:
            print("Usted ha cancelado la acción.")
            print(instructores2557861)
        else:
            print("Opción inválida.")
    else:
        print("El instructor no existe en el sistema.")
# Función para listar todos los instructores registrados
def listar():
    # Muestra todos los instructores registrados con sus materias y teléfonos
    for x in instructores2557861:
        print(f"Los instructores registrados son {x} con la materia {instructores2557861[x]['Materia']} y un número de teléfono {instructores2557861[x]['Telefono']}")
# Bucle principal para interactuar con el usuario
while seguir == "s" or seguir == "S":
    # Muestra un menú con las opciones disponibles
    opcion = int(input("Elija una opción: \n1. Añadir/Modificar.\n2. Buscar.\n3. Borrar.\n4. Listar.\n5. Salir\n"))   
    # Ejecuta la acción correspondiente según la opción seleccionada
    if opcion == 1:
        modificar()  # Llamada a la función modificar
    elif opcion == 2:
        buscar()  # Llamada a la función buscar
    elif opcion == 3:
        borrar()  # Llamada a la función borrar
    elif opcion == 4:
        listar()  # Llamada a la función listar
    elif opcion == 5:
        # Sale del ciclo
        seguir = input("Escriba s o S para seguir en su lista, cualquier otra tecla para salir \n")
    else:
        print("¡¡ERROR!! Opción no válida.")
