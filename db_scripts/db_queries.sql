-- Creating a table to hold all the user details of the application
-- The table will be created in the existing database and schema provided by postgreSQL
CREATE TABLE IF NOT EXISTS users (
  user_id SERIAL PRIMARY KEY,
  username VARCHAR(45) NOT NULL UNIQUE,
  user_password VARCHAR(45) NOT NULL,
  email VARCHAR(45) UNIQUE,
  first_name VARCHAR(45) NOT NULL,
  last_name VARCHAR(45) NOT NULL);

SELECT * FROM users;

