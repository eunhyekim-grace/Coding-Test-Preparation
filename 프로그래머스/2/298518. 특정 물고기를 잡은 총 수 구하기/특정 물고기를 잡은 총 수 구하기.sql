-- 코드를 작성해주세요

select count(*) as FISH_COUNT
from FISH_INFO A
join (
    select FISH_TYPE
    from FISH_NAME_INFO
    where FISH_NAME IN ('BASS', 'SNAPPER')) as B
on A.FISH_TYPE = B.FISH_TYPE