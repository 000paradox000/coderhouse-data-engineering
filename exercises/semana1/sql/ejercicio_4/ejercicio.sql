-- ============================================================================
-- Ejercicio 4
-- Escribir una consulta que devuelva todas las
-- llamadas realizadas a clientes de la profesión de ingeniería y muestre
-- si son mayores o menores de 30, así como si terminaron comprando el
-- producto de esa llamada.

SELECT
    calls.callid,
	calls.customerid,
    customers.name AS customer_name,
    agents.name AS agent_name,
    CASE WHEN customers.age > 30 THEN 'SI' ELSE 'NO' END AS mayor30,
    CASE WHEN productsold = 1 THEN 'SI' ELSE 'NO' END AS compro
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
