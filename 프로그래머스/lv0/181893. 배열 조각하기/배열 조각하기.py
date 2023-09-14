def solution(arr, query):
    result = arr
    for idx, num in enumerate(query):
				#index가 짝수나 0이면 해당 인덱스 이후로 다 지우기
        if (idx % 2 == 0) or (idx == 0): 
            result = result[:num+1]
        else: #홀수면 해당 인덱스 전 elem들 다 지우기
            result = result[num:]
    return result