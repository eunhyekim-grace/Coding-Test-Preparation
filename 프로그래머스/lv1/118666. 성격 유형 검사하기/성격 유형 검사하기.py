def solution(survey, choices):
    scores = {1:3, 2:2, 3:1, 4:0, 5:1,6:2,7:3}
    types = {}
    
    for ty, c in zip(survey, choices):
        # print(ty, c)
        if c == 4:
            continue
        else:
            t = ty[0] if c < 4 else ty[1]
            # print(t)
            if t in types.keys():
                types[t] += scores.get(c)
            else:
                types[t] = scores.get(c)
    
    print(types)
    # 'R' 'T' comp
    # T 나오는 경우 
    #1 'T' > 'R' (cond : 'R', 'T' 둘 다 존재)
    #2 'T' 만 존재
    #3 'R', 'T' 둘다 없음 -> R
    answer = ['R' if 'R' not in types and 'T' not in types or 'T' not in types or 'R' in types and 'T' in types and types.get('T') <= types.get('R') else 'T'] 
    answer.append('C' if 'C' not in types and 'F' not in types or 'F' not in types or 'C' in types and 'F' in types and types.get('F') <= types.get('C') else 'F')
    answer.append('J' if 'J' not in types and 'M' not in types or 'M' not in types or 'J' in types and 'M' in types and types.get('M') <= types.get('J') else 'M')
    answer.append('A' if 'A' not in types and 'N' not in types or 'N' not in types or 'A' in types and 'N' in types and types.get('N') <= types.get('A') else 'N')
    # print(answer)
    
    
    # answer = ''
    return ''.join(answer)