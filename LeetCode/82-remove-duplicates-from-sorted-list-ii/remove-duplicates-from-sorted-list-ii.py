# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        prev = dummy
        # if we had empty or single element
        if not head or not head.next:
            return head

        temp1 = head
        temp2 = head

        while temp1:
            temp2 = temp1
            i, j = 0, 0
            # check if the temp2 has equal value with temp1 until it finds different number
            while temp2 and temp1.val == temp2.val:
                temp2 = temp2.next
                j += 1
            # if the movement is movment of the pointer is morethan once change the pointer
            if j - i != 1:
                prev.next = temp2
                temp1 = temp2
            # if the movment is only once just don't change the pointer
            else:
                prev.next = temp1
                prev = temp1
                temp1 = temp2

        return dummy.next