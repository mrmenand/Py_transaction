n = int(input())
p = input().split()
seat = [[0 for j in range(5)] for i in range(20)]
schedule = [5 for i in range(20)]
seat_result = [[] for i in range(n)]
# print(seat)
# print(schedule)
# print(seat_result)
for i in range(n):
    judge = False
    p[i] = int(p[i])
    for j in range(20):
        if p[i] <= schedule[j]:
            judge = True
            schedule[j] = schedule[j] - p[i]
            break

    if judge == True:
        for k in range(p[i]):
            for g in range(5):
                if seat[j][g] == 0:
                    seat[j][g] = 1
                    break
            seat_result[i].append(j * 5 + g + 1)
    elif judge == False:
        for k in range(p[i]):
            for g in range(20):
                for t in range(5):
                    if seat[g][t] == 0:
                        seat[g][t] = 1
                        break
            seat_result[i].append(j * 5 + g + 1)

for i in range(n):
    for j in range(len(seat_result[i])):
        print(seat_result[i][j], " ", end="")
    print("")
