n,k = list(map(int,input().split()))
cake = list(map(int,input().split()))
cnt = 0
sum = 0
for i in range(n):
    # if sum(cake[:i+1]) >=k:
    #     cnt +=1
    a = cake[i]
    sum += a
    if sum >=k:
        cnt+=1
        sum=0
if sum >0:
    cnt+=1


print(cnt)


