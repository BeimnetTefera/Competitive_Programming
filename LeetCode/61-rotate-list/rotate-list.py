# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return None

        cnt = 1
        temp = head
        while temp: 
            if temp.next is None:
                tail = temp
                break

            temp = temp.next
            cnt += 1

        step = cnt - (k % cnt)
        temp = head

        while step > 0:
            tail.next = temp
            temp = temp.next
            tail = tail.next
            tail.next = None
            step -= 1
            
        return temp