from itertools import chain

def solution(id_list, report, k):
    #1번에 1명 - 횟수 제한 X, 동일 유저 신고 -> 1번
    #k번 이상 신고 -> 정지, 메일 발송
    #마지막에 한 번에 처리
    
    report_user = {}
    report_num = {}
    
    for i in report:
        user, rep = i.split(' ')
        if rep in report_user:
            if user in report_user.get(rep):
                continue
            else:
                report_user[rep].append(user)
                report_num[rep] += 1
        else:
            report_user[rep] = [user]
            report_num[rep] = 1
    
    report_num = {user:num for user, num in report_num.items() if num >= k}
    print(report_num)
    if len(report_num) == 0:
        return [0]* len(id_list)
    else:
        answer = {name: 0 for name in id_list}
        # li = [report_user[name] for name in report_num.keys()]
        for i in list(chain(*[report_user[name] for name in report_num.keys()])):
            answer[i] += 1
        # for i in chain(*)
        return list(answer.values())
        
        # return 0
    # answer = []
    # return answer