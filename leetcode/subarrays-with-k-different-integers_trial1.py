class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def atMost(k):
            cnt = 0
            left = 0
            store = {}

            for right in range(len(nums)):
                store[nums[right]] = store.get(nums[right], 0) + 1

                # shrink the window 
                while len(store) > k:
                    store[nums[left]] -= 1
                    if store[nums[left]] == 0:
                        del store[nums[left]]

                    left += 1

                cnt += right - left + 1
                
            return cnt

        return atMost(k) - atMost(k - 1)