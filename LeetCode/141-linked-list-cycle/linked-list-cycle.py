# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:

            # slow moves one step
            slow = slow.next

            # fast moves two steps 
            fast = fast.next.next

            # if fast catchs the slow there is a cycle
            if slow == fast:
                return True

        return False

        