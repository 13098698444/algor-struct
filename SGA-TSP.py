"""
SGA python实现
"""
from random import randint, shuffle, choice, random
import math
import numpy as np
#适应度函数
def fit_func(chrom, pop_size,distance_mat):
    path_dis = [0] * pop_size
    fit = [0] * pop_size
    for i in range(pop_size):
        for j in range(city_num-1):
            path_dis[i] += distance_mat[chrom[i][j]][chrom[i][j+1]]
        path_dis[i] += distance_mat[chrom[i][0]][chrom[i][-1]]
        fit[i] = 1 / path_dis[i]
    return fit, path_dis
##选择子代  #采用轮盘赌选择方法
#封装成选择函数
def cumsum(fit_value):
    t = 0
    for i in range(len(fit_value)):
        t += fit_value[i]
        fit_value[i] = t
    return fit_value
def select_ch(fit, pop_size, chrom):
    newfit = [] #存储累计概率
    total_fit = sum(fit)
    for i in range(pop_size):
        newfit.append(fit[i] / total_fit)
    newfit = cumsum(newfit)  #累计概率
    #生成0-1随机概率序列
    ms = []
    for i in range(pop_size):
        ms.append(random())
    ms.sort()
    #开始选择
    newin = 0
    fitin = 0
    newchrom = [0] * pop_size
    while newin < pop_size:
        if ms[newin] < newfit[fitin]:
            newchrom[newin] = chrom[fitin]
            newin += 1
        else:
            fitin += 1
    return newchrom  #子代选择完毕 ，生成和原种群规模一样的新种群

#交叉函数 选择单点交叉形式
#交叉过后一条染色体会有重复节点，这在tsp问题中是不可取的 ，必须替换掉,
#需做冲突检测
cross_prob = 0.8  #交叉概率
def cross_ch(pop_size, chrom, cross_prob=0.8):
    #相邻之间交叉
    cross_list = list(range(0, pop_size, 2))
    for i in cross_list:
        if random() <= cross_prob:  #小于交叉概率则交叉
            chrom[i], chrom[i+1] = innercross(chrom[i], chrom[i+1])


def innercross(single1, single2):
    #产生交叉点
    city_num = len(single1)
    cross_point = randint(1, city_num-2) #1-12之间产生任意交叉点包含端点  0， 13两点交叉无意义
    single11 = single1.copy()
    single22 = single2.copy()
    single1[cross_point:] = single22[cross_point:]    #单点交叉操作
    single2[cross_point:] = single11[cross_point:]
    for i in range(cross_point):
        if single1[i] in single1[cross_point:]:
            r1 = i
            break
    for j in range(cross_point):
        if single2[j] in single2[cross_point:]:
            r2 = j
            break
    try:   #防止r1 r2 不存在
        single1[r1], single2[r2] = single2[r2], single1[r1]
    except:
        pass
    return single1, single2


#变异模块
mut_prob = 0.01
def mutation(chrom, pop_size, mut_prob=0.01):
    for i in range(pop_size):
        if random() <= mut_prob:
            r1 = randint(0, city_num-1)   #交换r1 r2 两点的位置 当做变异
            r2 = city_num - 1 - r1
            chrom[i][r1], chrom[i][r2] = chrom[i][r2], chrom[i][r1]
    return chrom



