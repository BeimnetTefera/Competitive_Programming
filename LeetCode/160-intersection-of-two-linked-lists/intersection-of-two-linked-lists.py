# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        store = set()

        temp1 = headA
        while temp1:
            store.add(temp1)
            temp1 = temp1.next
            
        temp2 = headB
        while temp2:
            if temp2 in store:
                return temp2
            temp2 = temp2.next
            
        return None