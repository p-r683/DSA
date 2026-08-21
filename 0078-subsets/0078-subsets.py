class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        total_subset = 1 << n  # 2^n subsets
        result = []           
        
        for num in range(total_subset):
            lst = []          
            for i in range(0, n):
                if num & (1 << i) != 0:
                    lst.append(nums[i])  # Include if bit is set
            result.append(lst) 
        
        return result