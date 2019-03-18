n,L,t = list(map(int,input().split()))
a = list(map(int,input().split()))
rd=[] #right direction
for i in a :
    rd.append(1)

for i in range(t):  ##向右则位置向前加一
    for j in  range(len(a)):
        if rd[j] == 1:
            a[j] +=1
        else:
            a[j]-=1

    # if a[len(a)-1] == L:
    #     rd[len(a)-1] = 0
    # if a[0] ==0:
    #     rd[0] = 1
    for b in range(len(a)):  # 到达边界要改变direction
        if a[b]==L:
            rd[b] = 0
        if a[b] ==0:
             rd[b] = 1



    for k in range(len(a)):  #小球发生碰撞时候的条件，方向会发生变化
        for m in  range(k+1,len(a)):
            if  a[k] == a[m] :
                if rd[k] ==1:
                    rd[k] =0
                else:
                    rd[k] =1
                if rd[m] ==1:
                    rd[m] =0
                else:
                    rd[m] =1
                # rd[k] = 0
                # rd[m] = 1


for i in a:
    print(i,end=" ")