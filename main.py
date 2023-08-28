
from fastapi import FastAPI
import pandas as pd

app = FastAPI()

movies_clean = pd.read_csv('movies_dataset_clean.csv')
movies_clean['production_countries'] = movies_clean['production_countries'].apply(eval)
movies_clean['crew'] = movies_clean['crew'].apply(eval)
movies_clean['spoken_languages'] = movies_clean['spoken_languages'].apply(eval)
movies_clean['belongs_to_collection'] = movies_clean['belongs_to_collection'].apply(eval)
movies_clean['revenue'] = movies_clean['revenue'].astype(int)
movies_clean['production_companies'] = movies_clean['production_companies'].apply(eval)

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
def get_director(nombre_director: str):
    nombre_director = nombre_director.lower()
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


#def peliculas_idioma( Idioma: str ): Se ingresa un idioma (como están escritos en el dataset, no hay que traducirlos!). Debe devolver la cantidad de películas producidas en ese idioma.
#                   Ejemplo de retorno: X cantidad de películas fueron estrenadas en idioma

@app.get('/peliculas_idioma/{Idioma}')
def peliculas_idioma(Idioma: str):
    Idioma = Idioma.lower()
    cantidad_peliculas = 0
    for i in movies_clean['spoken_languages']:
        for idioma in i:
            if idioma == Idioma:
                cantidad_peliculas += 1

    return f"{cantidad_peliculas} cantidad de películas fueron estrenadas en {Idioma}"


#def peliculas_pais( Pais: str ): Se ingresa un país (como están escritos en el dataset, no hay que traducirlos!), retornando la cantidad de peliculas producidas en el mismo.
#                    Ejemplo de retorno: Se produjeron X películas en el país X
@app.get('/peliculas_pais/{Pais}')
def peliculas_pais(Pais: str):
    Pais = Pais.lower()
    cantidad_peliculas = 0
    for i in movies_clean['production_countries']:
        for pais in i:
            if pais == Pais:
                cantidad_peliculas += 1

    return f"Se produjeron {cantidad_peliculas} películas en el país {Pais}"




#def franquicia( Franquicia: str ): Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio
#                    Ejemplo de retorno: La franquicia X posee X peliculas, una ganancia total de x y una ganancia promedio de xx
@app.get('/franquicia/{Franquicia}')
def franquicia(Franquicia: str):
<<<<<<< HEAD
    Franquicia = Franquicia.lower()
    peliculaNro = -1
=======
    peliculaNro = 0
>>>>>>> parent of 04e5caf (Update main.py)
    cantidad_peliculas = 0
    ganancia_total = 0
    ganancia_promedio = 0
    for i in movies_clean['belongs_to_collection']:
        peliculaNro += 1
        for franquicia in i:
            if franquicia == Franquicia:
                cantidad_peliculas += 1
                ganancia_total += movies_clean['revenue'][peliculaNro]
    ganancia_promedio = ganancia_total / cantidad_peliculas
    return f"La franquicia {Franquicia} posee {cantidad_peliculas} peliculas, una ganancia total de {ganancia_total} y una ganancia promedio de {ganancia_promedio}"


#def productoras_exitosas( Productora: str ): Se ingresa la productora, entregandote el revunue total y la cantidad de peliculas que realizo.
#                    Ejemplo de retorno: La productora X ha tenido un revenue de x

@app.get('/productoras_exitosas/{Productora}')
def productoras_exitosas(Productora: str):
<<<<<<< HEAD
    Productora = Productora.lower()
    peliculaNro = -1
=======
    peliculaNro = 0
>>>>>>> parent of 04e5caf (Update main.py)
    cantidad_peliculas = 0
    ganancia_total = 0
    for i in movies_clean['production_companies']:
        peliculaNro += 1
        for productora in i:
            if productora == Productora:
                cantidad_peliculas += 1
                ganancia_total += movies_clean['revenue'][peliculaNro]
    return f"La productora {Productora} ha tenido un revenue de {ganancia_total} y ha realizado {cantidad_peliculas} peliculas"
