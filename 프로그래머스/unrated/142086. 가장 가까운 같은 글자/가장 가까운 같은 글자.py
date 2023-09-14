def solution(s):
    string_dict = {}
    answer = []
    
    for idx, string in enumerate(s):
        if string_dict.get(string) == None:
            answer.append(-1)
            string_dict[string] = idx
        else:
            answer.append(idx - string_dict[string])
            string_dict[string] = idx
    
    return answer