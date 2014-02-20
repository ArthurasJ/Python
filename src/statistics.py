#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

def getArguments():
	if len(sys.argv) > 3: #argumentų skaičius negali būti didesnis nei 2
		sys.exit("Per daug parametrų arba jie nurodyti nekorektiškai.")
	if len(sys.argv) < 3: #argumentų skaičius negali būti mažesnis nei 2
		sys.exit("Per mažai parametrų arba jie nurodyti nekorektiškai.")

	pathForAnalysis = sys.argv[1] #nuoroda iki norimo aplanko analizei
	pathForResults = sys.argv[2] #nuoroda iki norimo aplanko bei failo pavadinimas, kuriame bus išsaugotas rezultatas
	
getArguments()
		
