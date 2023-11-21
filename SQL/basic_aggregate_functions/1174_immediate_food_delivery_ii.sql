WITH first AS (
    SELECT customer_id,
        MIN(order_date) AS order_date
    FROM Delivery
    GROUP BY customer_id
)
SELECT ROUND(
        100 * AVG(d.order_date = d.customer_pref_delivery_date),
        2
    ) AS immediate_percentage
FROM Delivery d,
    first f
WHERE d.customer_id = f.customer_id
    AND d.order_date = f.order_date;