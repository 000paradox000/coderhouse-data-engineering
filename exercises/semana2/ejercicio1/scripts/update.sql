UPDATE Customers SET Phone = '9876543210' WHERE CustomerID = 1;

INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount) VALUES (2, 1, '2022-02-01', 200.00);

INSERT INTO OrderItems (OrderItemID, OrderID, ProductID, Quantity, Price) VALUES (2, 2, 1, 3, 50.00);
