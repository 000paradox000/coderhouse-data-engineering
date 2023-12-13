-- ============================================================================
-- Ejercicio 5
-- Escribir dos consultas:

-- Una que calcule las ventas totales y las llamadas totales realizadas a los
-- clientes de la profesión de ingeniería.

-- Otra que calcule las mismas métricas para toda la base de clientes.

SELECT
    SUM(calls.productsold) AS total_sales,
    COUNT(calls.callid) AS total_calls
FROM
    calls,
    customers
WHERE
    calls.customerid = customers.customerid
    AND
    UPPER(customers.occupation) LIKE '%ENGINEER%'

SELECT
    SUM(ca.productsold) AS total_sales,
    COUNT(*) AS total_calls
FROM
    customers cu
JOIN calls ca ON ca.customerid = cu.customerid
WHERE
    UPPER(cu.occupation) LIKE '%ENGINEER%'
