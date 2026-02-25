class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

        result = []
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)

        if result:
            return result

        else:
            return nums