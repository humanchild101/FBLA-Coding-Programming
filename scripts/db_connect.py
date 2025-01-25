#logging is a module that is used to log the messages to the console or file.
import logging
import psycopg2

# Connection parameters to the database

db_params = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "password123",
    "port": 5432  
}


def get_connection():
    try:
        # Connect to the database
        conn = psycopg2.connect(**db_params)
        return conn
    except (Exception, psycopg2.Error) as error:
        print("Error connecting to database:", error)
        return None

        
def execute_query(query):
    try:
        # Connect to the database
        conn = get_connection()

        # Create a cursor object
        cursor = conn.cursor()

        # Execute a query
        cursor.execute(query)

        # Fetch the result
        result = cursor.fetchone()

        # return the result
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
