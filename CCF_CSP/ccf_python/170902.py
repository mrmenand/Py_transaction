N,K = list(map(int,input().split()))
info = []
for i in range(K):
    info.append(list(map(int,input().split()))) #二维列表信息

box =[i+1 for i in range(N)] #钥匙盒
rent = [i[0] for i in info ]
start = [i[1] for i in info] #开始时间
end = [i[1]+i[2] for i in info] #结束时间

def return_lend_key(info,time,t):# 输入的都是list,
    RL_key= []
    for i in range(0,len(time)):
        if time[i] ==t:
            RL_key.append(info[i][0])
    return  RL_key


for t in range(1,max(end)+1):
    ##每一秒判断是否都要先还后借
    if t in end:
        return_key = return_lend_key(info,end,t)
        return_key.sort()
        for k in range(len(return_key)):
            for i in range(N):
                if box[i] ==0:
                    box[i] = return_key[k]
                    break

    if t in start:
        lend_key = return_lend_key(info,start,t)
        for k in range(len(lend_key)):
            for i in range(N):
                if box[i] ==lend_key[k]:
                    box[i] = 0

for i in box :
    print(i,end =" ")







