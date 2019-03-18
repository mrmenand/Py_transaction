n,k = list(map(int,input().split()))
alive =[1 for i in range(n)] #小朋友是否GG，单人模式吃鸡
total = sum(alive)
cnt = 0 #报数
while  total>1: #吃鸡条件
    for i in range(n):
        if alive[i] != 0:
            cnt +=1
        if (cnt %k ==0) or (cnt %10==k):
            alive[i] = 0
            total = sum(alive)
            # if total ==1:
            #     break


index = alive.index(1)
print(index+1)










