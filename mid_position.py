class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new_node

    def add_beg(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def find_middle(self):
        if self.head is None:
            return None
        slow = self.head
        fast = self.head
        position = 1

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            position+=1
        return slow.data,position
    
    def display(self):
        itr = self.head

        while itr:
            print(itr.data, end=" --> ")
            itr = itr.next

        print("None")
ll = LinkedList()
ll.add_end(10)
ll.add_end(20)
ll.add_end(30)
ll.add_end(40)
ll.add_end(50)
print("Linked List:")
ll.display()
print("Middle Element:", ll.find_middle())