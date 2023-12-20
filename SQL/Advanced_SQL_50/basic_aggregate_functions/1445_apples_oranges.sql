SELECT sale_date,
    SUM(
        IF(fruit = "apples", sold_num, sold_num * -1)
    ) AS diff
FROM Sales
GROUP BY sale_date
ORDER BY sale_date;