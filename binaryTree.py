class bnode:

    def __init__(self, root=None):
        self.root = root
        self.left = None
        self.right = None

    def set_root(self, root):
        self.root = root

    def insert_left(self, bnode):
        self.left = bnode

    def insert_right(self, bnode):
        self.right = bnode

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

class binaryTree:

    def __init__(self, head=None):
        self.head = bnode(head)

    def insert(self, node, value):
        if value < node.root:
            if node.left == None:
                new_node = bnode(value)
                node.left = new_node
                print('inserted %s'%(value))
            else:
                self.insert(node.left, value)
        else:
            if node.right == None:
                new_node = bnode(value)
                node.right = new_node
                print('inserted %s'%(value))
            else:
                self.insert(node.right, value)

    def print_inorder(self):
        stack = []
        current_node = self.head.left
        while current_node != None:
            stack.append(current_node.root)
            current_node = current_node.left

        while len(stack) != 0:
            print(stack.pop())

        print(self.head.root)

        #Right Tree
        current_node = self.head.right
        while current_node != None:
            stack.append(current_node.root)
            current_node = current_node.right

        while len(stack) != 0:
            print(stack.pop())


if __name__ == '__main__':
    bt = binaryTree(4)
    bt.insert(bt.head, 3)
    bt.insert(bt.head, 2)
    bt.insert(bt.head, 1)
    bt.insert(bt.head, 8)
    bt.insert(bt.head, 7)
    bt.print_inorder()
