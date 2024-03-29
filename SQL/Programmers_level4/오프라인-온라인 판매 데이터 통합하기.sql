-- DATE_FORMAT으로 원하는 형식으로 날짜 출력
-- NULL인 컬럼은 NULL as '컬럼명'으로 처리
SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') as SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM ONLINE_SALE 
WHERE MONTH(SALES_DATE)=3 AND YEAR(SALES_DATE)=2022
UNION
SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') as SALES_DAT, PRODUCT_ID,  NULL as USER_ID, SALES_AMOUNT
FROM OFFLINE_SALE 
WHERE MONTH(SALES_DATE)=3 AND YEAR(SALES_DATE)=2022
ORDER BY SALES_DATE ASC, PRODUCT_ID ASC, USER_ID ASC