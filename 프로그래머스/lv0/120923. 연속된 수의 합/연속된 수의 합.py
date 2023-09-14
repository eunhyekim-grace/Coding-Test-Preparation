import numpy as np

def solution(num, total):
    middle = int(total/num)
    
    if num % 2 == 1:
        n1 = middle - int(num/2)
        n2 = middle + int(num/2) +1
        answer = list(range(n1,n2))
    else:
        n = int(num/2)
        n1 = middle - n +1
        n2 = middle+ n +1
        answer = list(range(n1,n2))
    
    return answer