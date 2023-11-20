WITH first AS (
    SELECT player_id,
        MIN(event_date) AS event_date
    FROM Activity
    GROUP BY player_id
)
SELECT ROUND(
        AVG(a.event_date IS NOT NULL),
        2
    ) AS fraction
FROM first f
    LEFT JOIN Activity a ON f.player_id = a.player_id
    AND DATEDIFF(a.event_date, f.event_date) = 1;