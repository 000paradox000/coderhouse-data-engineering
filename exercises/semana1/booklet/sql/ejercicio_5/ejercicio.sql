-- Escribir dos consultas:

-- Una que calcule las ventas totales y las llamadas totales realizadas a los
-- clientes de la profesión de ingeniería.

-- Otra que calcule las mismas métricas para toda la base de clientes.

SELECT
    customers.name,
    SUM(calls.productsold),
    COUNT(calls.callid)
FROM
    calls,
    customers
WHERE
    calls.customerid = customers.customerid
    AND
    UPPER(customers.occupation) LIKE '%ENGINEER%'
GROUP BY customers.name;

SELECT
    customers.name,
    SUM(calls.productsold),
    COUNT(calls.callid)
FROM
    calls,
    customers
WHERE
    calls.customerid = customers.customerid
GROUP BY customers.name;
