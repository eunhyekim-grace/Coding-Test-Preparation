def chartoint(num,num_dict):
    leng = [3,4,5]
    for i in leng:
        if num[:i] in num_dict:
            return i, num_dict[num[:i]]

def solution(s):
    num_dict = {}
    eng_num = ['zero', 'one', 'two', 'three','four','five','six', 'seven', 'eight','nine']
    
    for i in range(10): #영단어와 해당하는 숫자를 매칭하는 dict 생성
        num_dict[eng_num[i]] = i
    
    answer = []
    idx = 0
    
    while True:
        if idx == len(s): #문자열의 길이와 index가 같으면 while문 종료
            break
        elif s[idx].isdigit() == True: #문자열의 해당 idx가 숫자면 answer에 숫자 append
            answer.append(s[idx])
            idx += 1
        else: #영어 단어인 경우 chartoint함수에 대입
            a, num = chartoint(s[idx:],num_dict)
            idx+=a
            answer.append(str(num))
            
    
    return int(''.join(answer))