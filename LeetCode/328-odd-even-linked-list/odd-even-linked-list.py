# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        # works when we have nodes greater or equal to 4 nodes
        cur = head
        slow = head.next
        fast = slow.next

        evenHead = slow

        while fast:
            if fast.next:
                p2 = fast.next
            else: 
                p2 = None


            cur.next = fast
            fast.next = slow

            if p2:
                slow.next = p2
            else:
                slow.next = None


            # move pointers
            cur = fast
            slow = p2

            if p2:
                fast = p2.next
            else:
                fast = None


        cur.next = evenHead

        return head
        