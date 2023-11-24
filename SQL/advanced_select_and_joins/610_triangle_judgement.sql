SELECT x,
    y,
    z,
    CASE
        WHEN x < y + z
        AND y < x + Z
        AND z < x + y THEN "Yes"
        ELSE "No"
    END AS triangle
FROM Triangle;