WITH cte AS (
    SELECT DISTINCT seller_id AS seller_id
    FROM Orders
    WHERE YEAR(sale_date) = 2020
)
SELECT s.seller_name
FROM Seller s
    LEFT JOIN cte ON s.seller_id = cte.seller_id
WHERE cte.seller_id IS NULL
ORDER BY s.seller_name;