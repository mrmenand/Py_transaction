block = []
shape = []
for i in range(15):
    block.append(list(map(int,input().split())))

for i in range(4):
    shape.append(list(map(int,input().split())))
pos = int(input())
for i in range(4):##扩展到4乘10行
    shape[i] = [0]*(pos-1)+shape[i]+[0]*(10-4-pos+1)


for i in range(3):  ##让下面block[i+j] 不超出范围
    block.append([1]*10)

judge = False # 判断是否碰撞
row = 0
for i in range(15):
    for j in range(4):
        collision = [a+b for a,b in zip(block[i+j],shape[j])]
        if (2 in collision):
            row  = i-1
            judge =True
            break
    if (i==14):
        row = 14
    if (judge==True):
        break

for j in range(4):
    block[row+j] = [a+b for a,b in zip(block[row+j],shape[j])]


for i in range(15):
    print(" ".join(map(str,block[i])))  #需要转化成字符串拼接