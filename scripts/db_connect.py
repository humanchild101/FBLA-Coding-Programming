#logging is a module that is used to log the messages to the console or file.
import logging
import psycopg2 # type: ignore


# Connection parameters to the database
db_params = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "password123",
    "port": 5432  
}

try:
    # Connect to the database
    conn = psycopg2.connect(**db_params)

    # Create a cursor object
    #Cursor is an object used to interact with the database by executing SQL queries
    cursor = conn.cursor()

    # Execute a query
    cursor.execute("SELECT version();")

    # Fetch the result
    result = cursor.fetchone()

    # Print the result
    print(result)

except (Exception, psycopg2.Error) as error:
    print("Error connecting to database:", error)

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()

