# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next

        middle = (length // 2) - 1

        temp = head
        while middle:
            middle -= 1
            temp = temp.next

        temp.next = temp.next.next
        return head