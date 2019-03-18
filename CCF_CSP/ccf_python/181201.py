r,y,g = list(map(int,input().split()))
# print(list(map(int,input().split())))
n = int(input())
s = 0
for i in range(n):
    k,t = input().split()
    k,t = int(k),int(t)
    if k == 0:
        s += t
    elif k==1:
        s += t
    elif k==2:
        s =s + t +r
    elif k==3:
        pass

print(s)



