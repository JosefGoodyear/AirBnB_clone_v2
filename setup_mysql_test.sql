-- create A database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create user hbnb_test ans set password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant all privileges for hbnb_test
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
-- grant select privileges
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
