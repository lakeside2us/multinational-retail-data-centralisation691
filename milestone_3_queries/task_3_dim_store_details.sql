--Task 3: Update the dim_stores_detials table to the correct data types.
	
--Finding the maximum length.

SELECT 
	length
		(CAST(store_code AS TEXT))
	AS max_len
FROM 
	dim_store_details
GROUP BY 
	store_code
ORDER BY
	max_len	
DESC
LIMIT 
	1;
--12


SELECT 
	length
		(CAST(country_code AS TEXT))
	AS max_len
FROM 
	dim_store_details
GROUP BY 
	country_code
ORDER BY
	max_len
DESC
LIMIT 
	1;
--2

--Updating N/A to NULL

UPDATE 
	dim_store_details
SET 
	address = NULL
WHERE 
	address = 'N/A';
	
--

UPDATE 
	dim_store_details
SET 
	longitude = NULL
WHERE 
	longitude = 'N/A';
	
--
UPDATE 
	dim_store_details
SET 
	locality = NULL
WHERE 
	locality = 'N/A';

--Updating the data type

ALTER TABLE 
	dim_store_details
		ALTER COLUMN longitude TYPE FLOAT USING CAST(longitude AS FLOAT),
    	ALTER COLUMN locality TYPE VARCHAR(255),
    	ALTER COLUMN store_code TYPE VARCHAR(12),
    	ALTER COLUMN staff_numbers TYPE SMALLINT,
    	ALTER COLUMN opening_date TYPE DATE USING CAST(opening_date AS DATE),
    	ALTER COLUMN store_type TYPE VARCHAR(255),
    	ALTER COLUMN latitude TYPE FLOAT USING CAST(latitude AS FLOAT),
    	ALTER COLUMN country_code TYPE VARCHAR(2),
    	ALTER COLUMN continent TYPE VARCHAR(255);






-- SELECT * from dim_store_details

	