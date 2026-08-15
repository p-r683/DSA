class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        max_count=0
        for i in range(n):
            if nums[i]==1:
                count=count+1
            else:
                count=0    
            max_count=max(max_count,count)    
        return max_count