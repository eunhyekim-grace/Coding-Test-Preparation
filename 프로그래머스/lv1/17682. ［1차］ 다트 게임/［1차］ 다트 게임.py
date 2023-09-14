def solution(dartResult):
    nums = []
    num_idx = 0
    tens = 0
    for idx, i in enumerate(dartResult):
        try:
            if (i == '0') and (dartResult[idx-1] == '1'):
                nums[-1] *= 10
                tens += 1
            else:
                nums.append(int(i))
        except:
            if i == 'S':
                num_idx += 1
            elif i == 'D':
                nums[num_idx] = nums[num_idx] ** 2
                num_idx +=1
            elif i == 'T':
                nums[num_idx] = nums[num_idx] ** 3
                num_idx += 1
            elif i == '#':
                nums[num_idx-1] *= -1
            elif i == '*':
                if num_idx -1 == 0:
                    nums[0] *= 2
                else:
                    nums[num_idx-1] *= 2
                    nums[num_idx-2] *= 2
            else:
                continue
            
    return sum(nums)