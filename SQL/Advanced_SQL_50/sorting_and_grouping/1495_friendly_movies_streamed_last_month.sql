SELECT DISTINCT(c.title) AS title
FROM TVProgram t,
    Content c
WHERE c.content_id = t.content_id
    AND YEAR(t.program_date) = 2020
    AND MONTH(t.program_date) = 6
    AND c.Kids_content = 'Y'
    AND content_type = 'movies';