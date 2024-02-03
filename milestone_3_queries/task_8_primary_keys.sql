--Task 8: Create the primary keys in the dimension table.


ALTER TABLE 
	dim_date_times
ADD PRIMARY KEY 
	(date_uuid);
	

ALTER TABLE 
	dim_users
ADD PRIMARY KEY 
	(user_uuid);


ALTER TABLE 
	dim_card_details
ADD PRIMARY KEY 
	(card_number);


ALTER TABLE 
	dim_store_details
ADD PRIMARY KEY 
	(store_code);


ALTER TABLE 
	dim_products
ADD PRIMARY KEY 
	(product_code);


SELECT * from orders_table 
SELECT * from dim_date_times
SELECT * from dim_users 
SELECT * from dim_card_details
SELECT * from dim_store_details;
SELECT * from dim_products
	