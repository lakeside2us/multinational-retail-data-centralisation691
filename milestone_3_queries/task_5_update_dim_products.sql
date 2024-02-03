--Task 5: Update the dim_products table.
	
-- Rename the removed column to still_available.

ALTER TABLE 
	dim_products
RENAME COLUMN 
	removed to still_available;

-- Maximun length of EAN column

SELECT 
	length(CAST("EAN" AS TEXT))
FROM 
	dim_products
GROUP BY 
	"EAN"
ORDER BY 
	length(CAST("EAN" AS TEXT)) 
DESC
LIMIT
1;
--17


-- Maximun length of product_code column

SELECT 
	length(CAST(product_code AS TEXT))
FROM 
	dim_products
GROUP BY 
	product_code
ORDER BY 
	length(CAST(product_code AS TEXT)) 
DESC
LIMIT
1;
--11

-- Maximun length of weight_class column

SELECT 
	length(CAST(weight_class AS TEXT))
FROM 
	dim_products
GROUP BY 
	weight_class
ORDER BY 
	length(CAST(weight_class AS TEXT)) 
DESC
LIMIT
1;
--14

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






-- SELECT * from dim_products
	