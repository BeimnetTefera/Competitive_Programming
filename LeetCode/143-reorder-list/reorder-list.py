# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
       
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        middle = slow.next
        slow.next = None


        prev = None
        temp = middle
        front = middle

        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        new_head = prev

        temp1 = head
        front1 = head.next
        temp2 = new_head
        front2 = new_head.next

        while temp1 and temp2:
            temp1.next = temp2
            temp1 = front1

            temp2.next = temp1
            temp2 = front2
            
            if front1 and front2:
                front1 = front1.next
                front2 = front2.next

        return head
