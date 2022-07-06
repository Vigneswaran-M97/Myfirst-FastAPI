import os
from pymongo import MongoClient 
from dotenv import load_dotenv

load_dotenv(dotenv_path='./.env')
DB = os.getenv("DB")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

connection_string = f"{DB}://{DB_HOST}:{DB_PORT}"
con = MongoClient(connection_string)
