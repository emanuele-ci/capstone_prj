import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

#os.chdir("**Put here the directory where you have the file with your function**")

from models import setup_db, Actor, Movie

from api import create_app

#import database.models.setup_db

#os.chdir("**Put here the directory where you were working**")

from flask import current_app

#from api import app
# set our application to testing mode
#app.testing = True

JWT_PRODUCER = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImF0WGJSTmcxenpQWnRmUkZZakduWiJ9.eyJpc3MiOiJodHRwczovL3VjaWUuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDY3N2E4MDY2MWRjYWQxMTc0MTcxMDdlZSIsImF1ZCI6InRlc3QxIiwiaWF0IjoxNzQ2NTQzMjIzLCJleHAiOjE3NDY2Mjk2MjIsInNjb3BlIjoiIiwiYXpwIjoiRmVockhxNG5FckhXRDNMNUg0cmU5TTg5RDRKSzgxanAiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.DHQhlTNXlTQpoGwO6-uCILzUpb_0EOvnLRcmecQSJz0_Skrsw8mRC2t3MmYqMFoObl-bZTItp4V1Ejw4pYaJjx-cnS5ROnoCiLVR1_vYbA1goP1kSGHzCHQm7E8uUB2Hab-YPwx2BaDF9gc-8gxXMQRgjIhhZ6KAtqOtgBGb8TG8xbuWTgYp5rHGMHTdPz8Cq8I9bb7NhPam7o4jFuEi_0oX_APObMnU4tJkSJntDZflPeJC1llFJ3TeUDVVyhFlfUb5TNZ08o34lebmIPCQv6Qp_2e4W8sYwdu9nX3gp1ZWALLokgAK7yN49WfSi0H7wTY-ATRnsZ0UIj-Ztt2ypw'

JWT_ASSISTANT = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImF0WGJSTmcxenpQWnRmUkZZakduWiJ9.eyJpc3MiOiJodHRwczovL3VjaWUuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDY3ODUyYmVjM2VhYWIxZDgxMTY2ZmRjOCIsImF1ZCI6InRlc3QxIiwiaWF0IjoxNzQ2NTQzMjg1LCJleHAiOjE3NDY2Mjk2ODQsInNjb3BlIjoiIiwiYXpwIjoiRmVockhxNG5FckhXRDNMNUg0cmU5TTg5RDRKSzgxanAiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.cYDXlIubcd3ztZt_Oq_QDRXhf1m97UGF1R4lKwfR7OE9xqb60srLF-hmgNLkuPe6ESFlPBpuezjup3RcZA5konedhlW6Sx6a-Dw2XzKtzGVkjvfdySeGfUu0zoOCujWRVtQLXV5yTUM7darlJyYtgOMmfY4EhrsUXRNlkz_riNH89jBqAyhIhmFQZi1IA5ujNaSFnT4T2cKqDScNU1MjkhwkmGlT2x9PZCpflGQmJ4vXwwvB8Y87qFboRjjUV-IaWUvY62eciqdxDT4oVhReToeAOuFBm-CY67btsX2bf58KjOpvgUQBV5rgBJ5gOVvoDiBYMMuVWcQGK0enFJrteQ'

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