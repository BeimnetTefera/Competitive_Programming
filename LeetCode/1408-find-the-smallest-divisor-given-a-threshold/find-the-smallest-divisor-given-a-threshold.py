class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        max_value = max(nums)
        left = 1
        right = max_value
        answer = right
        
        while left <= right:
            mid = left + (right - left) // 2
            store = []
            for num in nums:
                store.append(math.ceil(num/mid))

            total = sum(store)

            if total <= threshold:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer