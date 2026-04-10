# Write your MySQL query statement below
SELECT
    id
FROM (
    SELECT
        id,
        recordDate,
        temperature,
        LAG(temperature) OVER (ORDER BY recordDate) AS prev_temp,
        LAG(recordDate) OVER (ORDER BY recordDate) AS prev_date
    FROM Weather) t
WHERE temperature > prev_temp AND
    recordDate = DATE_ADD(prev_date, INTERVAL 1 DAY)