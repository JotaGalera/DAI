from burbuja import Burbuja
from seleccion import Seleccion

import random

try:
	number=int(input("Number:"))
except ValueError:
	print("This is not a number.")

i=0
array = []

#while i < number:
for i in range(number):
    rand = random.randint(1,100)
    array.insert(i,rand)

print (array)

print("Burbuja:\n")
Burbuja(array)
print("Seleccion:\n")
Seleccion(array)
