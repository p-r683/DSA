from functools import cache
from itertools import accumulate

class Solution:
    def stoneGameV(self, stoneValue):

        prefix = list(accumulate(stoneValue, initial=0))

        @cache
        def dfs(l, r):
            if l == r:
                return 0

            ans = 0
            left = 0
            right = prefix[r + 1] - prefix[l]

            for k in range(l, r):
                left += stoneValue[k]
                right -= stoneValue[k]

                if left < right:
                    # Keep left
                    ans = max(ans, left + dfs(l, k))

                elif left > right:
                    # Keep right
                    ans = max(ans, right + dfs(k + 1, r))

                else:
                    # Equal: choose either side
                    ans = max(
                        ans,
                        left + dfs(l, k),
                        right + dfs(k + 1, r)
                    )

            return ans

        return dfs(0, len(stoneValue) - 1)