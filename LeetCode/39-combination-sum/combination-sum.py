class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        store = []

        def helper(idx, k):

            # base case
            if idx == len(candidates):
                if k == 0:
                    ans.append(store.copy())

                return


            # pick
            if k - candidates[idx] >= 0:

                store.append(candidates[idx])
                helper(idx, k - candidates[idx])

                # backtrack
                store.pop()
                
            # not pick
            helper(idx + 1, k)

        helper(0, target)

        return ans