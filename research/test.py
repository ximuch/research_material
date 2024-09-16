import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import os
list_file=[]
text_path='D:/pythonProjects/画图测试/2023.8/'
for txt_dir in os.listdir(text_path):
    print(txt_dir)
    for txt_file in os.listdir(text_path+txt_dir):
        if txt_file.endswith('.txt'):
            # 如果是 .txt 文件，则提取
            list_file.append(text_path+txt_dir+'/'+txt_file)

        print(list_file)




