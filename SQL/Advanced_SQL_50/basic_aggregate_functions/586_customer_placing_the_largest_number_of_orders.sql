WITH cte AS (
    SELECT customer_number,
        COUNT(order_number) AS orders
    FROM Orders
    GROUP BY customer_number
)
SELECT customer_number
FROM cte
WHERE orders = (
        SELECT MAX(orders)
        FROM cte
    );