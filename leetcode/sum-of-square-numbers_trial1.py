class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        nums = [i for i in range(int(math.sqrt(c)) + 1)]
        print(nums)
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            val = nums[left] ** 2 + nums[right] ** 2
            if val == c:
                return True

            elif val > c:
                right -= 1

            else:
                left += 1

        return False