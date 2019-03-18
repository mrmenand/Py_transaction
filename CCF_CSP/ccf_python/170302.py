n = int(input())
m = int(input())
adjust = []
for i in range(m):
    adjust.append(list(map(int, input().split())))

p = [adjust[i][0] for i in range(len(adjust))]
q = [adjust[i][1] for i in range(len(adjust))]


ln = [i+1 for i in range(n)]

def queue(ln,p,q):
    for i in range(len(p)):
        ind = ln.index(p[i]) #获得要排队的小朋友的编号
        # ln.insert((ind-1+q[i]),ln.pop(ind))
        if q[i] >=0: #向右移动，先插入，后删除
            ln.insert(ind+q[i]+1,p[i])
            ln.pop(ind)
        else:
            ln.pop(ind)
            ln.insert(ind+q[i],p[i])
    return ln

queue =queue(ln,p,q)
for i in  ln:
    print(i,end=" ")







