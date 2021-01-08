# def mergeSortedLinkedList(head1,head2):
#     if head1.next == None:
#         res.next = head2
#     elif head2.next == None:
#         res.next = head1
#     else:
#         if head1.data<head2.data:
#             res.data=head1.data
#             res.next=None
#             head1=head1.next
#         else:
#             res.data=head2.data
#             res.next=None
#             head2=head2.next
#         return mergeSortedLinkedList(head1,head2)


class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=node(0)

    def addElement(self,data):
        element=node(data)
        cur=self.head
        while(cur.next!=None):
            cur=cur.next
        cur.next=element
    def printElements(self):
        cur=self.head
        while(cur.next!=None):
            cur=cur.next
            print(cur.data)
    
    def mergeSortedLinkedList(self,first,second,res): 
        while(first.next!=None or second.next!=None):   
            if(first is None):
                res = second.next      
            elif(second is None):
                res = first.next
            else:
                if first.data < second.data:
                    print(first.data)
                    res.data=first.data
                    first=first.next
                
                else:
                    print(second.data)
                    res.data=second.data
                    second=second.next

            res.next=None
        return res


firstList=LinkedList()
secondList=LinkedList()
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
mergedList=LinkedList()
mergedList=mergedList.mergeSortedLinkedList(firstList.head.next,secondList.head.next,mergedList.head)
# print("Merged Linked List")
# mergedList.printElements()
# # firstList.printElements()