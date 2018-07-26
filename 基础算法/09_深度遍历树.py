class Node(object):
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)
    # 广度遍历

    def breath_travel(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.item, end=' ')
            if cur_node.lchild:
                queue.append(cur_node.lchild)
            if cur_node.rchild:
                queue.append(cur_node.rchild)

    # 前序遍历
    def preorder(self, node):
        if node is None:
            return
        print(node.item, end=" ")
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    # 中序遍历
    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.item, end=" ")
        self.inorder(node.rchild)

    # 后序遍历
    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.item, end=" ")

if __name__ == "__main__":
    import random
    tree = Tree()
    alist = [i for i in range(3,25,3)]
    random.shuffle(alist)
    for each in alist:
        tree.add(each)

    
    # print('\n先序', end=" ")
    tree.preorder(tree.root)
    print('\n中序', end=" ")
    tree.inorder(tree.root)
    print('\n后序', end=" ")
    tree.postorder(tree.root)
    print('\n'*30)
    print('\n原序', end=" ")
    tree.breath_travel()