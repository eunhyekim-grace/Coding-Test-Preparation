def solution(array, commands):
    answer = []
    for nums in commands:
        i,j,k = nums
        temp = array[i-1:j]
        #print(sorted(temp)[k-1])
        answer.append(sorted(temp)[k-1])
    
    return answer