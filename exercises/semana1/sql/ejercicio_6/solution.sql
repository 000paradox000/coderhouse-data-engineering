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
    MIN(calls.duration) AS shortest_call,
    MAX(calls.duration) AS longest_call,
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

SELECT
    ag.name AS agent_name,
    COUNT(*) AS total_calls,
    MIN(ca.duration) AS shortest_call,
    MAX(ca.duration) AS longest_call,
    AVG(ca.duration) AS avg_duration,
    SUM(ca.productsold) AS total_sales
FROM
    calls ca
JOIN agents ag ON ca.agentid = ag.agentid
WHERE
    ca.pickedup = 1
GROUP BY
    ag.name
ORDER BY
    ag.name ASC;
