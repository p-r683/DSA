class Solution:

    def combination(self, ind, subset,candidates, result, target):

        if target ==0:
           
            result.append(subset.copy())
            return

        if target < 0 or ind >= len(candidates):
            return

        for i in range(ind ,len(candidates)):
            if i > ind and candidates[i]==candidates[i-1]:
                continue
            subset.append(candidates[i])    
            sum=target-candidates[i]
            self.combination(i+1,subset,candidates,result,sum)
            subset.pop()
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result =[]
        candidates.sort()

        self.combination(
            0,
            [],
            candidates,
            result,
            target
        )

        return result