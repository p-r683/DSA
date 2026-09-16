class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # dp[j] = C(current + j, 2*j)
        dp = [[0] * (2 * k + 1) for _ in range(n + k)]

        # Calculate combinations using Pascal's triangle
        for i in range(n + k):
            dp[i][0] = 1

            for j in range(1, min(i, 2 * k) + 1):
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD

        return dp[n + k - 1][2 * k]