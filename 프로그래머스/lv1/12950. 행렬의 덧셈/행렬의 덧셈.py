def solution(arr1, arr2):
    r = len(arr1)
    c = len(arr1[0])
    
    answer = []
    for i in range(r):
        temp = []
        for j in range(c):
            temp.append(arr1[i][j] + arr2[i][j])
        answer.append(temp)
    
    # answer = [[]]
    return answer