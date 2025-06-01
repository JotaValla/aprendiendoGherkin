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
        progreso_por_objetivo = [1.5, 2.0, 3.75, 0.99, 4.0]
    )
    context.estudiante.agregar_perfil(context.perfil)
    assert len(context.estudiante.get_historial_perfiles()) > 0, "El estudiante no tiene perfiles registrados en su historial"

@step("la carrera de software tiene el siguiente (?P<objetivo>.+):")
def step_impl(context, objetivo):
    context.carrera = Carrera(nombre="Ingeniería de Software")
    context.carrera.agregar_objetivo(objetivo)
    assert objetivo in context.carrera.get_objetivos(), f"El objetivo '{objetivo}' no se ha agregado correctamente a la carrera de software"

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
    # Guardamos el progreso en el contexto para validaciones posteriores
    context.progreso_mostrado = ultimo_perfil.progreso
    # Verificación simple
    assert len(context.progreso_mostrado) > 0, "No se mostró progreso alguno"





# @step("se destacarán los que superen la media de progreso de cada objetivo de los demás estudiantes del mismo nivel")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(
#         u'STEP: Y se destacarán los que superen la media de progreso de cada objetivo de los demás estudiantes del mismo nivel')
