import os
import shutil

"""
把这些文件都拷贝出来放在一个目录下，也就是把这些文件都抽离出来，方便查看。
"""
# 将一个文件夹中的所有文件（包括子文件夹），拷贝到另一个文件夹中，去除子文件夹。
def copyfile_to_onedir(srcpath, dstpath):
    # 遍历源文件夹，得到根目录，子目录和文件名列表
    for root, dirs, files in os.walk(srcpath, topdown=True):
        counter = 0
        #获取文件名依次遍历
        for name in files:
            # 如果该文件在目标目录中已经存在，也就是重复文件，则给文件重命名，否则无法拷贝。
            if os.path.exists(dstpath + '\\' + name):
                counter += 1
                # 获取文件名
                filename = name[0: name.rindex('.')]
                # 获取文件类型（后缀）
                filetype = name[name.rindex('.') + 1: ]
                # 将文件名重命名后，拷贝到目标文件夹，注意，copy的两个参数都要是绝对路径的完整文件名
                shutil.copy(os.path.join(root, name), dstpath + '\\' + filename + str(counter) + '.' + filetype)
            else:
                # 如果该文件未重复，那就直接拷贝就好。
                shutil.copy(os.path.join(root, name), dstpath + '\\' + name)
 
# copyfile_to_onedir('F:\\新建文件夹', "G:\\新建文件夹1")