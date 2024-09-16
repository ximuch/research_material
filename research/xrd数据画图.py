import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import os


def txt_resolve(txt_path):
    # 读取TXT文件内容
    col_list1 = []
    col_list2 = []
    try:
        with open(txt_path, 'r', encoding='utf-8') as file:
            file_data = file.read().split('Angle,       PSD,')[1]

        # 数据提取并处理
        for line in file_data.split('\n'):
            col_tmp = []
            if line.strip() == '':
                continue
            for col in line.split(','):
                col_strip = col.strip()
                if col_strip == '':
                    continue
                col_tmp.append(col_strip)
            if len(col_tmp) > 0:
                col_list1.append(col_tmp[0])
                if len(col_tmp) > 1:
                    col_list2.append(col_tmp[1])
    except Exception as e:
        print(f"Error processing file: {e}")
        pass
    return col_list1, col_list2


# 画图的函数
# 注意：我从处理另一个实验数据的脚本中拷贝了部分代码，所以变量名有些奇怪
def draw(theta2, intensity, label, line_color):
    theta2_list = np.array(theta2)
    intensity_list = np.array(intensity)
    plt.figure(1)
    plt.plot(theta2_list, intensity_list, color=line_color, label=label, lw=2)

# 定义一个分割文本列的函数
# 这 step 变量有的作用：增加纵坐标的值，便于区分图线
def split_txt(txt, step=0):
    a = []
    b = []

    col_list1, col_list2 = txt_resolve(txt)
    for l1 in col_list1:
        m=float(l1)
        a.append(m)
    for l2 in col_list2:
        n= float(l2)
        n += step
        b.append(n)
    return a, b

# 建立一个 Figure 对象
fig = plt.figure(1, figsize=(24, 12))
# 设置全局字体为Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'
# count 的值传给 draw 函数中的 step 变量，
# 达到「增加纵坐标的值，便于区分图线」的目的
count = 0
list_file=[]
text_path='D:/pythonProjects/画图测试/2023.8/'
# 我准备了多种不同图线的颜色
colors = ['red', 'blue', 'green', 'black', 'orange', 'pink', 'purple']
for txt_dir in os.listdir(text_path):
    print(txt_dir)
    for txt_file in os.listdir(text_path+txt_dir):
        if txt_file.endswith('.txt'):
            # 如果是 .txt 文件，则提取
            list_file.append(text_path+txt_dir+'/'+txt_file)
for txt_file, color in zip(list_file, colors):
    x_list, y_list = split_txt(txt_file, step=count)
    name = os.path.splitext(os.path.basename(txt_file))[0]
    draw(x_list, y_list, name, color)
    count += 4000


# 设置图像的参数
# 横坐标文本
plt.xlabel('2θ (degree)', fontsize=24)
# 纵坐标文本
plt.ylabel('Intensity (a.u.)', fontsize=24)
# 图像名字
plt.title('XRD Figure')
# 设置纵坐标最小刻度
plt.gca().xaxis.set_minor_locator(MultipleLocator(10))
ax = plt.gca()  # 获取当前的Axes对象
ax.set_yticks([])  # 设置纵坐标刻度为空，即不显示刻度值
# 设置刻度标签的字体大小为22
ax.tick_params(axis='both', which='major', labelsize=22)
# 设置边框粗细为2
for spine in ax.spines.values():
    spine.set_linewidth(2)
plt.xlim(20, 90)
plt.legend()
# 显示图像
plt.show()
# 还可以导出图像
# plt.savefig('../xrd.png')





