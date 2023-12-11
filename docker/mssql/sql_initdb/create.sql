CREATE DATABASE coderhouse;
GO

USE coderhouse;
GO

CREATE LOGIN coderhouse WITH PASSWORD = 'C0d3rhous3';
GO
CREATE USER coderhouse FOR LOGIN coderhouse;
GO

CREATE TABLE customers(
    customerid INT PRIMARY KEY,
    name VARCHAR(50),
    occupation VARCHAR(50),
    email VARCHAR(50),
    company VARCHAR(50),
    phonenumber VARCHAR(20),
    age INT
);
GO
GRANT SELECT, INSERT, UPDATE, DELETE ON customers TO coderhouse;
GO

CREATE TABLE agents(
    agentid INT PRIMARY KEY,
    name VARCHAR(50)
);
GO
GRANT SELECT, INSERT, UPDATE, DELETE ON agents TO coderhouse;
GO

CREATE TABLE calls(
    callid INT PRIMARY KEY,
    agentid INT,
    customerid INT,
    pickedup SMALLINT,
    duration INT,
    productsold SMALLINT
);
GO
GRANT SELECT, INSERT, UPDATE, DELETE ON calls TO coderhouse;
GO

BULK INSERT agents
FROM '/opt/data/csv/agents.csv'
WITH
(
    FIRSTROW = 2,
	FORMAT = 'CSV',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
	FIELDQUOTE = '"',
    TABLOCK
);
GO

BULK INSERT customers
FROM '/opt/data/csv/customers.csv'
WITH
(
    FIRSTROW = 2,
	FORMAT = 'CSV',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
	FIELDQUOTE = '"',
    TABLOCK
);

BULK INSERT calls
FROM '/opt/data/csv/calls.csv'
WITH
(
    FIRSTROW = 2,
	FORMAT = 'CSV',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
	FIELDQUOTE = '"',
    TABLOCK
);