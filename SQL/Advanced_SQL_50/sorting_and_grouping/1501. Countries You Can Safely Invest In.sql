WITH cte AS(
    SELECT caller_id AS id,
        duration
    FROM Calls
    UNION ALL
    SELECT callee_id AS id,
        duration
    FROM Calls
)
SELECT c.name AS country
FROM Country c,
    Person p,
    cte
WHERE cte.id = p.id
    AND SUBSTRING(p.phone_number, 1, 3) = c.country_code
GROUP BY c.name
HAVING AVG(cte.duration) > (
        SELECT AVG(duration)
        FROM cte
    );