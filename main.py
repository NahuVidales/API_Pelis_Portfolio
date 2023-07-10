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