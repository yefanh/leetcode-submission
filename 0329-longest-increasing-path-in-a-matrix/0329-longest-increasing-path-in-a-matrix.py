class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        dp = {} # (i, j) -> LIP

        def dfs(i: int, j: int, preVal: int) -> int:
            if (i < 0 or j < 0 or i == ROWS or j == COLS or matrix[i][j] <= preVal):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            res = 1
            res = max(res, 1 + dfs(i + 1, j, matrix[i][j]))
            res = max(res, 1 + dfs(i - 1, j, matrix[i][j]))
            res = max(res, 1 + dfs(i, j + 1, matrix[i][j]))
            res = max(res, 1 + dfs(i, j - 1, matrix[i][j]))
            dp[(i, j)] = res
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(dp.values())