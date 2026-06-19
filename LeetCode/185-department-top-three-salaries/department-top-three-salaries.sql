/* Write your T-SQL query statement below */
WITH MainTable AS (
    SELECT 
        emp.name AS Employee,
        salary AS Salary,
        dept.name AS Department,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS RankBySalary
    FROM Employee AS emp
    JOIN Department AS dept
        ON emp.departmentId = dept.id
)
SELECT 
    Employee,
    Salary,
    Department
FROM MainTable
WHERE RankBySalary <= 3