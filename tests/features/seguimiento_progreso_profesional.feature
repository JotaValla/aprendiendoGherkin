# Created by jotacode at 27/5/2025
# language: es
Característica: : Seguimiento de autoevaluación de progreso formativo
  # Como estudiante de la carrera de Software de la EPN
  Como estudiante de la EPN
  quiero conocer mi progreso a lo largo de cada semestre, en relación a los objetivos de la carrera
  para determinar posibles falencias en mi proceso académico y tomar acciones correctivas

  # Estudiante - NUMUNICO, NOMBRE
  # Perfil -
  # Historial -
  # Carrera -


#    Y el umbral de aceptación minimo es de 70%

    Escenario: Seguimiento sin falencias
    Dado que el estudiante tiene registrado al menos un perfil en su historial
    Y la carrera de software tiene los siguientes objetivos:
      | objetivo|
      | Verificación, validación y aseguramiento de la calidad del Software|
      | Administración de proyectos de Software.|
      | Investigación aplicada en proyectos de conceptualización, desarrollo, innovación y transferencia de Software.|
      | Ingeniería de Software para el desarrollo de Sistemas de Información y Sistemas Inteligentes.|
      | Emprendimiento de empresas de investigación, innovación, desarrollo y comercialización de Software.|
    # la carrera podria ser un ejemplo
    Cuando consulte el progreso de su último perfil
    Entonces se mostrará un porcentaje de progreso de cada objetivo
    Y se destacarán los que superen la media de progreso de cada objetivo de los demás estudiantes del mismo nivel:
      | nombre  | semestre | progreso materia 1 | progreso materia 2 | progreso materia 3 | progreso materia 4 | progreso materia 5 |
      | Ana     | 1        | 2.0                | 1.8                | 3.2                | 1.5                | 3.5                |
      | Carlos  | 1        | 1.8                | 2.2                | 3.0                | 2.0                | 3.8                |
      | Maria   | 1        | 2.2                | 1.9                | 3.5                | 1.8                | 4.2                |


#      | Verificación, validación y aseguramiento de la calidad del Software; Administración de proyectos de Software; Investigación aplicada en proyectos de conceptualización, desarrollo, innovación y transferencia de Software; Ingeniería de Software para el desarrollo de Sistemas de Información y Sistemas Inteligentes; Emprendimiento de empresas de investigación, innovación, desarrollo y comercialización de Software|

#    Escenario: Seguimiento con falencias
#      Dado que el estudiante tiene registrado al menos un historial de perfil
#      Y su progreso esta por debajo de mínimo
#      Cuando consulte el progreso del historial
#      Entonces mostrara un porcentaje de progreso por cada objetivo
#      Y se mostrará la media de progreso de estudiantes
#      Y se mostrará una serie de recomendaciones
