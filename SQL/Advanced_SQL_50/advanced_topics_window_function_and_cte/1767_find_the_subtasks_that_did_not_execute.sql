WITH RECURSIVE cte (n) AS (
    SELECT 1
    UNION ALL
    SELECT n + 1
    FROM cte
    WHERE n < 20
)
SELECT t.task_id,
    cte.n AS subtask_id
FROM Tasks t
    CROSS JOIN cte
WHERE n <= subtasks_count
    AND (task_id, n) NOT IN (
        SELECT task_id,
            subtask_id
        FROM Executed
    );