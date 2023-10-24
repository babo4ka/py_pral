#Алгоритм сортировки Хоара
import random
numbersList = list()

n = int(input("введите количество чисел: "))

for i in range(n):
    numbersList.append(random.randint(0, 150))

print("исходный массив: ", numbersList)


def sort(numsList):
    if(len(numsList) < 2): #если длина массива меньше двух, то возвращается массив
        return numsList

    pivot = numsList[0] #опорным элементом выбирается первый элемент массива
    pivots = list() #массив значений равных опорному элементу
    left = list() #массив значений меньше опорного элемента
    right = list() #масси значений больше опорного элемента

    for i in numsList:
        if i < pivot:
            left.append(i) #если элемент меньше опорного, записываем в массив left

        elif i > pivot:
            right.append(i) #если больше - в массив right

        else:
            pivots.append(i) #если равен - в массив pivots

    return(sort(left) + pivots + sort(right)) #снова вызываем функцию для левой и правой части

print("результат: ", sort(numbersList))

