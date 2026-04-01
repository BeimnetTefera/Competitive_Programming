# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        k = head
        dummy = ListNode(-1, head)
        slow = dummy 
        fast = dummy
        while k:
            count += 1
            k = k.next

        mid = int(count / 2)
        if count % 2 == 0:
            
            for _ in range(mid):
                fast = fast.next

        else:
            for _ in range(mid + 1):
                fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        return slow.next
