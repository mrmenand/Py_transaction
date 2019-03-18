n = int(input())
a = list(map(int,input().split()))
b = []
for i in range(len(a)):
    for j in range(i+1,len(a)):
        b.append(abs(a[i]-a[j]))
b.sort()
print(b[0])