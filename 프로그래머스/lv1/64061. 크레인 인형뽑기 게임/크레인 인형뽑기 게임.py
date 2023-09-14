def solution(board, moves):
    leng = len(board)
    first_idx = [-1] * leng
    result = [0]
    cnt = 0
    r_idx = 0
    
    if len(moves) == 1: #move가 1개인 경우
        return 0
    
    for i in range(0,leng): #각 열의 인형이 들어있는 첫 번째 행 저장
        first_idx = [i if (board[i][j] != 0) and (first_idx[j] == -1) else first_idx[j] for j in range(0,leng)]
    
    
    for move in moves: #move iter
        idx = move -1 #열
        if first_idx[idx] == leng: #해당 idx의 board가 빈 경우 
            continue
        else:
            r_idx = len(result) -1
            current = board[first_idx[idx]][idx] #인형

            if current == result[r_idx]: #result라는 바구니 맨 위에 있는 거랑 같은 경우 
                result.pop()
                
                cnt += 2 #사라지는 인형 개수 2개 추가
            else: #같지 않은 경우 result에 추가
                result.append(current)
                    
            first_idx[idx] += 1 #해당 열의 행 + 1
            
    
    return cnt

# [1,5,3,5,1,2,1,4]