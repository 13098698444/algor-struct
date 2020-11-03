


import time    #装饰器计时
def Cal_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(func.__name__, time.time() - start)
        return result
    return wrapper

@Cal_time
def linear_search(l, val):
    for index, v in enumerate(l):
        if v == val:
            return index
    else:
        return None

#二分查找  首先是先排好序的列表   一定是有序列表
@Cal_time
def binary_search(l, val):       #时间复杂度 O(logn)
    left = 0
    right = len(l) - 1
    while left <= right: #候选区有值
        mid = (left + right) // 2
        if l[mid] == val:
            return mid
        elif l[mid] > val:
            right = mid - 1
        else:  #l[mid] < val
            left = mid + 1
    else:  #找不到时
        return None

l1 = list(range(1000))
print(l1)
print(l1.index(5))   #列表内置函数index 是线性查找  适合小数据量的
linear_search(l1, 980)
binary_search(l1, 980)



