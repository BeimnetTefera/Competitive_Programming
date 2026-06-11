# Write your MySQL query statement below
SELECT 
    DISTINCT(num) AS ConsecutiveNums
FROM (
    SELECT 
        num,
        LEAD(num) OVER (ORDER BY id) AS num2,
        LEAD(num, 2) OVER (ORDER BY id) AS num3
    FROM Logs 
) AS t
WHERE 
    num = num2 AND
    num = num3