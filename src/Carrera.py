class Carrera:
    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.objetivos: list[str] = []

    def agregar_objetivo(self, objetivo: str):
        self.objetivos.append(objetivo)

    def get_objetivos(self):
        return self.objetivos