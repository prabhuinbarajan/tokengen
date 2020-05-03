CREATE DATABASE IF NOT EXISTS tokendb;
GRANT ALL PRIVILEGES ON tokendb.* TO 'txnuser'@'%';
flush privileges;
USE tokendb;
