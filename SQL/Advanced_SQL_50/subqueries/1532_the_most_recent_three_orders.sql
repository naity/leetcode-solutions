WITH cte AS (
    SELECT order_id,
        order_date,
        customer_id,
        RANK() OVER(
            PARTITION BY customer_id
            ORDER BY order_date DESC
        ) AS date_rank
    FROM Orders
)
SELECT c.name AS customer_name,
    cte.customer_id,
    cte.order_id,
    cte.order_date
FROM Customers c,
    cte
WHERE c.customer_id = cte.customer_id
    AND cte.date_rank <= 3
ORDER BY customer_name,
    cte.customer_id,
    cte.order_date DESC;