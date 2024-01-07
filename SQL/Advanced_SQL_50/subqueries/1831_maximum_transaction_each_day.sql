SELECT transaction_id
FROM Transactions
WHERE (day, amount) IN (
        SELECT day,
            MAX(amount)
        FROM Transactions
        GROUP BY day
    )
ORDER BY transaction_id;