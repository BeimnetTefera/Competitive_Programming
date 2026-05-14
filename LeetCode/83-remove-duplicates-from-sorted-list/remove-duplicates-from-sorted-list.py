# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set()

        temp1 = head
        while temp1:
            nums.add(temp1.val)
            temp1 = temp1.next


        nums = sorted(nums)

        dummy = ListNode(-1)
        cur = dummy

        for num in nums:
            cur.next = ListNode(num)

            cur = cur.next

        return dummy.next