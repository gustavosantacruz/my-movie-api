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
    }
]
@app.get('/', tags=["Home"])
def message():
    return HTMLResponse ('<h1> Hello world </h1>')

@app.get('/movies', tags=["Movies"])
def get_movies():
    return movies_list