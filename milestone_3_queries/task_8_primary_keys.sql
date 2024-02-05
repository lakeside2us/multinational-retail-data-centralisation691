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


--SELECT * FROM orders_table 
--SELECT * FROM dim_date_times
--SELECT * FROM dim_users 
--SELECT * FROM dim_card_details
--SELECT * FROM dim_store_details;
--SELECT * FROM dim_products


-- select * FROM dim_users ORDER BY user_uuid DESC