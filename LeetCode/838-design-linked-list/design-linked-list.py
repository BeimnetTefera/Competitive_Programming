class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)

        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next

        while cur != self.right and index > 0:
            cur = cur.next
            index -= 1

        if cur != self.right and index == 0:
            return cur.value

        return -1

    def addAtHead(self, val: int) -> None:
        prev = self.left
        next = self.left.next
        newNode = ListNode(val)

        prev.next = newNode
        newNode.prev = prev

        newNode.next = next
        next.prev = newNode

    def addAtTail(self, val: int) -> None:
        prev = self.right.prev
        next = self.right
        newNode = ListNode(val)

        prev.next = newNode
        newNode.prev = prev

        newNode.next = next
        next.prev = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next

        while cur != self.right and index > 0:
            cur = cur.next
            index -= 1

        if index == 0:
            prev = cur.prev
            newNode = ListNode(val)

            prev.next = newNode
            newNode.prev = prev

            newNode.next = cur
            cur.prev = newNode

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next

        while cur != self.right and index > 0:
            cur = cur.next
            index -= 1

        if cur != self.right and index == 0:
            prev = cur.prev
            next = cur.next

            prev.next = next
            next.prev = prev 


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)