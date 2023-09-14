def solution(price, money, count):
    amount = sum([price * c for c in range(1, count+1)])
    
    answer = amount -  money if amount >= money else 0
    
    
    # answer = -1

    return answer