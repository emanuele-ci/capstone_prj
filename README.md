# Capstone - Casting Agency Application


URL of the endpoint:
https://capstone-prj.onrender.com


## JWT to test access to the endpoints


1) Casting Assistant

'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImF0WGJSTmcxenpQWnRmUkZZakduWiJ9.eyJpc3MiOiJodHRwczovL3VjaWUuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDY3ODUyYmVjM2VhYWIxZDgxMTY2ZmRjOCIsImF1ZCI6InRlc3QxIiwiaWF0IjoxNzQ2NzAyMDQ2LCJleHAiOjE3NDY3ODg0NDUsInNjb3BlIjoiIiwiYXpwIjoiRmVockhxNG5FckhXRDNMNUg0cmU5TTg5RDRKSzgxanAiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.PPJlwNb6fybiEphZj-SEV7_PX-ZrIpkj1VY-liQ4ecuU1GosJDRGwA_Ft53Ef66p8GattdCNVH45HoI2GLtS-PUbzU7tt7FcxQ4zU-7edNI3x2x8-qWQ3jnzrIwZhAx0FtKFOy3Q9sRglhqPwZO2ti3v96GTZce3Hf9KAkRGt3AKT3ZZAkNg2geaY5E2WyS4EjaQl-xCHO97W3wbWSbNZpg0rskGCjvI6wd4bLiEz7zqjBZ3mMLbNPP2VphcRcumGbf-0N0By_nSsKFGEyL5qhSTphvrWMRaE23WPuyWFcw5Hbt_xj1xEY0PSAEEiS6IQ_hkzkmS9O-omPekXkx5qQ'


2) Executive Producer

'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImF0WGJSTmcxenpQWnRmUkZZakduWiJ9.eyJpc3MiOiJodHRwczovL3VjaWUuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDY3N2E4MDY2MWRjYWQxMTc0MTcxMDdlZSIsImF1ZCI6InRlc3QxIiwiaWF0IjoxNzQ2NzAxOTM4LCJleHAiOjE3NDY3ODgzMzcsInNjb3BlIjoiIiwiYXpwIjoiRmVockhxNG5FckhXRDNMNUg0cmU5TTg5RDRKSzgxanAiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.T3YnDNBnhOpcQMonhn7o4mwkUtEI1NLTyhjYZm0XSJ2kzldan7mgsA1VonE_w5_Y3IT0wVP-M60518WmVkQXu-p_cAI8cnQ1AMvwhoAxOHkFfihN-xB1ashEOeFL1psHpdQX55NW6BksfqqQqnxTl_-jkTsFCyjgl6q5_mojJi8PZzD2IvKk0uuz5IJ419Uh2KaGiwG3G2v-_BZ2yLJ_3oEaep8qoE3lFEkjQAcid637UVvc5yZ_-YDpSXt8HkoyEDP0qI4_sbGFnuKDndX09zfhVORSm6AGfgTweZ56WbbtO_3RpESQUOb2R_8XJZ70Fyg9pD86NMV-CGZIb351gw'


## General introduction

This project is for the APIs necessary to an application dedicated to a casting agency, which needs to create/ modify / update / delete:
- a list of movies
- a list of actors

Access to the APIs require an authentication on Auth0.

Possible authorization roles are:

1) Casting Assistant
Can view actors and movies

2) Executive Producer
All permissions a Casting Assistant has and…
Add or delete an actor from the database
Modify actors or movies
Add or delete a movie from the database




## Information to use the deployed service

### URL

URL of the endpoint:
https://capstone-prj.onrender.com





## API endpoints tests

Tests are provided as Postman collection in file 
udacity-fsnd-capstone.postman_collection.json`


## API List of endpoints and description

### GET: '/movies'


Returns a dictionary of existing movies

Request sample with CURL:

curl -X GET http://.../movies


Response sample:

{
    "movies": [
        {
            "id": 1,
            "release_year": 2025,
            "title": "Whitesnow"
        }
    ],
    "success": true
}


### get:actors


Returns a dictionary of existing actors

Request sample with CURL (WT has to be added):

curl -X GET http://.../actors


Response sample:

{
    "actors": [
        {
            "birth_year": 1987,
            "gender": "X",
            "id": 1,
            "name": "Actor Test 2"
        },
        {
            "birth_year": 1989,
            "gender": "F",
            "id": 2,
            "name": "Actor Test 3"
        }
    ],
    "success": true
}

### POST '/movies'


Sends a post request in order to add a new movie

Request sample with CURL (JWT has to be added):

curl -X POST http://.../movies -H 'Content-Type: application/json' -d '{"title":"Whitesnow","release_year":2025}'

Response sample:

{
    "movie_id": 4,
    "success": true
}


### post:actors


Sends a post request in order to add a new actor

Request sample with CURL (JWT has to be added):

curl -X POST http://.../actors -H 'Content-Type: application/json' -d '{"name":"Sarah Smith","birth_year":1997,"gender":"F"}'

Response sample:

{
    "actor_id": 6,
    "success": true
}


### PATCH '/movies/${id}'

Modifies a specified movie using the id of the movie
Request Arguments: id - integer


Request sample with CURL:

curl -X PATCH http://.../movies/1 -H 'Content-Type: application/json' -d '{"title":"Updated title"}'

Response sample:

{
    "movie": {
        "id": 1,
        "release_year": 2025,
        "title": "Updated title"
    },
    "success": true
}


### patch '/actors/${id}'

Modifies a specified actor using the id of the actor
Request Arguments: id - integer


Request sample with CURL:

curl -X PATCH http://.../actors/1 -H 'Content-Type: application/json' -d '{"name":"Updated name"}'

Response sample:

{
    "actor": {
        "birth_year": 1987,
        "gender": "X",
        "id": 1,
        "name": "Updated name"
    },
    "success": true
}


### DELETE '/movies/${id}'

Deletes a specified movie using the id of the movie
Request Arguments: id - integer

Request sample with CURL:

curl -X DELETE http://.../movies/1

Response sample:

{
    "delete": 1,
    "success": true
}

### DELETE '/actors/${id}'

Deletes a specified movie using the id of the movie
Request Arguments: id - integer

Request sample with CURL:

curl -X DELETE http://127.0.0.1:5000/movies/1

Response sample:

{
    "delete": 3,
    "success": true
}


## Information to install the project locally

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### PIP Dependencies

Install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the database.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server locally for development purposes

For running the server, it is necessary having created a local postgres database named "capstone"

In the first execution, it is necessary to uncomment and run the 
db_drop_and_create_all()
command in file api.py

The database parameters are configured in file settings.py

For running the tests, it is necessary having created a local postgres database named "capstone_test"


Auth0 configurations are in the first lines of file auth.py
(AUTH0_DOMAIN, ALGORITHMS, API_AUDIENCE)

To install dependencies, please run

```bash
pip install -r requirements.txt
```

To run the server, each time a new terminal session is open, please run:

```bash
export FLASK_APP=app.py;
```

To run the server, execute:

```bash
flask run --reload
```
