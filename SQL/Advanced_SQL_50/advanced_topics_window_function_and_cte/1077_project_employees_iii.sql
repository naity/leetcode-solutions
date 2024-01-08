WITH cte AS (
    SELECT p.project_id,
        p.employee_id,
        e.experience_years
    FROM Project p,
        Employee e
    WHERE e.employee_id = p.employee_id
)
SELECT project_id,
    employee_id
FROM cte
WHERE (project_id, experience_years) IN (
        SELECT project_id,
            MAX(experience_years)
        FROM cte
        GROUP BY project_id
    );