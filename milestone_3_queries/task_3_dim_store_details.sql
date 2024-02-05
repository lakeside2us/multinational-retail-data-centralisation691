--Task 3: Update the dim_stores_detials table to the correct data types.
	
--Finding the maximum length.

SELECT 
	LENGTH(MAX(CAST(country_code AS Text)))
FROM 
	dim_store_details
GROUP BY 
	country_code
ORDER BY 
	LENGTH(MAX(CAST(country_code AS Text))) 
DESC
LIMIT 
	1; 
-- (2)

SELECT 
	LENGTH(MAX(CAST(store_code AS Text)))
FROM 
	dim_store_details
GROUP BY 
	store_code
ORDER BY 
	LENGTH(MAX(CAST(store_code AS Text))) desc
LIMIT 
	1; 
-- (12)


-- Updating the N/A values to NULL

UPDATE 
	dim_store_details 
SET 
	address = NULL
WHERE 
	address = 'N/A';
	

UPDATE 
	dim_store_details 
SET 
	longitude = NULL
WHERE 
	longitude = 'N/A';
	

UPDATE 
	dim_store_details 
SET 
	locality = NULL
WHERE 
	locality = 'N/A';
	

UPDATE 
	dim_store_details 
SET 
	lat = NULL
WHERE 
	lat = 'N/A';


-- Merging the lat with latitude

UPDATE 
	dim_store_details
SET 
	latitude = CONCAT(CAST(lat AS FLOAT), 
					  CAST(latitude AS FLOAT));


-- Dropping columns

ALTER TABLE 
	dim_store_details
DROP lat,
DROP level_0;


-- Casting the data types

ALTER TABLE 
	dim_store_details
		ALTER COLUMN longitude TYPE FLOAT USING CAST(longitude AS FLOAT),
		ALTER COLUMN locality TYPE VARCHAR(255),
		ALTER COLUMN store_code TYPE VARCHAR(12),
		ALTER COLUMN staff_numbers TYPE SMALLINT,
		ALTER COLUMN opening_date TYPE DATE USING CAST(opening_date AS DATE),
		ALTER COLUMN store_type TYPE VARCHAR(255),
		ALTER COLUMN country_code TYPE VARCHAR(2),
		ALTER COLUMN continent TYPE VARCHAR(255);




-- SELECT * FROM dim_store_details

	