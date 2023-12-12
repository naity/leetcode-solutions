SELECT e.machine_id,
    ROUND(AVG(e.timestamp - s.timestamp), 3) AS processing_time
FROM (
        SELECT *
        FROM Activity
        WHERE activity_type = 'end'
    ) e
    JOIN (
        SELECT *
        FROM Activity
        WHERE activity_type = 'start'
    ) s ON e.machine_id = s.machine_id
    AND e.process_id = s.process_id
GROUP BY e.machine_id;