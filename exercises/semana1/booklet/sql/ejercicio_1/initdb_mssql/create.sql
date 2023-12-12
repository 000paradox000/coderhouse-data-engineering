USE master;

CREATE DATABASE coderhouse;
USE DATABASE coderhouse;

CREATE LOGIN coderhouse WITH PASSWORD = 'coderhouse';
CREATE USER coderhouse FOR LOGIN coderhouse;
ALTER ROLE db_owner ADD MEMBER coderhouse;

CREATE TABLE IF NOT EXISTS customers(
    customerid INT PRIMARY KEY,
    name VARCHAR(50),
    occupation VARCHAR(50),
    email VARCHAR(50),
    company VARCHAR(50),
    phonenumber VARCHAR(20),
    age INT
);

CREATE TABLE IF NOT EXISTS agents(
    agentid INT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS calls(
    callid INT PRIMARY KEY,
    agentid INT,
    customerid INT,
    pickedup SMALLINT,
    duration INT,
    productsold SMALLINT
);

-- BULK INSERT calls
-- FROM 'C:\Users\Ariel Calzada\instances\github.com\000paradox000\000paradox000\coderhouse-data-engineering\ejercicios\semana1\booklet\sql\ejercicio_1\csv\calls.csv'
-- WITH
-- (
--     FIRSTROW = 2,
-- 	FORMAT = 'CSV',
--     FIELDTERMINATOR = ',',
--     ROWTERMINATOR = '0x0a',
-- 	FIELDQUOTE = '"',
--     TABLOCK
-- )