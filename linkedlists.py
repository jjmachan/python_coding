class Node:

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_next(self, next_node):
        self.next_node = next_node

    def get_next(self):
        return self.next_node

class LinkedList():

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
       
    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.get_next()
    
    def print_list(self):
        current = self.head
        while current != None:
            print(current.get_data())
            current = current.get_next()

    def search(self, query):
        current = self.head
        is_found = False
        while current != None:
            if current.get_data() == query:
                is_found = True
            current = current.get_next()

        if is_found:
            print(" Item found")
        else:
            print("Not Found")

    def delete(self, query):
        found = False
        current = self.head
        while current != None:
            if  current.get_data() == query:
                previous.set_next(current.get_next())
                found = True
            previous = current
            current = current.get_next()
            if found:
                print('delete successful!')

if __name__ == "__main__":
    list_linked = LinkedList()
    list_linked.insert(20)
    list_linked.insert(30)
    list_linked.insert(31)
    list_linked.insert(33)
    list_linked.insert(34)
    list_linked.print_list()

    list_linked.search(55)
    list_linked.search(20)

    list_linked.delete(20)
    list_linked.print_list()

    list_linked.print_list()
