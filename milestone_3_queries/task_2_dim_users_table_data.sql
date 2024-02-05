--Task 2: Cast the column of the dim_users_table to the correct data types.
	
--Finding the maximum lengths.

SELECT 
	LENGTH(MAX(CAST(country_code AS Text))) 
FROM 
	dim_users
GROUP BY 
	country_code
ORDER BY 
	LENGTH(MAX(CAST(country_code AS Text)))
DESC
LIMIT 
	1;
-- (3)

--Updating the colums in the table

ALTER TABLE 
	dim_users
    	ALTER COLUMN first_name TYPE VARCHAR(255),
    	ALTER COLUMN last_name TYPE VARCHAR(255),
    	ALTER COLUMN date_of_birth TYPE DATE using (date_of_birth::DATE),
    	ALTER COLUMN country_code TYPE VARCHAR(3),
    	ALTER COLUMN user_uuid TYPE UUID USING user_uuid::uuid,
    	ALTER COLUMN join_date TYPE DATE;
	
-- SELECT * FROM dim_users