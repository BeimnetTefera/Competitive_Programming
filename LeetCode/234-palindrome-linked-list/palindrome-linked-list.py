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
        print(store)
        # compare
        temp = head
        j = len(store) - 1
        while temp:
            if temp.val != store[j]:
                return False

            temp = temp.next
            j -= 1

        return True