#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

def getArguments():
	if sys.argv[1] == "help":
		sys.exit("Naudojimas:  python statistics.py '/nuoroda/iki/aplanko/ištyrimui/' '/nuoroda/iki/rezultatų/failo/' 'failopavadinimas' ")
	if len(sys.argv) > 4: #argumentų skaičius negali būti didesnis nei 2
		sys.exit("Klaida: Per daug parametrų arba jie nurodyti nekorektiškai. 'Python statistics.py help me' - naudojimo instrukcija")
	if len(sys.argv) < 4: #argumentų skaičius negali būti mažesnis nei 2
		sys.exit("Klaida: Per mažai parametrų arba jie nurodyti nekorektiškai. 'Python statistics.py help me' - naudojimo instrukcija")
	
	pathForAnalysis = sys.argv[1] #nuoroda iki norimo aplanko analizei
	pathForResults = sys.argv[2] #nuoroda iki norimo aplanko bei failo pavadinimas, kuriame bus išsaugotas rezultatas
	filename = sys.argv[3] #failo pavadinimas

	if os.path.exists(pathForAnalysis) and os.path.exists(pathForResults):
		return(pathForAnalysis, pathForResults, filename)
	else:
		sys.exit("Klaida: nėra tokio katalogo, kurį norima ištirti/įrašyti rezultatų failą.")

def createResultsFile(pathForResults, filename): #sukuriamas arba atidaromas rezultatų failas
	if os.path.isfile(pathForResults + filename): #jei toks jau yra 
		try: 
			f = open(pathForResults + filename, "r+")
		except IOerror:
			sys.exit("Klaida: neįmanoma nuskaityti esamo rezultatų failo")
	else: #jei tokio dar nėra 
		try:
			f = open(pathForResults + filename, "w")
		except IOerror:
			sys.exit("Klaida: neįmanoma sukurti tokio failo")
	return f	

def getFilesList(pathForAnalysis):
	listOfNames = [f for f in os.listdir(pathForAnalysis) if os.path.isfile(os.path.join(pathForAnalysis,f))]
	return listOfNames

def analyseFiles(listOfNames, frez):
	listOfSymbols = {}
	TotListOfSymbols = {}
	for x in xrange(0, len(listOfNames)):
		try:
			f = open(pathForAnalysis + listOfNames[x], "r")
			printStringToFile("\n Failas:"+ pathForAnalysis + listOfNames[x] + "\n", frez) 
		except IOerror:
			sys.exit("Klaida:Nepavyko nuskaityti failo esančio direktorijoje")

		fileText = f.read()
		i = 0
		while i < len(fileText):
			if fileText[i] in listOfSymbols:
				number = listOfSymbols[fileText[i]] + 1
				listOfSymbols[fileText[i]] = number
			else:
				listOfSymbols[fileText[i]] = 1
			i=i+1

		printStringToFile(str(listOfSymbols), frez)

		for symbol in listOfSymbols:
			TotListOfSymbols[symbol] = TotListOfSymbols.get(symbol, 0) + listOfSymbols[symbol]
		listOfSymbols = {}
	printStringToFile("\n Visame kataloge: \n", frez) 
	printStringToFile(str(TotListOfSymbols), frez)

def printStringToFile(stringline, f):
	f.write(stringline)

#metodų iškvietimai:

pathForAnalysis, pathForResults, filename = getArguments()
f = createResultsFile(pathForResults, filename)
listOfNames = getFilesList(pathForAnalysis)
analyseFiles(listOfNames, f) 
