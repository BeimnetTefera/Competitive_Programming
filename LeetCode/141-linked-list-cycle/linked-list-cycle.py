# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        if not head or head.next is None:
            return False

        while fast and fast.next:

            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False