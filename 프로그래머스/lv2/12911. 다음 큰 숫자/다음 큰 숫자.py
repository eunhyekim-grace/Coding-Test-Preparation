def solution(n):
    binary = bin(n)[2:]
    ones = binary.count('1')
    # print(ones)
    leng = len(binary) +1
    answer = 0
    for num in range(n+1, int('1'*leng,2)):
        if bin(num)[2:].count('1') == ones:
            answer = num
            break
            
    return answer