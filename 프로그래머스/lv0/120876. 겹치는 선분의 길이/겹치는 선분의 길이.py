# from itertools import combinations

# def solution(lines):
#     s_lines = sorted(lines)
#     combs = list(combinations(s_lines, 2))
    
#     s = []
#     e = []
    
#     for comb in combs:
#         s1, e1 = comb[0][0], comb[0][1]
#         s2, e2 = comb[1][0], comb[1][1]
#         if s2 >= e1:
#             continue
#         else:
#             s = s + [max(s1, s2)]
#             e = e + [min(e1, e2)]
    
#     if len(s) == 0:
#         return 0
#     elif len(s) == 1:
#         return e[0] - s[0]
#     else:
#         s1 = s[0]
#         e1 = e[0]
#         for i in range(1, len(s)):
#             if s[i] > e1:
#                 answer = e1 - s1 + e[i] - s[i]
#                 return answer
#             else:
#                 s1 = min(s1, s[i])
#                 e1 = max(e1, e[i])
#         return e1 - s1

def solution(lines):
    answer = 0
    s1 = set(i for i in range(lines[0][0], lines[0][1]))
    s2 = set(i for i in range(lines[1][0], lines[1][1]))
    s3 = set(i for i in range(lines[2][0], lines[2][1]))
    answer=len((s1 & s2) | (s2 & s3) | (s1 & s3))
    return answer