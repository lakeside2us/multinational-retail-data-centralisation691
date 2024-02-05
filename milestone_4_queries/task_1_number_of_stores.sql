--Task 1: Number of stores in the business and locations.


SELECT 
	country_code
AS
	country,
COUNT
	(country_code) 
AS 
	total_no_stores
FROM 
	dim_store_details
GROUP BY 
	country_code
ORDER BY 
	total_no_stores 
DESC;


-- SELECT * FROM dim_store_details order by country_code DESC