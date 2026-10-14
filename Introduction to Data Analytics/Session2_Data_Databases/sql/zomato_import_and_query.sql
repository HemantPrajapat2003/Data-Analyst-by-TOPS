-- Optional SQL example for a MySQL table created from the restaurant CSV.
CREATE DATABASE IF NOT EXISTS session2_practice;
USE session2_practice;

CREATE TABLE IF NOT EXISTS zomato_restaurants (
    restaurant_id INT PRIMARY KEY,
    restaurant_name VARCHAR(100),
    city VARCHAR(80),
    cuisine VARCHAR(80),
    rating DECIMAL(2,1),
    average_cost_for_two INT
);

-- After importing the CSV with MySQL Workbench's Table Data Import Wizard:
SELECT city, COUNT(*) AS restaurant_count
FROM zomato_restaurants
GROUP BY city
ORDER BY restaurant_count DESC;
