--Task 6: Update the dim_date_times table.

-- Maximun length of month column

SELECT 
	length(CAST(month AS TEXT))
FROM 
	dim_date_times
GROUP BY 
	month
ORDER BY 
	length(CAST(month AS TEXT))
DESC
LIMIT
1;
--2


-- Maximun length of year column

SELECT 
	length(CAST(year AS TEXT))
FROM 
	dim_date_times
GROUP BY 
	year
ORDER BY 
	length(CAST(year AS TEXT))
DESC
LIMIT
1;
--4

-- Maximun length of day column

SELECT 
	length(CAST(day AS TEXT))
FROM 
	dim_date_times
GROUP BY 
	day
ORDER BY 
	length(CAST(day AS TEXT))
DESC
LIMIT
1;
--2

-- Maximun length of time_period column

SELECT 
	length(CAST(time_period AS TEXT))
FROM 
	dim_date_times
GROUP BY 
	time_period
ORDER BY 
	length(CAST(time_period AS TEXT))
DESC
LIMIT
1;
--10

-- Alter the data types

ALTER TABLE 
	dim_date_times
		ALTER COLUMN month TYPE VARCHAR(2),
		ALTER COLUMN year TYPE VARCHAR(4),
		ALTER COLUMN day TYPE VARCHAR(2),
		ALTER COLUMN time_period TYPE VARCHAR(10),
		ALTER COLUMN date_uuid TYPE UUID USING date_uuid::UUID;


SELECT * from dim_date_times
	