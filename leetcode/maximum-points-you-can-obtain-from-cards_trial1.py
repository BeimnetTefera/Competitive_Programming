class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        step = 0
        max_sum = 0
        cur_sum = 0
        left = -k

        for right in range(-k, k):
            cur_sum += cardPoints[right]
            step += 1

            while step > k:
                cur_sum -= cardPoints[left]
                left += 1
                step -= 1

            max_sum = max(max_sum, cur_sum)

        return max_sum