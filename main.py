import uvicorn
from fastapi import FastAPI
import pandas as pd

app = FastAPI()

movies_clean = pd.read_csv('movies_dataset_clean.csv')

@app.get('/')
async def root():
    return {'message': 'Hello World'}

#def peliculas_idioma( Idioma: str ): Se ingresa un idioma (como están escritos en el dataset, no hay que traducirlos!). Debe devolver la cantidad de películas producidas en ese idioma.
#                   Ejemplo de retorno: X cantidad de películas fueron estrenadas en idioma
@app.get('/peliculas_duracion/{Pelicula}')
def peliculas_duracion(Pelicula: str):
    duracion = movies_clean[movies_clean['title'] == Pelicula]['runtime'].values[0]
    anio = movies_clean[movies_clean['title'] == Pelicula]['release_year'].values[0]
    return f"{Pelicula}. Duración: {duracion} minutos. Año: {anio}"

#def get_director( nombre_director ): Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma, en formato lista.

@app.get('/get_director/{nombre_director}')
def get_director(nombre_director):
    movies_clean['crew'] = movies_clean['crew'].apply(eval)
    peliculas_producidas = 0
    titulo = []
    fecha_lanzamiento = []
    retorno = []
    costo = []
    ganancia = []
    retorno_total = 0

    for i, lista_directores in enumerate(movies_clean['crew']):
        for director in lista_directores:
            if director == nombre_director:
                peliculas_producidas += 1
                retorno_total += movies_clean['return'].values[i]
                titulo.append(movies_clean['title'].values[i])
                fecha_lanzamiento.append(movies_clean['release_date'].values[i])
                retorno.append(movies_clean['return'].values[i])
                costo.append(movies_clean['budget'].values[i])
                ganancia.append(movies_clean['revenue'].values[i])
    lista_peliculas = {'titulo': titulo, 'fecha_lanzamiento': fecha_lanzamiento, 'retorno': retorno, 'costo': costo, 'ganancia': ganancia}
    print(f"El director {nombre_director} produjo {peliculas_producidas} peliculas, con un retorno total de {retorno_total}")
    df_movies = pd.DataFrame(lista_peliculas)

    return df_movies