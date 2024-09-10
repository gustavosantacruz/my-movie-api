from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"

movies_list = [
    {
        "id": 1, 
        "title": "CONSTANTINE",
        "overview": "exorcismos",
        "year": 2005,
        "rating": 10.0
    },
    {
        "id": 2, 
        "title": "BUSCANDO A NEMO",
        "overview": "PEZ PERDIDO",
        "year": 2010,
        "rating": 10.0
    },
    {
        "id": 3, 
        "title": "AVATAR",
        "overview": "Ciencia ficción épica",
        "year": 2009,
        "rating": 10.0},
    {
        "id": 4, 
        "title": "TITANIC",
        "overview": "Romance y desastre",
        "year": 1997,
        "rating": 10.0},
    {
        "id": 5, 
        "title": "Shrek 2",
        "overview": "Comedia animada",
        "year": 2004,
        "rating": 10.0},
    {
        "id": 6, 
        "title": "Harry Potter y la piedra filosofal",
        "overview": "Fantasía mágica ",
        "year": 2001,
        "rating": 10.0},
    {
        "id": 7, 
        "title": "El Señor de los Anillos: El Retorno del Rey",
        "overview": "Fantasía épica",
        "year": 2003,
        "rating": 10.0},
    {
        "id": 8, 
        "title": "La Era de Hielo 2",
        "overview": "Animación y comedia",
        "year": 2002,
        "rating": 10.0},
    {
        "id": 9, 
        "title": "Piratas del Caribe: El Cofre de la Muerte",
        "overview": "Superhéroes y acción",
        "year": 2002,
        "rating": 10.0},
    {
        "id": 10, 
        "title": "Piratas del Caribe: El Cofre de la Muerte",
        "overview": "Aventura y fantasía",
        "year": 2007,
        "rating": 10.0},
        
]
@app.get('/', tags=["Home"])
def message():
    return HTMLResponse ('<h1> Hello world </h1>')

@app.get('/movies', tags=["Movies"])
def get_movies():
    return movies_list
@app.get('/movies/{id}' , tags=["Movies"])
def get_movie(id: int):
    for item in movies_list:
        if item["id"] == id:
            return item
    return []