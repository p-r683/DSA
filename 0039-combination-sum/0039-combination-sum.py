class Solution:

    def combination(self, ind, subset, total, candidates, result, target):

        if total == target:
            result.append(subset.copy())
            return

        if total > target or ind >= len(candidates):
            return

        # TAKE
        subset.append(candidates[ind])

        # ind stays same because we can reuse the element
        self.combination(
            ind,
            subset,
            total + candidates[ind],
            candidates,
            result,
            target
        )

        # BACKTRACK
        subset.pop()

        # NOT TAKE
        self.combination(
            ind + 1,
            subset,
            total,
            candidates,
            result,
            target
        )

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        self.combination(
            0,
            [],
            0,
            candidates,
            result,
            target
        )

        return result