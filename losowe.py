import random

lista = [0,0,0,0,0,0]
for i in range(0,6):
	lista[i] = random.randint(0, 1000)
lista.sort()
print(lista)