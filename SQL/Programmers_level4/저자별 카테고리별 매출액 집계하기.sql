-- 코드를 입력하세요
WITH S AS (
 SELECT BOOK_ID, SUM(SALES) AS SALES
 FROM BOOK_SALES 
 WHERE YEAR(SALES_DATE) = 2022 AND MONTH(SALES_DATE) = 1
 GROUP BY BOOK_ID
)

SELECT A.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY, SUM(S.SALES * B.PRICE) AS TOTAL_SALES
FROM BOOK B, AUTHOR A, S
WHERE B.AUTHOR_ID = A.AUTHOR_ID AND B.BOOK_ID = S.BOOK_ID
GROUP BY A.AUTHOR_ID, B.CATEGORY
ORDER BY AUTHOR_ID ASC, CATEGORY DESC;