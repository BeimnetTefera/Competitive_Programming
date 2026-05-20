# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        deq = deque()

        temp = head
        while temp:
            deq.append(temp.val)
            temp = temp.next

        deq.rotate(k)
        
        new_head = ListNode(deq[0])
        cur = new_head
        for i in range(1, len(deq)):
            new_node = ListNode(deq[i])
            cur.next = new_node

            cur = cur.next

        return new_head