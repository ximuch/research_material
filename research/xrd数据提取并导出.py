import pandas as pd

def txt_to_excel(txt_path, excel_path):
    # 读取TXT文件内容
    try:
        with open(txt_path, 'r', encoding='utf-8') as file:
            # lines = file.readlines()
            file_data = file.read().split('[Data]')[1]

        col_list1 = []
        col_list2 = []
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

    # 将TXT文件的内容转换为DataFrame
    data = {'2theta': col_list1, 'Intensity': col_list2}
    excel_data = pd.DataFrame(data)
    # 将DataFrame写入Excel文件
    excel_data.to_excel(excel_path, index=False)

# 使用函数
txt_file = "D:/pythonProjects/input.txt" # 输入的xrd txt文件名
excel_file = 'D:/pythonProjects/output.xlsx'  # 输出的Excel文件名
txt_to_excel(txt_file, excel_file)







