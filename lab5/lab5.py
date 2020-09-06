import math
import numpy
from scipy.misc import derivative
from sympy import diff
import mpmath
import decimal

def math_func(x):
    return x*x*x - 6*x + 2 #функция

eps = float(input("Введите точность: "))
a = float(input("Введите левую границу интервала: "))
a1 = a
b = float(input("Введите правую границу интервала: "))
b1 = b
x = (b+a)/2 #полагаем значение х
count1 = 0 #кол-во итераций методом бисекции
count2 = 0 #кол-во интераций методом Ньютона

if math_func(a) * math_func(b) >= 0:
    print('Не выполнено условие теоремы о выделении корня!')
    quit()

print('Метод бисекции:')
while b-a >= eps*2:
    if math_func(x)*math_func(a) > 0:
        a = x
    else:
        b = x
    count1 += 1
    x = (b+a)/2
    print('Номер','Начало', 'Конец', 'Середина', 'Длина')
    print(count1, a, b, ((a+b)/2), (b-a))


print("Корень: %f" % x)
print("Значение функции при найденном корне: %f" % math_func(x))
print("Количество итераций: %d" % count1)

f1 = 0
if math_func(a1)*derivative(math_func, a1, n=2) > 0:
	x0 = a1
elif math_func(b1)*derivative(math_func, b1, n=2) > 0:
	x0 = b1
else:
	for i in range(a1, b1, 0.1):
		if math_func(i)*derivative(math_func, i, n=2) > 0:
			x0 = i
			fl = 1
			break
	if fl == 0:
		print("Не могу подобрать начальное значение! Не выполяняется теорема о сходимости!")
		quit()

print('Метод Ньютона:')
print("Начальное приближение: %d" %x0)

x1 = x0 - (math_func(x0))/(derivative(math_func, x0))
count2 += 1
print("Номер","Xn")
print(count2, x1)

while abs(x1-x0) > eps:
    x0 = x1
    x1 = x0 - (math_func(x0))/(derivative(math_func, x0))
    count2 += 1
    print("Номер","Xn")
    print(count2, x1)

print("Корень: %f"%x1)
print("Значении функции при найденном корне: %f"%math_func(x1))
print("Количество итераций: %d"%count2)



