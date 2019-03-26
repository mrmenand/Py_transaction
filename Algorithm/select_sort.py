def selection_sort(alist):
    """选择排序"""
    n = len(alist)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if alist[min_index] > alist[j]:
                min_index = j
        alist[i],alist[min_index] = alist[min_index],alist[i]

"""最优时间复杂度：O(n2)
最坏时间复杂度：O(n2)
稳定性：不稳定（考虑升序每次选择最大的情况）"""

li = [54,26,93,17,77,31,44,55,20]
selection_sort(li)
print(li)