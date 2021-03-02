-- Script that creates the database hbtn_0d_usa and
-- the table cities (in the database hbtn_0d_usa) on your MySQL server.
-- cities description:
--  -id INT unique, auto generated, cant be null and is a primary key.
--  -state_id INT, cant be null and must be a FOREIGN KEY that references to id of the states table.
--  -name VARCHAR(256) cant be null.
-- If the database hbtn_0d_usa already exists, your script should not fail.
-- If the table cities already exists, your script should not fail.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
    id INT PRIMARY KEY UNIQUE AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id)
);
