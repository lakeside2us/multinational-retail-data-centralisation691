--Task 4: Mkae changes to the dim_products table for the delivery team.

UPDATE 
	dim_products
SET 
	product_price = CAST(SUBSTRING(product_price FROM 2) AS DOUBLE PRECISION);


-- Altering the column to a float type

ALTER TABLE 
	dim_products 
		ALTER COLUMN weight TYPE FLOAT USING CAST(weight AS DOUBLE PRECISION),
		ADD COLUMN weight_class VARCHAR;


-- Adding the text categories based on the weights of the products

UPDATE 
	dim_products
SET 
	weight_class =
		CASE 
			WHEN weight < 2.0 THEN 'Light'
			WHEN weight >= 2 
				AND weight < 40 THEN 'Mid_Sized'
			WHEN weight >= 40 
				AND weight <140 THEN 'Heavy'
			WHEN weight >= 140 THEN 'Truck_Required'
		END;
	



-- SELECT * FROM dim_products

