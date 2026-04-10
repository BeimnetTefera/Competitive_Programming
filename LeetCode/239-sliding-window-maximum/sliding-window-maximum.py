class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        right_ptr = left_ptr = 0
        que = deque()
        ans = []

        for i in range(len(nums)):
            while que and nums[que[-1]] < nums[i]:
                que.pop()

            que.append(i)
            right_ptr += 1

            if left_ptr > que[0]:
                que.popleft()
            
            if right_ptr >= k:
                ans.append(nums[que[0]])
                left_ptr += 1

        return ans