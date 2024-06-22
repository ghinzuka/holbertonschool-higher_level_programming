-- 18. Temperatures #0
-- Write a script that displays the average temperature 
-- (Fahrenheit) by city ordered by temperature (descending).
-- using the the AVG abregation tu get the average temp - 
-- GROUP by the city so it knows from wich group of (values) it needs to do the AVG from - 
-- order by the avg temp in descending order
SELECT
    city,
    AVG(value) AS avg_temp
	FROM temperatures
	WHERE month = 7 or month = 8 
	GROUP BY city
	ORDER BY avg_temp DESC
	LIMIT 3;
