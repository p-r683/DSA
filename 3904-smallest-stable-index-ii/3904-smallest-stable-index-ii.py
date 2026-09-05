class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # Suffix minimum
        right = [0] * n
        right[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            right[i] = min(nums[i], right[i + 1])

        # Prefix maximum + check
        left = nums[0]

        for i in range(n):
            left = max(left, nums[i])

            if left - right[i] <= k:
                return i

        return -1