-- 코드를 작성해주세요
select year(DIFFERENTIATION_DATE) as YEAR,
    b.max_size - a.SIZE_OF_COLONY as YEAR_DEV,
    ID
from ECOLI_DATA a
join (select max(size_of_colony) as max_size,
        year(DIFFERENTIATION_DATE) as year
     from ECOLI_DATA
     group by 2) as b
on year(a.DIFFERENTIATION_DATE) = b.year
order by 1, 2