from behave import *

from src.Estudiante import  Estudiante
from src.Perfil import Perfil
from src.Carrera import Carrera

use_step_matcher("re")

@step("que el estudiante tiene registrado al menos un perfil en su historial")
def step_impl(context):
    context.estudiante = Estudiante(nombre = "Pepito")
    context.perfil = Perfil(
        semestre = 1,
        progreso_por_objetivo = [0.5, 0, 0, 0, 0.1]
    )
    context.estudiante.agregar_perfil(context.perfil)
    assert len(context.estudiante.get_historial_perfiles()) > 0, "El estudiante no tiene perfiles registrados en su historial"

@step("la carrera de software tiene los siguientes objetivos")
def step_impl(context):
    context.carrera = Carrera(nombre="Ingeniería de Software")

    for row in context.table:
        objetivo = row['objetivo']
        context.carrera.agregar_objetivo(objetivo)
        assert objetivo in context.carrera.get_objetivos(), \
            f"El objetivo '{objetivo}' no se ha agregado correctamente a la carrera de software"


@step("consulte el progreso de su último perfil")
def step_impl(context):
     estudiante_actual = context.estudiante
     ultimo_perfil = estudiante_actual.obtener_ultimo_perfil()
     assert ultimo_perfil is not None, "No se encontró el último perfil del estudiante."
     context.progreso_del_ultimo_perfil = ultimo_perfil.progreso

@step("se mostrará un porcentaje de progreso de cada objetivo")
def step_impl(context):
    ultimo_perfil = context.estudiante.obtener_ultimo_perfil()
    ultimo_perfil.mostrar_progreso()
    context.progreso_mostrado = ultimo_perfil.progreso
    assert len(context.progreso_mostrado) > 0, "No se mostró progreso alguno"

@step("se destacarán los que superen la media de progreso de cada objetivo de los demás estudiantes del mismo nivel")
def step_impl(context):
    for row in context.table:
        nombre = row['nombre']
        semestre = int(row['semestre'])

        progreso = [
            float(row[col])
            for col in row.headings
            if col.lower().startswith("progreso objetivo")
        ]

        estudiante = Estudiante(nombre=nombre)
        perfil = Perfil(semestre=semestre, progreso_por_objetivo=progreso)
        estudiante.agregar_perfil(perfil)
        context.carrera.agregar_estudiante(estudiante)

    # Agregar el estudiante principal a la carrera
    context.carrera.agregar_estudiante(context.estudiante)

    # Obtener el último perfil del estudiante principal
    ultimo_perfil = context.estudiante.obtener_ultimo_perfil()

    # Calcular la media por objetivo para el nivel del estudiante
    media_por_objetivo = context.carrera.calcular_media_por_objetivo(ultimo_perfil.semestre)

    # Destacar objetivos que superen la media
    objetivos_destacados = ultimo_perfil.destacar_objetivos_sobre_media(media_por_objetivo)

    # Guardar en contexto para posibles validaciones posteriores
    context.objetivos_destacados = objetivos_destacados
    context.media_por_objetivo = media_por_objetivo

    # Validación
    assert isinstance(objetivos_destacados, list), "La función de destacar objetivos no retornó una lista"
