# import pandas as pd

def solution(data, ext, val_ext, sort_by):
    
#     분석 - pandas
#     df = pd.DataFrame(data, columns = ['code', 'date', 'maximum', 'remain'])
#     df = df[df[ext] <= val_ext]
#     df.sort_values(by = sort_by, inplace = True)
#     ans = df.values.tolist()


    
    col = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    ans = []
    for i in data:
        if i[col.get(ext)] < val_ext:
            ans.append(i)
    return sorted(ans, key = lambda x: x[col.get(sort_by)])