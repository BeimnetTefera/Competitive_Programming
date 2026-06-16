# Write your MySQL query statement below
SELECT 
    id,
    CASE 
        WHEN p_id IS NULL THEN 'Root'
        WHEN NOT EXISTS (SELECT p_id FROM Tree parent WHERE node.id = parent.p_id) THEN 'Leaf'
        ELSE 'Inner'
    END AS type
FROM Tree node