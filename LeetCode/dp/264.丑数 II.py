# 264. 丑数 II
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        import heapq
        heap = [1]
        heapq.heapify(heap)
        res = 0
        for _ in range(n):
            res = heapq.heappop(heap)
            while heap and res == heap[0]:
                res = heapq.heappop(heap)
            a, b, c = res * 2, res * 3, res * 5
            for t in a, b, c:
                heapq.heappush(heap, t)

        return res


if __name__ == '__main__':
    print(Solution().nthUglyNumber(n=10))
