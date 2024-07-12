-- Script to rank country origins of bands by the number of non-unique fans

-- Import the table dump first
-- $ cat metal_bands.sql | mysql -uroot -p holberton

-- Query to rank country origins by number of non-unique fans
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;

