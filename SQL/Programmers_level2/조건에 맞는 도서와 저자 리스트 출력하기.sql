-- 코드를 입력하세요
SELECT B.BOOK_ID AS BOOK_ID, A.AUTHOR_NAME AS AUTHOR_NAME, DATE_FORMAT(B.PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK B, AUTHOR A
WHERE B.AUTHOR_ID = A.AUTHOR_ID
AND B.CATEGORY = '경제' 
ORDER BY PUBLISHED_DATE ASC;