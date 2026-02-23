class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def insert_after(self, key, value):
        temp = self.head

        while temp and temp.data != key:
            temp = temp.next

        if temp is None:
            print("Element not found")
            return

        new_node = Node(value)
        new_node.next = temp.next
        temp.next = new_node

    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None

    def delete_after(self, key):
        temp = self.head

        while temp and temp.data != key:
            temp = temp.next

        if temp is None or temp.next is None:
            print("Deletion not possible")
            return

        temp.next = temp.next.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

sll = SinglyLinkedList()

sll.insert_end(10)
sll.insert_end(20)
sll.insert_end(30)
sll.display()

sll.insert_after(20, 25)
sll.display()

sll.delete_end()
sll.display()

sll.delete_after(10)
sll.display()