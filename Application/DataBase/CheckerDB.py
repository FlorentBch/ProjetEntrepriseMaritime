import os
from dotenv import load_dotenv, find_dotenv
import psycopg2
import sys

def ConnectDB_Checker():
    
    ValueResponse = "OK"
    
    load_dotenv(find_dotenv())                                                      
    try: 
        conn = psycopg2.connect(                                                  
            user = os.getenv("DATABASE_USERNAME"),                                      
            password = os.getenv("DATABASE_PASSWORD"),                                  
            host = os.getenv("DATABASE_IP"),                                            
            port = os.getenv("DATABASE_PORT"),                                          
            database = os.getenv("DATABASE_NAME")                             
        )
        conn.close()
    except psycopg2.Error as e:
        ValueResponse = e
        print(e)
        # sys.exit(1)

    # # Execute a SQL query
    # try:
    #     cur = conn.cursor()
    #     cur.execute('SELECT version()')
    # except psycopg2.Error as e:
    #     ValueResponse = e
    #     print(e)
    #     sys.exit(1)

    # # Fetch the results
    # try:
    #     rows = cur.fetchall()
    # except psycopg2.Error as e:
    #     ValueResponse = e
    #     print(e)
    #     sys.exit(1)

    # # Close the connection
    # try:
    #     conn.close()
    # except psycopg2.Error as e:
    #     ValueResponse = e
    #     print(e)
    #     sys.exit(1)

    return ValueResponse