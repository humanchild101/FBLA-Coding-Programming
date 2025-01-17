#logging is a module that is used to log the messages to the console or file.
import logging
import psycopg2 # type: ignore

#db_connect is a class that is used to connect the database to the program and execute query.
class db_connect:
    #get_connection is a method that is used to get the db connection.
    def get_connection(self, connection_string):
        psycopg2.connect()
        return "Connection object"