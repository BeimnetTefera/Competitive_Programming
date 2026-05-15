# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        store = []
        temp = head

        while temp:
            store.append(temp.val)
            temp = temp.next

        left = 0
        right = len(store) - 1

        while left <= right:
            if store[left] != store[right]:
                return False

            left += 1
            right -= 1
            
        return True