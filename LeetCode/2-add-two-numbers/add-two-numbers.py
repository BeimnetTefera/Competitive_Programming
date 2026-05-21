# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-1)
        cur = dummy
        
        temp1 = l1
        temp2 = l2
        
        carry = 0
        digit = 0
        
        while temp1 or temp2:
            
            if temp1 and temp2:
                res = temp1.val + temp2.val + carry
                temp1 = temp1.next
                temp2 = temp2.next
                
            elif temp1:
                res = temp1.val + carry
                temp1 = temp1.next
                
            else:
                res = temp2.val + carry
                temp2 = temp2.next
                
            carry = res // 10
            digit = res % 10
            
            
            new_node = ListNode(digit)
            cur.next = new_node
            
            cur = cur.next
            

            
            
        if carry:
            new_node = ListNode(carry)
            cur.next = new_node
            
        return dummy.next
        