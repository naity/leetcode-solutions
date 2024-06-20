WITH cte AS (
    SELECT customer_id,
        product_id,
        COUNT(*) AS cnt
    FROM Orders
    GROUP BY customer_id,
        product_id
),
cte2 AS (
    SELECT customer_id,
        product_id,
        cnt,
        
        MAX(cnt) OVER(PARTITION BY customer_id) as max_count
    FROM cte
)
SELECT cte2.customer_id,
    cte2.product_id,
    p.product_name
FROM cte2,
    Products p
WHERE cte2.cnt = cte2.max_count
    AND p.product_id = cte2.product_id;