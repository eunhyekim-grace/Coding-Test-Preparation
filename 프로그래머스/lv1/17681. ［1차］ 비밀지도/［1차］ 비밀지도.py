def getbin(num): #정수를 2진수로 변환해서 0b 빼고 리턴
    binnum = bin(num)
    return binnum[2:]
    
def getmap(m, arr1, arr2): #arr1과 arr2의 각 수를 or 비트 연산 실행 후 2진수 결과값을 map에 저장해 리턴
    for num1, num2 in zip(arr1, arr2):
        binstr = getbin(num1 | num2)
        m.append([i for i in binstr])
    return m

def solution(n, arr1, arr2):
    m = []
    m = getmap(m, arr1, arr2)
    answer = []
    for line in m: #map의 요소가 1이면 '#'(벽)으로 0이면 ' '(공백)으로 변환
        temp = ''.join(['#' if i == '1' else ' ' for i in line])
        if len(temp) < n: #만약 한 줄의 길이가 정해진 map의 크기와 맞지 않을 경우 앞에 공백을 넣어 길이 맞춤
            temp = ' ' * (n - len(temp)) +temp
        answer.append(temp)
    return answer