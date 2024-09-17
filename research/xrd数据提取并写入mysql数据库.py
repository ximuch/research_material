import os
import json
import pymysql
import re

"""
尝试插入json文件到 MySQL 数据库。
dbInfo: MySQL数据库信息
table_name:  MySQL数据中表名
table_items_obj:  MySQL数据中表头各项名称
json_directory_path: 本地的json文件路径
"""
dbInfo = {
    'host': '123.60.146.92',
    'port': 3306,
    'user': 'root',
    'password': 'Chenximu520',
    'db': 'research'
}

table_name = 'experience'

table_items_obj = ('time', 'mass', 'result', 'count', 'test' )
json_directory_path = os.getcwd()


def connect_to_database(host, port, user, password, database):
    """
    尝试连接到 MySQL 数据库并返回连接对象和状态。

    :param host: 数据库主机地址
    :param port: 数据库端口号
    :param user: 数据库用户名
    :param password: 数据库密码
    :param database: 要连接的数据库名
    :return: (connection) - 连接对象
    """
    connection = None
    status_message = "数据库尝试连接...\n"

    try:
        # 尝试连接到数据库
        connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        status_message = status_message+"数据库连接成功\n"

        # 检查连接状态
        if connection.open:
            status_message = status_message+"检查数据库状态：已连接\n"
        else:
            status_message = status_message+"检查数据库状态：未连接\n"

    except pymysql.err.OperationalError as e:
        # 捕获连接错误
        status_message = status_message+f"连接数据库错误: {e}"+'\n'
    print(status_message+'\n')
    return connection


def close_database_connection(connection):
    """
    关闭数据库连接。

    :param connection: 数据库连接对象
    """
    if connection and connection.open:
        connection.close()
        print("数据库连接已关闭")
    else:
        print("数据库连接已关闭或数据库对象无效")

def insert_one_data_to_database(connection,table_name,table_items,table_values):

    """
    插入一条数据到数据库

    :param connection: 数据库连接对象
    :param table_name: 数据库表名
    :param table_values:表头项名称
    :param table_values:表数据各项的值
    """

    if not(connection and connection.open):
        print("数据库连接已关闭或数据库对象无效")
        return None

    print('table_name:',table_name)
    print('table_items:', table_items)
    print('table_values:', table_values)

    """
    #table_items = ('productID', 'productName', 'price', 'nums', 'date')
    #sql_table_items='(productID, productName, price, nums, date)'
    """
    sql_table_items = f"({', '.join(table_items)})"

    """
    #table_values = ('00004', '桔子', 9.88, 10, '2024-08-18 11:03:02)
    #sql_table_values='(%s, %s, %s, %s, %s)'
    """
    # 生成占位符
    sql_table_values="("
    for index, value in enumerate(table_values):
        if index == len(table_values) - 1:
            sql_table_values += '%s)'
        else:
            sql_table_values += '%s,'

    """
    table_name=sales
    sql_table_items='(productID, productName, price, nums, date)'
    sql_insert_cmd=
        INSERT INTO sales  (productID, productName, price, nums, date) 
        VALUES (%s, %s, %s, %s, %s)
    """
    sql_insert_cmd = "INSERT INTO "+table_name+" "+sql_table_items+"\n"+"VALUES "+sql_table_values+"\n"

    print('sql insert cmd:', sql_insert_cmd)
    try:
        with connection.cursor() as cursor:
            # 执行插入操作
            cursor.execute(sql_insert_cmd, table_values)
            # 提交事务
            connection.commit()
            print("sql插入数据命令执行，数据插入成功")
    except pymysql.err.OperationalError as e:
        print(f"sql插入数据命令执行,插入数据错误: {e}")

def get_json_data(data, indent=0,infileName=None,connection=None):
    """
    递归遍历 JSON 数据并打印每个键值对。
    :param data: JSON 数据（字典或列表）。
    :param indent: 当前层级的缩进级别。
    """

    # 示例字符串
    filename = "current_version2024_01_02.txt"

    # 使用正则表达式提取时间信息
    new_date_string = ''
    match = re.search(r'(\d{4})_(\d{2})_(\d{2})', filename)
    if match:
        year, month, day = match.groups()
        # 重新组成时间字符串，例如 "2024-01-02"
        new_date_string = f"{year}-{month}-{day}"
        print(new_date_string)
    else:
        print("No date found")

    values = []
    for category, stores in data.items():
        for store, platforms in stores.items():
            for platform, details in platforms.items():
                for key, value in details.items():
                    values.append((category, store, platform, key, value,infileName,new_date_string))
    print(values)
    for value in values:
        insert_one_data_to_database(connection,table_name,table_items_obj, value)
    return values


def read_json_files(directory,connection):
    """
    读取目录下所有 JSON 文件并打印其内容
    :param directory: 目录路径
    """
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            print(f"\n匹配.txt文件成功===========Reading file:============= {filename}")
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                    print(f"\n===========Reading file:============= {filename}")
                    in_indent = 0
                    get_json_data(data, in_indent, filename, connection)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON from file {filename}: {e}")
        else:
            print(f"\n非.txt文件，跳过处理===========Ignore file:============= {filename}")





if __name__ == "__main__":
    connect_obj=connect_to_database(dbInfo['host'],dbInfo['port'],dbInfo['user'],dbInfo['password'],dbInfo['db'])
    # items_obj = ('productID', 'productName', 'price', 'nums', 'date')
    # values_obj = ('000010', '桔子', 9.88, 10, '2024-08-18 11:03:02')
    # insert_one_data_to_database(connect_obj,'sales',items_obj,values_obj)
    # 指定你的目录路径

    # print(f"\n处理从文件插入数据的目录:",json_directory_path)
    values = [('2019-02-02 13:09:09', 9.88, '是', 1,'sem'),
              ('2009-02-02 13:09:09', 200, 'success', 8, 'sem') ]
    for value in values:
        insert_one_data_to_database(connect_obj,table_name,table_items_obj, value)
    # read_json_files(json_directory_path,connect_obj)
    # 调用函数读取和处理 JSON 文件
    # read_and_process_json(r'.\current_version2024_01_01.txt')


    close_database_connection(connect_obj)