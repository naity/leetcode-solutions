SELECT e.left_operand,
    e.operator,
    e.right_operand,
    CASE
        WHEN e.operator = "=" THEN IF(v1.value = v2.value, 'true', 'false')
        WHEN e.operator = ">" THEN IF(v1.value > v2.value, 'true', 'false')
        ELSE IF(v1.value < v2.value, 'true', 'false')
    END AS value
FROM Expressions e,
    Variables v1,
    Variables v2
WHERE e.left_operand = v1.name
    AND e.right_operand = v2.name;