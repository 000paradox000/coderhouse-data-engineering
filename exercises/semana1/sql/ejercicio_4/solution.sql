-- ============================================================================
-- Ejercicio 4
-- Escribir una consulta que devuelva todas las
-- llamadas realizadas a clientes de la profesión de ingeniería y muestre
-- si son mayores o menores de 30, así como si terminaron comprando el
-- producto de esa llamada.

SELECT
    calls.callid AS call_id,
	calls.customerid AS customer_id,
    customers.name AS customer_name,
    CASE WHEN customers.age >= 30 THEN 'SI' ELSE 'NO' END AS mayor30,
    CASE WHEN calls.productsold >= 1 THEN 'SI' ELSE 'NO' END AS compro
FROM
    calls,
    customers
WHERE
    calls.customerid = customers.customerid
    AND
    UPPER(customers.occupation) LIKE '%ENGINEER%'
ORDER BY customers.name DESC;

SELECT
    ca.callid AS call_id,
    cu.customerid AS customer_name,
    cu.name AS customer_name,
    CASE WHEN cu.age >= 30 THEN 'SI' ELSE 'NO' END AS mayor30,
    CASE WHEN ca.productsold >= 1 THEN 'SI' ELSE 'NO' END AS compro
FROM
    customers cu
JOIN calls ca ON ca.customerid = cu.customerid
WHERE
    UPPER(cu.occupation) LIKE '%ENGINEER%'
ORDER BY cu.name DESC;
