import os

def suffix_change_m2(file_path,old_suffix,new_suffix):
    """
    这段代码当前只能遍历指定目录下的直接子文件!!
    这段代码首先列出当前目录下所有文件，然后遍历文件列表，对于以 ".m4a" 结尾的文件，使用 replace 方法将 ".m4a" 替换为 ".mp3"，最后使用 os.rename 方法重命名文件。请确保在执行此代码前备份您的文件，以防止意外损失。
    """
    
    # 获取当前目录下所有文件
    file_list = os.listdir(file_path)
    for file in file_list:
        if file.endswith(old_suffix):
            # 构建新文件名
            new_name = file.replace(old_suffix, new_suffix)
            # 重命名文件
            os.rename(file, new_name)


suffix_change_m2('D:/Music','.m4a','.mp3')