# 495. 提莫攻击
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ret = 0
        if not timeSeries:
            return ret
        for i in range(len(timeSeries)-1):
            ret += duration if timeSeries[i+1] -timeSeries[i] >= duration else  timeSeries[i+1] - timeSeries[i]

        return ret + duration
