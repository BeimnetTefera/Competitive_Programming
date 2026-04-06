"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        store = {}
        temp = head

        while temp:
            new_node = Node(temp.val)
            store[temp] = new_node
            temp = temp.next

        temp = head

        while temp:
            copy_node = store[temp]
            if temp.next:
                copy_node.next = store[temp.next]
            if temp.random:
                copy_node.random = store[temp.random]
            temp = temp.next

        return store[head]