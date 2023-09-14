def solution(n, left, right):
    mat = [i+1 if j <= i else j+1 for i in range(int(left/n),int(right /n)+1) for j in range(n)]
    # print(mat)
    l = int(left % n)
    r = n - (int(right % n) + 1)

    if r == 0:
        answer = mat[l:]
    else:
        answer = mat[l:-r]
    
    return answer