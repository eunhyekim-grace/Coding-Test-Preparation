def solution(quiz):
    answer = []
    for i in quiz:
        eq = i.split()
        if eq[1] == '+':
            if int(eq[0]) + int(eq[2]) == int(eq[4]):
                answer.append('O')
            else:
                answer.append("X")
        else:
            if int(eq[0]) - int(eq[2]) == int(eq[4]):
                answer.append("O")
            else:
                answer.append("X")
                
    return answer