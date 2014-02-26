#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

def getArguments():
	if len(sys.argv) > 4: #argumentų skaičius negali būti didesnis nei 2
		sys.exit("Per daug parametrų arba jie nurodyti nekorektiškai. 'Python statistics.py help me' - naudojimo instrukcija")
	if len(sys.argv) < 4: #argumentų skaičius negali būti mažesnis nei 2
		sys.exit("Per mažai parametrų arba jie nurodyti nekorektiškai. 'Python statistics.py help me' - naudojimo instrukcija")
	if sys.argv[1] == "help" and sys.argv[2] == "me":
		print("Naudojimas:  python statistics.py '/nuoroda/iki/aplanko/ištyrimui' '/nuoroda/iki/rezultatų/failo' 'failopavadinimas' ")
		sys.exit()	

	pathForAnalysis = sys.argv[1] #nuoroda iki norimo aplanko analizei
	pathForResults = sys.argv[2] #nuoroda iki norimo aplanko bei failo pavadinimas, kuriame bus išsaugotas rezultatas
	filename = sys.argv[3] #failo pavadinimas

	if os.path.exists(pathForAnalysis) and os.path.exists(pathForResults):
		return(pathForAnalysis, pathForResults, filename)
	else:
		sys.exit()

pathForAnalysis, pathForResults, filename = getArguments()
		
def getFilesList(pathForAnalysis):
	list = os.listdir(pathForAnalysis)
	

getFilesList(pathForAnalysis)