# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        odd = head
        even = head.next
        con = head.next

        while even and even.next:

            # connect the odd 
            odd.next = odd.next.next
            # move the odd pointer
            odd = odd.next

            # connect the even 
            even.next = even.next.next
            # move the even pointer
            even = even.next

        # connect thr even to odd
        odd.next = con

        return head