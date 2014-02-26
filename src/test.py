listOfSymbols = {'a':1, 'b':2}
fileText="aaaaaaaabbbbbababbbaaba"
i = 0
while i < len(fileText):
	if fileText[i] in listOfSymbols:
		number = listOfSymbols[fileText[i]] + 1
		listOfSymbols[fileText[i]] = number
	else:
		listOfSymbols[fileText[i]] = 1
	i=i+1
print(listOfSymbols)