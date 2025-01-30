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


CREATE TABLE IF NOT EXISTS transactions
(
    id SERIAL PRIMARY KEY,
    income_or_expense VARCHAR(45) NOT NULL,
    source VARCHAR(45) NOT NULL,
    date_of_transaction date NOT NULL,
    need_or_want VARCHAR(5) NOT NULL,
    note VARCHAR(150) NOT NULL,
	  amount decimal(10,2),
    user_id integer,
    CONSTRAINT fk_user_id FOREIGN KEY (user_id)
        REFERENCES users (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

insert into transactions (income_or_expense,source,date_of_transaction,need_or_want,note,amount,user_id) 
values ('income','Salary',TO_DATE('2024-02-20', 'YYYY-MM-dd'),'need','salary',3000.00,32)



