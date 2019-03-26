def  bubble_sort(alist):
    """冒泡排序"""
    for i in range(len(alist)-1,0,-1):
        # i表示每次遍历需要比较的次数，是逐渐减小的
        for j in range(i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]

"""最优时间复杂度：O(n) （表示遍历一次发现没有任何可以交换的元素，排序结束。）
最坏时间复杂度：O(n2)
稳定性：稳定"""
if __name__ == '__main__':
    li = [54,26,93,17,77,31,44,55,20]
    bubble_sort(li)
    print(li)