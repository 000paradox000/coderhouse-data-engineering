-- Extraer agentes cuyo nombre empieza por M o termina en O.
SELECT
    *
FROM
    agents
WHERE
    UPPER(name) LIKE 'M%'
    OR
    UPPER(name) LIKE '%O';