y = int(input())
d = int(input())
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]


sum =0
if (y%4==0 and y%4!=0) or y%400==0:
    days[2] =29
for i in range(13):
    m = sum
    sum+=days[i]
    if sum >=d:
        print(i)
        print(d-m)
        break


