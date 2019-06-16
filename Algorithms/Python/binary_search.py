class Binary_Search(object):
    def binary_search_rec(self, alist, target):
        """二分查找，递归"""
        n = len(alist)
        if n > 0:
            mid = n // 2
            if alist[mid] == target:
                return True
            elif target < alist[mid]:
                return self.binary_search_rec(alist[:mid], target)
            else:
                return self.binary_search_rec(alist[mid + 1:], target)
        return False

    def binary_search(self, alist, target):
        """二分查找，非递归"""
        low, high = 0, len(alist) - 1
        while low <= high:
            mid = (low + high) // 2
            if alist[mid] == target:
                return mid
            elif alist[mid] < target:
                low += 1
            else:
                high += 1

        return False

    def binary_search_first(self, alist, target):
        """"二分查找，查找第一个值等于给定值的元素
        alist = [1,3,4,5,6,8,8,8,11,18],找第一个8"""
        low, high = 0, len(alist) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if alist[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

            if alist[low] == target:
                return low
            else:
                return False

    def binary_search_last(self, alist, target):
        """"二分查找，查找第一个值等于给定值的元素
        alist= [1,3,4,5,6,8,8,8,11,18],找第三个8"""
        low, high = 0, len(alist) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if alist[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1

            if alist[high] == target:
                return high
            else:
                return False

    def binary_search_gte(self, alist, target):
        """二分查找，查找第一个大于等于给定值的元素
        alist = [3,4,6,7,10],找大于等于5的"""
        low, high = 0, len(alist) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if alist[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

            if alist[low] >= target:
                return low
            else:
                return False

    def binary_search_lte(self, alist, target):
        """二分查找，查找最后一个小于等于给定值的元素
        alist = [3,4,6,7,10],找小于等于5的"""
        low, high = 0, len(alist) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if alist[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

            if alist[high] <= target:
                return high
            else:
                return False
