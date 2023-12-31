WITH cte AS(
    SELECT Wimbledon AS player_id
    FROM Championships
    UNION ALL
    SELECT Fr_open AS player_id
    FROM Championships
    UNION ALL
    SELECT US_open AS player_id
    FROM Championships
    UNION ALL
    SELECT Au_open AS player_id
    FROM Championships
)
SELECT p.player_id,
    p.player_name,
    COUNT(*) AS grand_slams_count
FROM Players p,
    cte
WHERE p.player_id = cte.player_id
GROUP BY p.player_id;