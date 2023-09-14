import math

def same(number, hand, rr, rc, lr, lc):
    if number == 0:
        tr, tc = 3, 1
    else:
        tr, tc = (number-1) // 3, (number -1 )%3
    left = abs(tr - lr) + abs(tc - lc)
    right = abs(tr - rr) + abs(tc - rc)
            
    if left > right:
        return 'R', tr, tc
    elif left < right:
        return 'L', tr, tc
    else:
        if hand == 'right':
            return 'R', tr, tc
        else:
            return 'L', tr, tc
    
        

def solution(numbers, hand):
    hand_ = 'R' if hand == 'right' else 'L'
    
    keypad = [[0,0,0],[0,0,0],[0,0,0]]
    
    for i in range(9):
        keypad[i//3][i%3] = i+1
        
    keypad = keypad + [['*', 0, '#']]
    
    answer = []
    lr, lc = 3, 0
    rr, rc = 3, 2
    tr, tc = 0, 0
    for number in numbers:
        if number == 0:
            LR, tr, tc = same(number, hand, rr, rc, lr, lc)
            answer.append(LR)

            if LR == 'R':
                rr, rc = tr, tc
            else:
                lr, lc = tr, tc
        elif number % 3 == 0:
            answer.append('R')
            rr, rc = (number-1) // 3, 2

        elif number % 3 == 1:
            answer.append('L')
            lr, lc = (number -1) // 3, 0

        else:
            LR, tr, tc = same(number, hand, rr, rc, lr, lc)
            answer.append(LR)
            if LR == 'R':
                rr, rc = tr, tc
            else:
                lr, lc = tr, tc
            
    return ''.join(answer)
