# Write your MySQL query statement below
SELECT 
    event_day AS day,
    emp_id,
    SUM(time_spent) AS total_time
FROM (
    SELECT 
        emp_id,
        event_day,
        in_time,
        out_time - in_time AS time_spent
    FROM Employees
    GROUP BY  emp_id,
            event_day,
            in_time,
            out_time
) AS temp
GROUP BY emp_id, event_day