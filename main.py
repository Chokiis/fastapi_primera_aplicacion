from fastapi import Depends, FastAPI, Body, Path, Query, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer

app = FastAPI()
app.title = "VINOC"
app.version = '0.0.1'

class User(BaseModel):
    email: str
    password: str

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="Credenciales son inválidas")

## Sin utilizar la clase "Config".
# class Movie(BaseModel):
#     id: Optional[int] = None
#     title: str = Field(default='Mi película', min_length=5, max_length=15)
#     overview: str = Field(default='Descripción de la película', min_length=15, max_length=50)
#     year: int = Field(default=2022, le=2022)
#     rating: float
#     category: str

## Utilizando la clase "Config".
class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2022)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=5, max_length=15)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "title": "Mi película",
                    "overview": "Descripción de la película",
                    "year": 2022,
                    "rating": 9.9,
                    "category": "Acción",
                }
            ]
        }
    }
##################

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planteta llamado Pandora viven los Na'vi",
        'year': '2009',
        'rating': 7.8,
        'category': 'Suspenso'
    },
    {
        'id': 2,
        'title': 'Avatar 2',
        'overview': "En un exuberante planteta llamado Pandora viven los Na'vi",
        'year': 2022,
        'rating': 7.8,
        'category': 'Acción'
    },
    {
        'id': 3,
        'title': 'Avatar 3',
        'overview': "En un exuberante planteta llamado Pandora viven los Na'vi",
        'year': 2022,
        'rating': 7.8,
        'category': 'Suspenso'
    },
]


@app.get('/', tags=['Home'])
def message():
    return HTMLResponse('<h1>Hello World</h1>')
    # return {'Hello' : 'World'} 

@app.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.model_dump())
        return JSONResponse(status_code=200, content=token)

@app.get('/movies', tags = ['Movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies()-> List[Movie]:
    return JSONResponse(status_code=200, content=movies)

@app.get('/movies/{id}', tags=['Movies'], response_model=Movie)
def get_movie(id: int = Path(ge= 1, le=2000)) -> Movie:
    for item in movies:
        if item['id'] == id:
            return JSONResponse(content=item)
    return JSONResponse(status_code=404, content=[])

# @app.get('/movies/', tags=['Movies'])
# def get_movies_by_category(category: str, year: int):
    # return category

@app.get('/movies/', tags=['Movies'], response_model=List[Movie])
def get_movie_by_category_filter(category: str = Query(min_length= 5, max_length= 15)) -> List[Movie]:
    category_list = []
    for item in movies:
        if item['category'] == category:
            category_list.append(item)
        if len(category_list) == 0:
            return {
                'error_message': 'List not found'
            }
    return JSONResponse(content=[category_list])

## POST SIN PYDANTIC
# @app.post('/movies/', tags=['Movies'])
# def create_movie(id: int, title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
#     movies.append({
#         'id': id,
#         'title': title,
#         'overview': overview,
#         'year': year,
#         'rating': rating,
#         'category': category
#     })
#     return movies

## POST CON PYDANTIC
@app.post('/movies/', tags=['Movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie)-> dict:
    movies.append(movie)
    return JSONResponse(status_code=201, content={"Message": "Se ha registrado la película"})

## PUT SIN PYDANTIC
# @app.put('/movies/{id}', tags = ['Movies'])
# def update_movie(id: int, title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
#     for item in movies:
#         if item['id'] == id:
#             item['title'] = title
#             item['overview'] = overview
#             item['year'] = year
#             item['rating'] = rating
#             item['category'] = category
#             return movies

## PUT CON PYDANTIC
@app.put('/movies/{id}', tags=['Movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie)-> dict: 
    for item in movies:
        if item['id'] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
            return JSONResponse(status_code=200, content={"Message": "Se ha modificado la película"})

@app.delete('/movies/{id}', tags=['Movies'], response_model=dict, status_code=200)
def delete_movie(id: int)-> dict:
    for item in movies:
        if item['id'] == id:
            movies.remove(item)
            return JSONResponse(status_code=200, content={"Message": "Se ha eliminado la película"})