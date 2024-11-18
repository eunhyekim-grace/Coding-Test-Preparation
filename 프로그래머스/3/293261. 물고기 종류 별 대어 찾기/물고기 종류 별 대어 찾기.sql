-- 코드를 작성해주세요

select ID,
    FISH_NAME,
    LENGTH
from FISH_NAME_INFO A
join (
    select ID,
        FISH_TYPE,
        LENGTH,
        row_number() OVER (PARTITION BY FISH_TYPE ORDER BY LENGTH DESC) AS RN
    from FISH_INFO) as B
on A.FISH_TYPE = B.FISH_TYPE
and B.RN = 1
order by ID