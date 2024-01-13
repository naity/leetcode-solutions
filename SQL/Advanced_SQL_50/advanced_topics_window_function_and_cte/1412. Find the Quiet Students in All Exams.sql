# Write your MySQL query statement below
WITH cte AS (
    SELECT exam_id,
        MAX(score) AS max_score,
        MIN(score) AS min_score
    FROM Exam
    GROUP BY exam_id
),
cte2 AS (
    SELECT student_id
    FROM Exam
    WHERE (exam_id, score) IN (
            SELECT exam_id,
                max_score
            FROM cte
        )
        OR (exam_id, score) IN (
            SELECT exam_id,
                min_score
            FROM cte
        )
)
SELECT student_id,
    student_name
FROM Student
WHERE student_id IN (
        SELECT student_id
        FROM Exam
    )
    AND student_id NOT IN (
        SELECT student_id
        FROM cte2
    )