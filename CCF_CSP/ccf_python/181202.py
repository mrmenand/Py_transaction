r,y,g = list(map(int,input().split()))
n = int(input())
s = 0 #小明放学花的所有时间

def fun1202(k,t,s):
    if k ==0:
        return t

    if k==1:
        if s <t: ###走的时间小于红灯
            return t-s
        ### 大于红灯
        else :
            return fun1202(3,g,s-t)

    if k==2:
        if s<t:
            return t-s+r
        else :
            return fun1202(1,r,s-t)

    if k==3:
        if s<t:
            return 0
        else:
            return fun1202(2,y,s-t)

for i in range(n):
    k, t = list(map(int,input().split()))
    S=s %(r+g+y)  #红绿灯是否开启下一轮计数
    s += fun1202(k,t,S)

print(s)


