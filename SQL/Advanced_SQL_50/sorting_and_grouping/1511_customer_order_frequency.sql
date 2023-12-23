SELECT c.customer_id,
    c.name
FROM Customers c,
    Product p,
    Orders o
WHERE o.product_id = p.product_id
    AND o.customer_id = c.customer_id
    AND YEAR(o.order_date) = 2020
GROUP BY c.customer_id
HAVING SUM(
        IF(MONTH(o.order_date) = 6, quantity, 0) * p.price
    ) >= 100
    AND SUM(
        IF(MONTH(o.order_date) = 7, quantity, 0) * p.price
    ) >= 100;