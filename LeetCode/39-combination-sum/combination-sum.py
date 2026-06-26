class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        store = []
        n = len(candidates)

        def findCombination (idx, target, store):
            # condition
            if idx == n:
                if target == 0:
                    ans.append(store[:])

                return

            # pick
            if target - candidates[idx] >= 0:
                store.append(candidates[idx])
                findCombination (idx, target - candidates[idx], store)
                # not pick
                store.pop()

            findCombination(idx + 1, target, store)

        findCombination(0, target, [])
        
        return ans