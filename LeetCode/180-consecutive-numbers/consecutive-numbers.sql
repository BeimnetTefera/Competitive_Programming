# Write your MySQL query statement below
WITH Final_Table AS (
    SELECT 
        *,
        COUNT(*) OVER (PARTITION BY bucket, num) AS cnt
    FROM (
        SELECT
            id,
            num,
            id - ROW_NUMBER() OVER (PARTITION BY num ORDER BY id) AS bucket
        FROM Logs
        ) t
)
SELECT DISTINCT
    num AS ConsecutiveNums
FROM Final_Table
WHERE cnt >= 3