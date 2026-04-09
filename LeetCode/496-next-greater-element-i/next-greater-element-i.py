class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
            # populate the store with -1 vlue
            store = {num : -1 for num in nums1}

            stack = []
            # loop through the ararray nums2 and fill tht stack in decreasing manner
            for i in range(len(nums2)):
                # if there is vlue in stack and the current value greater than top of stack
                while stack and stack[-1] < nums2[i]:
                    # remove the top of the stack
                    stack_top = stack.pop()
                    # if the popped value in store
                    if stack_top in store:
                        # store of the popped value is updated with the greater number
                        store[stack_top] = nums2[i]

                # add to the stack
                stack.append(nums2[i])
            # move through store values and add it to some variable
            result = [store[num] for num in nums1]

            return result
