def solution(s):
    answer = True
    
    if s[0] == ')':
        return False
    else:
        stack = [s[0]]
        for i in s[1:]:
            if len(stack) != 0 and i == ')':
                stack.pop()
            else:
                stack.append(i)
        
        if len(stack):
            return False
        else:
            return True
    # return True