if __name__ == '__main__':
    cities = [[16.47, 66.10],
              [16.47, 94.44],
              [20.09, 82.54],
              [22.39, 63.37],
              [25.23, 97.24],
              [22.00, 96.05],
              [20.47, 67.02],
              [17.20, 96.29],
              [16.30, 87.38],
              [14.05, 98.12],
              [16.53, 97.38],
              [21.52, 95.59],
              [19.41, 57.13],
              [20.09, 72.55]]
    # cities = [[35.0,	35.0],  #benchmark 101 的示例
    #         [41.0,	49.0],
    #         [35.0, 17.0],
    #         [55.0, 	45.0],
    #         [55.0, 	20.0],
    #         [15.0, 30.0],
    #         [25.0, 	30.0],
    #         [20.0, 50.0],
    #         [10.0, 	43.0],
    #         [55.0, 	60.0],
    #         [30.0,  60.0],
    #         [20.0, 	65.0],
    #         [50.0, 	35.0],
    #         [30.0, 	25.0],
    #         [15.0, 	10.0],
    #         [30.0, 	5.0],
    #         [10.0, 	20.0],
    #         [5.0, 	30.0],
    #         [20.0, 	40.0],
    #         [15.0, 	60.0],
    #         [45.0, 	65.0],
    #         [45.0, 	20.0],
    #         [45.0, 	10.0],
    #         [55.0, 	5.0],
    #         [65.0, 	35.0],
    #         [65.0, 	20.0],
    #         [45.0, 	30.0],
    #         [35.0, 	40.0],
    #         [41.0, 	37.0],
    #         [64.0, 	42.0],
    #         [40.0, 	60.0],
    #         [31.0, 	52.0],
    #         [35.0, 	69.0],
    #         [53.0, 	52.0],
    #         [65.0, 	55.0],
    #         [63.0, 	65.0],
    #         [2.0, 	60.0],
    #         [20.0, 	20.0],
    #         [5.0,   5.0],
    #         [60.0, 	12.0],
    #         [40.0, 	25.0],
    #         [42.0, 	7.0],
    #         [24.0, 	12.0],
    #         [23.0, 	3.0],
    #         [11.0, 	14.0],
    #         [6.0, 	38.0],
    #         [2.0, 	48.0],
    #         [8.0, 	56.0],
    #         [13.0, 	52.0],
    #         [6.0 , 68.0],
    #         [47.0, 47.0],
    #         [49.0, 	58.0],
    #         [27.0, 	43.0],
    #         [37.0, 	31.0],
    #         [57.0, 	29.0],
    #         [63.0, 	23.0],
    #         [53.0, 	12.0],
    #         [32.0, 	12.0],
    #         [36.0, 	26.0],
    #         [21.0, 	24.0],
    #         [17.0, 	34.0],
    #         [12.0, 	24.0],
    #         [24.0, 	58.0],
    #         [27.0, 	69.0],
    #         [15.0, 	77.0],
    #         [62.0, 	77.0],
    #         [49.0, 	73.0],
    #         [67.0, 	5.0],
    #         [56.0, 	39.0],
    #         [37.0, 	47.0],
    #         [37.0, 	56.0],
    #         [57.0, 	68.0],
    #         [47.0, 	16.0],
    #         [44.0, 	17.0],
    #         [46.0, 	13.0],
    #         [49.0, 	11.0],
    #         [49.0, 	42.0],
    #         [53.0, 	43.0],
    #         [61.0, 	52.0],
    #         [57.0, 	48.0],
    #         [56.0, 	37.0],
    #         [55.0, 	54.0],
    #         [15.0, 	47.0],
    #         [14.0, 	37.0],
    #         [11.0, 	31.0],
    #         [16.0, 	22.0],
    #         [4.0, 	18.0],
    #         [28.0, 	18.0],
    #         [26.0, 	52.0],
    #         [26.0, 	35.0],
    #         [31.0, 	67.0],
    #         [15.0, 	19.0],
    #         [22.0, 	22.0],
    #         [18.0, 	24.0],
    #         [26.0, 27.0],
    #         [25.0, 	24.0],
    #         [22.0, 	27.0],
    #         [25.0, 	21.0],
    #         [19.0, 	21.0],
    #         [20.0, 	26.0],
    #         [18.0, 18.0]]
    city_num = len(cities)
    distance_mat = [[0 for i in range(city_num)] for i in range(city_num)]
    for i in range(city_num):  # 还可以优化
        for j in range(city_num):
            distance_mat[i][j] = ((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2) ** (1 / 2)
    pop_size = 1000  # 种群规模
    chrom = [[] for i in range(pop_size)]
    # 种群中每个个体路径长度
    path_dis = [0] * pop_size
    # 每个个体的适应度
    fit = [0] * pop_size
    # 产生初始种群 #计算每个个体的路径值与适应度
    for i in range(pop_size):  # 符号编码方式
        random_single = list(range(city_num))
        shuffle(random_single)
        chrom[i] = random_single
        for j in range(city_num - 1):
            path_dis[i] += distance_mat[random_single[j]][random_single[j + 1]]
        # 首尾相连
        path_dis[i] += distance_mat[random_single[0]][random_single[-1]]
        fit[i] = 1 / path_dis[i]  # 适应度函数取倒数 ，fit越大适应度越好
    print('初始种群中的路径平均值:', np.mean(path_dis))
    print('初始种群中的路径最小值:', min(path_dis))
    print('初始种群中最小值的路径:', chrom[path_dis.index(min(path_dis))])


    #开始迭代 代数 100
    maxgen = 200
    for i in range(1, maxgen+1):
        fit, path_dis = fit_func(chrom, pop_size, distance_mat)
        chrom = select_ch(fit, pop_size, chrom)
        cross_ch(pop_size, chrom, cross_prob=0.3)   #经多次试验， 0.3容易产生表较好的结果
        chrom = mutation(chrom, pop_size, mut_prob=0.01)
        if i % 50 == 0:
            print('第{}次迭代后种群中的路径平均值:'.format(i), np.mean(path_dis))
            print('第{}次迭代后种群中的路径最小值:'.format(i), min(path_dis))
            print('第{}次迭代后种群中最小值的路径:'.format(i), chrom[path_dis.index(min(path_dis))])

    print('结束种群中的路径平均值:', np.mean(path_dis))
    print('结束种群中的路径最小值:', min(path_dis))
    print('结束种群中最小值的路径:', chrom[path_dis.index(min(path_dis))])













