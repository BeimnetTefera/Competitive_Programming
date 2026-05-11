# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # cur and head are pointers to newly created linked list
        dummy = ListNode(-1)
        cur = dummy
        # assign the pointers
        ptr1 = list1
        ptr2 = list2
        # compare the two values and form the array
        while ptr1 and ptr2:

            if ptr1.val >= ptr2.val:
                cur.next = ptr2
                ptr2 = ptr2.next

            else:
                cur.next = ptr1
                ptr1 = ptr1.next

            # move the pointer
            cur = cur.next

        # if the traverse didn't end
        if ptr1:
            cur.next = ptr1

        elif ptr2:
            cur.next = ptr2

        return dummy.next
