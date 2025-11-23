# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
#生成包含15个0-100之间随机整数的列表
shus = [random.randint(0, 100) for _ in range(15)]
print("数据列表:", shus)
#找到并删除一个最大值和一个最小值
maxshu = max(shus)
minshu = min(shus)
shus.remove(maxshu)
shus.remove(minshu)
#计算剩余13个数的和与平均值
he = sum(shus)
average = he/len(shus)
#打印结果，平均值保留两位小数
print("剩余13个数的总和为: {}".format(he))
print("剩余13个数的平均值为: {:.2f}".format(average))



#提示词
print("长方体体积计算器")
print("提示：输入0 0 0则可以退出程序")
while True:
    #提醒用户按格式输入长宽高数据
    shu = input("请输入长 宽 高（用空格分隔）：").strip()
    #打破循环
    if shu == "0 0 0":
        print("感谢您的使用，再见！")
        break
    #避免由于输入非正整数引起的错误
    try:
        a,b,c = map(int,shu.split())
        if a <= 0 or b <= 0 or c <= 0:
            print("长、宽、高必须是正整数，请重新输入！")
            continue
        #计算体积结果并打印
        tiji = a*b*c
        print(f"体积 = {a} × {b} × {c} = {tiji} 立方厘米\n")
    #避免其他数据输入的不规范引起的错误
    except ValueError:
        print("输入格式错误，请确保输入三个整数并用空格分隔！")