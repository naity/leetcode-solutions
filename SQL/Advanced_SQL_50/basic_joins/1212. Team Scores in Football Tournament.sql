WITH host AS (
    SELECT t.team_id,
        t.team_name,
        IFNULL(
            SUM(
                CASE
                    WHEN m.host_goals > m.guest_goals THEN 3
                    WHEN m.host_goals = m.guest_goals THEN 1
                    ELSE 0
                END
            ),
            0
        ) AS num_points
    FROM Teams t
        LEFT JOIN Matches m ON t.team_id = m.host_team
    GROUP BY t.team_id
),
guest AS (
    SELECT t.team_id,
        t.team_name,
        IFNULL(
            SUM(
                CASE
                    WHEN m.host_goals < m.guest_goals THEN 3
                    WHEN m.host_goals = m.guest_goals THEN 1
                    ELSE 0
                END
            ),
            0
        ) AS num_points
    FROM Teams t
        LEFT JOIN Matches m ON t.team_id = m.guest_team
    GROUP BY t.team_id
)
SELECT h.team_id AS team_id,
    h.team_name AS team_name,
    h.num_points + g.num_points AS num_points
FROM host h,
    guest g
WHERE h.team_id = g.team_id
ORDER BY num_points DESC,
    team_id;