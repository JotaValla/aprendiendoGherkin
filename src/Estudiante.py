from src.Perfil import Perfil, Objetivo  # Asumiendo que Perfil está en src/Perfil.py

class Estudiante:
    def __init__(self, nombre:str):
        self.nombre: str = nombre
        self.codigo_unico: str = ""
        self.historial_perfiles: list[Perfil] = []

    def agregar_perfil(self, perfil: Perfil): # Es bueno añadir el type hint
        self.historial_perfiles.append(perfil)

    def get_historial_perfiles(self): # Nombre corregido para ser consistente
        return self.historial_perfiles

    def obtener_ultimo_perfil(self) -> Perfil | None: # Método útil
        if self.historial_perfiles:
            return self.historial_perfiles[-1]
        return None