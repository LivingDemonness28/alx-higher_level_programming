-- Write a script that creates the table
-- unique_id on your MySQL server.
SET @dbName = 'your_database';
CREATE TABLE IF NOT EXISTS `your_database`.`unique_id` (`id` INT DEFAULT 1 UNIQUE, `name` VARCHAR(256));
SELECT 'Table unique_id created or already exists' AS result;
