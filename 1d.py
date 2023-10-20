#Алгоритм сортировки Хоара
import random
numbersList = list()

n = int(input("введите количество чисел: "))

for i in range(n):
    numbersList.append(random.randint(0, 150))

print("исходный массив: ", numbersList)



def sort(numsList):
    if(len(numsList) == 0):
        return numsList
    pivot = numsList[0]
    pivots = list()
    left = list()
    right = list()

    for i in numsList:
        if i < pivot:
            left.append(i)

        elif i > pivot:
            right.append(i)

        else:
            pivots.append(i)

    return(sort(left) + pivots + sort(right))

    
print("результат: ", sort(numbersList))

