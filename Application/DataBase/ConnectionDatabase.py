import os
from dotenv import load_dotenv, find_dotenv
import psycopg2
from CheckerDB import ConnectDB_Checker

def ConnectionDB():
    """
    Simple connexion à la base de données avec check de connexion en amont
    """
    if ConnectDB_Checker()=="OK":
        load_dotenv(find_dotenv())                                                      
        conn = psycopg2.connect(                                                  
            user = os.getenv("DATABASE_USERNAME"),                                      
            password = os.getenv("DATABASE_PASSWORD"),                                  
            host = os.getenv("DATABASE_IP"),                                            
            port = os.getenv("DATABASE_PORT"),                                          
            database = os.getenv("DATABASE_NAME")
        )
        return conn
    else:
        print("ERROR CONNECTION")

print(ConnectionDB())