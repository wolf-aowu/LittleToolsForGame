import os
import sys
import tkinter as tk
from tkinter import filedialog

# 为当前目录下的文件批量改名
def RenameFileInCurrentFolder():
    # 选择文件夹
    root = tk.Tk().withdraw()
    folderPath = filedialog.askdirectory()
    if folderPath == "":
        sys.exit()
    
    prefixName = input("请输入前缀名：")
    suffixName = input("请输入带 '.' 的后缀名（-1为不限制后缀）：")

    # 当前文件夹下所有文件列表
    fileList = os.listdir(folderPath)
    i = 0
    for file in fileList:
        path = folderPath + "\\" + file
        # 判断是否是文件
        if not os.path.isfile(path):
            continue
        # 将文件名与后缀分开
        name,suffix = os.path.splitext(file)
        # 如果要重命名，就必须到文件的当前目录，不然会报找不到文件的错
        os.chdir(folderPath)
        if suffixName == "-1" or suffix == suffixName:
            # 重命名
            os.rename(file,prefixName + '_' + str(i) + suffix)
            i += 1

if __name__ == '__main__':
    RenameFileInCurrentFolder()
