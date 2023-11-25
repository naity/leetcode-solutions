SELECT p1.product_id,
    IFNULL(p2.price, 10) AS price
FROM (
        SELECT DISTINCT product_id
        FROM Products
    ) p1
    LEFT JOIN (
        SELECT product_id,
            new_price as price
        FROM Products
        WHERE (product_id, change_date) IN (
                SELECT product_id,
                    MAX(change_date) AS change_date
                FROM Products
                WHERE change_date <= '2019-08-16'
                GROUP BY product_id
            )
    ) p2 ON p1.product_id = p2.product_id;