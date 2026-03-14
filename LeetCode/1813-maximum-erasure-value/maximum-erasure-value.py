class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        max_sum = 0
        cur_sum = 0
        store = {}

        for right in range(len(nums)):
            store[nums[right]] = store.get(nums[right], 0) + 1
            cur_sum += nums[right]

            while store[nums[right]] > 1:
                store[nums[left]] -= 1
                cur_sum -= nums[left]
                if store[nums[left]] == 0:
                    del store[nums[left]]

                left += 1

            max_sum = max(max_sum, cur_sum)

        return max_sum