def merge_sort(alist):
    """归并排序"""
    n = len(alist)
    if n<=1:
        return alist
    mid = n // 2

    left_li = merge_sort(alist[:mid])
    right_li = merge_sort(alist[mid:])

    left_pointer,right_pointer = 0, 0
    result = []

    while left_pointer <len(left_li) and right_pointer <len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
    # 当一边取完，一边还有剩余的时候
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]

    return result
if __name__ == '__main__':
    li = [54,26,93,17,77,31,44,55,20]
    sorted_li = merge_sort(li)
    print(sorted_li)