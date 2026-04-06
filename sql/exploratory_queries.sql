
-- promedio de impuestos por año
SELECT YEAR, AVG(PAGADO) as avg_pagado
FROM imports
GROUP BY YEAR;

-- cantidad de inspecciones
SELECT INSPECCION, COUNT(*) as total
FROM imports
GROUP BY INSPECCION;

-- top aduanas con más inspecciones
SELECT CODIGO_ADUANA, COUNT(*) as total
FROM imports
WHERE INSPECCION = 'INSPECCION'
GROUP BY CODIGO_ADUANA
ORDER BY total DESC;