#Number 1
a = 600000
b = 7
c = 2

d = (a / b)
e = (a / c)
f = (e - d)

print(d)
print(e)
print(f)

#Number 2
L = 10000
XXL = 10150
XXXL = ((XXL / L) * 100)
print(XXXL)

#Number 3 
# -*- coding:utf -8 -*-
#!/usr/bin/python3

import random

chars = '1234567890QWERTYUIOPASDFGHJKKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
number = input('количество паролей?'+ "\n")
length = input('длина пароля?'+ "\n")
number = int(number)
length = int(length)
for n in range(number):
    pasword =''
    for i in range(length):
        pasword += random.choice(chars)
        print(pasword)
