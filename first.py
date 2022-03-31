
intake="aahfckgkuutkgvktkgk"
l=[]
for letter in intake:
	print(letter,end="")
	if letter not in l:
		l.append(letter)

print(l)