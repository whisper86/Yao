# 作者：许垚
# 开发时间：2022年10月09日

from 成绩查询2 import *

print("***************成绩查询系统2.0*****************")

PERFORMANCE = []
for name, score in zip(Name, All_Score_Performances):
    Performance = {name: score}
    PERFORMANCE.append(Performance)


def PANDAN():
    NAME = input("学生姓名(Enter 'q' to exit)")
    if NAME not in Name and NAME != 'q':
        print("查无此人")
        return PANDAN()
    else:
        for SCORE in PERFORMANCE:
            for param, value in SCORE.items():
                if param == NAME:
                    print(f"{NAME}的成绩为：" + str(value))
                    return PANDAN()
                elif param == 'q':
                    exit()
                else:
                    continue


PANDAN()
