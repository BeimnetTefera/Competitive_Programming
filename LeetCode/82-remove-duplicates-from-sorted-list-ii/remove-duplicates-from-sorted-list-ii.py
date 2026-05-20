# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        nums = []

        temp = head

        while temp:
            nums.append(temp.val)
            temp = temp.next
        

        distinct = []
        left = 0
        right = 1
        duplicate = False

        while left <= right and right < len(nums):

            if nums[left] == nums[right]:
                duplicate = True
                right += 1
                continue

            if duplicate:
                left = right
                right += 1
                duplicate = False
                continue

            distinct.append(nums[left])

            left += 1
            right += 1

        if left == len(nums) - 1:
            if nums[left] != nums[left - 1]:
                distinct.append(nums[left])

        if distinct:
            new_head = ListNode(distinct[0])
            temp = new_head
            for i in range(1, len(distinct)):
                new_node = ListNode(distinct[i])
                temp.next = new_node
                temp = temp.next

            return new_head

        return None