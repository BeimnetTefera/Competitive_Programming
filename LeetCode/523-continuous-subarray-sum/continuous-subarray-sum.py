class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = set()
        running_sum = 0
        prev_mod = 0
        
        for num in nums:
            running_sum += num
            if k != 0:
                running_sum %= k
            
            if running_sum in seen:
                return True
            
            seen.add(prev_mod)
            prev_mod = running_sum
        
        return False