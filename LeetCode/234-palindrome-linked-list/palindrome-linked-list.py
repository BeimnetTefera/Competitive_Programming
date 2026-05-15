# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp1 = head
        temp2 = head

        def helper(temp_head):

            nonlocal temp1
            
            if not temp_head:
                return True

            if not helper(temp_head.next):
                return False

            if temp_head.val != temp1.val:
                return False

            temp1 = temp1.next

            return True

        return helper(temp2)