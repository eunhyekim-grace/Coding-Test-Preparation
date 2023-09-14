import pandas as pd
import numpy as np
from collections import Counter

def solution(board):
    board = np.array(board)
    c = Counter(board.reshape(-1)) #board에서 0,1의 개수 파악
    
    if c[1] == board.size: #배열이 모두 1로 차있는 경우 = 안전지역이 없는 경우
        answer = 0
    else:
        temp = np.where(board == 1) #폭탄의 위치 탐색
        one_rows = temp[0] #폭탄의 위치 - 행
        one_cols = temp[1] #폭탄의 위치 - 열
        df = pd.DataFrame(board)
        for r, c in zip(one_rows, one_cols): #모든 폭탄에 대해 한 번 씩
            df.loc[r-1:r +1, c -1 :c +1] = 1 # 주변을 모두 1로 변경
        safety_zone = np.array(df)
        answer = Counter(safety_zone.reshape(-1))[0] #safety_zone 배열의 0 개수 
    
    return answer