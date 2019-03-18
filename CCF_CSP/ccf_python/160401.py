n = int(input())
sales = list(map(int,input().split()))
cnt = 0
for i in range(1,n-1): ##第一个和最后一个没有折点
    if (sales[i]-sales[i-1])*(sales[i+1]-sales[i])<0:
        cnt +=1

print(cnt)
