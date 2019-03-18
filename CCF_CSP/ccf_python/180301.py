a = list(map(int,input().split()))

s = 0
comb = 0
for i in a:
    if  i==0:
        break
    elif i==1:
        comb = 0
        s+=1

    elif i==2:
        comb +=2
        s =s+comb

print(s)
