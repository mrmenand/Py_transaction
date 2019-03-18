n = int(input())
prices = list(map(int,input().split()))
new_price =[]
for i in range(n):
    if i==0:
        price= int((prices[0]+prices[1])/2)
        new_price.append(price)
    elif i==n-1:
        price = int((prices[n-1]+prices[n-2])/2)
        new_price.append(price)
    else:
        price = int((prices[i]+prices[i-1]+prices[i+1])/3)
        new_price.append(price)

for i in new_price:
    print(i,end=" ")
