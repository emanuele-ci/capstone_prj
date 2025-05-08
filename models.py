import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
#from settings import DB_NAME, DB_USER, DB_PASSWORD

#database_filename = "capstone"
#database_filename= DB_NAME 
#project_dir = os.path.dirname(os.path.abspath(__file__))
#database_path = "postgresql:///{}".format(os.path.join(project_dir, database_filename))
#database_path = "postgresql://{}:{}@{}/{}".format("postgres", "postgres", "localhost:5432", database_filename)
#database_path = 'postgresql://{}:{}@{}/{}'.format(DB_USER,DB_PASSWORD,'localhost:5432', database_name)


database_path = os.environ.get('DATABASE_URI')
#if database_path.startswith("postgres://"):
 # database_path = database_path.replace("postgres://", "postgresql://", 1)
  
#database_filename = "fyyurdb"
#database_path = "postgresql://{}:{}@{}/{}".format("postgres", "postgres", "localhost:5432", database_filename)


#DATABASE_URL = os.environ.get('DATABASE_URL')

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, i_database_path=DATABASE_URL):
    app.config["SQLALCHEMY_DATABASE_URI"] = i_database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    if i_database_path != DATABASE_URL:
        db.create_all()


'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multiple verisons of a database
'''


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
    # add demo rows which can help with testing
    
    actor = Actor(
        name='Anna James',
        gender='F',
        birth_year=1987   
    )

    actor.insert()

    movie = Movie(
        title='Whitesnow',
        release_year=2025  
    )

    movie.insert()



# ROUTES




'''
Actor
a persistent actor entity, extends the base SQLAlchemy Model
'''


class Actor(db.Model):
    __tablename__ = 'actor'    
    # Autoincrementing, unique primary key
    id = db.Column(db.Integer, primary_key=True)
    # String Title
    name = db.Column(db.String(80))

    gender = db.Column(db.String(1))
    # sample values : M , F, X
    birth_year = db.Column(db.Integer)

    '''
    insert()
        inserts a new model into a database
        the model must have a unique name
        the model must have a unique id or null id
        EXAMPLE
            actor = Actor(name=req_name, gender=req_gender, birth_year=req_birth_year)
            actor.insert()
    '''

    def __init__(self, name, gender, birth_year):
        self.name = name
        self.gender = gender
        self.birth_year = birth_year


    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a new model into a database
        the model must exist in the database
        EXAMPLE
            actor = Actor.query.filter(Actor.id == id).one_or_none()
            actor.delete()
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
        EXAMPLE
            actor = Actor.query.filter(Actor.id == id).one_or_none()
            actor.name = 'Jennifer Lopez Affleck'
            actor.update()
    '''

    def update(self):
        db.session.commit()

    def __repr__(self):
        self_repr = {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'birth_year': self.birth_year            
        }
        return json.dumps(self_repr)
        
    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'birth_year': self.birth_year  
        } 
        
        
        
        
'''
Movie
a persistent actor entity, extends the base SQLAlchemy Model
'''



class Movie(db.Model):
    __tablename__ = 'movie'    
    # Autoincrementing, unique primary key
    id = db.Column(db.Integer, primary_key=True)
    # String Title
    title = db.Column(db.String(80))
    #release_date = db.Column(db.DateTime)    
    release_year = db.Column(db.Integer)          


    '''
    insert()
        inserts a new model into a database
        the model must have a unique name
        the model must have a unique id or null id
        EXAMPLE
            movie = Movie(title=req_title, release_date=req_rel_date)
            movie.insert()
    '''

    def __init__(self, title, release_year):
        self.title = title
        #self.release_date = release_date
        self.release_year = release_year


    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a new model into a database
        the model must exist in the database
        EXAMPLE
            movie = Movie.query.filter(Movie.id == id).one_or_none()
            movie.delete()
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
        EXAMPLE
            movie = Movie.query.filter(Movie.id == id).one_or_none()
            movie.title = 'Whitesnow'
            movie.update()
    '''

    def update(self):
        db.session.commit()

    def __repr__(self):
        self_repr = {
            'id': self.id,
            'title': self.title,
            #'release_date': self.release_date     
            'release_year': self.release_year              
        }
        return json.dumps(self_repr)
        
    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            #'release_date': self.release_date    
            'release_year': self.release_year      
        } 
        
        
