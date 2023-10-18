-- create db
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- select a db
USE hbtn_0d_usa;

-- create table
  CREATE TABLE IF NOT EXISTS cities(
      id INT PRIMARY KEY AUTO_INCREMENT,
state_id INT NOT NULL REFERENCES states(id),
    name VARCHAR(256) NOT NULL
    );

