import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

#os.chdir("**Put here the directory where you have the file with your function**")

from models import setup_db, Actor, Movie

from app import create_app

#import database.models.setup_db

#os.chdir("**Put here the directory where you were working**")

from flask import current_app

#from app import app
# set our application to testing mode
#app.testing = True

JWT_ASSISTANT = os.environ.get('ASSISTANT_JWT')

JWT_PRODUCER = os.environ.get('PRODUCER_JWT')

class CapstoneTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    #def setUp(self):
    #    self.app = create_app()        
    #    self.ctx = app.app_context()
    #    self.ctx.push()
    #    self.client = app.test_client()

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path ="postgresql://{}:{}@{}/{}".format('postgres', 'postgres','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()


    def tearDown(self):
        #self.ctx.pop()
        pass

    #def test_app(self):
    #    assert self.app is not None
    #    assert current_app == self.app

    def test_post_actors(self):
          res = self.client().post("/actors", json={"name":"Actor Test 2","birth_year":1987,"gender":"X"}, headers={"Authorization": "Bearer {}".format(JWT_PRODUCER)})
          data = json.loads(res.data)

          self.assertEqual(res.status_code, 200)
          #self.assertTrue(data["actors"])
          #self.assertTrue(len(data["actors"]))
          #actor_id = data["actor_id"]
          
    def test_post_actors_error(self):
          res = self.client().post("/actors", json={"name":"Actor Test 2","birth_year":"wrong format","gender":"X"}, headers={"Authorization": "Bearer {}".format(JWT_PRODUCER)})
          data = json.loads(res.data)

          self.assertEqual(res.status_code, 500)
          #self.assertTrue(data["actors"])
          #self.assertTrue(len(data["actors"]))
          #actor_id = data["actor_id"]          
 
    def test_patch_actors(self):
          res = self.client().patch("/actors/1", json={"name":"Updated name"}, headers={"Authorization": "Bearer {}".format(JWT_PRODUCER)})
          data = json.loads(res.data)
          self.assertEqual(res.status_code, 200)
          
    def test_patch_actors_error(self):
          res = self.client().patch("/actors/", json={"name":"Updated name"}, headers={"Authorization": "Bearer {}".format(JWT_PRODUCER)})
          data = json.loads(res.data)
          self.assertEqual(res.status_code, 404)          
 
    def test_get_actors_producer(self):
          res = self.client().get("/actors", headers={"Authorization": "Bearer {}".format(JWT_PRODUCER)})
          data = json.loads(res.data)
          self.assertEqual(res.status_code, 200)
          
    def test_get_actors_assistant(self):
          res = self.client().get("/actors", headers={"Authorization": "Bearer {}".format(JWT_ASSISTANT)})
          data = json.loads(res.data)
          self.assertEqual(res.status_code, 200)        

    def test_get_actors_auth_error(self):
          res = self.client().get("/actors", )
          data = json.loads(res.data)
          self.assertEqual(res.status_code, 401)          

    def test_delete_actors(self):
          res = self.client().delete("/actors/1", headers={"Authorization": "Bearer {}".format(JWT_PRODUCER)})
          data = json.loads(res.data)
          self.assertEqual(res.status_code, 200)    

    def test_delete_actors_error(self):
          res = self.client().delete("/actors/", headers={"Authorization": "Bearer {}".format(JWT_PRODUCER)})
          data = json.loads(res.data)
          self.assertEqual(res.status_code, 404)    

    def test_post_movies(self):
          res = self.client().post("/movies", json={"title":"Movie Test 2","release_year":1987}, headers={"Authorization": "Bearer {}".format(JWT_PRODUCER)})
          data = json.loads(res.data)

          self.assertEqual(res.status_code, 200)
          #self.assertTrue(data["movies"])
          #self.assertTrue(len(data["movies"]))
          #movie_id = data["movie_id"]

    def test_post_movies_error(self):
          res = self.client().post("/movies", json={"title":"Movie Test 2","release_year":"wrong format"}, headers={"Authorization": "Bearer {}".format(JWT_PRODUCER)})
          data = json.loads(res.data)

          self.assertEqual(res.status_code, 500)
          #self.assertTrue(data["movies"])
          #self.assertTrue(len(data["movies"]))
          #movie_id = data["movie_id"]
 
    def test_patch_movies(self):
          res = self.client().patch("/movies/1", json={"title":"Updated title"}, headers={"Authorization": "Bearer {}".format(JWT_PRODUCER)})
          data = json.loads(res.data)
          self.assertEqual(res.status_code, 200)
 
    def test_patch_movies_error(self):
          res = self.client().patch("/movies/", json={"title":"Updated title"}, headers={"Authorization": "Bearer {}".format(JWT_PRODUCER)})
          data = json.loads(res.data)
          self.assertEqual(res.status_code, 404)
 
    def test_get_movies_producer(self):
          res = self.client().get("/movies", headers={"Authorization": "Bearer {}".format(JWT_PRODUCER)})
          data = json.loads(res.data)
          self.assertEqual(res.status_code, 200)
          
    def test_get_movies_assistant(self):
          res = self.client().get("/movies", headers={"Authorization": "Bearer {}".format(JWT_ASSISTANT)})
          data = json.loads(res.data)
          self.assertEqual(res.status_code, 200)     

    def test_get_movies_auth_error(self):
          res = self.client().get("/movies")
          data = json.loads(res.data)
          self.assertEqual(res.status_code, 401)          
          
    def test_delete_movies(self):
          res = self.client().delete("/movies/1", headers={"Authorization": "Bearer {}".format(JWT_PRODUCER)})
          data = json.loads(res.data)
          self.assertEqual(res.status_code, 200)     
        
    def test_delete_movies_error(self):
          res = self.client().delete("/movies/", headers={"Authorization": "Bearer {}".format(JWT_PRODUCER)})
          data = json.loads(res.data)
          self.assertEqual(res.status_code, 404)  
        
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
