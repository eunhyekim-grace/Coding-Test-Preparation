-- 코드를 작성해주세요

select ID,
    case when LENGTH is null
        then 10 else LENGTH end
    as LENGTH
from FISH_INFO
order by 2 desc, 1
limit 10