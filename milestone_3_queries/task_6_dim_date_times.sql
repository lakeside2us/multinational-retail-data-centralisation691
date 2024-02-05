--Task 6: Update the dim_date_times table.

-- Maximun length of month column

SELECT 
	LENGTH(MAX(CAST(month AS TEXT)))
FROM 
	dim_date_times
GROUP BY 
	month
ORDER BY 
	LENGTH(MAX(CAST(month AS TEXT)))
DESC
LIMIT
	1;
-- 	(2)


-- Maximun length of year column

SELECT 
	LENGTH(MAX(CAST(year AS TEXT)))
FROM 
	dim_date_times
GROUP BY 
	year
ORDER BY 
	LENGTH(MAX(CAST(year AS TEXT)))
DESC
LIMIT
	1;
-- (4)

-- Maximun length of day column

SELECT 
	LENGTH(MAX(CAST(day AS TEXT)))
FROM 
	dim_date_times
GROUP BY 
	day
ORDER BY 
	LENGTH(MAX(CAST(day AS TEXT)))
DESC
LIMIT
	1;
-- (2)

-- Maximun length of time_period column

SELECT 
	LENGTH(MAX(CAST(time_period AS TEXT)))
FROM 
	dim_date_times
GROUP BY 
	time_period
ORDER BY 
	LENGTH(MAX(CAST(time_period AS TEXT)))
DESC
LIMIT
	1;
-- (10)

-- Alter the data types

ALTER TABLE 
	dim_date_times
		ALTER COLUMN month TYPE VARCHAR(2),
		ALTER COLUMN year TYPE VARCHAR(4),
		ALTER COLUMN day TYPE VARCHAR(2),
		ALTER COLUMN time_period TYPE VARCHAR(10),
		ALTER COLUMN date_uuid TYPE UUID USING date_uuid::UUID;


-- SELECT * FROM dim_date_times
	