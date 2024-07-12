-- Script to list Glam rock bands ranked by their longevity

-- Import the table dump first
-- $ cat metal_bands.sql | mysql -uroot -p holberton

SELECT 
    name AS band_name, 
    CASE 
        WHEN split IS NULL THEN 2022 - formed
        ELSE split - formed
    END AS lifespan
FROM 
    metal_bands
WHERE 
    main_style = 'Glam rock'
ORDER BY 
    lifespan DESC;

