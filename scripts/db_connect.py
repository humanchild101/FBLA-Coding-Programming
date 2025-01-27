#logging is a module that is used to log the messages to the console or file 
#Initially imported logging -- not used so far
import logging

import psycopg2 #will be used for connecting to db

# Connection parameters to the database
# Contains details of the database login -- will be used for connecting
db_params = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "password123",
    "port": 5432  
}


def get_connection():
    try:
        conn = psycopg2.connect(**db_params) #Connect to the database
        return conn
    except (Exception, psycopg2.Error) as error:
        print("Error connecting to database:", error)
        return None

        
def execute_query(query):
    try:
        conn = get_connection() # Connect to the database
        cursor = conn.cursor() #Cursor is used to navigate through the db
        cursor.execute(query) # For executing the SQL query statements
        result = cursor.fetchone() # To get the values from db and return those
        return result

    except (Exception, psycopg2.Error) as error: 
        print("Error connecting to database:", error)
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()



def insert_values(query):
    try:
        conn = get_connection() # Connect to the database
        cursor = conn.cursor() #Cursor is used to navigate through the db
        print(query)
        cursor.execute(query) # For executing the SQL query statements
        conn.commit()

    except (Exception, psycopg2.Error) as error: 
        raise Exception(error)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()


