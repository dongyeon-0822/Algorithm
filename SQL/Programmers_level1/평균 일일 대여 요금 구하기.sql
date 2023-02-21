-- 평균을 표현하는 집계함수 AvG
-- 소수점 첫번째 자리에서 반올림하는 ROUND
-- 별명을 지정하는 AS
SELECT ROUND(AVG(DAILY_FEE)) as AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE='SUV';