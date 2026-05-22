# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # if list had single element or doesn't have an elemnt return as it is cause no need to sort it
        if not head or not head.next:
            return head

        # find the middle of the linkedlist
        def findMiddle(head):
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        # merge function to connect the lists
        def merge(head1, head2):

            dummy = ListNode(-1)
            cur = dummy
            
            while head1 or head2:

                if head1 and head2:
                    if head1.val <= head2.val:
                        cur.next = head1
                        head1 = head1.next
                    else:
                        cur.next = head2
                        head2 = head2.next

                elif head1:
                    cur.next = head1
                    head1 = head1.next

                else:
                    cur.next = head2
                    head2 = head2.next

                cur = cur.next

            return dummy.next


        # find the middle of the node
        middle = findMiddle(head)

        # left part takes the previous head
        left_head = head
        # right part would take the node after the middle as head
        right_head = middle.next
        # disconnect the left part from the right
        middle.next = None

        # do the left part until one node lefts
        left_head = self.sortList(left_head)
        # do the right part again until one node lefts
        right_head = self.sortList(right_head)

        # mererge the right and left part
        return merge(left_head, right_head)