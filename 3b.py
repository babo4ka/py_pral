#Красно-черное дерево

class Node():
    def __init__(self, item):
        self.item = item
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1 # 0 - черное, 1 - красное

colors = ["черное", "красное"]

class Tree():
    def __init__(self):
        self.nullNode = Node(0)
        self.nullNode.color = 0
        self.nullNode.left = None
        self.nullNode.right = None
        self.root = self.nullNode

    def printTree():
        printNode(self.root, False)

    space = ""

    def printNode(node, isLeft):
        if node != nullNode:
            print(space)
            if isLeft:
                print("L-----")
                space += "|    "
            else:
                print("R-----")
                space += "     "


        print(node.item, "(", colors[node.color], ")")
        printNode(node.left, True)
        printNode(node.right, False)            

     
       