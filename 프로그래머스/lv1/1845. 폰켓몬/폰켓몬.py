def solution(nums):
    leng = int(len(nums)/2)
    unique = set(nums)
    if len(unique)> leng:
        return leng
    else:
        return len(unique)