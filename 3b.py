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
        self.insertFix(current)

    

    def insertFix(self, node):
        while node.parent.color == 1:
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left
                if uncle.color == 1:
                    uncle.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rightRotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 0
                    self.leftRotate(node.parent.parent)
            else:
                uncle = node.parent.parent.right

                if uncle.color == 1:
                    uncle.color = 0
                    node.parent.color = 0
                    node.parent.parent = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.leftRotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.rightRotate(node.parent.parent)
                if node == self.root:
                    break
        self.root.color = 0
                


        
t = Tree()
n = int(input("введите n: "))
for i in range(n):
    t.insertItem(random.randint(2,40))
t.printTree()