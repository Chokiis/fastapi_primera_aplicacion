# Curso de Introducción a FastAPI

## 1.- FastAPI
Es un framework de alto rendimiento para la creación de API mediante Python, recopilando lo mejor del ecosistema de Python 

### Características
- Rápido
- Menos errores
- Fácil e intuitivo
- Robusto
- Basado en estándares

### Marco utilizado por FastAPI
- Starlette: Framework asíncrono para la construcción de servicios y es uno de los más rapidos de Python
- Pydantic: Encargado de las validaciones de datos en Python.
- Uvicorn: Encargado de ejecturar las aplicaciones con FastAPI.
------------
## 2.- Creación de un entorno virtual e instalación de FastAPI y Uvicorn
* Levantamiento de entorno con Venv.
	```shell
	py -m venv venv
	```
* Activación del entorno virtual con Windows.
    ```shell
    venv/Scripts/activate
    ```
* Activación del entorno virtual con Linux.
    ```shell
    source venv/bin/activate
    ```
* Instalación de FastAPI.
    ```shell
    pip install fastapi
    ```
* Instalación de Uvicorn.
    ```shell
    pip install uvicorn
    ```
* Creación de primera app con FastAPI.
    ```python
    from fastapi import FastAPI

    app = FastAPI()

    @app.get('/')
    def message():
        return "Hello World!"
    ```
* Ejecutar la app en el entorno de desarrollo para ver los cambios reflejados.
    ```shell
    uvicorn main:app --reload
    ```
    ```shell
    uvicorn main:app --reload --port 5000
    ```
------------
## 3.- Documentación automática con Swagger
Describe cada uno de los endpoints que tiene la aplicación basándose en los estándares abiertos de OpenAPI.

* Para acceder a la documentación, solamente agregar la dirección "/docs" mediante http://localhost:5000/docs

    ```python
    from fastapi import FastAPI

    app = FastAPI()
    app.title = "Mi aplicación con FastAPI" #Coloca el nombre de la app
    app.version = "0.0.1" # Coloca la versión de la app

    # Creación del Endpoint
    @app.get('/', tags=["home"])
    def message():
        return "Hello World!"
    ```
## 4.- Métodos HTTP
El protocolo HTTP es aquel que define un conjunto de métodos de petición que indican la acción que se desea realizar para un recurso determinado del servidor.

Los principales métodos soportados por HTTP y por ello usados por una API REST son:
- POST: crear un recurso nuevo.
- PUT: modificar un recurso existente.
- GET: consultar información de un recurso.
- DELETE: eliminar un recurso.

### ¿De qué tratará la app?
El proyecto a realizar será una API que brindará información relacionada con películas, por lo que se tiene lo siguiente:
- **Consulta de todas las películas:** Se utilizará el método GET para las consultar y solicitar los datos de todas las películas.
- **Filtrado de películas:** Se solicitará la información de las películas por su ID y por la categoría en la que pertenecen, por lo que se utilizará el método GET y se pasarán parámetros de ruta y parámetros de query.
- **Registro de películas:** Se utilizará el método POST para registros los datos de las películas junto con la ayuda de la librería Pydantic para el manejo de los datos.
- **Modificación y eliminación de películas:** Se utilizará los métodos PUT y DELETE paa la modificacíón y eliminación de datos en la aplicación.   

## 5.- Método GET

- Lista de películas
    ```python
    movies = [
        {
            "id": 1,
            "title": "The Galactic Adventure",
            "overview": "Una película galáctica.",
            "year": 2020,
            "rating": 8.0,
            "category": "Acción",
        },
        {
            "id": 2,
            "title": "La Gran Comedia",
            "overview": "Una película graciosa.",
            "year": 2019,
            "rating": 7.5,
            "category": "Comedia",
        },
        {
            "id": 3,
            "title": "Drama in the City",
            "overview": "Una película de drama.",
            "year": 2021,
            "rating": 8.5,
            "category": "Drama",
        },
        {
            "id": 4,
            "title": "Mystery Island",
            "overview": "Una película misteriosa.",
            "year": 2018,
            "rating": 9.0,
            "category": "Misterio",
        },
        {
            "id": 5,
            "title": "Aventura Extrema",
            "overview": "Una película extrema.",
            "year": 2022,
            "rating": 7.8,
            "category": "Acción",
        },
        # Agrega más películas ficticias basadas en películas reales según sea necesario
    ]

    # Creación de la función GET para obtener todas las películas.
    @app.get('/movies', tags=['movies']) #Etiqueta 'movies'.
    def get_movies():
        return movies
    ```
