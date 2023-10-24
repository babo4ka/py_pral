#Алгортим Флойда

import math

n = int(input("введите n: "))

w = list()

w = [[0, math.inf, -2, math.inf], #исходная матрица
[4,0,3,math.inf],
[math.inf, math.inf, 0,2],
[math.inf, -1, math.inf, 0]]

# for i in range(n):
#     temp = list()
#     for j in range(n):
#         a = input("введите число: ")
#         temp.append(int(a) if a!= "i" else math.inf)
#     w.append(temp)

print("исходные данные:")
for i in range(n):
    print(w[i])

lastIter = w #записываем исходные данные как последнюю итерацию

#применяем формулу к каждому элементу матрицы
for k in range(n):
    for i in range(n):
        for j in range(n):
            w[i][j] = min(lastIter[i][j], lastIter[i][k-1] + lastIter[k-1][j]) 
            
    
    lastIter = w #записываем результат последней итерации

    print("результат на итерации :", k+1)
    for i in range(n):
        print(w[i])


print("результат:")
for i in range(n):
    print(w[i])