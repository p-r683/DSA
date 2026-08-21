from typing import List
from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        # Count how many valid amounts are <= x
        def count(x):
            n = len(coins)
            total = 0

            # Inclusion-exclusion over all subsets
            for mask in range(1, 1 << n):
                lcm = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1

                        g = gcd(lcm, coins[i])
                        lcm = lcm // g * coins[i]

                        # No need to continue if LCM > x
                        if lcm > x:
                            valid = False
                            break

                if not valid:
                    continue

                multiples = x // lcm

                if bits % 2 == 1:
                    total += multiples
                else:
                    total -= multiples

            return total

        # Binary search
        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left