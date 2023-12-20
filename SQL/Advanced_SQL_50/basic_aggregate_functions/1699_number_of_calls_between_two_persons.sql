WITH cte AS (
    SELECT from_id AS person1,
        to_id AS person2,
        duration
    FROM Calls
    WHERE from_id < to_id
    UNION ALL
    SELECT to_id AS person1,
        from_id AS person2,
        duration
    FROM Calls
    WHERE from_id > to_id
)
SELECT person1,
    person2,
    COUNT(duration) AS call_count,
    SUM(duration) AS total_duration
FROM cte
GROUP BY person1,
    person2;