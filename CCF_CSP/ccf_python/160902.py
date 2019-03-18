n = int(input())
ticket = list(map(int,input().split()))
seat =  [5 for i in range(20)] #空座，判断是否可以买连排

for i in ticket:
    judge = False
    for j in range(len(seat)): #连续座位
        if i <=seat[j]:
            judge = True
            start = j*5 +(5-seat[j])+1  #可以连排的初始位置
            seat[j]-=i
            for k in range(start,start+i):
                print(k,end =" ")
            print()
            break

    if judge == False:# 按从小到大编号
        for j in range(len(seat)):
                start = j * 5 + (5 - seat[j]) + 1
                length = seat[j]
                if (i>seat[j]): #该排买满
                    i -=seat[j]
                    seat[j] = 0
                    for k in range(start,start+length):
                        print(k,end=" ")
                else:#该排还有空位置
                    seat[j] -=i
                    for  k in range(start,start+i):
                        print(k,end=" ")
                    print()
                    i = 0
                    break








