from fastapi import FastAPI
from typing import Union

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hola": " todos"}

@app.get('/messi')
async def get_messi():
    return {'yyyy'}

@app.get("/peli")
async def get_peli():
    nombre = 'titanic'
    return {nombre}

@app.get("/get_max_duration")
def get_max_duration(release_year=None, platform=None, duration_type=None):
    df = streaming
    # Filtro el DataFrame según los filtros opcionales
    filtro_striming = df.copy()
    if release_year:
        filtro_striming = filtro_striming[filtro_striming['release_year'] == release_year]
    if platform:
        filtro_striming = filtro_striming[filtro_striming['plataforma_numerico'] == platform] 
    if duration_type:
        filtro_striming = filtro_striming[filtro_striming['duration_numerico'] == duration_type]
        
    
    # Busco la película con la mayor duración
    max_duration_movie = filtro_striming.loc[filtro_striming['duration_int'].sort_values()]
    
    # devuelve el nombre de la pelicula
    return {max_duration_movie['title']}

@app.get("/get_score_count")
async def get_score_count(platform, scored, year):
    # Filtro por plataforma y año
    df_filtered = streaming[(streaming['date_added']) & (streaming['release_year'] == year)]
    
    # Contar películas con puntaje mayor a XX
    count = (df_filtered['rating'] >= scored).sum()
    
    return {count}

@app.get('/get_score_count')
async def get_score_count(platform, scored, year):
    # Filtro el DataFrame para el año y la puntuación deseados
    filtered_streaming = streaming[(streaming['release_year'] == year) & (streaming['rating'] >= scored)]
    
    # de la columna plataforma contamos las pelis
    platform_counts = filtered_streaming[filtered_streaming['plataforma']].count()
    
    # Filtro los resultados por la plataforma deseada
    platform_count = platform_counts.loc[platform]
    
    # Devuelve el número de películas de las plataformas
    return {platform_count}
