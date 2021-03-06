class node:
    def __init__(self, data=None, next=None, prev=None):
        self.next = next
        self.prev = prev
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = node(0)

    def addElement(self, data):
        element = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = element

    def printElements(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next
            print(cur.data)

    def mergeSortedLinkedList(self, first, second, res):
        while True:
            if first is None:
                res.next = second
                return
            elif second is None:
                res.next = first
                return
            else:
                if first.data < second.data:
                    res.next = first
                    first = first.next

                else:
                    res.next = second
                    second = second.next
            # print(res.next.data)
            res = res.next
            res.next = None
        return res


firstList = LinkedList()
secondList = LinkedList()
firstList.addElement(1)
firstList.addElement(2)
firstList.addElement(5)

secondList.addElement(3)
secondList.addElement(4)
secondList.addElement(6)

print("First Linked List")
firstList.printElements()
print("Second Linked List")
secondList.printElements()

print("inside function")
mergedList = LinkedList()
mergedList.mergeSortedLinkedList(
    firstList.head.next, secondList.head.next, mergedList.head
)
mergedList.printElements()
