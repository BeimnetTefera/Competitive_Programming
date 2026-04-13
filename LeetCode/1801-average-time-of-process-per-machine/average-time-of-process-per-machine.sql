# Write your MySQL query statement below


-- take the previous time from timestamp(LAG)
-- filter where activity_type is end
-- then compute the deduction 
-- then group by machine id and sum them up the time taken

WITH temp_table AS (
    SELECT
        *,
        (timestamp - LAG(timestamp) OVER (PARTITION BY machine_id, process_id ORDER BY timestamp)) AS time_taken
    FROM Activity
)
SELECT
    machine_id,
    ROUND(AVG(time_taken), 3) AS processing_time
FROM temp_table
WHERE activity_type = "end"
GROUP BY machine_id