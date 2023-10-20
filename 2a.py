#Алгортим Флойда

import math

n = int(input("введите n: "))
m = int(input("введите m: "))

w = list()

# w = [[0, math.inf, -2, math.inf],
# [4,0,3,math.inf],
# [math.inf, math.inf, 0,2],
# [math.inf, -1, math.inf, 0]]

for i in range(n):
    temp = list()
    for j in range(m):
        a = input("введите число: ")
        temp.append(int(a) if a!= "i" else math.inf)
    w.append(temp)

print("исходные данные:")
for i in range(n):
    print(w[i])

lastIter = w

for k in range(m):
    for i in range(n):
        for j in range(m):
            w[i][j] = min(lastIter[i][j], lastIter[i][k-1] + lastIter[k-1][j])
    
    lastIter = w


print("результат:")
for i in range(n):
    print(w[i])