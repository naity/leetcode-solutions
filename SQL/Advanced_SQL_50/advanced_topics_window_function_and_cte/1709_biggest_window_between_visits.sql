WITH cte AS (
    (
        SELECT DISTINCT user_id as user_id,
            '2021-1-1' AS visit_date
        FROM UserVisits
    )
    UNION ALL
    (
        SELECT *
        FROM UserVisits
    )
),
cte2 AS (
    SELECT user_id,
        visit_date,
        LAG(visit_date, 1) OVER (
            PARTITION BY user_id
            ORDER BY visit_date
        ) AS previous_visit_date
    FROM cte
)
SELECT user_id,
    MAX(DATEDIFF(visit_date, previous_visit_date)) AS biggest_window
FROM cte2
GROUP BY user_id
ORDER BY user_id;