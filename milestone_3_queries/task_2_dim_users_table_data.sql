--Task 2: Cast the column of the dim_users_table to the correct data types.
	
--Finding the maximum lengths.

SELECT 
	length
		(max(cast(country_code as Text))) 
	AS max_len
FROM 
	dim_users
GROUP BY 
	country_code
ORDER BY 
	max_len 
DESC
LIMIT 
2; 

--Updating the colums in the table

ALTER TABLE 
	dim_users
    	ALTER COLUMN first_name TYPE VARCHAR(255),
    	ALTER COLUMN last_name TYPE VARCHAR(255),
    	ALTER COLUMN date_of_birth TYPE DATE using (date_of_birth::DATE),
    	ALTER COLUMN country_code TYPE VARCHAR(3),
    	ALTER COLUMN user_uuid TYPE UUID USING user_uuid::uuid,
    	ALTER COLUMN join_date TYPE DATE;
	
-- select * from dim_users