def binary_search(alist,item):
    """二分查找，递归"""
    n = len(alist)
    if n > 0:
        mid = n//2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid],item)
        else:
            return binary_search(alist[mid+1:],item)
    return False

def binary_search_2(alist,item):
    """二分查找，非递归"""
    # n = len(alist)
    # first = 0
    # last = n-1
    # while first <= last:
    #     mid = (first + last) // 2
    #     if alist[mid] == item:
    #         return True
    #     elif item < alist[mid]:
    #         last = mid - 1
    #     else:
    #         first = mid + 1
    # return False
    first = 0
    last = len(alist) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            return True
        elif item < alist[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return False


if __name__ == '__main__':
    li = [54,26,93,7,77,31,44,55,20]
    li.sort()
    print(binary_search(li,7))
    print(binary_search(li,100))