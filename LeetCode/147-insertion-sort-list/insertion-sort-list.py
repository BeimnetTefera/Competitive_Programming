# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
            
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
            
        arr.sort()
        new_head = ListNode(arr[0])
        cur = new_head
        
        for i in range(1, len(arr)):
            
            new_node = ListNode(arr[i])
            
            cur.next = new_node
            cur = cur.next
            
        return new_head