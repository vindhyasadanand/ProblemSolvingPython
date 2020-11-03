class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self,data):
        self.root = Node(data)
    def print_tree(self,traversal_type):
        if traversal_type =='preorder':
            return self.preorder_print(tree.root," ")
        elif traversal_type=='inorder':
            return self.inorder_print(tree.root," ")
        elif traversal_type=='postorder':
            return self.post_order(tree.root," ")

        else:
            print("traversal type is not supported")
            return False

    def preorder_print(self,start,traversal):
        if start:
            traversal +=(str(start.value)+"-")
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.right,traversal)

        return traversal
    def inorder_print(self,start,traversal):
        if start:
            traversal = self.inorder_print(start.left,traversal)
            traversal += (str(start.value)+"-")
            traversal = self.inorder_print(start.right,traversal)
        return traversal

    def post_order(self,start,traversal):
        if start:
            traversal = self.post_order(start.left,traversal)
            traversal = self.post_order(start.right,traversal)
            traversal += (str(start.value)+'-')
        return traversal






tree = BinaryTree(1)
tree.root.left =Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree('preorder'))
print(tree.print_tree('inorder'))
print(tree.print_tree('postorder'))