## 5.- Parámetros de ruta
Parámetros de ruta: Estos son valores que se extraen directamente de la ruta misma, como {id}. 

Para ingresar un parámetro dentro de la ruta, será necesario definir una lista de elementos para que funcione correctamente.

* Crear lista con varias películas.
    ```python
    movies = [
        {
            "id": 1,
            "title": "The Galactic Adventure",
            "overview": "Una película galáctica.",
            "year": 2020,
            "rating": 8.0,
            "category": "Acción",
        },
        {
            "id": 2,
            "title": "La Gran Comedia",
            "overview": "Una película graciosa.",
            "year": 2019,
            "rating": 7.5,
            "category": "Comedia",
        }
    ]
    
    # Crear ruta con parámetro
    @app.get('/movies/{id}', tags=['movies'])
    def get_movie(id: int): # Solamente recibirá un valor INT.
    for item in movies: # item: iterador,  movies: lista.
            if item['id'] == id: # Si el iterador entra un ID igual que el del parámetro,  regresa el item (la película).
                return item
        return [] # Si no encuentra el item, regresa una lista vacía.
    ```
### Request Query:
* Ejemplo de la URL: 
    ```shell
    http://127.0.0.1:5000/movies/1
    ```
----- 
## 6.- Parámetros Query
Parámetro Query: son un conjunto de parámetros opcionales que se añaden en la URL al finalizar la ruta, con la finalidad de definir acciones o contenido en la URL, se pueden visualizar estos elementos después de un '**?**', para agregar más parámetros query se utiliza '**&**'.

* Crear la ruta por categorías.
    ```python
    @app.get('/movies', tags=['movies'])
    def get_movies_by_category(category: str, year: int) # Parámetros categoria y año.
        return [item for item in movies if item['category'] == category] # Devuelve un item en un for que recorre toda la lista de 'movies' y si el item coincide con una categoría de la lista, trae las películas de esa categoría en una lista.
    ```
En la URL se refleja de la siguiente manera:
* Con un parámetro:
    ```shell
    http://127.0.0.1:5000/movies/?category=Suspenso
    ```

* Con dos parámetros:
    ```shell
    http://127.0.0.1:5000/movies/?category=Suspenso&year=2022
    ```

## 7.- Método POST
Importar la librería Body, para que los parámetros no cuenten como un contenido Query, sino como un contenido Body importar en "fastapi" la librería Body, para que cambie de parámetros a un objeto que contiene cada uno de los valores de la película.
* Importando Body
    ```python
    from fastapi import Body
    ```
* Crear un nuevo recurso (película).
    ```python
    @app.post('/movies', tags=['movies'])
    def create_movie(id: int = Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
        movies.append({
            "id": id,
            "title": title,
            "overview": overview,
            "year": year,
            "rating": rating,
            "category": category
        })
        return title
    ```
* En la documentación de la API, se mostrará el objeto describiendo el tipo de elemento que tiene el objeto, para así, utilizarlo para crear un nuevo recurso.
    ```json
    
    {
        "id": 0,
        "title": "string",
        "overview": "string",
        "year": 0,
        "rating": 0,
        "category": "string"
    }
    ```
## 8.- Método PUT y DELETE
### Método PUT
* Modificar un recurso creado.
    ```python
    @app.put('/movies/{id}', tags=['movies'])
    def update_movie(id: int, title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
        for item in movies:
            if item["id"] == id:
                item['title'] = title
                item['overview'] = overview 
                item['year'] = year 
                item['rating'] = rating 
                item['category'] = category
                return movies
    ```
### Método DELETE
* Eliminar un recurso.
    ```python
    @app.delete('/movies/{id}', tags=['movies'])
    def delete_movie(id: int):
        for item in movies:
            if item["id"] == id:
                movies.remove(item)
                return movies
    ```
## 9.- Creación de esquemas
Para la creación de esquemas con FastAPI, se recomienda el uso de la librería Pydantic y para hacer un elemento opcional se recomienda lal= librería Typing
* Instalación de la librería Pydantic
    ```python
    from pydantic import BaseModel
    from typing import Optional
    ```
* Crear el esquema de datos
    ```python
    class Movie(BaseModel):
        id: Optional[int] = None
        title: str
        overview: str
        year: int
        rating: float
        category: str
    ```
Al hacer los cambios, se modificará los métodos POST y PUT de la siguiente forma:
* POST
    ```python
    @app.post('/movies', tags=['movies'])
    def create_movie(movie: Movie):
        movies.append(movie.dict())
        return movie
    ```
