import random


class Sorts(object):

    def bubble_sort(self, alist):
        """冒泡排序"""
        for i in range(len(alist) - 1, 0, -1):
            for j in range(i):
                if alist[j] > alist[j + 1]:
                    alist[j], alist[j + 1] = alist[j + 1], alist[j]

    def insert_sort(self, alist):
        """插入排序"""
        for i in range(1, len(alist)):
            for j in range(i, 0, -1):
                if alist[j] < alist[j - 1]:
                    alist[j], alist[j - 1] = alist[j - 1], alist[j]

    def select_sort(self, alist):
        """选择排序"""
        for i in range(len(alist) - 1):
            min_idx = i
            for j in range(i + 1, len(alist)):
                if alist[min_idx] > alist[j]:
                    min_idx = j
            alist[i], alist[min_idx] = alist[min_idx], alist[i]

    def shell_sort(self, alist):
        """希尔排序，一种特殊的插入排序"""
        n = len(alist)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                j = i
                while j > 0:
                    if alist[j] < alist[j - gap]:
                        alist[j], alist[j - gap] = alist[j - gap], alist[j]
                        j -= gap
                    else:
                        break

            gap = gap // 2

    def merge_sort(self, alist):
        """归并排序"""
        n = len(alist)
        if n <= 1:
            return alist
        mid = n // 2
        ## mid = (start + end) // 2

        left = self.merge_sort(alist[:mid])
        right = self.merge_sort(alist[mid:])

        l, r = 0, 0
        result = []

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1

        result += left[l]
        result += right[r]

        return result

    def quick_sort(self, alist, start, end):
        """快速排序"""
        if start >= end:
            return

        mid = random.choice(alist)
        low, high = start, end

        while low < high:
            if alist[high] >= mid:
                high -= 1
            alist[low] = alist[high]

            if alist[low] < mid:
                mid += 1
            alist[high] = alist[low]

        alist[low] = mid

        self.quick_sort(alist, start, low - 1)
        self.quick_sort(alist, low + 1, end)
