# 690. 员工的重要性
class Solution:
    def getImportance(self, employees, id):
        hashmap = {}

        for employee in employees:
            hashmap[employee.id] = [employee.importance, employee.subordinates]
        """DFS"""
        self.res= 0
        def dfs(subs):
            for sub in subs:
                self.res += hashmap[sub][0]
                dfs(hashmap[sub][1])

        dfs([id])
        return self.res



        """BFS"""
        # stack = [id]
        # res = 0
        # while stack:
        #     emp = stack.pop()
        #     res += hashmap[emp][0]
        #     for subemp in hashmap[emp][1]:
        #         stack.append(subemp)
        #
        # return res


