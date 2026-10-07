class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        s = sum(nums) - abs(target)
        if s < 0 or s % 2:
            return 0
        m = s // 2
        n = len(nums)
        f = [[0] * (m + 1) for _ in range(n + 1)]
        f[0][0] = 1
        for i, x in enumerate(nums):
            for c in range(m + 1):
                if c < x:
                    f[i + 1][c] = f[i][c]
                else:
                    f[i + 1][c] = f[i][c] + f[i][c - x]
        return f[n][m]
