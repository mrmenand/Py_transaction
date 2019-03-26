def shell_sort(alist):
    """希尔排序，一种特殊的插入排序"""
    n = len(alist)
    gap = n // 2
    while gap >0:
        for j in range(gap,n):
            i = j
            while i >0:
                if alist[i] < alist[i-gap]:
                    alist[i],alist[i-gap] = alist[i-gap],alist[i]
                    i -= gap
                else:
                    break
        gap = gap//2

if __name__ == '__main__':
    li = [54,26,93,17,77,31,44,55,20]
    shell_sort(li)
    print(li)

