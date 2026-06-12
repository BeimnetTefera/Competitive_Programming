/* Write your T-SQL query statement below */
SELECT 
    EmployeeName AS Employee
FROM (
    SELECT 
        emp.id,
        emp.name AS EmployeeName,
        emp.salary AS EmployeeSalary,
        emp.managerId,
        man.salary AS ManagerSalary,
        man.name AS ManagerName
    FROM Employee AS emp
    INNER JOIN Employee AS man
        ON emp.managerId = man.id
) t
WHERE EmployeeSalary > ManagerSalary