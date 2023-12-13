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
