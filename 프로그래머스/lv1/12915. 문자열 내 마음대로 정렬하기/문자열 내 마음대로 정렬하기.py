def solution(strings, n):
    answer = []

    string_dict = {}
    for word in strings:
        if string_dict.get(word[n]) != None:
            if type(string_dict[word[n]]) == list:
                string_dict[word[n]].append(word)
            else:
                temp = [string_dict[word[n]]]
                temp.append(word)
                string_dict[word[n]] = temp
        else:
            string_dict[word[n]] = word
    
    sorted_str = sorted(string_dict.keys())
    for i in sorted_str:
        if type(string_dict[i]) == list:
            temp = sorted(string_dict[i])
            for string in temp:
                answer.append(string)
        else:
            answer.append(string_dict[i])
                
    
    return answer