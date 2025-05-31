class Carrera:
    def __init__(self, nombre):
        self.nombre = nombre
        self.objetivos = []

    def agregar_objetivo(self, objetivo):
        self.objetivos.append(objetivo)

    def get_objetivos(self):
        return self.objetivos