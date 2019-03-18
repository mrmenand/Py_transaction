rate =[0.03,0.1,0.2,0.25,0.30,0.35,0.45]
A = [0,1500,4500,9000,35000,55000,80000] #超出部分需要的税率
S = [i+3500 for i in A]
r_money= [0]
s = 0
for i in range(1,len(A)):  # r_money = [0,45,300,900,6500,6000,8750] #需要交的最大税钱
    s += int((A[i]-A[i-1])*rate[i-1])
    r_money.append(s)

money = [S[i]-r_money[i] for i in range(len(A))] ###税后最大工资区间
# print(S)
# print(r_money)
# print(money)

t = int(input())
for i in range(len(money)+1):
    if i ==len(money):
        break
    elif t<=money[i]:
        break
if i ==0:
    print(t)
else:
    qian =int( S[i-1] +(t-money[i-1])/(1-rate[i-1]))
    print(qian)





