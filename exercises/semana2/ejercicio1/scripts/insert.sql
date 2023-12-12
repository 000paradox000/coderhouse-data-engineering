INSERT INTO Customers (CustomerID, FirstName, LastName, Email, Phone)
VALUES (1, 'John', 'Doe', 'john.doe@example.com', '1234567890');

INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount)
VALUES (1, 1, '2022-01-01', 100.00);

INSERT INTO OrderItems (OrderItemID, OrderID, ProductID, Quantity, Price)
VALUES (1, 1, 1, 2, 50.00);

INSERT INTO Products (ProductID, ProductName, Category, Price)
VALUES (1, 'Product A', 'Category A', 50.00);
