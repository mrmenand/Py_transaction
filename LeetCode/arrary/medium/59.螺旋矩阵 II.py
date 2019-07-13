class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l, r, u, d = 0, n - 1, 0, n - 1
        num , tar = 1 , n * n
        mat = [[0 for _ in range(n)] for _ in range(n)]


        while num <= tar :
            #  left --> right
            for i in range(l,r+1):
                mat[l][i]   = num
                num += 1
            u += 1
            #  up --> down
            for i in range(u,d+1):
                mat[i][r] = num
                num += 1
            r -= 1

            #  right --> left
            for i in range(r,l-1,-1):
                mat[d][i] = num
                num += 1
            d -= 1

            # down --> up
            for i in range(d, u - 1, -1):
                mat[i][l] = num
                num += 1

            l += 1

        return mat









