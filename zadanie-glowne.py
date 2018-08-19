q = ['Nazwa jezyka z tego kursu? ', 'Python jest napisany z wykorzystaniem bibliotek jezyka...? ', 'Czy program w Pythonie bedzie szybszy od programu w asemblerze? ', 'A czy prawdopodobnie zostanie szybciej napisany? ', 'Czy Python ma ponad 10 lat? ', 'Czy jest jakis zwiazek pomiedzy Pythonem a Monty Pythonem? ', 'Czy Ptyhon jest dobrze udokumentowany? ', 'Czy Python jest rozwijany? ', 'Czy Python ma dynamiczny system typow? ', 'Ile metrow dlugosci ma domniemany warszawski python? Zaokraglij w gore i podaj cyfrowo. ']
a = ['python', 'c', 'nie', 'tak', 'tak', 'tak', 'tak', 'tak', 'tak', '6']

ok = 0

for i in range(len(q)):

	an = input(q[i])
	if an.lower() == a[i]:
		print('OK! :)')
		ok = ok + 1
	else:
		print('NO OK :(')

print('Twoj wynik to ', ok, 'prawidlowych odpowiedzi, czyli ', ok/len(q)*100, '%')
