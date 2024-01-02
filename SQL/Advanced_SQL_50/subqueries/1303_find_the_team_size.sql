WITH cte AS (
    SELECT team_id,
        COUNT(employee_id) AS team_size
    FROM Employee
    GROUP BY team_id
)
SELECT e.employee_id,
    cte.team_size
FROM Employee e,
    cte
WHERE e.team_id = cte.team_id;