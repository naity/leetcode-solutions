WITH cte AS (
    SELECT *
    FROM Employees
    WHERE manager_id NOT IN (
            SELECT employee_id
            FROM Employees
        )
)
SELECT employee_id
FROM cte
WHERE salary < 30000
ORDER BY employee_id;