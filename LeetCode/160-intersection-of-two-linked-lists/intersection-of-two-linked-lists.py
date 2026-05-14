# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        # helper function to check if the match is found or not
        def helper(head1, head2):

            while head1 and head2:

                if head1 == head2:
                    return head1

                head1 = head1.next
                head2 = head2.next

            return None

        # lenght count variables
        length_1 = 0
        length_2 = 0

        # traverse in the first linked list and count the length
        temp1 = headA
        while temp1:
            length_1 += 1
            temp1 = temp1.next

        # travers over the second linked list and count the length
        temp2 = headB
        while temp2:
            length_2 += 1
            temp2 = temp2.next

        # check the differnce
        diff = length_1 - length_2
        cnt = abs(diff)

        # assign the pointers
        cur1 = headA
        cur2 = headB

        # length_2 is greater if  diff is less than 0
        if diff < 0:
            while cnt:
                cur2 = cur2.next
                cnt -= 1

        # length_1 is greater if  diff is greater than 0
        elif diff > 0:
            while cnt:
                cur1 = cur1.next
                cnt -= 1

        # call helper function to get an answer
        return helper(cur1, cur2)