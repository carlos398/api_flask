from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PASSWORD']
host = os.environ['MYSQL_HOST']
db = os.environ['MYSQL_DB']

JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']

# flask secret key
SECRET_KEY = os.environ['SECRET_KEY']

DATABASE_CONECTION_URI = f'mysql://{user}:{password}@{host}/{db}'
