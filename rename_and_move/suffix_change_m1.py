import os

def suffix_change(directory, old_extension, new_extension):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path) and file.endswith(old_extension):
            new_file_path = os.path.splitext(file_path)[0] + new_extension
            os.rename(file_path, new_file_path)

# 示例使用
directory = 'E:\\video\\audio'  # 替换为你的目标文件夹路径
old_extension = '.m4s'  # 替换为你想要更改的旧后缀
new_extension = '.mp3'  # 替换为你想要更改的新后缀

suffix_change(directory, old_extension, new_extension)




# 获取当前目录下所有文件
file_list = os.listdir('.')
for file in file_list:
    if file.endswith('.m4a'):
        # 构建新文件名
        new_name = file.replace('.m4a', '.mp3')
        # 重命名文件
        os.rename(file, new_name)

"""
这段代码当前只能遍历指定目录下的直接子文件!!
这段代码首先列出当前目录下所有文件，然后遍历文件列表，对于以 ".m4a" 结尾的文件，使用 replace 方法将 ".m4a" 替换为 ".mp3"，最后使用 os.rename 方法重命名文件。请确保在执行此代码前备份您的文件，以防止意外损失。
"""