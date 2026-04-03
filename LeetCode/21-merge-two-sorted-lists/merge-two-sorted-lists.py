# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        store = []
        temp1 = list1
        temp2 = list2
        while temp1:
            store.append(temp1.val)
            temp1 = temp1.next

        while temp2:
            store.append(temp2.val)
            temp2 = temp2.next

        if not store:
            return None

        store.sort()
        head = ListNode(store[0])
        temp = head
        for i in range(1, len(store)):
            new_node = ListNode(store[i])
            temp.next = new_node
            temp = temp.next

        return head