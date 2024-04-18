#Ordene 5 numeros de menor a mayor

from random import randint
numeros = [randint(1,5) for _ in range (5)]
print (numeros)
numeros.sort ()
print (numeros)
