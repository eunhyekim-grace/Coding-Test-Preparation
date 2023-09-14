from itertools import permutations
import math

def solution(n, k):
    
    k_ = k
    
    if n == 1:
        return [1]
    
    flag = 0
    nums = [i for i in range(1, n+1)]
    answer = []
    
    for i in range(n, 1, -1):
        pos = math.factorial(i)
        per = int(pos / i)
        # print(pos, per)
        
        idx = int(k / per)
        mod = int(k % per)
        
        
        if (mod == 0) and (flag != 1):
            answer.append(nums.pop(idx-1))
            k = (k-1) % per
            flag = 1
        else:
            answer.append(nums.pop(idx))
            k = mod
            
    answer.append(nums.pop())
    
    return answer