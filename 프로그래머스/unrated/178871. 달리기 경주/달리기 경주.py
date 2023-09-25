import time

def solution(players, callings):
    # player_dict = {}
    # for idx, name in enumerate(players):
    #     player_dict[name] = idx
    

    # lst = player_dict.values()
    # print(lst)
    # #print(help(dict.update))
    # print(player_dict)
    # #leng = len(callings)
    # #i = 0
    # #while leng > i:
    # #    temp = callings[i]

#     answer = players

#     for name in callings:
#         idx = answer.index(name)
#         answer.remove(name)
#         answer.insert(idx-1, name)


    #같은거 묶어서 list - pop / insert로 해결
    
    # answer = players
    # pn = callings[0]
    # cnt = 1
    
#     for name in callings[1:]:
#         if name == pn:
#             cnt += 1
#         else:
#             # print(pn)
#             idx = answer.index(pn)
#             answer.pop(idx)
#             answer.insert(idx - cnt, pn)
#             pn = name
#             cnt = 1
#     # print(pn, cnt, answer)
#     idx = answer.index(pn)
#     answer.pop(idx)
#     answer.insert(idx - cnt, pn)


    #같은거 묶어서 dict - pop / insert로 해결
#     p_dict = {name: idx for idx, name in enumerate(players)}
#     # print(p_dict)
#     for name in callings[1:]:
#         if name == pn:
#             cnt += 1
#         else:
#             cur = p_dict[pn]
#             # print([name for name, idx in p_dict.items() if idx >= cur or idx < cur- cnt])
#             # p_dict = {name: idx+cnt -1}
#             # print([name for name, idx in p_dict.items() if idx< cur and idx >= cur - cnt])
#             p_dict = {name: idx if idx >cur or idx < cur-cnt else idx+1 if idx== cur-cnt and cnt== 1 else idx+cnt-1 for name, idx in p_dict.items()}
#             p_dict[pn] = cur - cnt
#             # print(p_dict)
#             cnt = 1
#             pn = name
    
#     cur = p_dict[pn]
#     p_dict = {name: idx if idx >cur or idx < cur-cnt else idx+1 if idx== cur-cnt and cnt== 1 else idx+cnt-1 for name, idx in p_dict.items()}
#     p_dict[pn] = cur -cnt
    
#     # print(p_dict)
#     # answer = [i[0] for i in sorted(p_dict.items(), key = lambda x: x[1])]
#     answer = sorted(p_dict.keys(), key = lambda x: p_dict[x])
    
    players_dict = {key: idx for idx, key in enumerate(players)}
    for name in callings:
        cur = players_dict[name]
        # prev = [key for key, val in players_dict.items() if val == cur -1][0]
        # players_dict[prev] += 1
        players_dict[name] -= 1
        players_dict[players[cur -1]] += 1
        
        players[cur], players[cur -1] = players[cur-1], name
    
    # cur = time.time()
    # rev = {val:key for key, val in players_dict.items() if val < 2}
    # # rev = dict(map(reversed, players_dict.items()))
    # end = time.time()
    # print(end - cur)
    # print(players_dict)
    # answer = [key for (key, value) in sorted(players_dict.items(), key = lambda x: x[1])]
    # print(players, players_dict)
    # answer = 0
    return players