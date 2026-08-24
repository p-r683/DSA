class Solution:

    def solve(self,ind,subset,nums,result):
            if ind>=len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[ind])
            self.solve(ind+1,subset,nums,result)
            subset.pop()
            self.solve(ind+1,subset,nums,result) 
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        self.solve(0,[],nums,result)
        return result  
