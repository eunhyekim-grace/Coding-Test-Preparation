import math
from itertools import combinations

def cal_slope(xy1, xy2):
    #기울기가 같으면 평행
    #직선의 기울기 = y2 - y1 / x2 - x1
    x1, y1 = xy1
    x2, y2 = xy2
    slope = (y2 - y1) / (x2 - x1)
    return abs(round(slope, 3))


def solution(dots):
    idx = list(range(len(dots)))
    
    for i in idx[:-2]:
            other = list(set(idx) ^ set([i, i+1]))
            if cal_slope(dots[i], dots[i+1]) == cal_slope(dots[other[0]], dots[other[1]]):
                return 1
            else:
                continue

    return 0