* PUT
    ```python
    @app.put('/movies/{id}', tags=['movies'])
    def update_movie(id: int, movie: Movie):
        for item in movies:
            if item["id"] == id:
                item['title'] == movie.title
                item['overview'] == movie.overview
                item['year'] == movie.year
                item['rating'] == movie.rating
                item['category'] == movie.catgory
    ```
## 10.- Validaciones de tipos de datos
Las validaciones ayudan a que lo stipos de datos cumplan con ciertos requerimientos.

* Importar la clase 'Field' de la librería pydantic.
    ```python 
    from pydantic import Field
    ```
* Cambiará la sintaxis de la clase Movie al integral la nueva clase.
    ```python
    class Movie(BaseModel):
        id: Optional[int] = None
        title: str = Field(default="Mi película", min_Length=5, max_Length=15) # Valor default, mínimo de 5 digitos y máximo de 15 dígitos
        overview: str = Field(default="Descripción de la película", min_Length=15, max_Length=50)
        year: int = Field(default=2022 le=2022) # le = menoir a cierta cantidad, 
        rating: float = Field(ge=1, le=10) # Mayor o igual a 1, y menor o igual a 10.
        category: str = Field(min_length=3, max_length=10)
    ```
* Se recomienda crear una clase con la configuración predeterminada de los ejemplos (dentro de la clase "Movie")
    ```python
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "title": "Mi película",
                    "overview": "Descripción de la película",
                    "year": 2022,
                    "rating": 9.9,
                    "category": "Acción"
                }
            ]
        }
    }
    ```
## 11.- Tipos de parámetros
Se pueden realizar validaciones a los parámetros, en donde se puede validar los parámetros de ruta y parámetros query.
### Parámetro Query
- Envian en la URL después de un signo de interrogación "?".
- Se usan para buscar información.
- Ejemplo: **example.com/items?id=2**
* Se importa la clase "Path" de la librería fastapi para validar los parámetros query.
    ```python
    from fastapi import Path
    ```
* Se realiza una validación de parámetros query de la siguiente manera:
    ```python
    @app.get("/movies/{id}", tags=["movies"])
    def get_movies_by_category(category: str = Query(min_length= 5, max_length= 15))
        return [item for item in movies if item['category'] == category]
    ```
### Parámetros Patch
- Se incluyen directamente en la URL.
- Se usa para acceder a un recurso en específico dentro de la aplicación.
- Ejemplo: **example.com/movies/2**
* Se importa la clase "Query" de la librería fastapi para validad los parámetros de ruta.
    ```python
    from fastapi import Path
    ```

* Se realiza una validación para los parámetros de ruta de la siguiente manera:
    ```python
        @app.get("/movies/{id}", tags=["movies"])
        def get_movie(id: int = Path(ge=1,le=2000)):
            for item in movies:
                if item['id'] == id:
                    return item
            return []
        ```
## 12.- Tipos de respuesta
En defecto FastAPI convierte los valores retornados a JSON, transformando y usando por detrás el formato JSON. 

### Tipos de respuesta en FastAPI:
Tipos de Respuesta en FastAPI:

- **JSONResponse:** se utiliza para enviar respuestas JSON desde rutas.
- **HTMLResponse:** se utiliza para enviar respuestas HTML.
- **PlainTextResponse:** se utiliza para enviar respuestas en texto plano. 
- **ORJSONResponse:** proporciona una respuesta JSON utilizando la biblioteca "orjson" para serializar objetos como Python.
- **UJSONResponse:** similar a "ORJSONResponse", pero utiliza la biblioteca "ujson".
- **RedirectResponse:** se utiliza para realizar redirecciones.
- **StreamingResponse:** se utiliza para enviar respuestas de transmisión (ejemplo: transmitir archivos grandes).
- **FileResponse:** se utiliza para enviar archivos como respuesta.

### Código
- Se importan las clases de la librería "fastapi.responses":
    ```python
    from fastpi.responses import HTMLResponse, JSONResponse
     ``` 

- Ejemplo con la clase "JSONResponse":
    ```python
    @app.get('/movies/{id}', tags=['movies'])
    def get_movies():
        return JSONResponse(content=("message": "Se ha registrado la película")) # Se añade el contenido a enviar.
    ```
