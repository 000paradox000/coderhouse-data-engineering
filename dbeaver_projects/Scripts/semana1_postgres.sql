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