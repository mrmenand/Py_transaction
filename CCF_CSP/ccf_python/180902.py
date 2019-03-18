n = int(input())
H = []
W = []
for i in range(n):
    a = list(map(int,input().split()))
    H.append(a)
for i in range(n):
    b = list(map(int,input().split()))
    W.append(b)
t = 0
# time = 0
#H和W的装货时间，存在六种可能
for i in H:
    for j in W:
        # if i[0] >= j[1]:
        #     continue
        # elif i[1] <= j[0]:
        #     break
        # elif i[0] <= j[0] and j[1] >= i[1]:
        #     time += abs(i[1] - j[0])
        # elif i[0] <= j[0] and j[1] <= i[1]:
        #     time += abs(j[1] - j[0])
        # elif i[0] >= j[0] and j[1] >= i[1]:
        #     time += abs(i[1] - i[0])
        # elif j[0] <= i[0] and j[1] <= i[1]:
        #     time += abs(j[1] - i[0])

        if i[0] >=j[1]:
            continue
        elif j[0]>=i[1]:
             break
        elif j[0]<=i[0] and j[1]<=i[1]:
            t +=abs(j[1]-i[0])
        elif i[0]<=j[0] and j[1]<=i[1]:
            t +=abs(j[1]-j[0])
        elif i[0]<=j[0] and i[1]<=j[1]:
            t +=abs(i[1]-j[0])
        elif j[0]<=i[0] and i[1]<=j[1]:
            t+=abs(i[1]-i[0])


print(t)