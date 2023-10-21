#Красно-черное дерево

import random
import sys

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

    def printTree(self):
        self.printNode(self.root, True)


    def printNode(self, node, isLeft, space = ""):
        if node != None:
            sys.stdout.write(space)
            if isLeft:
                sys.stdout.write("L-----")
                space += "|    "
            else:
                sys.stdout.write("R-----")
                space += "     "

            print(node.item, "(", colors[node.color], ")")
            self.printNode(node.left, True, space)
            self.printNode(node.right, False, space)     
                   

    def insertItem(self, item):
        current = self.root
        parent = None
        isLeft = True

        while current != None:
            if item >= current.item:     
                parent = current   
                current = current.right
                isLeft = False
            else:
                parent = current
                current = current.left
                isLeft = True


        current = Node(item)
        current.parent = parent
        if isLeft:
            current.parent.left = current
        else:
            current.parent.right = current

        
t = Tree()
n = int(input("введите n: "))
for i in range(n):
    t.insertItem(random.randint(2,40))
t.printTree()