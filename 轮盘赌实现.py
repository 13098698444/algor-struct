"""
轮盘赌 算子的实现
"""

import random

#累计概率计算
def cumsum(fit_value):
    t = 0
    for i in range(len(fit_value)):
        t += fit_value[i]
        fit_value[i] = t
    return fit_value
#轮盘赌算法
def ga_select(pop, fit_value):
    newfit_value = [] #存储累计概率
    total_fit = sum(fit_value)
    for i in range(len(fit_value)):
        #计算每个适应度占适应度综合的比例
        newfit_value.append(fit_value[i]/total_fit)
    newfit_value = cumsum(newfit_value)

    ms = [] #随机数序列
    for i in range(len(pop)):
        ms.append(random.random())
    ms.sort()


    #轮盘赌选择
    fitin = 0
    newin = 0
    newpop = [0] * len(pop)
    while newin < len(pop):
        #选择--累计概率大于随机概率
        if ms[newin] < newfit_value[fitin]:
            newpop[newin] = pop[fitin]
            newin += 1
        else:
            fitin += 1
    return newpop

if __name__ == '__main__':
    pop = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    obj = [1, 3, 0, 2, 4, 8, 5]

    print(ga_select(pop, obj))
