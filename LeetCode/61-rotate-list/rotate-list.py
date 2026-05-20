# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next:
            return head


        temp = head
        length = 0
        # find the length of the list
        while temp:
            length += 1
            tail = temp
            temp = temp.next

        print(length)

        # find step we should go 
        step = k % length
        # move cur until the new tail
        if step == 0:
            return head

        cur = head
        # tail points to head and become circular
        tail.next = head

        move = length - step

        while move:
            prev = cur
            cur = cur.next
            move -= 1
        
        new_head = cur
        prev.next = None

        return new_head