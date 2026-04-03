# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        infinity = float("inf")
        temp1 = list1
        temp2 = list2

        if not list1:
            list1 = ListNode(infinity)
        if not list2:
            list2 = ListNode(infinity)

        while temp1 and temp1.next:
            temp1 = temp1.next

        if temp1:
            temp1.next = ListNode(infinity)

        while temp2 and temp2.next:
            temp2 = temp2.next

        if temp2:
            temp2.next = ListNode(infinity)

        temp3 = list1
        temp4 = list2
        result = ListNode(0)
        cur = result
        while temp3 and temp4 and cur:
            if temp3.val <= temp4.val and temp3.val != infinity:
                cur.next = ListNode(temp3.val)
                temp3 = temp3.next

            elif temp4.val < temp3.val and temp4.val != infinity:
                cur.next = ListNode(temp4.val)
                temp4 = temp4.next

            if cur:
                cur = cur.next

        return result.next