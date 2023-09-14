import queue

def solution(s):
    q = queue.Queue()
    for i in s:
        q.put(i)
        
    cnt = 0
    dict = {}
    for i in range(q.qsize()):
        if len(dict) == 0:
            main = q.get()
            dict[main] = 1
            dict['other'] = 0
        else:
            other = 'other' if q.get() != main else main
            dict[other] += 1
            if dict.get(main) == dict['other']:
                dict = {}
                cnt+=1
    if len(dict) != 0:
        cnt +=1

    return cnt