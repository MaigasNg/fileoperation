import os

def remove_empty_folders(path):
    """
    清理空文件夹和空文件
    :param path: 文件路径，检查此文件路径下的子文件
    :return: None
    """
    files = os.listdir(path)  # 获取路径下的子文件(夹)列表
    for file in files:
        print('遍历路径:', file)
        if os.path.isdir(file):  # 如果是文件夹
            if not os.listdir(file):  # 如果子文件为空
                os.rmdir(file)  # 删除这个空文件夹
        elif os.path.isfile(file):  # 如果是文件
            if os.path.getsize(file) == 0:  # 文件大小为0
                os.remove(file)  # 删除这个文件

if __name__ == "__main__":
    # 执行本文件则执行下述代码
    # 输入路径,尽量使用双斜杠的地址路径，防止转义字符读取错误路径
    path = input("请输入文件夹路径：")  
    remove_empty_folders(path)
    print("清理完成！")