### Modelos de respuesta.
Podemos añadir modelos de respuesta que pueden contener datos / listas como respuesta.
* Se importa la clase "List" de la libreria typing.
    ```python
    # Get movies.
    @app.get("/movies", tags=["movies"], response_model=List[Movie]) # Responde con una lista de tipo Movie.
    def get_movies() -> List[Movie]: # Lista de películas (movie).
        return JSONResponse(content=movies) # Devuelve la película.

    # Get Movies.
    @app.get("/movies/{id}", tags=["movies"], response_model=Movie) # Responde con una película.
    def get_movie(id: int = Path(ge=1, le=2000)) -> Movie: # Devuelve una película (Movie).
        for item in movies:
            if item['id'] == id:
                return JSONResponse(content=item, status_code=200)
        return JSONResponse(content={"message": "no se ha encontrado la pelicula"})

    # Get Movies by category
    @app.get("/movies/", tags=["movies"], response_model=List[Movie]) # Responde con una lista de películas.
    def get_movies_by_category(
        category: str = Query(min_length=5, max_length=15,
                            title="Categoria Movie",
                            description="This is the movie category")) -> List[Movie]: # Devuelve la lista de películas.
        data = [item for item in movies if item['category'] == category]
        return JSONResponse(content=data, status_code=200)

    # Borrar película.
    @app.delete("/movies", tags=["movies"], response_model=dict, status_code=200)
    def delete_movie(id: int) -> dict: # Responde un diccionario 
        for item in movies:
            if item['id'] == id:
                movies.remove(item)
        return JSONResponse(content={"message": "se ha eliminado la pelicula"})
    
    # Crea película.
    @app.put('/movies/{id}', tags=['Movies'], response_model=dict) # Devuelve un diccionario
    def update_movie(id: int, movie: Movie)-> dict: # Devuelve un diccionario
        for item in movies:
            if item['id'] == id:
                item['title'] = movie.title
                item['overview'] = movie.overview
                item['year'] = movie.year
                item['rating'] = movie.rating
                item['category'] = movie.category
                return JSONResponse(status_code=200, content={"Message": "Se ha modificado la película"}) 
    ```
## 13.- Códigos de estado
Los códigos de estados indican si una petición de ha ejecutado correctamente o ha ocurrido algún error.

### Tipos de código de estado:
* Respuestas informativas **(100 – 199)**
* Respuestas exitosas **(200 – 299)**
* Mensajes de redirección **(300 – 399)**
* Respuestas de error del cliente **(400 - 499)**
* Respuestas de error del servidor **(500 - 599)**

Estos códigos se utilizan para dar a entender una situación específica al usuario al momento de cargar un elemento / página.

* Aplicando de código de estados a todos los métodos:
    ```python
        # Get movies.
        @app.get("/movies", tags=["movies"], response_model=List[Movie], estatus_code=200) # Devuelve un código de estado 200 (OK).
        def get_movies() -> List[Movie]:
            return JSONResponse(status_code=200, content=movies) # Responde con un código de estado 200 (OK).
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
            return JSONResponse(status_code=201, content=[category_list])

        # Obtener una película
        @app.post('/movies/', tags=['Movies'], response_model=dict, status_code=201)
        def create_movie(movie: Movie)-> dict:
            movies.append(movie)
            return JSONResponse(status_code=201, content={"Message": "Se ha registrado la película"})

        # Actualizar una película
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

        # Eliminar una película
        @app.delete('/movies/{id}', tags=['Movies'], response_model=dict, status_code=200)
        def delete_movie(id: int)-> dict:
            for item in movies:
                if item['id'] == id:
                    movies.remove(item)
                    return JSONResponse(status_code=200, content={"Message": "Se ha eliminado la película"})

        # Código de estado 404
        @app.get('/movies/{id}', tags=['Movies'], response_model=Movie)
        def get_movie(id: int = Path(ge= 1, le=2000)) -> Movie:
            for item in movies:
                if item['id'] == id:
                    return JSONResponse(content=item)
            return JSONResponse(status_code=404, content=[]) # Devuelve un código de estado 404.
    ```
## 14.- Flujo de autenticación.

### Flujo de autenticación
Ahora empezaremos con el módulo de autenticaciones pero antes quiero explicarte un poco acerca de lo que estaremos realizando en nuestra aplicación y cómo será el proceso de autenticación y autorización.

### Ruta para iniciar sesión
Lo que obtendremos como resultado al final de este módulo es la protección de determinadas rutas de nuestra aplicación para las cuales solo se podrá acceder mediante el inicio de sesión del usuario. Para esto crearemos una ruta que utilice el método POST donde se solicitarán los datos como email y contraseña.

### Creación y envío de token
Luego de que el usuario ingrese sus datos de sesión correctos este obtendrá un token que le servirá para enviarlo al momento de hacer una petición a una ruta protegida.

### Validación de token
Al momento de que nuestra API reciba la petición del usuario, comprobará que este le haya enviado el token y validará si es correcto y le pertenece. Finalmente se le dará acceso a la ruta que está solicitando. 

