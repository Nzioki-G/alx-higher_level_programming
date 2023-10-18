-- create db
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- 'cd' into db,, maybe not necessary
USE hbtn_0d_usa;

-- create table.. note I don't use UNIQUE or DEFAULT
-- they re coverd in PK and AUTO_INC resp.
CREATE TABLE IF NOT EXISTS states(
    id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(256) NOT NULL
);

