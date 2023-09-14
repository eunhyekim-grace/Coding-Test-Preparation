from itertools import permutations

def solution(numbers):
    computed = []
    #perm = list(permutations(numbers,2))
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i] + numbers[j] not in computed:
                computed.append(numbers[i]+numbers[j])
    return sorted(computed)

#nested for loop 사용
# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             # print(i,j)
#             answer.append(numbers[i] + numbers[j])
#     result = list(set(answer))
#     result = sorted(result)
#     # print(result)
#     return result