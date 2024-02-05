--Task 5: Update the dim_products table.
	
-- Renaming the removed column to still_available.

ALTER TABLE 
	dim_products
RENAME COLUMN 
	removed TO still_available;

-- Maximun length of EAN column

SELECT 
	LENGTH(MAX(CAST("EAN" AS TEXT)))
FROM 
	dim_products
GROUP BY 
	"EAN"
ORDER BY 
	LENGTH(MAX(CAST("EAN" AS TEXT)))
DESC
LIMIT
	1;
-- (17)


-- Maximun length of product_code column

SELECT 
	LENGTH(MAX(CAST(product_code AS TEXT)))
FROM 
	dim_products
GROUP BY 
	product_code
ORDER BY 
	LENGTH(MAX(CAST(product_code AS TEXT))) 
DESC
LIMIT
	1;
-- (11)

-- Maximun length of weight_class column

SELECT 
	LENGTH(MAX(CAST(weight_class AS TEXT)))
FROM 
	dim_products
GROUP BY 
	weight_class
ORDER BY 
	LENGTH(MAX(CAST(weight_class AS TEXT)))
DESC
LIMIT
	1;
-- (14)

-- Alter the data type

ALTER TABLE 
	dim_products
		ALTER COLUMN product_price TYPE FLOAT USING CAST(product_price AS FLOAT),
    	ALTER COLUMN weight TYPE FLOAT USING CAST(weight AS FLOAT),
    	ALTER COLUMN "EAN" TYPE VARCHAR(17),
    	ALTER COLUMN product_code TYPE VARCHAR(11),
    	ALTER COLUMN date_added TYPE DATE USING CAST(date_added AS DATE),
    	ALTER COLUMN uuid TYPE UUID USING uuid::UUID,
    	ALTER COLUMN still_available TYPE BOOL USING(still_available = 'Still_avaliable'),
    	ALTER COLUMN weight_class TYPE VARCHAR(14);






-- SELECT * FROM dim_products
	