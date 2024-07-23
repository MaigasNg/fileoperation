import os

def suffix_change(directory, old_extension, new_extension):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path) and file.endswith(old_extension):
            new_file_path = os.path.splitext(file_path)[0] + new_extension
            os.rename(file_path, new_file_path)

# 示例使用
directory = 'E:\\video\\audio'  # 替换为你的目标文件夹路径
old_extension = '.m4a'  # 替换为你想要更改的旧后缀
new_extension = '.mp3'  # 替换为你想要更改的新后缀

suffix_change(directory, old_extension, new_extension)

