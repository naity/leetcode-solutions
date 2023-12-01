WITH cte AS (
    SELECT DISTINCT visited_on,
        SUM(amount) OVER(
            ORDER BY visited_on RANGE BETWEEN INTERVAL 6 DAY PRECEDING
                AND CURRENT ROW
        ) AS amount,
        MIN(visited_on) OVER() AS first_date
    FROM Customer
)
SELECT visited_on,
    amount,
    ROUND(amount / 7, 2) AS average_amount
FROM cte
WHERE visited_on >= first_date + 6;