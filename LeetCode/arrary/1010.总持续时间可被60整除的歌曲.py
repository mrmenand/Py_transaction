# 1010. 总持续时间可被 60 整除的歌曲

## 最后一个样例没通过
# class Solution:
#     def numPairsDivisibleBy60(self,time):
#             # time: List[int]) -> int:
#             cnt = 0
#             for i in range(len(time)):
#                 for j in range(i+1,len(time)):
#                     if (time[i] + time[j])%60 == 0:
#                         cnt += 1
#
#             return cnt

