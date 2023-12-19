-- Utilities
-- =======================================================================================================
-- DROP TABLE coderhouse_de_ari.public.eventos_apocalipticos;
-- select query_id, line_number, column_name, error_message from sys_load_error_detail order by query_id DESC;

-- 0. Crear base de datos
-- =======================================================================================================
CREATE DATABASE coderhouse_de_ari;


-- 1. Crear la tabla llamada “eventos_apocalipticos”
-- =======================================================================================================
CREATE TABLE "public"."eventos_apocalipticos"(
    id_evento INTEGER,
    nombre_evento VARCHAR(255),
    fecha_evento DATE,
    descripcion_evento VARCHAR(255)
 ) ENCODE AUTO;

-- 2. Insertar en la tabla del paso 1 los registros
-- =======================================================================================================
COPY coderhouse_de_ari.public.eventos_apocalipticos
FROM 's3://MYS3BUCKET/data.csv'
IAM_ROLE 'MYROLEARN'
FORMAT AS CSV DELIMITER ',' DATEFORMAT 'YYYY-MM-DD'
IGNOREHEADER 1
REGION AS 'us-east-1';

SELECT * FROM coderhouse_de_ari.public.eventos_apocalipticos;

-- 3. Crear la tabla “prediccion_fin_mundo”
-- =======================================================================================================
CREATE TABLE coderhouse_de_ari.public.prediccion_fin_mundo (
    id_evento INTEGER,
    nombre_evento VARCHAR(255),
    fecha_evento DATE,
    descripcion_evento VARCHAR(255)
 ) ENCODE AUTO;


-- 4. Generar una query que a partir de la tabla de origen permita rellenar la tabla destino
-- =======================================================================================================
INSERT INTO coderhouse_de_ari.public.prediccion_fin_mundo (
    SELECT * FROM coderhouse_de_ari.public.eventos_apocalipticos
);

SELECT * FROM coderhouse_de_ari.public.prediccion_fin_mundo;

-- 5. Además deberás responder está pregunta: ¿Cuál es el número promedio de días restantes hasta los
--    eventos apocalípticos en cada década, y cuántos eventos comienzan con la letra 'D' y la letra 'A'
--    en cada década?.
-- =======================================================================================================
SELECT * FROM coderhouse_de_ari.public.prediccion_fin_mundo ORDER BY fecha_evento DESC;

SELECT
    (EXTRACT(YEAR FROM fecha_evento) - EXTRACT(YEAR FROM fecha_evento) % 10)::TEXT || '-' || (EXTRACT(YEAR FROM fecha_evento) - EXTRACT(YEAR FROM fecha_evento) % 10 + 9)::TEXT AS decade,
    COUNT(*) AS number_of_events,
    AVG((fecha_evento - CURRENT_DATE)::INTEGER) AS average_days,
    SUM(CASE WHEN nombre_evento LIKE 'D%' THEN 1 ELSE 0 END) AS D_events,
    SUM(CASE WHEN nombre_evento LIKE 'A%' THEN 1 ELSE 0 END) AS A_events
FROM eventos_apocalipticos
GROUP BY decade
ORDER BY decade ASC;
