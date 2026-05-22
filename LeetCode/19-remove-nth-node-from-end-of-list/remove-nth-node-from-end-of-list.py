# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next

        if n == length:
            head = head.next
        else:
            mov = length - n - 1
            temp1 = head

            while mov:
                mov -= 1
                temp1 = temp1.next


            temp1.next = temp1.next.next
        return head
