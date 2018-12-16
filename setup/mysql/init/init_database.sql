-- -----------------------------------------------------
-- create user
-- -----------------------------------------------------
DROP USER IF EXISTS 'admin';
CREATE USER `admin`@`%` IDENTIFIED BY 'admin';

-- -----------------------------------------------------
-- grant privileges
-- -----------------------------------------------------
GRANT ALL PRIVILEGES ON *.* TO `admin`@`%`;

-----------------------------------------------------
-- create schema
-----------------------------------------------------
DROP SCHEMA IF EXISTS `sandbox`;
CREATE SCHEMA `sandbox`;
