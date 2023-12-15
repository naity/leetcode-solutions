WITH cte AS (
    SELECT student_id,
        MAX(grade) AS grade
    FROM Enrollments
    GROUP BY student_id
    ORDER BY student_id
)

SELECT student_id,
    MIN(course_id) AS course_id,
    grade
FROM Enrollments
WHERE (student_id, grade) IN (
        SELECT *
        FROM cte
    )
GROUP BY student_id, grade
ORDER BY student_id;