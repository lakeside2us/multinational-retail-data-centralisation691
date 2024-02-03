--Task 1: Cast the column of the orders_table to the correct data types.
	
--Finding the maximum lengths.

SELECT 
	length
		(max(cast(card_number as Text))) 
	AS max_len	  
FROM 
	orders_table
GROUP BY 
	card_number
ORDER BY 
	max_len
DESC
LIMIT 
	1; 

SELECT 
	length
		(max(cast(store_code as Text)))
	AS max_len
FROM 
	orders_table
GROUP BY 
	store_code
ORDER BY
	max_len
DESC
LIMIT 
	1; 
	
SELECT 
	length
		(max(cast(product_code as Text)))
	AS max_len
FROM 
	orders_table
GROUP BY 
	product_code
ORDER BY 
	max_len
DESC
LIMIT 1;

--Updating the colums in the table

ALTER TABLE 
	orders_table
		ALTER COLUMN date_uuid TYPE UUID USING CAST(date_uuid as UUID),
		ALTER COLUMN user_uuid TYPE UUID USING CAST(user_uuid as UUID),
		ALTER COLUMN card_number TYPE VARCHAR(19),
		ALTER COLUMN store_code TYPE VARCHAR(12),
		ALTER COLUMN product_code TYPE VARCHAR(11),
		ALTER COLUMN product_quantity TYPE SMALLINT;

select * from orders_table;