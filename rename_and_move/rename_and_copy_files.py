import os
import shutil

def rename_and_copy_files(source_directory, target_directory):
    count = 1
    '''
    将文件夹及其子文件夹中的文件先重命名，再复制提取到另外一个文件夹中
    '''
    # 创建目标文件夹
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    
    # 递归遍历源文件夹及其子文件夹
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if file.split('.')[-1].lower() == ".m4a":  # 判断文件扩展名
                source_path = os.path.join(root, file)
                new_name = f"audio{count}.m4a"
                renamed_path = os.path.join(root, new_name)
                
                os.rename(source_path, renamed_path)  # 重命名文件
                target_path = os.path.join(target_directory, new_name)
                shutil.copy(renamed_path, target_path)  # 复制重命名后的文件
                count += 1

# 示例使用
source_directory = 'E:\\video\\bilibili'  # 替换为你的源文件夹路径
target_directory = 'E:\\video\\audio'  # 替换为你的目标文件夹路径

rename_and_copy_files(source_directory, target_directory)