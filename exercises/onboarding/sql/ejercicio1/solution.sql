-- ============================================================================
-- 1.1 En la última reunión el equipo de marketing de tu compañía levanto la
-- idea de poder identificar si los ingenieros mayores de 30 años son los que
-- realmente están comprando más productos en las tiendas, es por esto que te
-- piden que con base en esta base de datos dada puedas dar respuesta a dos
-- preguntas críticas para el negocio

-- ============================================================================
-- General

-- All
SELECT COUNT(*) FROM calls;
SELECT COUNT(*) FROM customers;
SELECT COUNT(*) FROM agents;

-- Engineers
SELECT COUNT(*) FROM customers WHERE occupation LIKE 'Engineer%';

-- Calls for customer 839
SELECT COUNT(*) FROM calls WHERE customerid=839;

-- Not Engineers
SELECT COUNT(*) FROM customers WHERE occupation NOT LIKE 'Engineer%';

-- ============================================================================
-- a. Calcular las ventas totales y las llamadas totales realizadas a los
-- clientes de la profesión de ingeniería

SELECT
	COUNT(callid) AS total_calls,
	SUM(productsold) AS total_sales
FROM
	calls
WHERE
	customerid IN (
        SELECT customerid FROM customers WHERE occupation LIKE 'Engineer%'
    );


SELECT
	COUNT(*) as total_calls,
	SUM(productsold) as total_sales
FROM
	customers cu
JOIN
	calls ca ON ca.customerid = cu.customerid
WHERE
    occupation LIKE 'Engineer%';

-- ============================================================================
-- b. Generar otra consulta que calcule las mismas métricas para toda la
-- base de clientes.

SELECT
	COUNT(callid) AS total_calls,
	SUM(productsold) AS total_sales
FROM
	calls
WHERE
	customerid IN (
        SELECT customerid FROM customers WHERE occupation NOT LIKE 'Engineer%'
    );


SELECT
	COUNT(*) as total_calls,
	SUM(productsold) as total_sales
FROM
	customers cu
JOIN
	calls ca ON ca.customerid = cu.customerid
WHERE
    occupation NOT LIKE 'Engineer%';

-- ============================================================================
-- c. ¿Qué puedes concluir con respecto a la tasa de conversión entre los
-- clientes de ingeniería frente a la base de clientes en general?

SELECT
	CAST((SUM(productsold) * 100) AS DECIMAL) / COUNT(*) AS rate
FROM
	customers cu
JOIN
	calls ca ON ca.customerid = cu.customerid
WHERE
    occupation LIKE 'Engineer%';


SELECT
	CAST((SUM(productsold) * 100) AS DECIMAL) / COUNT(*) AS rate
FROM
	calls
WHERE
	customerid IN (
        SELECT customerid FROM customers WHERE occupation LIKE 'Engineer%'
    );


-- ============================================================================
-- d. ¿Valdría la pena invertir en publicidad en el segmento de clientes
-- que son ingenieros y mayores de 30 años?

SELECT
	COUNT(*) AS total_calls,
	SUM(productsold) AS total_sales
FROM
	customers cu
JOIN
	calls ca ON ca.customerid = cu.customerid
WHERE
    occupation LIKE 'Engineer%'
    AND
    age > 30;

SELECT
	COUNT(*) AS total_calls,
	SUM(productsold) AS total_sales
FROM
	customers cu
JOIN
	calls ca ON ca.customerid = cu.customerid
WHERE
    occupation LIKE 'Engineer%'
    AND
    age <= 30;