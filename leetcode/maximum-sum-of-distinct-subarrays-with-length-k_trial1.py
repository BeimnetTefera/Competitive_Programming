class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        cur_arr = {}
        cur_sum = 0
        max_sum = 0

        for i in range(k):
            cur_arr[nums[i]] = cur_arr.get(nums[i], 0) + 1
            cur_sum += nums[i]

            while cur_arr[nums[i]] > 1:
                cur_sum -= nums[left]
                cur_arr[nums[left]] -= 1
                if cur_arr[nums[left]] == 0:
                    del cur_arr[nums[left]]
                left += 1

        if len(cur_arr) == k:
            max_sum = cur_sum

        for right in range(k, len(nums)):
                      
            cur_arr[nums[right]] = cur_arr.get(nums[right], 0) + 1
            cur_sum += nums[right]

            while cur_arr[nums[right]] > 1:  
                cur_sum -= nums[left]
                cur_arr[nums[left]] -= 1  
                if cur_arr[nums[left]] == 0:
                    del cur_arr[nums[left]]
                left += 1

            if right - left + 1 > k:
                cur_sum -= nums[left]
                cur_arr[nums[left]] -= 1
                if cur_arr[nums[left]] == 0:
                    del cur_arr[nums[left]]
                left += 1

            if right - left + 1 == k and len(cur_arr) == k:
                max_sum = max(max_sum, cur_sum)

        return max_sum