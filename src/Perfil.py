from enum import Enum

class Objetivo ( Enum ):
    VERIFICACION = "Verificación, validación y aseguramiento de la calidad del Software"
    ADMINISTRACION = "Administración de proyectos de Software"
    INVESTIGACION = "Investigación aplicada en proyectos de conceptualización, desarrollo, innovación y transferencia de Software"
    INGENIERIA = "Ingeniería de Software para el desarrollo de Sistemas de Información y Sistemas Inteligentes"
    EMPRENDIMIENTO = "Emprendimiento de empresas de investigación, innovación, desarrollo y comercialización de Software"

class Perfil:
    # Definido como atributo de CLASE
    objetivos_definidos: list[Objetivo] = [
        Objetivo.VERIFICACION,
        Objetivo.ADMINISTRACION,
        Objetivo.INVESTIGACION,
        Objetivo.INGENIERIA,
        Objetivo.EMPRENDIMIENTO
    ]

    def __init__(self, semestre: int, progreso_por_objetivo: list):
        self.semestre: int = semestre
        self.progreso: dict[Objetivo, int] = dict(zip(Perfil.objetivos_definidos, progreso_por_objetivo))

    def mostrar_progreso(self) -> str:
        """Muestra el progreso ya definido para cada objetivo"""
        return f"Progreso del semestre {self.semestre}:\n" + \
               "\n".join(f"{objetivo.value}: {valor_progreso}%" for objetivo, valor_progreso in self.progreso.items())

    def destacar_objetivos_sobre_media(self, media_por_objetivo: dict):
        """Destaca los objetivos que superan la media y retorna la lista y el reporte como string"""
        objetivos_destacados = []
        reporte = [f"Comparación con la media del semestre {self.semestre}:"]

        for objetivo, progreso_actual in self.progreso.items():
            media_objetivo = media_por_objetivo.get(objetivo, 0)
            if progreso_actual > media_objetivo:
                reporte.append(f"🌟 {objetivo.value}: {progreso_actual}% (Media: {media_objetivo:.2f}%) - ¡DESTACADO!")
                objetivos_destacados.append(objetivo)
            else:
                reporte.append(f"   {objetivo.value}: {progreso_actual}% (Media: {media_objetivo:.2f}%)")

        return objetivos_destacados, "\n".join(reporte)
