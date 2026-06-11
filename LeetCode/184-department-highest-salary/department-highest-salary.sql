/* Write your T-SQL query statement below */
SELECT 
    Department,
    Employee,
    Salary
FROM (
    SELECT 
        dept.name AS Department,
        emp.name AS Employee,
        salary AS Salary,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rnk
    FROM Employee AS emp
    INNER JOIN Department AS dept
    ON emp.departmentId = dept.id
) AS t
WHERE rnk = 1; 