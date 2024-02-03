--Task 7: Update the dim_card_details table.

-- Maximun length of card_number column

SELECT 
	length(CAST(card_number AS TEXT))
FROM 
	dim_card_details
GROUP BY 
	card_number
ORDER BY 
	length(CAST(card_number AS TEXT))
DESC
LIMIT
1;
--19


-- Maximun expiry_date of year column

SELECT 
	length(CAST(expiry_date AS TEXT))
FROM 
	dim_card_details
GROUP BY 
	expiry_date
ORDER BY 
	length(CAST(expiry_date AS TEXT))
DESC
LIMIT
1;
--5

-- Alter the data types

ALTER TABLE 
	dim_card_details
		ALTER COLUMN card_number TYPE VARCHAR(19),
    	ALTER COLUMN expiry_date TYPE VARCHAR(5),
    	ALTER COLUMN date_payment_confirmed TYPE DATE USING CAST(date_payment_confirmed AS DATE);


-- SELECT * from dim_card_details
	