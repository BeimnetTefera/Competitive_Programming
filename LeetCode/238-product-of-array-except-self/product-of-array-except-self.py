class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        cur_pfx = nums[0]
        for i in range(1, len(nums)):
            cur_pfx *= nums[i]
            prefix.append(cur_pfx)
        print(prefix)

        suffix = [nums[-1]]
        cur_sfx = nums[-1]
        for j in range(len(nums) - 2, -1, -1):
            cur_sfx *= nums[j]
            suffix.append(cur_sfx)

        suffix.reverse()
        print(suffix)

        ans = []
        for idx in range(len(nums) - 1):
            if idx > 0 and idx < len(nums):
                ans.append(prefix[idx - 1] * suffix[idx + 1])
            elif idx == 0:
                ans.append(suffix[idx + 1])
        ans.append(prefix[-2])
        return ans

# 1 2 3 4
  
# 1 2 6 24
# 24 24 12 4

# 24 12 8 6