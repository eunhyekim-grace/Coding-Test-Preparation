-- 코드를 작성해주세요

with avg as(
select FISH_TYPE,
    SUM(LENGTH) / COUNT(ID) as AVG_LENGTH
from FISH_INFO
group by 1)

select count(ID) as FISH_COUNT,
    max(LENGTH) as MAX_LENGTH,
    A.FISH_TYPE
from FISH_INFO A
join (
    select FISH_TYPE
    from avg
    where AVG_LENGTH >= 33) AS B
on A.FISH_TYPE = B.FISH_TYPE
group by 3
order by 3
