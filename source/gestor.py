from source.persona import Persona

class GestorPersonas:
    def __init__(self):
        self.personas = []

    def agregar_persona(self, persona):
        self.personas.append(persona)

    def listar_personas(self):
        return self.personas