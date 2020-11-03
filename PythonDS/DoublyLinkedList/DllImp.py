class Node:
    def __init__(self,data):
        self.data=data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    #implementing append()
    def append(self,data):
        new_node = Node(data)
        # check if the list is empty
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        new_node.prev = cur
    # to calculate the lenght
    def get_length(self):
        if self.head is None:
            return 0
        count = 0
        cur = self.head
        while cur:
            count+=1
            cur = cur.next
        return count

    # print list
    def print(self):
        # check for empty list
        if self.head is None:
            print("Empty list")
            return
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
    # method to add value at the beginning of the list
    def prepend(self,data):
        new_node = Node(data)
       #check for empty list
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    # insert at specific location
    def insert_at(self,data,index):
        if index<0 or index>self.get_length():
            raise Exception("Index does not found")
        if index==0:
            self.prepend(data)
        else:
            count =0
            cur = self.head
            while cur:
                if count==index-1:
                    new_node = Node(data)
                    cur.next = new_node
                    new_node.prev= cur
                    break
                count+=1
                cur = cur.next













