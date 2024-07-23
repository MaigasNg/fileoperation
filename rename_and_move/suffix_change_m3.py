import os


# 如果您需要递归遍历文件夹下的所有子文件夹，您可以使用 os.walk 方法。以下是修改后的代码：
# 遍历目录及子目录下所有文件
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.m4a'):
            # 构建旧文件完整路径
            old_path = os.path.join(root, file)
            # 构建新文件名
            new_name = file.replace('.m4a', '.mp3')
            # 构建新文件完整路径
            new_path = os.path.join(root, new_name)
            # 重命名文件
            os.rename(old_path, new_path)