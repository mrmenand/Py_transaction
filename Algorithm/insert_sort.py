def insertion_sort(alist):
    """插入排序"""
    n = len(alist)
    for i in range(1,n):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j  in range(i,0,-1):
            if alist[j] < alist[j-1]:
                alist[j],alist[j-1] = alist[j-1],alist[j]

"""  最优时间复杂度：O(n）（升序排列，序列已经处于升序状态）
最坏时间复杂度：O(n2)
稳定性：稳定"""
if __name__ == '__main__':
    li = [54,26,93,17,77,31,44,55,20]
    insertion_sort(li)
    print(li)