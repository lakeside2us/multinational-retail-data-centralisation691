--Task 1: Cast the column of the orders_table to the correct data types.
	
--Finding the maximum lengths.

SELECT 
	LENGTH(MAX(CAST(card_number AS Text)))   
FROM 
	orders_table
GROUP BY 
	card_number
ORDER BY 
	LENGTH(MAX(CAST(card_number AS Text)))
DESC
LIMIT 
	1; 
-- (19)

SELECT 
	LENGTH(MAX(CAST(store_code AS Text)))
FROM 
	orders_table
GROUP BY 
	store_code
ORDER BY
	LENGTH(MAX(CAST(store_code AS Text)))
DESC
LIMIT 
	1;
-- (12)
	
SELECT 
	LENGTH(MAX(CAST(product_code AS Text)))
FROM 
	orders_table
GROUP BY 
	product_code
ORDER BY 
	LENGTH(MAX(CAST(product_code AS Text)))
DESC
LIMIT
	1;
-- (11)

--Updating the colums in the table

ALTER TABLE 
	orders_table
		ALTER COLUMN date_uuid TYPE UUID USING CAST(date_uuid AS UUID),
		ALTER COLUMN user_uuid TYPE UUID USING CAST(user_uuid AS UUID),
		ALTER COLUMN card_number TYPE VARCHAR(19),
		ALTER COLUMN store_code TYPE VARCHAR(12),
		ALTER COLUMN product_code TYPE VARCHAR(11),
		ALTER COLUMN product_quantity TYPE SMALLINT;

-- SELECT * FROM orders_table;