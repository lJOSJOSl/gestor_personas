class Persona:
    def __init__(self, id, nombre, edad):
        self.id = id
        self.nombre = nombre
        self.edad = edad

    def to_dict(self):
        return {
            "id" : self.id,
            "nombre" : self.nombre,
            "edad" : self.edad
        }

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.edad} años"