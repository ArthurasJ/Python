#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re

def getArguments():
	if sys.argv[1] == "help":
		sys.exit("Naudojimas:  python statistics.py '/nuoroda/iki/aplanko/ištyrimui/' '/nuoroda/iki/rezultatų/failo/' 'failopavadinimas' ")
	if len(sys.argv) > 4: #argumentų skaičius negali būti didesnis nei 2
		sys.exit("Klaida: Per daug parametrų arba jie nurodyti nekorektiškai. 'Python statistics.py help' - naudojimo instrukcija")
	if len(sys.argv) < 4: #argumentų skaičius negali būti mažesnis nei 2
		sys.exit("Klaida: Per mažai parametrų arba jie nurodyti nekorektiškai. 'Python statistics.py help' - naudojimo instrukcija")
	
	pathForAnalysis = sys.argv[1] #nuoroda iki norimo aplanko analizei
	pathForResults = sys.argv[2] #nuoroda iki norimo aplanko bei failo pavadinimas, kuriame bus išsaugotas rezultatas
	filename = sys.argv[3] #failo pavadinimas

	if os.path.exists(pathForAnalysis) and os.path.exists(pathForResults):
		return(pathForAnalysis, pathForResults, filename)
	else:
		sys.exit("Klaida: nėra tokio katalogo, kurį norima ištirti ar įrašyti rezultatų failą.")

def createResultsFile(pathForResults, filename): #sukuriamas arba atidaromas rezultatų failas
	try: 
		f = open(pathForResults + filename, "w")
	except IOerror:
		sys.exit("Klaida: neįmanoma sukurti rezultatų failo")
	return f	

def getFilesList(pathForAnalysis):
	listOfNames = [f for f in os.listdir(pathForAnalysis) if os.path.isfile(os.path.join(pathForAnalysis,f))]
	return listOfNames

def openFiles(listOfNames, frez):
	TotListOfSymbols = {}
	TotListOfWords = {}
	for x in xrange(0, len(listOfNames)):
		try:
			f = open(pathForAnalysis + listOfNames[x], "r")
			printStringToFile("\n\n Failas:" + pathForAnalysis + listOfNames[x], frez) 
		except IOerror:
			sys.exit("Klaida: Nepavyko nuskaityti failo esančio direktorijoje")

		fileText = f.read()
		TotListOfSymbols = analyseFileSymbols(fileText, frez, TotListOfSymbols)
		TotListOfWords = analyseFileWords(fileText, frez, TotListOfWords)
		f.close()

	printStringToFile("\n\n Visame kataloge simbolių dažnis: \n\n", frez) 
	printStringToFile(str(TotListOfSymbols), frez)

	printStringToFile("\n\n Visame kataloge žodžių dažnis: \n\n", frez) 
	printStringToFile(str(TotListOfWords), frez)

def analyseFileWords(fileText, frez, TotListOfWords):
	listOfWords = {}

	words = re.split('\W+', fileText)
	i = 0
	while i < len(words):
		if words[i] in listOfWords:
			number = listOfWords[words[i]] + 1
			listOfWords[words[i]] = number
		else:
			listOfWords[words[i]] = 1
		i = i + 1

	printStringToFile('\n\n Žodžiai faile: \n\n', frez)
	printStringToFile(str(listOfWords), frez)

	for word in listOfWords:
		TotListOfWords[word] = TotListOfWords.get(word, 0) + listOfWords[word]

	return TotListOfWords

def analyseFileSymbols(fileText, frez, TotListOfSymbols):
	listOfSymbols = {}

	i = 0
	while i < len(fileText):
		if fileText[i] in listOfSymbols:
			number = listOfSymbols[fileText[i]] + 1
			listOfSymbols[fileText[i]] = number
		else:
			listOfSymbols[fileText[i]] = 1
		i = i + 1

	printStringToFile('\n\n Simboliai faile: \n\n', frez)
	printStringToFile(str(listOfSymbols), frez)

	for symbol in listOfSymbols:
		TotListOfSymbols[symbol] = TotListOfSymbols.get(symbol, 0) + listOfSymbols[symbol]

	return TotListOfSymbols

def printStringToFile(stringline, f):
	f.write(stringline)

#metodų iškvietimai:
pathForAnalysis, pathForResults, filename = getArguments()
f = createResultsFile(pathForResults, filename)
listOfNames = getFilesList(pathForAnalysis)
openFiles(listOfNames, f)
