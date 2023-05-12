CREATE USER IF NOT EXISTS `bd2-23L-z09`@`localhost` IDENTIFIED WITH caching_sha2_password BY 'bd2';
ALTER USER 'bd2-23L-z09'@'localhost' REQUIRE NONE
    WITH MAX_QUERIES_PER_HOUR 0
    MAX_CONNECTIONS_PER_HOUR 0
    MAX_UPDATES_PER_HOUR 0
    MAX_USER_CONNECTIONS 0;
CREATE DATABASE IF NOT EXISTS `bd2-23L-z09`;
GRANT ALL PRIVILEGES ON `bd2-23L-z09`.* TO 'bd2-23L-z09'@'localhost';
GRANT SHUTDOWN ON *.* TO 'bd2-23L-z09'@'localhost';
