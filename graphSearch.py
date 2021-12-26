class Node():
    def __init__(self, value, left, right, middle):
        self.value = value
        self.left = left
        self.right = right
        self.middle = middle
    
    def getValue(self):
        return self.value
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def getMiddle(self):
        return self.middle

    def printNode(self):
        print('{', ' value = ', self.value, ' left = ', self.left, ' right = ', self.right, ' }')

class Graph():
    def __init__(self, root):
        self.root = root
    
    def getRoot(self):
        return self.root
    
    def setRoot(self, root):
        self.root = root


# layer 4
node21 = Node(21, None, None, None)
node22 = Node(22, None, None, None)
node23 = Node(23, None, None, None)
node24 = Node(24, None, None, None)
node25 = Node(25, None, None, None)
node26 = Node(26, None, None, None)
node27 = Node(27, None, None, None)
node28 = Node(28, None, None, None)
node29 = Node(29, None, None, None)
node30 = Node(30, None, None, None)
node31 = Node(31, None, None, None)
node32 = Node(32, None, None, None)
node33 = Node(33, None, None, None)
node34 = Node(34, None, None, None)
node35 = Node(35, None, None, None)
node36 = Node(36, None, None, None)

# layer 3
node9 = Node(9, node21, node22, None)
node10 = Node(10, node23, node24, None)
node11 = Node(11, None, None, None)
node12 = Node(12, None, None, None)
node13 = Node(13, None, None, None)
node14 = Node(14, node25, node26, None)
node15 = Node(15, node27, node28, None)
node16 = Node(16, node29, node30, None)
node17 = Node(17, node31, node32, None)
node18 = Node(18, node33, node34, None)
node19 = Node(19, node35, node36, None)
node20 = Node(20, None, None, None)
node21 = Node(21, None, None, None)

# layer 2
node3 = Node(3, node9, node10, None)
node4 = Node(4, node11, node12, None)
node5 = Node(5, node13, node15, node14)
node6 = Node(6, node16, node17, None)
node7 = Node(7, node18, node19, None)
node8 = Node(8, node20, node21, None)

# layer 1
node1 = Node(1, node3, node5, node4)
node2 = Node(2, node6, node8, node7)

# lyaer 0
node0 = Node(0, node1, node2, None)
graph = Graph(node0)


def printInOrderTraversal(root):
    if root.left != None:
        printInOrderTraversal(root.left)
    
    print(root.value)
    
    if root.middle != None:
        printInOrderTraversal(root.middle)

    if root.right != None:
        printInOrderTraversal(root.right)



def printPreOrderTraversal(root):
    print(root.value)
    
    if root.left != None:
        printPreOrderTraversal(root.left)
    
    if root.middle != None:
        printPreOrderTraversal(root.middle)

    if root.right != None:
        printPreOrderTraversal(root.right)



def printPostOrderTraversal(root):
    if root.left != None:
        printPostOrderTraversal(root.left)
    
    if root.middle != None:
        printPostOrderTraversal(root.middle)

    if root.right != None:
        printPostOrderTraversal(root.right)
    
    print(root.value)


def depthFirstSearch(root, toFind):
    stack = []
    stack.append(root)
    found = False

    while len(stack) > 0 and not found:
        current = stack.pop()

        if current.value == toFind:
            current.printNode()
            found = True
        else:
            if current.left != None:
                stack.append(current.left)

            if current.middle != None:                
                stack.append(current.middle)

            if current.right != None:
                stack.append(current.right)
    
    
    if not found:
        print('Cannot find value ', toFind)


def breadthFirstSearch(root, toFind):
    queue = []
    queue.append(root)
    found = False

    while len(queue) > 0 and not found:
        current = queue[0]
        del queue[0]

        if current.value == toFind:
            found = True
            current.printNode()
        else:
            if current.left != None:
                queue.append(current.left)
            
            if current.middle != None:
                queue.append(current.middle)

            if current.right != None:
                queue.append(current.right)

    if not found:
        print('Cannot find value ', toFind)
