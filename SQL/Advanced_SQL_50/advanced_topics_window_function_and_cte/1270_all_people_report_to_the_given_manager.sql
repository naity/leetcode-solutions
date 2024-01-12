WITH cte1 AS (
    SELECT employee_id
    FROM Employees
    WHERE manager_id = 1
        AND employee_id != 1
),
cte2 AS (
    SELECT employee_id
    FROM Employees
    WHERE manager_id IN (
            SELECT employee_id
            FROM cte1
        )
),
cte3 AS (
    SELECT employee_id
    FROM Employees
    WHERE manager_id IN (
            SELECT employee_id
            FROM cte2
        )
)
SELECT *
FROM cte1
UNION
SELECT *
FROM cte2
UNION
SELECT *
FROM cte3;