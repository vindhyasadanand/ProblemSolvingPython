class Node:
    def __init__(self,data):
        self.data = data
        self.next=None
class CircularLinkedList:
    def __init__(self):
        self.head=None
    # function to add element at the end
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
        else:
            cur = self.head
            while cur.next !=self.head:
                cur = cur.next
            cur.next=new_node
            new_node.next = self.head
    # to print list
    def print_list(self):
        if self.head is None:
            return
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur.next ==self.head:
                print(cur.data)
                break

    #to add element at the beginning of the list
    def prepend(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
             cur = self.head
             while cur.next!=self.head:
                 cur = cur.next
             cur.next = new_node
             new_node.next = self.head
             self.head = new_node
list1  = CircularLinkedList()
list1.append("A")

list1.append("B")
#list1.print_list()
list1.prepend("C")
list1.print_list()
