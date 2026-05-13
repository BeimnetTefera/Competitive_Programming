# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        store = []
        temp1 = head
        temp2 = head.next

        while temp1 or temp2:
            # store odd values in store first
            if temp1:
                store.append(temp1.val)
                if temp1.next:
                    temp1 = temp1.next.next
                else:
                    temp1 = temp1.next
                
            # store even values in store nect to odd
            elif temp2:
                store.append(temp2.val)
                if temp2.next:
                    temp2 = temp2.next.next
                else:
                    temp2 = temp2.next

        # travere all over the stored array
        temp = head
        idx = 0
        while temp:
            # replace the existing value with a value in store
            temp.val = store[idx]
            temp = temp.next
            idx += 1

        return head