## 13.- Autenticación PyJWT.
PyJWT (Python JSON Web Token) es una biblioteca de Python que se utiliza para codificar y decodificar tokens JWT (JSON Web Token). 

Un token JWT es un objeto de seguridad que se utiliza para autenticar a los usuarios en aplicaciones web y móviles. Los tokens JWT se emiten por un servidor de autenticación y luego se envían al cliente, que los utiliza para demostrar su identidad al acceder a recursos protegidos en el servidor.

Se contruye de la siguiente manera:
* Header:
    ```json
    {
        "alg":"HS246",
        "typ":"JWT"
    }
    ```
* PLayload:
    ```json
    "sub":"123456789",
    "name":"George White",
    "admin":true,
    "lat":"1516239022"
    ```
* Signature:
    ```shell
    Base64URLSafe(
        HMACSHA256(<header>.
        <playload>, <secret key>
        )
    )
    ```
### Implementación de pywtj.
Se hace la instalación de un módulo para crear el token.
* Instalar el módulo pyjwt:
    ```shell
    pip install pyjwt
    ```
### Crear token.
* Crear un nuevo archivo con algún nombre para identificar o en recomendación "jwt_manager.py"
* Crear la función para crear el token.
    ```python
    def create_token(data: dict) -> str: # Recibe un diccionario con los datos y retorna un string.
        token: str = encode(payload=data, key="my_secret_key", algorithm="HS256") # Es el contenido a convertir, una contraseña secreta y un algoritmo para generar el token.
        return token # Regresa el token generado
    ```
* Importar el archivo "jwt_manager" la función "create_token".
    ```python
    from jwt_manager import encode
    ```
* Crear un nuevo model para añadir la información del usuario.
    ```python
    class User(BaseModel):
        email: str
        password: str
    ```
* Crear una ruta para que el usuario pueda iniciar sesión con el token.
    ```python
    @app.get('/login', tags=['auth'])
    def login(user: User):
        return user
    ```
### Validando token
* Importar la libreria 'jwt' y traer la clase 'encode':
    ```python
    from jwt import encode
    ``` 
* Crear una condicional para validar el token.
    ```python
    @app.get('/login', tags=['auth'])
    def login(user: User):
        if user.email == "admin@gmail.com" and user.password == "admin": # Validar si la información que ingresa el usuario es correcta para generar el token
            token: str = create_token(user.dict) # Pasar los datos como tipo diccionario.
            return JSONResponse(status_code: 200, content=token) # Regresa el token y un código de estado 200.
    ```
### Crear función para validar token.
En el archivo "jwt_manager" crear una función para validar el token.
* Importar la clase "decode":
    ```python
    from jwt_manager import decode
    ```
* Función validate_token:
    ```python
    def validate_token(token: str) -> dict: # Retorna un diccionario
        data: dict = decode(token, key="my_secret_key", algorithm=['HS256'] # Recibe el token, la clave secreta y el algoritmo para decifrar mediante un diccionario.
        return data # Retorna el diccionario 'data'.
    ```
## 14.- Middlewares de autenticación
 Crear una función de solicitar el token generado previamente.
 * Importa la librería "fastapi.security la clase "HTTPBearer", la clase "Request" y la clase "HTTPException":
    ```python
    from fastapi import Request, HTTPException
    from fastapi.security import HTTPBearer
    ```
* Crear la clase:
    ```python
    class JWTBearer(HTTPBearer): # Hereda de la clase HTTPBearer
    async def __call__(self, request: Request): # Función(__call__) para acceder a la información del usuario y es requerida. Esta es una función asíncrona.
        auth = await super().__call__(request) # Guarda los datos de las credenciales.
        data = validate_token(auth.credentials) # La información pasa desde la función de validar y se guarda en data
        if data['email'] != "admin@gmail.com": # Verifica si los datos estan correctos.
            raise HTTPException(status_code=403, detail="Credenciales son inválidas") # Envia credenciales inválidas mediante HTTPException.
    ```
### Hacer una ruta con autentificación:
Añadir a una ruta la autenticación que se hizo previamente para ser utilizada solamente con token:
* Se usa el argumento dependencies=[Depends()] para hacer que se ejecute nuestra clase y asi realizar la validación del token, por lo que ya no se requiere hacer las validaciones dentro de cada metodo HTTP.
    ```python:
    @app.get('/movies', tags = ['Movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())]) # Contiene una tatributo llamado dependencias, la cual contiene ciertas dependencias que se van a ejecutar al momento de realizar una petición a la ruta.
    def get_movies()-> List[Movie]:
        return JSONResponse(status_code=200, content=movies)
    ```