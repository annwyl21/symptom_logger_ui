-- POSTGRES DATABASE CREATION SCRIPT

-- docker exec -it some-postgres /bin/bash
-- psql -h localhost -p5432 -U postgres

create database simple_logger;
-- \c simple_logger

CREATE SCHEMA IF NOT EXISTS my_log;

CREATE TABLE my_log.main (
    symptom_id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    time TIME NOT NULL,
    symptom VARCHAR(255) NOT NULL,
    pain_score INT
);

-- varchar(255) is the max length of a string in MySQL, example:
-- "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur quis est vel elit faucibus pulvinar. Sed suscipit, mi et eleifend laoreet, nisl libero bibendum justo, vitae scelerisque eros metus sit amet justo. Lorem."

-- To add a foreign key to a table post-creation, use the following syntax:
-- ALTER TABLE symptom_log.symptom_collection
-- ADD COLUMN user_id int,
-- ADD CONSTRAINT fk_symptom_collection_user_id FOREIGN KEY (user_id) REFERENCES user_data(user_id);