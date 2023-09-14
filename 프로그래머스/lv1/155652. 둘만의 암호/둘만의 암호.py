def solution(s, skip, index):
    
    nums = [chr(i) for i in range(97, 123) if chr(i) not in skip]
    alphabets = {idx: alphabet for idx, alphabet in enumerate(nums)}

    leng = len(nums)
    result = []
    for i in s:
        num = (nums.index(i) + index) % leng
        # print(num)
        result.append(alphabets.get(num))


    return ''.join(result)

