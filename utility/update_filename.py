import os

path = r'C:\Users\Dell\Desktop\preprocessing_data\phase2\phase(45001-50000)'

# 获取该目录下所有文件，存入列表中
fileList = os.listdir(path)
# 按顺序排列
fileList.sort(key=lambda x: int(x[:-4]))
n = 45000
for i in fileList:
    n += 1
    # 设置旧文件名（就是路径+文件名）
    oldname = path + os.sep + fileList[n - 45001]  # os.sep添加系统分隔符

    # 设置新文件名
    newname = path + os.sep + f'{n}' + '.txt'

    os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名
    # print(oldname, '======>', newname)
