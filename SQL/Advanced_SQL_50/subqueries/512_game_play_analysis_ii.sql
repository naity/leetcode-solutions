WITH cte AS (
    SELECT player_id,
        MIN(event_date) AS event_date
    FROM Activity
    GROUP BY player_id
)
SELECT a.player_id,
    a.device_id
FROM Activity a,
    cte
WHERE a.player_id = cte.player_id
    AND a.event_date = cte.event_date;