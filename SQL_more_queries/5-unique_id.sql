-- Write a script that creates the table unique_id on your MySQL server.
-- 5. Unique ID
CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));