# class Solution:
#     def gameOfLife(self, board: List[List[int]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         m,n = len(board),len(board[0])
#         new_board = [[0] * (n+2)]+ [[0] + row + [0] for row in board] + [[0]*(n+2)]
#         for i in range(1,m+1):
#             for j in range(1,n+1):
#                 cnt = 0
#                 for a in [-1,0,1]:
#                     for b in [-1,0,1]:
#                         cnt += new_board[i+a][j+b]
#                 cnt -= new_board[i][j]
#                 if cnt < 2 or cnt > 3:
#                     board[i-1][j-1] = 0
#                 elif  board[i-1][j-1] == 0 and cnt == 3:
#                     board[i-1][j-1] = 1

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """位运算，左移1位，最后一位保存状态信息，进行位或运算"""
        m, n = len(board), len(board[0])
        def count_cell(x,y):
            points = [(x-1, y-1),(x-1, y),(x-1, y+1),
                (x, y-1),(x, y+1),
                (x+1, y-1),(x+1, y),(x+1, y+1)]
            return sum((board[i][j] & 1) for i,j in points  if 0 <= i < m and 0 <= j < n)

        for i in range(m):
            for j in range(n):
                cnt = count_cell(i,j)
                cnt <<= 1 # 左移一位，最后一位保存生死信息
                board[i][j] |= cnt

        for i in range(m):
            for j in range(n):
                cnt = board[i][j] >> 1
                board[i][j]  &= 1 # 生死情况 0 死 1 生
                if board[i][j]:
                    if cnt <2 or cnt >3 :
                        board[i][j] = 0
                else:
                    if cnt ==3 :
                        board[i][j] = 1

        return board



