# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val = 0
        carry = 0
        dummy = ListNode(-1)
        cur = dummy

        while l1 or l2:

            # if both of them are numbers
            if l1 and l2:
                summation = (l1.val + l2.val + carry)
                l2 = l2.next
                l1 = l1.next

            # if l2 is none
            elif l1:
                summation = l1.val + carry
                l1 = l1.next
            # if l1 is none
            elif l2:
                summation = l2.val + carry
                l2 = l2.next


            val = summation %  10
            carry = summation // 10

            cur.next = ListNode(val)

            # move the pointers
            cur = cur.next

        if carry > 0:
            cur.next = ListNode(carry)

        return dummy.next
