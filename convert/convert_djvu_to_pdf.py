import os
import subprocess

def convert_djvu_to_pdf(djvu_path, pdf_path):
    # 检查输入文件是否存在
    if not os.path.isfile(djvu_path):
        raise FileNotFoundError(f"DJVU file '{djvu_path}' not found")

    # 中间的 PostScript 文件路径
    ps_path = djvu_path.replace('.djvu', '.ps')

    # 使用 djvups 将 DJVU 文件转换为 PostScript 文件
    subprocess.run(['djvups', djvu_path, ps_path], check=True)

    # 使用 ps2pdf 将 PostScript 文件转换为 PDF 文件
    subprocess.run(['ps2pdf', ps_path, pdf_path], check=True)

    # 删除中间的 PostScript 文件
    os.remove(ps_path)

    print(f"Successfully converted '{djvu_path}' to '{pdf_path}'")

# 示例用法
djvu_file = 'example.djvu'
pdf_file = 'example.pdf'

convert_djvu_to_pdf(djvu_file, pdf_file)