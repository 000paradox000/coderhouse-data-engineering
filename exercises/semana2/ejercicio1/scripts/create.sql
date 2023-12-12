CREATE TABLE IF NOT EXISTS Customers(
    CustomerID INT PRIMARY KEY,
    FirstName  VARCHAR(50),
    LastName   VARCHAR(50),
    Email      VARCHAR(100),
    Phone      VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS Orders(
    OrderID     INT PRIMARY KEY,
    CustomerID  INT,
    OrderDate   DATE,
    TotalAmount DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID)
);

CREATE TABLE IF NOT EXISTS OrderItems(
    OrderItemID INT PRIMARY KEY,
    OrderID     INT,
    ProductID   INT,
    Quantity    INT,
    Price       DECIMAL(10, 2),
    FOREIGN KEY (OrderID) REFERENCES Orders (OrderID)
);

CREATE TABLE IF NOT EXISTS Products(
    ProductID   INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Category    VARCHAR(50),
    Price       DECIMAL(10, 2)
);
