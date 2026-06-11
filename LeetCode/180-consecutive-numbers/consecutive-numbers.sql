# Write your MySQL query statement below
SELECT 
    L1.num AS ConsecutiveNums
FROM Logs L1, Logs L2, Logs L3
WHERE 
    L1.num = L2.num AND
    L1.num = L3.num AND
    L2.id = L1.id + 1 AND
    L3.id = L2.id + 1
GROUP BY L1.num