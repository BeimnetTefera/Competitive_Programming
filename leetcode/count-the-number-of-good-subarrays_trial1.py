class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        pairs = 0
        good_subarr = 0
        n = len(nums)

        for right in range(n):
            freq[nums[right]] += 1
            pairs += (freq[nums[right]] - 1)

            while pairs >= k:
                good_subarr += n - right
                freq[nums[left]] -= 1
                pairs -= freq[nums[left]]
                left += 1

        return good_subarr