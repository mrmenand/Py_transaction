n = int(input())
a = list(map(int,input().split()))
dict_ele = {}
list_ele = []

for ele in a:
    if ele in dict_ele.keys():
        dict_ele[ele] +=1
    else:
        dict_ele[ele] = 1

for key,value in dict_ele.items():
    list_ele.append([key,value])

list_ele = sorted(list_ele,key= lambda x:(x[1],-x[0]),reverse =True)

for ele in list_ele:
    print(ele[0],ele[1])
