a = int(input('Podaj poczatek zakresu: '))
b = int(input('Podaj koniec zakresu: '))

for i in range(a,b+1):
	if i % 5 == 0:
			print (i)
