-- POSTGRES DATABASE CREATION SCRIPT

-- docker exec -it some-postgres /bin/bash
-- psql -h localhost -p5432 -U postgres

create database simple_logger;
-- \c logger

create schema logger;

create table logger.main (
    symptom_id serial primary key,
    date date not null,
    time time not null,
    symptom varchar(255) not null,
    pain_score int;

-- varchar(255) is the max length of a string in MySQL, example:
-- "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur quis est vel elit faucibus pulvinar. Sed suscipit, mi et eleifend laoreet, nisl libero bibendum justo, vitae scelerisque eros metus sit amet justo. Lorem."

-- To add a foreign key to a table post-creation, use the following syntax:
-- ALTER TABLE symptom_log.symptom_collection
-- ADD COLUMN user_id int,
-- ADD CONSTRAINT fk_symptom_collection_user_id FOREIGN KEY (user_id) REFERENCES user_data(user_id);