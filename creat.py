import os
import json

def replace_nulls_in_file(file_path):
    # 读取文件内容
    with open(file_path, 'r') as f:
        content = f.read()

    # 将'"null"'字符串替换为'null'
    content = content.replace('"null"', 'null')

    # 重新写入文件
    with open(file_path, 'w') as f:
        f.write(content)

# 文件夹路径
folder_path = 'json'

# 遍历文件夹及子文件夹中的所有JSON文件
for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        if file_name.endswith('.json'):
            file_path = os.path.join(root, file_name)

            # 替换文件中的'"null"'字符串
            replace_nulls_in_file(file_path)
