import re

def getbin(num): #정수를 2진수로 변환해서 0b 빼고 리턴
    binnum = bin(num)
    return binnum[2:]

def solution(s):
    answer = []
    cnt = 0
    zero_cnt = 0
    
    while s != '1':
        temp = sum([1 for i in s if i == '0'])
        leng = len(re.sub('0', '',s))
        s = getbin(leng)
        cnt += 1
        zero_cnt += temp
    
    return [cnt, zero_cnt]