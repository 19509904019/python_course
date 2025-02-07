import os
import matplotlib.pyplot as plt

# 相位数据存储路径
phasePath = r'C:\Users\Dell\Desktop\preprocessing_data\phase\phase'
frequencyPath = r'C:\Users\Dell\Desktop\frequency\frequency.txt'

# 打开文件夹
phaseName = os.listdir(phasePath)

# 按文件顺序排列
phaseName.sort(key=lambda x: int(x[:-4]))

# 存放文件内容
phase = []
frequency = []

# 频率
with open(frequencyPath, 'r') as f:
    # 按行读取全部内容
    lines = f.readlines()
    for line in lines:
        a = line.split()  # 数组
        a = float(a[0])  # 转化为浮点数
        frequency.append(a)

# 首先读取相位数据
for file in phaseName:
    fullPhasePath = os.path.join(phasePath, file)
    # 对文件内容进行读取
    with open(fullPhasePath, 'r') as f:
        # 按行读取全部内容
        lines = f.readlines()
        for line in lines:
            a = line.split()  # 数组
            a = float(a[0])  # 转化为浮点数
            phase.append(a)

    # 画图
    plt.plot(frequency, phase)
    plt.xlabel("Frequency(GHz)")
    plt.ylabel("Phase(degree)")

    # 清空数组
    phase.clear()

plt.rcParams['figure.figsize'] = (20, 15)
plt.show()
