import os
import json
import glob

def read_name_from_first_three_records(directory):
    # 遍历指定目录中的所有 JSON 文件
    json_files = glob.glob(os.path.join(directory, '*.json'))
    total_physical_lines = 0

    for file in json_files:
        filename = f" {os.path.basename(file)}"
        try:
            # 打开并读取 JSON 文件
            with open(file, 'r', encoding='utf-8') as f:
                total_physical_lines = sum(1 for _ in f)
                print(f"Filename,Name,LineCnt")
            
            with open(file, 'r', encoding='utf-8') as f:
                data = json.load(f)

                # 处理列表类型 JSON
                if isinstance(data, list):
                    for i, entry in enumerate(data[:3]):  # 遍历前三条记录
                        if isinstance(entry, dict) and 'name' in entry:
                            print(f"{filename},{entry['name']},{total_physical_lines} ")

                # 处理字典类型 JSON
                elif isinstance(data, dict):
                    items = list(data.items())[:3]  # 获取前三个键值对
                    for i, (key, value) in enumerate(items):
                        if key == 'name':
                            print(f"{filename},{value},{total_physical_lines} ")

        except Exception as e:
            print(f"读取文件时发生错误: {e}")
        print('-' * 50)

# 调用函数并传入目录路径
directory = "D:\\03.Nec工作\\读取json文件\\Test"  # 替换为实际目录路径
read_name_from_first_three_records(directory)
