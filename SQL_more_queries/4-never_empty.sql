-- Write a script that creates the table id_not_null on your MySQL server.
-- 4. ID can't be null
CREATE TABLE IF NOT EXISTS id_not_null (id INT NOT NULL DEFAULT 1, name VARCHAR (256));