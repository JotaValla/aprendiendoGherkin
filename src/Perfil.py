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
        # if len(progreso_por_objetivo) != len(Perfil.objetivos_definidos):
        #     raise ValueError(
        #         f"La lista progreso_por_objetivo debe tener {len(Perfil.objetivos_definidos)} elementos, "
        #         f"pero tiene {len(progreso_por_objetivo)}."
        #     )
        self.progreso: dict[Objetivo, int] = dict(zip(Perfil.objetivos_definidos, progreso_por_objetivo))

