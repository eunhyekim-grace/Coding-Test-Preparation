def solution(food):
    answer = []
    for i in range(1,len(food)): #물을 제외한 각 음식의 수를 2로 나눠 몫을 배열에 append
        num = int(food[i]/2)
        answer.append(f'{i}'*num)
        
    answer = answer + answer[::-1] #배열 순서를 뒤집어 append - 상대방 음식 순서
    answer.insert(int(len(answer)/2), '0') # 가운데 0 = 물 insert
    
    return ''.join(answer)