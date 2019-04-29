# 819. 最常见的单词
class Solution:
    def mostCommonWord(self, paragraph, banned):
            # paragraph: str, banned: List[str]) -> str:
            sym = "!?.',;"
            for i in sym:
                paragraph = paragraph.replace(i," ")
            paragraph = paragraph.lower()
            list_p = paragraph.split()
            dic = {}
            for i in list_p:
                if i not in banned:
                    # if i not in dic:
                    #     dic[i] = 1
                    # else:
                    #     dic[i] += 1
                    if i not in dic:
                        dic[i] = 0
                    dic[i] += 1

            return max(dic,key= lambda x : dic[x])



