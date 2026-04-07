# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        temp1, temp2 = l1, l2
        carry , digit = 0, 0

        cur = None
        while temp1 or temp2:
            # get the number one
            if temp1:
                num1 = temp1.val
            else:
                num1 = 0
            # move pointer None
            if temp1 is not None:
                temp1 = temp1.next
            # get number 2
            if temp2:
                num2 = temp2.val
            else:
                num2 = 0
            # move pointer if not none
            if temp2 is not None:
                temp2 = temp2.next

            # do the calculation
            sum_ = num1 + num2 + carry

            carry = sum_ // 10
            digit = sum_ % 10

            new_node = ListNode(digit)
            if cur is None:
                cur = new_node
                head = cur
            else:
                cur.next = new_node
                cur = cur.next
                
        # if carry add to the last one
        if carry:
            new_node = ListNode(carry)
            cur.next = new_node

        return head