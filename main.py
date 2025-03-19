# Inicializamos la lista de helados
helados = []
id_counter = 1  # Contador para generar IDs únicos

def crear_helado():
    global id_counter
    nombre = input("Ingrese el nombre del helado: ")
    descripcion = input("Ingrese la descripción del helado: ")
    precio = float(input("Ingrese el precio unitario del helado: "))
    
    helado = {
        'id': id_counter,
        'nombre': nombre,
        'descripcion': descripcion,
        'precio': precio
    }
    
    helados.append(helado)
    print(f"Helado '{nombre}' creado con éxito. ID: {id_counter}")
    id_counter += 1  # Incrementar el contador para el siguiente helado

def ver_helados():
    if not helados:
        print("No hay helados registrados.")
        return
    
    print("Lista de helados:")
    for helado in helados:
        print(f"ID: {helado['id']}, Nombre: {helado['nombre']}, Descripción: {helado['descripcion']}, Precio: {helado['precio']}")

def modificar_helado():
    id_helado = int(input("Ingrese el ID del helado que desea modificar: "))
    for helado in helados:
        if helado['id'] == id_helado:
            nombre = input("Ingrese el nuevo nombre del helado: ")
            descripcion = input("Ingrese la nueva descripción del helado: ")
            precio = float(input("Ingrese el nuevo precio unitario del helado: "))
            
            helado['nombre'] = nombre
            helado['descripcion'] = descripcion
            helado['precio'] = precio
            
            print(f"Helado con ID {id_helado} modificado con éxito.")
            return
    
    print(f"No se encontró un helado con ID {id_helado}.")

def eliminar_helado():
    id_helado = int(input("Ingrese el ID del helado que desea eliminar: "))
    for helado in helados:
        if helado['id'] == id_helado:
            helados.remove(helado)
            print(f"Helado con ID {id_helado} eliminado con éxito.")
            return
    
    print(f"No se encontró un helado con ID {id_helado}.")

def menu():
    while True:
        print("\n--- Gestión de Helados ---")
        print("1. Crear un helado")
        print("2. Ver la lista de helados")
        print("3. Modificar un helado")
        print("4. Eliminar un helado")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            crear_helado()
        elif opcion == '2':
            ver_helados()
        elif opcion == '3':
            modificar_helado()
        elif opcion == '4':
            eliminar_helado()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Ejecutar el menú
menu()
