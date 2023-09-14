def solution(nums):
    leng = int(len(nums)/2)
    unique = set(nums) #nums에서 겹치는 것 빼고 동일한 것만 return
    if len(unique)> leng:
        return leng
    else:
        return len(unique)
