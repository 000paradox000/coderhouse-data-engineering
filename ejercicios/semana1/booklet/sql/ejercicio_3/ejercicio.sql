-- Escribir una consulta que devuelva el ID del cliente, su nombre y una
-- columna nueva llamada “Mayor30” que contenga "Sí" si el cliente tiene más
-- de 30 años y "No" en caso contrario.

SELECT
    customerid,
    name,
    CASE WHEN age > 30 THEN 'SI' ELSE 'NO' END as mayor40
FROM
    customers;