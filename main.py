from source.persona import Persona
from source.gestor import GestorPersonas

gestor = GestorPersonas()
gestor.cargar_personas()

while True:
    print("\n===========================")
    print("    GESTOR DE PERSONAS")
    print("\n===========================")
    print("1.- Agrega persona")
    print("2.- Mostrar personas")
    print("3.- Salir")

    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        while True:
            nombre = input("Nombre: ").strip()
            if nombre:
                break

            print("El nombre no puede estar vacio")
        while True:
            try:
                edad = int(input("Edad: "))
                if 0 <= edad <= 120:
                    break
                print("La edad debe estar entre 0 y 120.")

            except ValueError:
                print("La edad debe ser un numero")

        id_persona = gestor.siguiente_id()
            
        persona = Persona(id_persona, nombre, edad)
        gestor.agregar_persona(persona)
        gestor.guardar_personas()

        print("Persona agregada correctamente")

    elif opcion =="2":
        personas = gestor.listar_personas()

        for persona in personas:
            print(persona)

    elif opcion == "3":
        print ("Vuelva pronto.")
    else:
        print("Opcion no valida.")