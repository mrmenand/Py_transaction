n = int(input())
a = list(map(int,input().split()))

middle =[]
for i in range(n):
    l = 0
    s = 0
    for j in range(n):
        if a[j] >a[i]:
            l+=1
        elif  a[j]<a[i]:
            s+=1
    if s==l:
        middle.append(a[i])
# print(middle)
middle =list(set(middle))
if middle == []:
    print(-1)
else:
    print(middle[0])

