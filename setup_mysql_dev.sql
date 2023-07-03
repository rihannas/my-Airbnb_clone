-- create database

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- set PRIVILEGES
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_dev'@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';