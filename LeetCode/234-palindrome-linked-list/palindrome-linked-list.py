# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next:
            return True

        # get the middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse
        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Compare half
        left = head
        right = prev   

        while right: 
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True