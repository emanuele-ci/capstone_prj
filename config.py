#from dotenv import load_dotenv
#load_dotenv() 
import os 



#SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
#basedir = os.path.abspath(os.path.dirname(__file__))

#DB_NAME = os.environ.get("DB_NAME", 'capstone') 
#DB_NAME = 'capstone' 
#DB_USER=os.environ.get("DB_USER", 'postgres')
#DB_USER='postgres'
#DB_PASSWORD = os.environ.get("DB_PASSWORD", 'postgres')
#DB_PASSWORD = 'postgres'


class Config:
   # Enable debug mode.
   DEBUG = True

   SECRET_KEY = os.urandom(32)
   # Grabs the folder where the script runs.
   basedir = os.path.abspath(os.path.dirname(__file__))
   
   AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN') 
   ALGORITHMS = os.environ.get('ALGORITHMS') 
   API_AUDIENCE = os.environ.get('API_AUDIENCE')

   ASSISTANT_JWT = os.environ.get('ASSISTANT_JWT')
   PRODUCER_JWT = os.environ.get('PRODUCER_JWT')

   
   # Connect to the database
   
   
   # DATABASE URL
   #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost:5432/capstone'
   #SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}/{}'.format(DB_USER,DB_PASSWORD,'localhost:5432', DB_NAME)

   DATABASE_URL = os.environ.get('DATABASE_URL')
   
