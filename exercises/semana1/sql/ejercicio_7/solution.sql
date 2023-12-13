-- ============================================================================
-- Ejercicio 7
-- Escribir una consulta que extraiga dos métricas del desempeño de los
-- agentes de ventas que le interesan a su empresa:

-- Para cada agente, cuántos segundos en promedio les toma vender un producto
-- cuando tienen éxito.

-- Para cada agente, cuántos segundos en promedio permanecen en el teléfono
-- antes de darse por vencidos cuando no tienen éxito.

SELECT
ag.name,
SUM(CASE WHEN ca.productsold = 0 THEN ca.duration ELSE 0 END) / SUM(CASE WHEN ca.productsold = 0 THEN 1 ELSE 0 END) AS avg_when_not_sold,
SUM(CASE WHEN ca.productsold >= 1 THEN ca.duration ELSE 0 END) / SUM(CASE WHEN ca.productsold >= 1 THEN 1 ELSE 0 END) AS avg_when_sold
FROM calls ca
JOIN agents ag ON ca.agentid = ag.agentid
GROUP BY ag.name
ORDER BY 1;
