/* Write your T-SQL query statement below */
SELECT 
    name,
    SUM(amount) AS balance
FROM Users AS us
LEFT JOIN Transactions AS trans
ON us.account = trans.account
GROUP BY name
HAVING SUM(amount) > 10000