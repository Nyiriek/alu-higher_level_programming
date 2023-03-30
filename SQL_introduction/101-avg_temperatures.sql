-- Displays the average temperature by city ordered by temperature
SELECT city AVG(value) AS avg_temp FROM temperetures GROUP BY city ORDER BY avg_temp DESC;
