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