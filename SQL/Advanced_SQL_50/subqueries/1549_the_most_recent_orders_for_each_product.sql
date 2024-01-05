SELECT p.product_name,
    o.product_id,
    o.order_id,
    o.order_date
FROM Products p,
    Orders o
WHERE p.product_id = o.product_id
    AND (o.product_id, o.order_date) IN (
        SELECT product_id,
            MAX(order_date)
        FROM Orders
        GROUP BY product_id
    )
ORDER BY p.product_name,
    o.product_id,
    o.order_id;