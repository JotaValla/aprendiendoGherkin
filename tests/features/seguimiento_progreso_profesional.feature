# Created by jotacode at 27/5/2025
# language: es
Característica: : Seguimiento de autoevaluación de progreso formativo
  Como estudiante de la EPN
  quiero conocer mi progreso a lo largo de cada semestre, en relación a los objetivos de la carrera
  para determinar posibles falencias en mi proceso académico y tomar acciones correctivas

  # Estudiante - NUMUNICO, NOMBRE
  # Perfil -
  # Historial -
  # Carrera -


#    Y el umbral de aceptación minimo es de 70%

  Esquema del escenario: Seguimiento sin falencias
    Dado que el estudiante tiene registrado al menos un perfil en su historial
    Y la carrera de software tiene el siguiente <objetivo>:
    Cuando consulte el progreso de su último perfil
    Entonces se mostrará un porcentaje de progreso de cada objetivo
    Y se destacarán los que superen la media de progreso de cada objetivo de los demás estudiantes del mismo nivel
    Ejemplos:
      | objetivo                      |
      | Verificación, validación y aseguramiento de la calidad del Software|
      | Administración de proyectos de Software.|
      | Investigación aplicada en proyectos de conceptualización, desarrollo, innovación y transferencia de Software.|
      | Ingeniería de Software para el desarrollo de Sistemas de Información y Sistemas Inteligentes.|
      | Emprendimiento de empresas de investigación, innovación, desarrollo y comercialización de Software.|

#      | Verificación, validación y aseguramiento de la calidad del Software; Administración de proyectos de Software; Investigación aplicada en proyectos de conceptualización, desarrollo, innovación y transferencia de Software; Ingeniería de Software para el desarrollo de Sistemas de Información y Sistemas Inteligentes; Emprendimiento de empresas de investigación, innovación, desarrollo y comercialización de Software|
#    Escenario: Seguimiento con falencias
#      Dado que el estudiante tiene registrado al menos un historial de perfil
#      Y su progreso esta por debajo de mínimo
#      Cuando consulte el progreso del historial
#      Entonces mostrara un porcentaje de progreso por cada objetivo
#      Y se mostrará la media de progreso de estudiantes
#      Y se mostrará una serie de recomendaciones
