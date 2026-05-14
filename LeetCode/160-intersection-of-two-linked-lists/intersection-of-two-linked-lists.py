# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1 = headA
        temp2 = headB

        while temp1 != temp2:
            temp1 = temp1.next
            temp2 = temp2.next

            if temp1 == temp2:
                return temp1

            if not temp1:
                temp1 = headB
            if not temp2:
                temp2 = headA


        return temp1