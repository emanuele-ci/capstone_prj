import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

#import database.models
#from database import models
#from database.models import db_drop_and_create_all, setup_db, Actor, Movie
from models import db_drop_and_create_all, setup_db, Actor, Movie
#from .models_2 import db_drop_and_create_all, setup_db, Actor, Movie
#from controllers.auth import AuthError, requires_auth
#from .auth.auth import AuthError, requires_auth
from auth import AuthError, requires_auth
#from .database.config import Config
from config import Config
#import config


def create_app():


    app = Flask(__name__)
    #app.config.from_object('config')
    app.config.from_object(Config)
    setup_db(app)
    CORS(app)

    '''
    @TODO uncomment the following line to initialize the datbase
    !! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
    !! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
    '''
    db_drop_and_create_all()
     
    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def actors(jwt):

    #def actors():
        try:       
          actors = Actor.query.all()  
          actors_repr = [actor.format() for actor in actors]
          
          return jsonify({
              'success': True,
              'actors': actors_repr
          })    
      
        except Exception as e:
          print(e) 
          abort(500)

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def new_actor(jwt):    
        req = request.get_json()
        try:
            if 'name' in req and 'birth_year' in req and 'gender' in req:
                i_name= req.get('name')
                i_birth_year = req.get('birth_year')
                i_gender = req.get('gender')            
            
                #print(i_name)    
                actor = Actor(name=i_name, birth_year=i_birth_year, gender=i_gender)
                #print('New actor:', actor)
                
                              
                actor.insert()    
                #actors = Actor.query.all()
                
                actor_id = actor.id
                
                return jsonify({
                    'success': True,
                    'actor_id': actor_id 
                    #'actors': [actor.format() for actor in actors]
                    #'actors': [repr(actor) for actor in actors]
                }), 200

            else:
                abort(422)
                
        except Exception as e:
            print(e)
            abort(500)

    @app.route("/actors/<int:id>", methods=["PATCH"])
    @requires_auth("patch:actors")
    def patch_actors(payload, id):
        
        req = request.get_json()
        
        try:
            actor = Actor.query.filter(Actor.id == id).one_or_none()
            if actor == None:
                abort(404)
                
            if req.get('name'):
                i_name = req['name']
                actor.name = i_name           
                
            if req.get('birth_year'):
                i_birth_year = req['birth_year']
                actor.birth_year = i_birth_year            

            if req.get('gender'):
                i_gender = req['gender']
                actor.gender = i_gender   
                
            actor.update()
            return jsonify({
                "success": True, 
                "actor": actor.format()
            }), 200
        except Exception as e:
            print(e)
            abort(422)

    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, id):
        try:
            actor = Actor.query.filter(Actor.id == id).first()
            if actor == None:
                abort(404)
        
            actor.delete()
            return jsonify({
                'success': True, 
                'delete': id
            }), 200
            
        except Exception as e:
            print(e)
            abort(422)



    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def movies(jwt):
        try:       
          movies = Movie.query.all()  
          movies_repr = [movie.format() for movie in movies]
        
          return jsonify({
            'success': True,
            'movies': movies_repr
          })    
      
        except Exception as e:
          print(e) 
          abort(500)



    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def new_movie(jwt):
        
        req = request.get_json()
        try:
            if 'title' in req and 'release_year' in req:
                i_title= req.get('title')
                i_release_year = req.get('release_year')       
            
                #print(i_title)    
                movie = Movie(title=i_title, release_year=i_release_year)
                #print('New movie:', movie)

                movie.insert()    
                #movies = Movie.query.all()
                
                movie_id = movie.id
                
                return jsonify({
                    'success': True,
                    'movie_id': movie_id
                    #'movies': [movie.format() for movie in movies]
                }), 200

            else:
                abort(422)

        except Exception as e:
            print(e)
            abort(500)



    @app.route("/movies/<int:id>", methods=["PATCH"])
    @requires_auth("patch:movies")
    def patch_movies(payload, id):
        
        req = request.get_json()
        
        try:
            movie = Movie.query.filter(Movie.id == id).one_or_none()
            if movie == None:
                abort(404)
                
            if req.get('title'):
                i_title = req['title']
                movie.title = i_title           
                
            if req.get('release_year'):
                i_release_year = req['release_year']
                movie.release_year = i_release_year            
                
            movie.update()
            return jsonify({
                "success": True, 
                "movie": movie.format()
            }), 200
        except Exception as e:
            print(e)
            abort(422)



    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, id):
        try:
            movie = Movie.query.filter(Movie.id == id).first()
            if movie == None:
                abort(404)
        
            movie.delete()
            return jsonify({
                'success': True, 
                'delete': id
            }), 200
            
        except Exception as e:
            print(e)
            abort(422)



    # Error Handling

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422



    @app.errorhandler(404)
    def resourcenotfound(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404


    @app.errorhandler(500)
    def internalservererror(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "internal server error"
        }), 500

    @app.errorhandler(400)
    def badrequest(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "unauthorized"
        }), 401

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
