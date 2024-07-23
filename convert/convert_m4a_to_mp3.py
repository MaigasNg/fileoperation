import os
import subprocess

"""
  要在Python中执行无损转换，您可以使用FFmpeg库，它是一个功能强大的多媒体处理工具。
  您可以使用FFmpeg将M4A文件转换为MP3文件。
  下面是一个示例代码，展示如何使用FFmpeg库来实现这一转换:  
"""

def convert_m4a_to_mp3(input_file, output_file):
    cmd = f'ffmpeg -i {input_file} -acodec libmp3lame {output_file}'
    subprocess.call(cmd, shell=True)

def convert_folder_m4a_to_mp3(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.m4a'):
                input_file = os.path.join(root, file)
                output_file = os.path.join(root, file.replace('.m4a', '.mp3'))
                convert_m4a_to_mp3(input_file, output_file)

# 指定要转换的文件夹
folder_path = 'your_folder_path_here'
convert_folder_m4a_to_mp3(folder_path)