SELECT c1.seat_id
FROM Cinema c1
    LEFT JOIN Cinema c2 ON c1.seat_id = c2.seat_id - 1
    LEFT JOIN Cinema c3 ON c1.seat_id = c3.seat_id + 1
WHERE c1.free = 1
    AND (
        c2.free = 1
        OR c3.free = 1
    );