import json

from source.persona import Persona

class GestorPersonas:
    def __init__(self):
        self.personas = []

    def agregar_persona(self, persona):
        self.personas.append(persona)

    def listar_personas(self):
        return self.personas

    def siguiente_id(self):
        if not self.personas:
            return 1

        return self.personas[-1].id + 1
    
    def guardar_personas(self):
        datos = []

        for persona in self.personas:
            datos.append(persona.to_dict())

        with open("data/personas.json", "w", encoding="UTF-8") as file:
            json.dump(datos, file, indent=4, ensure_ascii=False)

    def cargar_personas(self):
        try:
            with open("data/personas.json", "r", encoding="UTF-8") as file:
                datos = json.load(file)

            self.personas = []

            for dato in datos:
                persona = Persona(dato["id"], dato["nombre"], dato["edad"])
                self.personas.append(persona)
        except FileNotFoundError:
            print("No se encontro el archivo personas.")
        except json.JSONDecodeError:
            print("El archivo persona.json no contiene un json valido")
        except (KeyError, TypeError):
            print("El archivo personas.json contiene datos incorrectos")
        for dato in datos:
            persona = Persona(dato["id"], dato["nombre"], dato["edad"])
            self.personas.append(persona)