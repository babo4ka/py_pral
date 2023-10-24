#Красно-черное дерево

import random
import sys

class Node():#класс для узла дерева
    def __init__(self, item):
        self.item = item
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1 # 0 - черное, 1 - красное

colors = ["черное", "красное"]

class Tree():#класс дерева
    def __init__(self):
        self.nullNode = Node(0)
        self.nullNode.color = 0
        self.nullNode.left = None
        self.nullNode.right = None
        self.root = self.nullNode

    def printTree(self):
        self.printNode(self.root, False)


    def printNode(self, node, isLeft, space = ""):#функция для вывода узла дерева
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
                   

    def insertItem(self, item):#функция вставки элемента
        print("вставка ", item)
        newNode = Node(item)#создаем новый узел с заданным значением
        newNode.left = self.nullNode
        newNode.right = self.nullNode
        newNode.parent = None
        newNode.item = item
        newNode.color = 1

        current = self.root
        parent = None

        while current != self.nullNode:#ищем место для вставки нового узла
            parent = current   
            if newNode.item < current.item:     
                current = current.left
            else:
                current = current.right

        newNode.parent = parent

        if parent == None:
            self.root = newNode
        elif newNode.item > parent.item:
            parent.right = newNode
        else:
            parent.left = newNode


        if newNode.parent == None:
            newNode.color = 0
            return

        if newNode.parent.parent == None:
            return
        print("до балансировки")
        self.printTree()
        self.balanceInsert(newNode)
        print("после балансировки")
        self.printTree()

    

    def balanceInsert(self, node):#балансировка после вставки
        while node.parent.color == 1:
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left
                if uncle.color == 1: 
                    #перекрашиваем отца и дядю в черный, деда - в красный, если дядя и отец красные
                    uncle.color = 0 
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    #если дядя черный, выполняем левый поворот
                    if node == node.parent.left:
                        #если добавляемый узел был левым потомком, сначала выполняем правый поворот
                        node = node.parent
                        self.rightRotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 0
                    self.leftRotate(node.parent.parent)
            else:
                uncle = node.parent.parent.right
                if uncle.color == 1:
                    #перекрашиваем отца и дядю в черный, деда - в красный, если дядя и отец красные
                    uncle.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    #если дядя черный, выполняем правый поворот
                    if node == node.parent.right:
                        #если добавляемый узел был правым потомком, сначала выполняем левый поворот
                        node = node.parent
                        self.leftRotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.rightRotate(node.parent.parent)

            if node == self.root:
                break
        self.root.color = 0

    def deleteItem(self, item):
        print("удаление ", item)
        z = self.nullNode
        node = self.root
        while node != self.nullNode:
            #ищем узел с указанным значением
            if node.item == item:
                z = node
                break

            if node.item <= item:
                node = node.right
            else:
                node = node.left

        if z == self.nullNode:
            print("нет такого элемента")
            return

        if z.left == self.nullNode and z.right == self.nullNode:
            #если узел не имеет потомков, просто удаляем узел
            if z.parent.left == z:
                z.parent.left = self.nullNode
            elif z.parent.right == z:
                z.parent.right = self.nullNode
        elif z.left == self.nullNode or z.right == self.nullNode:
            #если имеет одного потомка, передаем родителю ссылку на его потомка
            if z.parent.parent.left == z.parent:
                z.parent.parent.left = z
            elif z.parent.parent.right == z.parent:
                z.parent.parent.right = z
            
            if z.color == 1 and z.parent.color == 1:
                z.color = 0
        else:
            #если у узла два потомка, то меняем его местами с ближайшим бОльшим узлом и удаляем
            y = z.right
            while y.left != self.nullNode:
                y = y.left
            z.item = y.item
            y_color = y.color
            y_parent = y.parent
            if y.right == self.nullNode:
                if y.item >= y.parent.item:
                    y.parent.right = self.nullNode
                else:
                    y.parent.left = self.nullNode
            else:
                if y.item >= y.parent.item:
                    y.parent.right = y.right
                else:
                    y.parent.left = y.right
            if y_color == 0:
                print("до балансировки")
                self.printTree()
                self.balanceDelete(y_parent)
                print("после балансировки")
                self.printTree()


    def balanceDelete(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    #если брат узла красный, то выполняем левый поворот
                    s.color = 0
                    x.parent.color = 1
                    self.leftRotate(x.parent)
                    s = x.parent.right
 
                if s.left.color == 0 and s.right.color == 0:
                    #если оба потомка брата черные, красим брата в красный и переходим к родителю узла
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        #если правый потомок брата черный, перекрашиваем брата и его левого потомка 
                        #и выполняем парвый поворот
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
        #перемещаем левого потомка правого потомка узла на позицию правого потомка узла
        y = x.right
        x.right = y.left
        if y.left != self.nullNode:
            y.left.parent = x
 
        y.parent = x.parent
        #перемещаем правого потомка узла на позицию потомка родителя узла
        if x.parent == None:
            #если узел был корнем, правый потомок узла становится корнем
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x#перемещаем узел на позицию левого потомка правого потомка узла
        x.parent = y
                
    def rightRotate(self, x):
        #перемещаем правого потомка левого потомка узла на позицию левого потомка узла
        y = x.left
        x.left = y.right
        if y.right != self.nullNode:
            y.right.parent = x
 
        y.parent = x.parent
        #перемещаем левого потомка узла на позицию потомка родителя узла
        if x.parent == None:
            #если узел был корнем, левый потомок узла становится корнем
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x#перемещаем узел на позицию правого потомка левого потомка узла
        x.parent = y


        
t = Tree()
n = int(input("введите n: "))
for i in range(n):
    t.insertItem(random.randint(2,150))
t.printTree()

for i in range(5):
    a = int(input("число для удаления: "))
    t.deleteItem(a)
    t.printTree()