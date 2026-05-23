# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        temp = head
        # count the length of the linked list
        while temp:
            length += 1
            temp = temp.next

        # find the amount for each box and the remainder
        remainder = length % k
        size = length // k

        result = []
        cur = head

        for i in range(k):
            part_head = cur
            part_size = size 
            
            if remainder:
                part_size += 1
                remainder -= 1

            for j in range(part_size - 1):
                if cur:
                    cur = cur.next


            if cur:
                next_head = cur.next
                cur.next = None
                cur = next_head

            result.append(part_head)

        return result


        # def mov (fast):
        #     count = 0
        #     store = []
        #     while count != amount:
        #         store.append(fast.val)
        #         fast = fast.next
        #         count += 1

        #     if remainder:
        #         store.append(fast.val)
        #         fast = fast.next
        #         remainder -= 1

        #     return store

        # main part 
        # dummy = ListNode(-1)
        # cur = dummy

        # slow = head
        # fast = head
        # step = 0

        # while step != amount:
        #     res = mov(fast)
        #     cur.next = ListNode(res)
        #     cur = cur.next
        #     step += 1

        # return dummy.next