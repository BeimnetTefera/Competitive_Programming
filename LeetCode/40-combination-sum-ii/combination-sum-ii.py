class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        store = []
        candidates.sort()

        def helper(idx, k):

            if idx == len(candidates) or k == 0:
                if k == 0:
                    ans.append(store.copy())

                return

            # pick 
            if k - candidates[idx] >= 0:
                store.append(candidates[idx])
                helper(idx + 1, k - candidates[idx])

                # backtrack
                store.pop()

            # skip duplicates
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1

            # not pick
            helper(idx + 1, k)

        helper(0, target)

        return ans 