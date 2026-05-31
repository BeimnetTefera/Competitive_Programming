class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)

        for i in range (n):
            val = float("inf")
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    val = nums[j]
                    break
            if val != float("inf"):
                res.append(val)
            else:
                res.append(None)

        print(res)

        for cur_idx in range(n):
            if res[cur_idx] == None:
                for prev_idx in range(cur_idx):
                    if nums[prev_idx] > nums[cur_idx]:
                        res[cur_idx] = nums[prev_idx]
                        break
                if res[cur_idx] == None:
                    res[cur_idx] = -1
                
        return res