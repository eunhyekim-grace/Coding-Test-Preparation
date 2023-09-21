def solution(s):
    # li = ' '.join(s.split()) #다중 공백 -> 공백 1개로 치환
    li = s.split(' ') #string -> list

    
    
    answer = ["" if i == "" else i[0].upper() + i[1:].lower() for i in li]
    answer = ' '.join(answer)
    return answer