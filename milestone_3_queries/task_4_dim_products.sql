--Task 4: Mkae changes to the dim_products table for the delivery team.
	
-- Remove the £ sign in the product_price column

UPDATE 
	dim_products
SET 
	product_price = REPLACE(product_price, '£', '');


-- Add the weight_class column.

ALTER TABLE 
	dim_products
ADD COLUMN 
	weight_class VARCHAR;


-- Add text categories based on the weights of the products
UPDATE dim_products
SET weight_class =
	CASE 
		WHEN weight < 2.0 THEN 'Light'
		WHEN weight >= 2 
			AND weight < 40 THEN 'Mid_Sized'
		WHEN weight >= 40 
			AND weight <140 THEN 'Heavy'
		WHEN weight >= 140 THEN 'Truck_Required'
		END;






-- SELECT * from dim_products
	