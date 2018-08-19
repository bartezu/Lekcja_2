a = int(input('Podaj liczbe a '))
b = int(input('Podaj liczbe b: '))
o = input('Podaj operacje: =,-,*,/: ')
if o == "/" and b == 0:
	print("dzielenie przez zero!!!")

else:
	if o=='+':
		print (a+b)
	if o=='-':
		print (a-b)
	if o=='*':
		print (a*b)
	if o=='/':
		print (a/b)
	if o=='**':
		print (a**b)
