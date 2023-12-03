WITH cte AS (
    SELECT name,
        DENSE_RANK() OVER(
            PARTITION BY departmentId
            ORDER BY salary DESC
        ) AS rnk,
        salary,
        departmentId
    FROM Employee
)
SELECT d.name AS Department,
    cte.name AS Employee,
    cte.salary AS Salary
FROM cte,
    Department d
WHERE cte.departmentId = d.id
    AND cte.rnk <= 3;