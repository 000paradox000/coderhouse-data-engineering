-- Escribir una consulta que extraiga dos métricas del desempeño de los
-- agentes de ventas que le interesan a su empresa:

-- Para cada agente, cuántos segundos en promedio les toma vender un producto
-- cuando tienen éxito.

-- Para cada agente, cuántos segundos en promedio permanecen en el teléfono
-- antes de darse por vencidos cuando no tienen éxito.

SELECT
    agents.name AS AgentName,
    CASE WHEN calls.productsold = 1 THEN AVG(calls.duration) ELSE 0 END AS time_to_sell,
    CASE WHEN calls.productsold = 0 THEN AVG(calls.duration) ELSE 0 END AS time_lost
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
    AgentName ASC;

-- ============================================================================

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
