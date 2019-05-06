# 811. 子域名访问计数
class Solution(object):
    def subdomainVisits(self, cpdomains):
        dic = {}
        for i in cpdomains:
            num, domains = i.split()
            list_domain = domains.split(".")
            tmp = list_domain[-1]
            dic[tmp] = dic.get(tmp,0) + int(num)

            for j in range(len(list_domain)-2,-1,-1):
                tmp = list_domain[j] + "." + tmp
                dic[tmp] = dic.get(tmp, 0) + int(num)

        res = []
        for i in dic.keys():
            res.append(str(dic[i]) + " " + i)

        return res
        # for dom, n in dic.items():
        #     res.append(str(n) + ' ' + dom)
        # return res

