-- 코드를 작성해주세요

select COUNT(FISH_TYPE) as FISH_COUNT,
    MAX(LENGTH) as MAX_LENGTH,
    FISH_TYPE
from (
    select FISH_TYPE,
        case when LENGTH is null 
            then 10 else LENGTH end
        as LENGTH
    from FISH_INFO) A
group by FISH_TYPE
having AVG(LENGTH) >= 33
order by 3