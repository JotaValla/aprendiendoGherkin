from behave import *

from src.Estudiante import  Estudiante
from src.Perfil import Perfil
from src.Carrera import Carrera

use_step_matcher("re")

@step("que el estudiante tiene registrado al menos un perfil en su historial")
def step_impl(context):

    row = context.table[0]
    nombre_estudiante = row["nombre"]
    semestre = int(row["semestre"])
    progreso_keys = sorted([h for h in row.headings if h.lower().startswith("progreso objetivo")])
    progreso_objetivos = [float(row[key]) for key in progreso_keys]
    context.estudiante = Estudiante(nombre=nombre_estudiante)
    context.perfil = Perfil(
        semestre=semestre,
        progreso_por_objetivo=progreso_objetivos
    )
    context.estudiante.agregar_perfil(context.perfil)

    assert context.estudiante.obtener_ultimo_perfil() is context.perfil, \
        "El perfil recién creado no es el último perfil registrado para el estudiante."

    assert len(context.estudiante.get_historial_perfiles()) >= 1, \
        "El estudiante no tiene perfiles registrados en su historial"

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
    objetivos_destacados, reporte = ultimo_perfil.destacar_objetivos_sobre_media(media_por_objetivo)

    # Guardar en contexto para posibles validaciones posteriores
    context.objetivos_destacados = objetivos_destacados
    context.media_por_objetivo = media_por_objetivo
    context.reporte_destacados = reporte

    # Validación
    assert isinstance(objetivos_destacados, list), "La función de destacar objetivos no retornó una lista"