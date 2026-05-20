# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        prev = dummy

        if not head or not head.next:
            return head

        temp1 = head
        temp2 = head

        while temp1:
            temp2 = temp1
            i, j = 0, 0

            while temp2 and temp1.val == temp2.val:
                temp2 = temp2.next
                j += 1

            if j - i != 1:
                prev.next = temp2
                temp1 = temp2
            else:
                prev.next = temp1
                prev = temp1
                temp1 = temp2

        return dummy.next