SELECT CASE
        WHEN id = (
            SELECT MAX(id)
            FROM Seat
        ) THEN id
        ELSE id + 1
    END AS id,
    student
FROM Seat
WHERE id % 2 = 1
UNION
SELECT id - 1 AS id,
    student
FROM Seat
WHERE id % 2 = 0
ORDER BY id;