# 621. 任务调度器
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if  not tasks:
            return 0
        dic = {}
        for i in tasks:
            dic[i] = dic.get(i,0) +1
        max_task = max(dic,key=dic.get)
        ret = (dic[max_task]-1)*(n+1) + 1
        for k,v in dic.items():
            if v == dic[max_task] and k!= max_task:
                ret += 1
        if ret < len(tasks):
            ret = len(tasks)

        return ret
