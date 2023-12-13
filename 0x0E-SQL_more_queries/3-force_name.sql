-- Write a script that creates the table
-- force_name on your MySQL server.
SET @dbName = 'your_database';
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
SELECT 'Table force_name created or already exists' AS result;
