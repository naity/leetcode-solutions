# Write your MySQL query statement below
WITH cte AS (
    (
        SELECT "failed" AS period_state,
            fail_date AS date
        FROM Failed
        WHERE fail_date BETWEEN '2019-01-01' and '2019-12-31'
    )
    UNION
    (
        SELECT "succeeded" AS period_state,
            success_date AS date
        FROM Succeeded
        WHERE success_date BETWEEN '2019-01-01' and '2019-12-31'
    )
),
cte2 AS (
    SELECT period_state,
        date,
        ROW_NUMBER() OVER(
            ORDER BY date
        ) AS row_num,
        RANK() OVER(
            PARTITION BY period_state
            ORDER BY date
        ) AS state_rank
    FROM cte
)
SELECT period_state,
    MIN(date) AS start_date,
    MAX(date) AS end_date
FROM cte2
GROUP BY period_state,
    row_num - state_rank
ORDER BY start_date;