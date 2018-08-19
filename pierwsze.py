a = int(input('Podaj do jakiej liczby sprawdzac: '))

dzielniki=0
for i in range(2, a+1):
	dzielniki = 0
	for j in range(2, i):
		if i % j == 0:
			break
	else:				# to else uzyte "na haku" - dotyczy for a nie if!
		print(i)
