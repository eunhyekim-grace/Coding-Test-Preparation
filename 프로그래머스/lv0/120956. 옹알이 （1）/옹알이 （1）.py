from itertools import permutations, chain

def solution(babbling):
    words = ['aya','ye','woo','ma']
    temp_list = []
    
    for i in range(1, 5):
        temp = list(permutations(words, i))
        temp_list.append(temp)
    temp_list = list(chain(*temp_list))
    
    all_words = []
    for i in temp_list:
        all_words.append(''.join(i))
    
    #print(all_words)
    cnt = 0
    for word in babbling:
        if word in all_words:
            cnt +=1
        else:
            continue
    
    return cnt