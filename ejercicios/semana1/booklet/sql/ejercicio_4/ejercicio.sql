-- Escribir una consulta que devuelva todas las
-- llamadas realizadas a clientes de la profesión de ingeniería y muestre
-- si son mayores o menores de 30, así como si terminaron comprando el
-- producto de esa llamada.

SELECT
    calls.callid,
    agents.name,
    customers.name,
    CASE WHEN customers.age > 30 THEN 'SI' ELSE 'NO' END as mayor30,
    CASE WHEN productsold = 1 THEN 'SI' ELSE 'NO' END as compro
FROM
    calls,
    customers,
    agents
WHERE
    calls.customerid = customers.customerid
    AND
    agents.agentid = calls.agentid
    AND
    UPPER(customers.occupation) LIKE '%ENGINEER%';
