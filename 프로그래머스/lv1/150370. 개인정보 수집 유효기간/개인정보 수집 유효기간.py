def solution(today, terms, privacies):
    dur = {val[0]:int(val[2:]) for val in terms}

    answer = []
    ty, tm, td = int(today[:4]), int(today[5:7]), int(today[8:])
    
    for idx, privacy in enumerate(privacies):
        py, pm, pd, term = int(privacy[:4]), int(privacy[5:7]), int(privacy[8:10]), privacy[-1]
        term_dur = dur.get(term)

        ed = pd + 27 
        em = pm + term_dur if ed >= 29 else pm + term_dur-1
        
        if em >13 and em % 12 == 0:
            # print('t')
            ey = py + int(em / 12) -1
        else:
            ey = py if em < 13 else py + int(em / 12)
        
        em = 12 if em%12 == 0 else em%12
        ed = 28 if ed%28 == 0 else ed%28
        # print('E: ',ey, em, ed)
        # print('T: ',ty, tm, td)
        
        # if ey < ty or ey >= ty and em < tm or ey >= ty and em >= tm and ed < td:
        if ey < ty:
            # print(1)
            answer.append(idx+1)
        elif ey == ty and em < tm:
            # print(2)
            answer.append(idx +1)
        elif ey == ty and em == tm and ed < td:
            # print(3)
            answer.append(idx+1)
        
    
    
    return answer