import os

path = r'C:\Users\12414\Desktop\matrix\6'

# 获取该目录下所有文件，存入列表中
fileList = os.listdir(path)

n = 25000
for i in fileList:
    n += 1
    # 设置旧文件名（就是路径+文件名）
    oldname = path + os.sep + fileList[n-25001]  # os.sep添加系统分隔符

    # 设置新文件名
    newname = path + os.sep + f'{n}-matrix' + '.txt'

    os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名
    # print(oldname, '======>', newname)