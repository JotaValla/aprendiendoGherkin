from src.Perfil import Objetivo


class Carrera:
    def __init__(self, nombre: str):
        self.__nombre: str = nombre
        self.__objetivos: list[str] = []
        self.__estudiantes: list = []  # Lista de estudiantes de la carrera

    def agregar_objetivo(self, objetivo: str):
        self.__objetivos.append(objetivo)

    def get_objetivos(self):
        return self.__objetivos

    def agregar_estudiante(self, estudiante):
        self.__estudiantes.append(estudiante)

    def obtener_estudiantes_por_nivel(self, nivel: int):
        estudiantes_mismo_nivel = []
        for estudiante in self.__estudiantes:
            ultimo_perfil = estudiante.obtener_ultimo_perfil()
            if ultimo_perfil and ultimo_perfil.semestre == nivel:
                estudiantes_mismo_nivel.append(estudiante)
        return estudiantes_mismo_nivel

    def calcular_media_por_objetivo(self, nivel: int):
        estudiantes_nivel = self.obtener_estudiantes_por_nivel(nivel)
        if not estudiantes_nivel:
            return {}
        # Inicializar suma por objetivo
        suma_por_objetivo = {objetivo: 0 for objetivo in Objetivo}
        total_estudiantes = len(estudiantes_nivel)
        # Sumar progreso de todos los estudiantes
        for estudiante in estudiantes_nivel:
            ultimo_perfil = estudiante.obtener_ultimo_perfil()
            for objetivo, progreso in ultimo_perfil.progreso.items():
                suma_por_objetivo[objetivo] += progreso

        # Calcular media
        media_por_objetivo = {
            objetivo: suma / total_estudiantes
            for objetivo, suma in suma_por_objetivo.items()
        }

        return media_por_objetivo