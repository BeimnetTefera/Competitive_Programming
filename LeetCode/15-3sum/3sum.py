class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        
        result = []
        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            p1 = i + 1
            p2 = len(nums) - 1
            
            while p1 < p2:

                if nums[i] + nums[p1] + nums[p2] == 0:
                    result.append([nums[i], nums[p1], nums[p2]])
                    p1 += 1
                    p2 -= 1

                    while p1 < p2 and nums[p1] == nums[p1-1]:
                        p1 += 1

                    while p1 < p2 and nums[p2] == nums[p2+1]:
                        p2 -= 1

                elif nums[p1] + nums[p2] + nums[i] < 0:
                    p1 += 1
                    
                else:
                    p2 -= 1

        return result