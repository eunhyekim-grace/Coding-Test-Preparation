-- 코드를 작성해주세요
# with test as (
#     select a.ID, 
#     case when b.ID is null then 0 
#         else count(b.ID) end as cnt
# from ECOLI_DATA a
# left join ECOLI_DATA b
# on a.ID = b.PARENT_ID
# group by a.ID, b.ID
# )

# select ID, 
#     sum(cnt) as CHILD_COUNT
# from test
# group by ID
# order by 1

select a.ID,
    IFNULL(count(b.PARENT_ID), 0) as CHILD_COUNT
from ECOLI_DATA a
left join ECOLI_DATA b
on a.ID = b.PARENT_ID
group by 1
order by 1