/* Write your T-SQL query statement below */
-- find maximum salary by department
SELECT 
    dept.name AS Department,
    emp.name AS Employee,
    salary AS Salary
FROM Employee AS emp
INNER JOIN Department AS dept
    ON emp.departmentId = dept.id
INNER JOIN (
    SELECT 
        departmentId,
        MAX(salary) AS mx_salary
    FROM Employee
    GROUP BY departmentId
) AS max_dept_salary
    ON max_dept_salary.departmentId = dept.id
WHERE salary = mx_salary