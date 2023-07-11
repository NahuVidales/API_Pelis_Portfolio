Rol a desarrollar

Empezaste a trabajar como Data Scientist en una start-up que provee servicios de agregación de plataformas de streaming. El mundo es bello y vas a crear tu primer modelo de ML que soluciona un problema de negocio: un sistema de recomendación que aún no ha sido puesto en marcha!

Vas a sus datos y te das cuenta que la madurez de los mismos es poca (ok, es nula 😭): Datos anidados, sin transformar, no hay procesos automatizados para la actualización de nuevas películas o series, entre otras cosas…. haciendo tu trabajo imposible 😩.

Debes empezar desde 0, haciendo un trabajo rápido de Data Engineer y tener un MVP (Minimum Viable Product) para el cierre del proyecto! Tu cabeza va a explotar 🤯, pero al menos sabes cual es, conceptualmente, el camino que debes de seguir ❗. Así que te espantas los miedos y te pones manos a la obra 💪


Introduccion 
Se nos pide hacer una API para consumir con los dataset asignados aplicando Transformacion y limpieza de datos en base a las consultas que necesitamos realizar y realizar el deploy de la misma en la plataforma que elijamos en este caso Render

Primeros Pasos
se empezo a trabajar los datos de los dataset entregados en el notebook ETL.ipynb eliminando filas nulas y duplicadas ademas de seleccionar columnas especificas ya que habia datos redundantes para las consultas que ibamos a realizar a nuestra API y generando columna en base a los datos que teniamos para poder realizar las consultas que necesitabamos

Desarrollo 
Para desarrollar las consultas adecuadamente y solucionar los problemas mas facilmente se desarrollaron en primer lugar las consultas en el notebook pruebaMain.ipynb para luego pasarlas a la API en el archivo main.py