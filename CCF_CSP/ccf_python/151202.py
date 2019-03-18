import copy

n,m = list(map(int,input().split()))
board = []
for i in range(n):
    board.append(list(map(int,input().split()))) #先生成二维列表
new_board =copy.deepcopy(board)
for i in range(n):
    for j in range(1,m-1): #消除行
        if board[i][j] ==board[i][j-1] and board[i][j+1] ==board[i][j]:
            new_board[i][j-1] = 0
            new_board[i][j] = 0
            new_board[i][j+1] = 0
            for k in range(j+2,m):
                if board[i][k] ==board[i][j]:
                    new_board[i][k] = 0
                else:
                    break





for j in range(m):
    for i in range(1, n - 1):  # 消除列
        if board[i-1][j] ==board[i][j] and board[i+1][j] ==board[i][j]:
            new_board[i-1][j] = 0
            new_board[i][j] = 0
            new_board[i+1][j] = 0
            for k in range(i+2,n):
                if board[k][j] ==board[i][j]:
                    new_board[k][j] = 0
                else:
                    break

for i in range(n):
    for j in range(m):
        print(new_board[i][j], end=" ")
    print()
