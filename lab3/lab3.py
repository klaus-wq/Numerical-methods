import numpy as np
from decimal import Decimal

'''n = 1
while n < 2:
    n = int(input("Введите размер матрицы: "))

mtx = np.zeros((n, n))
right = np.zeros(n)

print("Введите элементы матрицы:")
for i in range(n):
    for j in range(n):
        mtx[i][j] = float(input())

if np.linalg.det(mtx) == 0.0:
    print("Определитель должен быть не равен 0!")
    sys.exit(0)

print("Введите правую часть:")
for i in range(n):
    right[i] = float(input())

for i in range(len(mtx)): 
    print(mtx[i]," ", right[i])'''

eps = 0.00001
n = 5
mtx = [[0.45,0.03,-0.01,0.02,-0.111],[0.02,0.375,-0.01,-0.01,0],[0,0.07,0.44,0,0.113],[-0.03,0.015,-0.02,0.41,-0.084],[0.02,0.01,0,0,0.29]]
right = [-0.275,-0.78,1.745,-2.18,1.45]

print("Исходная матрица:")
for i in range(len(mtx)): 
    print(mtx[i]," ", right[i])

if np.linalg.det(mtx) == 0.0:
    print("Определитель должен быть не равен 0!")
    quit()

print("Транспонированная матрица:")

transpose_mtx = np.transpose(mtx)
for i in range(len(mtx)): 
    print(transpose_mtx[i]," ", right[i])

normal_mtx = np.dot(transpose_mtx, mtx)
normal_right = np.dot(transpose_mtx, right)

print("Нормализованная матрица:")
for i in range(len(normal_mtx)): 
    print(normal_mtx[i]," ", normal_right[i])

roots = np.zeros((n))
for i in range(n):
    roots[i] = Decimal(normal_right[i] / normal_mtx[i][i])

iterations = 0
while True:
    norm = 0
    for i in range(n):
        temp = normal_right[i] / normal_mtx[i][i]
        for j in range(n):
            if i != j:
                temp -= (normal_mtx[i][j] / normal_mtx[i][i]) * roots[j]
        diff = float("{0:.1f}".format(abs(roots[i] - temp)))
        #sb = abs(roots[i] - temp)
        if diff > norm:
            norm = diff
        roots[i] = temp
    if norm < eps: 
        break
    iterations += 1    

print("Корни:")
for i in range(n):
    print(roots[i])

print("Количество итераций:", iterations)

for i in range(n):
    for j in range(n):
        normal_right[i] -= normal_mtx[i][j] * roots[j]

print("Вектор невязок: ")
print(normal_right)
