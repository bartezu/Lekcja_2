lista = ['Warszawa', 'Lodz', 'to-delete', 'to-delete', 'Wroclaw', 'to-delete', 'Krakow', 'Opole']
print(lista, '\n')

for i in range(lista.count('to-delete')):
	lista.remove('to-delete')
	
for index, miasto in enumerate(lista):
	print (index, miasto)
