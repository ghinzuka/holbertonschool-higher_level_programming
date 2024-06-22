-- 20. temperature 2
-- Write a script that displays the max temperature of each state (ordered by State name).
-- select the state - we use the abregation MAX instead of AVG from the temperature - 
-- group by state instead of cities and order by state ascending'
SELECT
    state,
    MAX(value) AS max_temp
	FROM temperatures
	GROUP BY state
	ORDER BY state;
