-- 코드를 작성해주세요
# with temp as(
#     select ID,
#         PERCENT_RANK() over(ORDER BY SIZE_OF_COLONY desc) as RN
#     from ECOLI_DATA
# )
# select ID,
#     case 
#         when RN  <= 0.25 then 'CRITICAL'
#         when RN  <= 0.5 then 'HIGH'
#         when RN  <= 0.75 then 'MEDIUM'
#         else 'LOW' end
#     as COLONY_NAME
# from temp
# group by 1
# order by 1

with temp as (
    select *,
        ROW_NUMBER() over(ORDER BY SIZE_OF_COLONY desc) as RN,
        COUNT(*) over() as cnt_all
    from ECOLI_DATA
)
select ID,
    case when RN / cnt_all <= 0.25 then 'CRITICAL'
        when RN / cnt_all <= 0.5 then 'HIGH'
        when RN / cnt_all <=0.75 then 'MEDIUM'
        else 'LOW' end
    as COLONY_NAME
from temp
group by 1
order by 1
