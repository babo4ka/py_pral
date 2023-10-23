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
        if node != self.nullNode:
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
        newNode = Node(item)
        newNode.left = self.nullNode
        newNode.right = self.nullNode
        newNode.parent = None
        newNode.item = item
        newNode.color = 1

        current = self.root
        parent = None

        while current != self.nullNode:
            parent = current   
            if newNode.item >= current.item:     
                current = current.right
            else:
                current = current.left

        newNode.parent = parent

        if parent == None:
            self.root = newNode
        elif newNode.item > parent.item:
            parent.right = newNode
        else:
            parent.left = newNode


        if newNode.parent == None:
            current.color = 0
            return

        if newNode.parent.parent == None:
            return
        
        # if current != self.root:
        self.balanceInsert(current)

    

    def balanceInsert(self, node):
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

    def deleteItem(self, item):
        z = self.nullNode
        node = self.root
        while node != self.nullNode:
            if node.item == item:
                z = node

            if node.item <= item:
                node = node.right
            else:
                node = node.left

        if z == self.nullNode:
            print("нет такого элемента")
            return

        if z.left == self.nullNode and z.right == self.nullNode:
            if z.parent.left == z:
                z.parent.left = self.nullNode
            elif z.parent.right == z:
                z.parent.right = self.nullNode
        elif z.left == self.nullNode or z.right == self.nullNode:
            if z.parent.parent.left == z.parent:
                z.parent.parent.left = z
            elif z.parent.parent.right == z.parent:
                z.parent.parent.right = z
            
            if z.color == 1 and z.parent.color == 1:
                z.color = 0
        else:
            y = z.right
            while y.left != self.nullNode:
                y = y.left
            z.item, y.item = y.item, z.item
            y_color = y.color
            y_parent = y.parent
            deleteItem(y.item)        
            if y_color == 0:
                balanceDelete(y_parent)


    def balanceDelete(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.leftRotate(x.parent)
                    s = x.parent.right
 
                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.rightRotate(s)
                        s = x.parent.right
 
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.leftRotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.rightRotate(x.parent)
                    s = x.parent.left
 
                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.leftRotate(s)
                        s = x.parent.left
 
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.rightRotate(x.parent)
                    x = self.root
        x.color = 0



    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nullNode:
            y.left.parent = x
 
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
                
    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nullNode:
            y.right.parent = x
 
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y


        
t = Tree()
n = int(input("введите n: "))
for i in range(n):
    t.insertItem(random.randint(2,40))
    # t.insertItem(int(input("введите: ")))

t.printTree()