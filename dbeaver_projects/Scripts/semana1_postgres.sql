-- ============================================================================
-- Ejercicio 1
-- Extraer agentes cuyo nombre empieza por M o termina en O.

SELECT
    *
FROM
    agents
WHERE
    UPPER(name) LIKE 'M%'
    OR
    UPPER(name) LIKE '%O';
    
-- ============================================================================
-- Ejercicio 2
-- Escribir una consulta que produzca una lista, en orden alfabético, de
-- todas las distintas ocupaciones en la tabla Customer que contengan la
-- palabra "Engineer".

SELECT
    DISTINCT occupation
FROM
    customers
WHERE
    UPPER(occupation) LIKE '%ENGINEER%'
ORDER BY occupation ASC;

-- ============================================================================
-- Ejercicio 3
-- Escribir una consulta que devuelva el ID del cliente, su nombre y una
-- columna nueva llamada “Mayor30” que contenga "Sí" si el cliente tiene más
-- de 30 años y "No" en caso contrario.

SELECT
    customerid,
    name,
    CASE WHEN age > 30 THEN 'SI' ELSE 'NO' END as mayor30
FROM
    customers;
    
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
    CASE WHEN productsold >= 1 THEN 'SI' ELSE 'NO' END AS compro
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
