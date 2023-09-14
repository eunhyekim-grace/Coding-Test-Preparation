
import numpy as np
def make_one(leng): #1번 생성
    temp = [1,2,3,4,5]
    if leng > len(temp):
        temp = temp * int((leng/len(temp))+1)
    return temp[:leng]

def make_two(leng): #2번 생성
    temp = [2,1,2,3,2,4,2,5]
    if leng > len(temp):
        temp = temp * int((leng/len(temp)) +1 )
    return temp[:leng]
    
def make_three(leng): #3번 생성
    temp = [3,3,1,1,2,2,4,4,5,5]
    if leng > len(temp):
        temp = temp * int((leng/len(temp))+1)
    return temp[:leng]

def solution(answers):
    leng = len(answers)
    
    one = make_one(leng)
    two = make_two(leng)
    three = make_three(leng)

    cnt1 = 0; cnt2 = 0; cnt3 = 0
    for a,b,c,ans in zip(one,two, three, answers): #비교 해서 점수 할당
        if a == ans:
            cnt1 +=1
        if b == ans:
            cnt2 += 1
        if c == ans:
            cnt3 += 1
            
    cnt = [cnt1,cnt2,cnt3]
    answer = []
    for idx, c in enumerate(cnt): #제일 많이 맞춘 사람만 answer에 넣기
        if c == max(cnt):
            answer.append(idx+1)
            
    return answer