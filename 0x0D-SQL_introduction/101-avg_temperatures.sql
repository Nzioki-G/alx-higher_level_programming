-- import table dump: mysql -u grace db_name < dump.sql
-- get avg temperatures of each city
SELECT city, AVG(value) AS avg_temp
  FROM temperatures
 GROUP BY city
 ORDER BY avg_temp DESC;

