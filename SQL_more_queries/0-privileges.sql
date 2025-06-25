-- a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server 

-- Create users if they don’t exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Show privileges
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';