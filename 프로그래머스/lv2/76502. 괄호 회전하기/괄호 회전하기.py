from collections import Counter

def solution(s):
    answer = 0
        
    neg = [']', ')', '}']
    
    for i in range(len(s)):
        temp = s[i:] + s[:i]
        
        if temp[0] in neg:
            continue
        else:
            
            chr_stack = [temp[0]]
            # print(chr_stack)
            for chr in temp[1:]:
                # print(chr_stack[-1], chr)
                if (chr not in neg) or len(chr_stack) == 0:
                    chr_stack.append(chr)
                elif chr_stack[-1] == '[' and chr == ']':
                    chr_stack.pop()
                    # print(chr_stack, chr)
                elif chr_stack[-1] == '{' and chr == '}':
                    chr_stack.pop()
                    # print(chr_stack, chr)
                elif chr_stack[-1] == '(' and chr == ')':
                    chr_stack.pop(-1)
                else:
                    chr_stack.append(chr)
            
            answer += 0 if len(chr_stack) >= 1 else 1
        
    
    return answer