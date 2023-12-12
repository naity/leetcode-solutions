WITH cte AS(
    SELECT stu.student_id,
        stu.student_name,
        sub.subject_name
    FROM Students stu
        CROSS JOIN Subjects sub
)
SELECT cte.student_id,
    cte.student_name,
    cte.subject_name,
    COUNT(e.subject_name) AS attended_exams
FROM cte
    LEFT JOIN Examinations e ON cte.student_id = e.student_id
    AND cte.subject_name = e.subject_name
GROUP BY cte.student_id,
    cte.subject_name
ORDER BY cte.student_id,
    cte.subject_name;