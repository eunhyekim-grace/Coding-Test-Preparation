from itertools import chain

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def solution(n):
    #create walls
    # ex -> 4- 3- 3- 2- 2- 1- 1
    walls = [[i, i] for i in range(n, 0, -1)]
    walls = list(chain(*walls))
    walls.pop(0)

    #create n*n board filled with 0
    board = [[0] *  n for i in range(n)]
    
    #set variables
    operations = [add, sub]
    op_tog = 1 #toggle add & sub
    r, c = 0, 0 #row, col in board
    num = 1 # numbers range 1 ~ n*n 
    rc_tog = 0 #toggle which value to change: row and col 
    
    for idx, wall in enumerate(walls):
        if idx % 2 == 0: #add, sub changes every 2 times
            op_tog ^= 1
        op = operations[op_tog] #sub / add

        rc_tog ^= 1 # 고정 변동 row, col -> row & col changes every iter
        for num_idx, i in enumerate(range(num, num+wall)): #actually put values in board
            if rc_tog: # col index inc / desc
                if idx == 0:
                    board[r][op(c, num_idx)] = i
                else:
                    board[r][op(op(c,num_idx),1)] = i
                    
            else: #row index inc / desc
                if idx == 0:
                    board[op(r, num_idx)][c] = i
                else:
                    board[op(op(r, num_idx), 1)][c] = i
        
        #set next start point
        if rc_tog: # row / col to change -> col value change
            if idx == 0:
                c = n-1
            else:
                c = operations[op_tog](c, wall)
        else: #row value change 
            r = operations[op_tog](r, wall)
            
        num += wall #inc number 
    # print(board)
    return board