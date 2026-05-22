# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        nums = []
        temp = head

        while temp:
            nums.append(temp.val)
            temp = temp.next

        nums.sort()

        new_head = ListNode(nums[0])
        cur = new_head

        for i in range(1, len(nums)):
            new_node = ListNode(nums[i])
            cur.next = new_node

            cur = cur.next

        return new_head
