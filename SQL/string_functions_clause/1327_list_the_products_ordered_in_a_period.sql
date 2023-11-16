SELECT p.product_name,
    SUM(unit) AS unit
FROM Orders o,
    Products p
WHERE o.order_date BETWEEN '2020-02-01' AND '2020-02-29'
    AND o.product_id = p.product_id
GROUP BY o.product_id
HAVING unit >= 100;