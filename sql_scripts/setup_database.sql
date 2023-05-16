USE `bd2-23L-z09`;

CREATE TABLE CLIENTS (
    client_ID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    surname VARCHAR(40) NOT NULL,
    pesel CHAR(11) UNIQUE,
    gender CHAR(1) NOT NULL,
    phone_number VARCHAR(15),
    email_address VARCHAR(40),
    CONSTRAINT contact CHECK(phone_number IS NOT NULL OR email_address IS NOT NULL)
);
