(
    SELECT u.name AS results
    FROM MovieRating r,
        Users u
    WHERE r.user_id = u.user_id
    GROUP BY r.user_id
    ORDER BY COUNT(*) DESC,
        u.name ASC
    LIMIT 1
)
UNION ALL
(
    SELECT m.title AS results
    FROM Movies m,
        MovieRating r
    WHERE m.movie_id = r.movie_id
        AND r.created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY r.movie_id
    ORDER BY AVG(r.rating) DESC,
        m.title ASC
    LIMIT 1
);