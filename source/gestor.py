import json

from source.persona import Persona

class GestorPersonas:
    def __init__(self):
        self.personas = []

    def agregar_persona(self, persona):
        self.personas.append(persona)

    def listar_personas(self):
        return self.personas

    def guardar_personas(self):
        datos = []

        for persona in self.personas:
            datos.append(persona.to_dict())

        with open("data/personas.json", "w", encoding="UTF-8") as file:
            json.dump(datos, file, indent=4, ensure_ascii=False)