# 79.单词搜索
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        n, m = len(board), len(board[0])
        marked = [[False] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                    if self.traceback(board, i, j, m, n, marked, word, 0):
                        return True

        return False

    def traceback(self, board, i, j, m, n, marked, word, index):
        if index == len(word)-1:
            return word[index] == board[i][j]

        if board[i][j] == word[index]:
            marked[i][j] = True
            for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_i = i + direction[0]
                new_j = j + direction[1]
                if 0 <= new_i < n and 0 <= new_j < m and not marked[new_i][new_j] and \
                        self.traceback(board, new_i, new_j, m, n, marked, word, index+1):
                    return True
            marked[i][j] = False

        return False


