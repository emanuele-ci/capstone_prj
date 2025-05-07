#from dotenv import load_dotenv
#load_dotenv() 
import os 



SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

#DB_NAME = os.environ.get("DB_NAME", 'capstone') 
DB_NAME = 'capstone' 
#DB_USER=os.environ.get("DB_USER", 'postgres')
DB_USER='postgres'
#DB_PASSWORD = os.environ.get("DB_PASSWORD", 'postgres')
DB_PASSWORD = 'postgres'



class Config:
   # Enable debug mode.
   DEBUG = True
   
   # Connect to the database
   
   
   # DATABASE URL
   #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost:5432/capstone'
   SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}/{}'.format(DB_USER,DB_PASSWORD,'localhost:5432', DB_NAME)
   