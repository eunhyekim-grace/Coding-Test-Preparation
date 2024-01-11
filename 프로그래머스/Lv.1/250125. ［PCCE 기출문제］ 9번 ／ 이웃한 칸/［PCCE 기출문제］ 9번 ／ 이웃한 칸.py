def solution(board, h, w):
    
    #단순 계산은 for loop 보다 if 사용이 더 빠름
    findc = board[h][w]
    answer = 0
    leng = len(board)
    if h != 0 and board[h-1][w] == findc:
        answer += 1
    if h+1 < leng and board[h+1][w] == findc:
        answer += 1
    if w != 0 and board[h][w-1] == findc:
        answer += 1
    if w+1 < leng and board[h][w+1] == findc:
        answer += 1
    
    return answer