-- 코드를 입력하세요
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1;

# SELECT NAME
# FROM ANIMAL_INS
# WHERE DATETIME = (SELECT MIN(DATETIME) FROM ANIMAL_INS);

#  ORACLE
# SELECT NAME
# FROM (
#     SELECT NAME
#     FROM ANIMAL_INS
#     ORDER BY DATETIME)
# WHERE ROWNUM = 1;