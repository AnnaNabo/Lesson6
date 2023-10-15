# -*- coding: cp1251 -*-
#1
print("1. введите количество чисел:")
n = int(input())
i = 0
kn = 0
while i<n:
    x = int(input())
    if x == 0:
        kn+=1
    i+=1
print("количество нулей: ", kn)

#2
print("2. введите число")
x = int(input())
delitel = 2
kd = 1

if x > 9:
    kd=2

a = ""

while x > 1:
    if x%delitel == 0:
            kd+=1
            x = x//delitel
            a = a + str(delitel)
#            print(x, kd, delitel)
#            print(a)
            delitel =2
    else:
            delitel+=1


spisokd = list(a)
kd =1
#print(a)

delitel = 2
while delitel<=10:
    kd = kd*(a.count(str(delitel)) + 1)
    delitel +=1

print("количество делителей:", kd)


#3
print("введите число A")
a = int(input())

print("введите число B")
b = int(input())
s = ""

while a<=b:
    if a%2 == 0: 
        s = s + str(a) + " "
    a = a+1
print (s)