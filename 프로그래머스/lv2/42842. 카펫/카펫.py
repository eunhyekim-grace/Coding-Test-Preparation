def solution(brown, yellow):
    # total = brown+ yellow
    
    # 2x + 2y - 4 = brown
    # 2(x+y) = brown +4
    
    # (x-2) * (y -2) = yellow
    # xy -2x-2y +4 = yellow
    # xy - 2(x+y) = yellow -4
    # xy = yellow - 4 + brown +4
    # y = (yellow -4 + brown +4) / x
    
    diff = brown + yellow
    answer = []
    for x in range(brown // 2, 2, -1):
        y = (yellow -4 + brown +4) / x
        if y%1 == 0 and 2*(x+y) == brown + 4 and x>= y:
            answer = [x, int(y)]
        # if y%1 == 0 and x >= y and diff > x - y:
            # diff = x -y
            # answer = [x,int(y)]
        # print(x, y)
        # print(y %1)
    # print(answer)
    return answer


# 14	4	None	[6, 3]
# 18	6	None	[8, 3]
# 20	12	None	[8, 4]
# 22	8	None	[10, 3]
# 24	9	None	[11, 3]
# 24	16	None	[10, 4]
# 26	10	None	[12, 3]