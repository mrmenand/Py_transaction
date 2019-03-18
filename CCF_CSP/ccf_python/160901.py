n = int(input())
stock  = list(map(int,input().split()))
jitter = []
for i in range(1,n):
     jitter.append(abs(stock[i]-stock[i-1])) ## 别用i+1 -i
# print(jitter)
print(max(jitter))
