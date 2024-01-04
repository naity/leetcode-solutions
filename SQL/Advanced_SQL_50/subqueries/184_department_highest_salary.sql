SELECT d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM Department d,
    Employee e
WHERE d.id = e.departmentId
    AND (e.departmentId, e.salary) IN (
        SELECT departmentId,
            MAX(salary)
        FROM Employee
        GROUP BY departmentId
    );