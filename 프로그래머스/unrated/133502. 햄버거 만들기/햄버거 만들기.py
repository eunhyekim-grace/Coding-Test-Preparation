from collections import Counter

def solution(ingredient):
    comp = [1,2,3,1]
    cnt = 0
    ing_stack = []
    
    for i in ingredient:
        ing_stack.append(i)
        
        if ing_stack[-4:] == comp:
            # ing_stack = ing_stack[:-4] #시초 2개
            del ing_stack[-4:]
            cnt += 1
    return cnt