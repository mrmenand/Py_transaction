# 884.两句话中的不常见单词
class Solution(object):
    def uncommonFromSentences(self, A, B):
        list_ab = (A+" "+B).split()
        res =[]
        for i in list_ab:
            if list_ab.count(i) == 1:
                res.append(i)

        return res


