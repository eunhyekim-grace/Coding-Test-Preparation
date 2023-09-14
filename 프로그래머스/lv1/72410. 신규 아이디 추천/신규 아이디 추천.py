import re

def solution(new_id):
    
    lst = new_id.lower()
    lst = re.sub(r'[^a-z0-9-_.]', '', lst)
    print(lst)
    
    lst2 = [list(lst)[0]]
    for char in lst[1:]:
        idx = len(lst2) -1
        if char == '.' and lst2[idx] == '.':
            continue
        else:
            lst2.append(char)
    
    
    if len(lst2) == 1 and lst2[0] == '.':
        lst2 = ['a']
    else:
        while lst2[0] == '.':
            lst2 = lst2[1:]
        while lst2[-1] == '.':
            lst2 = lst2[:-1]
    
    if len(lst2) >= 16:
        lst2 = lst2[:15]
        while lst2[-1] == '.':
            lst2 = lst2[:-1]
    
    if len(lst2) <= 2:
        lst2 = lst2 + [lst2[-1]] * (3 - len(lst2))
        

    answer = ''.join(lst2)
    return answer