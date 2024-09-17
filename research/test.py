# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.ticker import MultipleLocator
# # import os
# # list_file=[]
# # text_path='D:/pythonProjects/画图测试/2023.8/'
# # for txt_dir in os.listdir(text_path):
# #     print(txt_dir)
# #     for txt_file in os.listdir(text_path+txt_dir):
# #         if txt_file.endswith('.txt'):
# #             # 如果是 .txt 文件，则提取
# #             list_file.append(text_path+txt_dir+'/'+txt_file)

data = {
    "A": {
        "store1": {"a": {'aa':1, 'ab':2}, "b": {'bb':3, 'bc':4}, "c": {'cc':5, 'cd':6}},
        "store2": {"a": {'aa':7, 'ab':8}, "b": {'bb':9, 'bc':10}, "c": {'cc':11, 'cd':12}}
    },
    "B": {
        "store1": {"a": {'aa':13, 'ab':14}, "b": {'bb':15, 'bc':16}, "c": {'cc':17, 'cd':18}},
        "store2": {"a": {'aa':19, 'ab':20}, "b": {'bb':21, 'bc':22}, "c": {'cc':23, 'cd':24}}
    }
}
# print(data.items())
# [('A', {'store1': {'a': 1, 'b': 2, 'c': 3}, 'store2': {'a': 4, 'b': 5, 'c': 6}}),
#  ('B', {'store1': {'a': 7, 'b': 8, 'c': 9}, 'store2': {'a': 10, 'b': 11, 'c': 12}})]

values = ['A', 'store1', 'a', 'aa', 1, '2243234', '2023-08-01'] # 列表，list
v2 = ('A', 'store1', 'a', 'aa', 1, '2243234', '2023-08-01') # 元组，tuple

print(values[-1])
print(v2[2])
infileName = '2243234'
new_date_string = '2023-08-01'
for category, stores in data.items():
    print('l1', category, stores)
    for store, platforms in stores.items():
        print('l2', store, platforms)
        for platform, details in platforms.items():
            print('l3', platform, details)
            for key, value in details.items():
                print('l4', key, value)
                values.append((category, store, platform, key, value, infileName, new_date_string))

print('values:', values)



