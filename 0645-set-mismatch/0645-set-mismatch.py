class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        duplicate = 0
        missing = 0

        for i in range(1, len(nums) + 1):
            if freq.get(i, 0) == 2:
                duplicate = i
            elif freq.get(i, 0) == 0:
                missing = i

        return [duplicate, missing]