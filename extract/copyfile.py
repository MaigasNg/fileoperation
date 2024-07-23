import os
import shutil

"""
    你有一个文件夹，里面有很多文件，包括很多多级的子目录。查阅起来挺麻烦，你想知道这些子文件夹里到底有哪些文件
"""
def copyfile(srcpath, dstpath):
    # 如果目标根目录不存在，则创建目标根目录。
    if not os.path.exists(dstpath):
        os.makedirs(dstpath)
    # 遍历源文件夹，得到根目录，子目录和文件名列表
    for root, dirs, files in os.walk(srcpath, topdown=True):
        # 将目录中根目录部分换成目标目录
        path = root.replace(srcpath, dstpath)
        # 在目标目录中,建立与源目录一样的目录体系
        for dir in dirs:
            if not os.path.exists(os.path.join(path, dir)):
                os.makedirs(os.path.join(path, dir))
        #获取文件名依次遍历
        for name in files:
            # 拷贝文件。
            shutil.copy(os.path.join(root, name), os.path.join(path, name))
 
srcpath = 'G:\\dir'
dstpath = 'G:\\dir4'
copyfile(srcpath, dstpath)