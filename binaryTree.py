class binaryTreeNode():
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None

    def print_node(self, depth):
        print('---' * depth, self.key)
        if self.left_child is not None:
            self.left_child.print_node(depth + 1)
        if self.right_child is not None:
            self.right_child.print_node(depth + 1)

    def insert_node(self, newNode):
        pass


class binaryTree():
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = binaryTreeNode(key)
            return
        current_node = self.root

        while current_node != key:
            if key < current_node.key:
                if current_node.left_child is None:
                    current_node.left_child = binaryTreeNode(key)
                    return
                else:
                    current_node = current_node.left_child
                    #return current_node

            if key > current_node.key:
                if current_node.right_child is None:
                    current_node.right_child = binaryTreeNode(key)
                    return
                else:
                    current_node = current_node.right_child
                    #return current_node

            if key == current_node.key:
                print 'key', key, ' already exist'
                return


    def print_tree(self):
        self.root.print_node(0)

if __name__ == '__main__':
    tree = binaryTree()
    tree.insert(5)
    tree.insert(28)
    tree.insert(17)
    tree.insert(22)
    tree.insert(21)
    tree.insert(229)
    tree.insert(222)
    tree.insert(2)
    tree.print_tree()
