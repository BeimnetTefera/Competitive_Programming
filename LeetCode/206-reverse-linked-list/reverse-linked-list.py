# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        
        while curr:
            # save next
            next_node = curr.next
            # reverse 
            curr.next = prev
            # move fwd
            prev = curr
            curr = next_node

        return prev