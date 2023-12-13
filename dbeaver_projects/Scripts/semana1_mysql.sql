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
    CASE WHEN age >= 30 THEN 'SI' ELSE 'NO' END as mayor30
FROM
    customers;
    
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

-- ============================================================================
-- Ejercicio 6
-- Escribir una consulta que devuelva

-- Para cada agente: el nombre del agente, la cantidad de llamadas, las
-- llamadas más largas y más cortas, la duración promedio de las llamadas y la
-- cantidad total de productos vendidos.

-- Nombra las columnas: AgentName, NCalls, Shortest, Longest, AvgDuration y
-- TotalSales

-- Luego ordenar la tabla por: AgentName en orden alfabético.
-- Consejo: Asegurarse de incluir la cláusula WHERE PickedUp = 1 para calcular
-- solo el promedio de todas las llamadas que fueron atendidas (de lo
-- contrario ¡todas las duraciones mínimas serán 0!)

SELECT
    agents.name AS agent_name,
    COUNT(calls.callid) AS total_calls,
    MAX(calls.duration) AS shortest_call,
    MIN(calls.duration) AS longest_call,
    AVG(calls.duration) AS avg_duration,
    SUM(calls.productsold) AS total_sales
FROM
    calls,
    agents
WHERE
    calls.agentid = agents.agentid
    AND
    calls.pickedup = 1
GROUP BY
    agents.name
ORDER BY
    agent_name ASC;

-- ============================================================================
-- Ejercicio 7
-- Escribir una consulta que extraiga dos métricas del desempeño de los
-- agentes de ventas que le interesan a su empresa:

-- Para cada agente, cuántos segundos en promedio les toma vender un producto
-- cuando tienen éxito.

-- Para cada agente, cuántos segundos en promedio permanecen en el teléfono
-- antes de darse por vencidos cuando no tienen éxito.

SELECT
    a.name,
    SUM(
        CASE
            WHEN productsold = 0 THEN duration
            ELSE 0
        END
    )
    /
    SUM(
        CASE
            WHEN productsold = 0 THEN 1
            ELSE 0
        END
    ) AS avgWhenNotSold,
    SUM(
        CASE
            WHEN productsold = 1 THEN duration
            ELSE 0
        END
    )
    /
    SUM(
        CASE
            WHEN productsold = 1 THEN 1
            ELSE 0
        END
    ) AS avgWhenSold
    FROM
        calls c
    JOIN
        agents a
    ON
        c.agentid = a.agentid
    GROUP BY
        a.name
    ORDER BY
        1;
   