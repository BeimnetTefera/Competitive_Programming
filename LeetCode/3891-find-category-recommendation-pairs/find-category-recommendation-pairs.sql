/* Write your T-SQL query statement below */
WITH MainTable AS (
    SELECT 
        user_id,
        category
    FROM ProductPurchases 
    INNER JOIN ProductInfo 
        ON ProductPurchases.product_id = ProductInfo.product_id
),
FinalTable AS (
    SELECT
        t1.user_id,
        t1.category AS category1,
        t2.category AS category2
    FROM MainTable AS t1
    INNER JOIN MainTable AS t2
        ON t1.user_id = t2.user_id AND
        t1.category < t2.category
)
SELECT
    category1,
    category2,
    COUNT(DISTINCT user_id) AS customer_count
FROM FinalTable
GROUP BY category1 , category2
HAVING COUNT(DISTINCT user_id) >= 3
ORDER BY customer_count DESC,
        category1 ASC,
        category2 ASC