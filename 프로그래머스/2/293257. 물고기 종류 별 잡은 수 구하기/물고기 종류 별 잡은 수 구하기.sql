-- 코드를 작성해주세요
select 
    count(*) as FISH_COUNT, FISH_NAME
from FISH_INFO a
join FISH_NAME_INFO b
    on a.FISH_TYPE = b.FISH_TYPE
group by 2
order by 1 desc