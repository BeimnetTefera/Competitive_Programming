# Write your MySQL query statement below
-- FIND A CUSTOMER WHO BAOUGHT EVERYTHING FROM PRODUCT KEY
SELECT DISTINCT
    customer_id
FROM Customer AS cust
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product);