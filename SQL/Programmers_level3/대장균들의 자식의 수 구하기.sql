WITH T AS (
    SELECT PARENT_ID, COUNT(*) AS CNT
    FROM ECOLI_DATA
    GROUP BY PARENT_ID
)
SELECT ID, IFNULL(T.CNT, 0) AS CHILD_COUNT
FROM ECOLI_DATA LEFT JOIN T ON ECOLI_DATA.ID = T.PARENT_ID
ORDER BY ID;