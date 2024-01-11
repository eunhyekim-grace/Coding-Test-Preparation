def solution(bandage, health, attacks):
    
    current_health = health
    cont_t = 0
    #변수 지정 
    t = bandage[0]
    x = bandage[1]
    y = bandage[2]
    # 공격이 일어나는 시간: 데미지 형식의 dict 생성
    damage_dict ={i[0]: i[1] for i in attacks}

    # 1 sec ~ max sec(마지막 공격이 발생하는 시간/초) 까지 
    for i in range(1, attacks[-1][0]+1):
        if i in damage_dict:
            cont_t = 0 # 연속 치유 시간 0으로 초기화
            current_health -= damage_dict.get(i) # 공격 받은 경우 체력 -
            #공격 받은 이후 남은 체력이 0 이하인 경우 -1 return
            if current_health <= 0:
                return -1
        else:
            #현재 체력이 최대 체력인 경우
            if current_health == health:
                continue
            #연속 붕대 감기시 추가 체력을 부여하는 시간이 1초인 경우
            if t == 1:
                current_health += (x+y)
            else:
                cont_t +=1
                # 연속 붕대 감기에 성공한 경우 
                if cont_t == t:
                    cont_t = 0 #연속 붕대 감기 시간 초기화
                    current_health += (x+y)
                else: #연속 붕대 감기에 실패한 경우
                    # cont_t += 1
                    current_health += x
            # print(i, current_heath, cont_t)
            #추가로 회복한 체력이 최대 체력 보다 높은 경우 최대 체력으로 맞춰줌
            current_health = health if current_health > health else current_health 
    return current_health

# question
## t sec + x life 
## continuous t -> + y life
## max life O
## spell - attacked => spell cancel + heal X + damaged
## if life <= 0 => dead = heal X
## after spell / cancelled -> healling + continuous reset
## whether the character can live till the end with the given information

# variable
## bandange (1d - list) -> healing time , 1 sec per x life, y life = [t, x, y]
## health (idx) -> max life
## attacks (2d - list) -> monster's attack time, damage = [time, damage]

# return
## solution (idx) -> health after every attack
## if character dead during the attack return -1