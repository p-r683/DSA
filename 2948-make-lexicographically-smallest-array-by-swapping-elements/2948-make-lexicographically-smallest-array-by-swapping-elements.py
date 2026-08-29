class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # (value, original_index)
        arr = sorted(zip(nums, range(n)))

        ans = [0] * n

        i = 0

        while i < n:
            j = i + 1

            # Find one connected group
            while j < n and arr[j][0] - arr[j - 1][0] <= limit:
                j += 1

            # Original indices of this group
            indices = sorted(k for _, k in arr[i:j])

            # Smallest values are already sorted in arr[i:j]
            for index, (value, _) in zip(indices, arr[i:j]):
                ans[index] = value

            i = j

        return ans