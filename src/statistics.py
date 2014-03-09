#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re

def get_arguments():
    if sys.argv[1] == "help":
        sys.exit("Naudojimas:  python statistics.py '/nuoroda/iki/aplanko/ištyrimui/' '/nuoroda/iki/rezultatų/failo/' 'failopavadinimas' ")
    if len(sys.argv) > 4: #argumentų skaičius negali būti didesnis nei 2
        sys.exit("Klaida: Per daug parametrų arba jie nurodyti nekorektiškai. 'Python statistics.py help' - naudojimo instrukcija")
    if len(sys.argv) < 4: #argumentų skaičius negali būti mažesnis nei 2
        sys.exit("Klaida: Per mažai parametrų arba jie nurodyti nekorektiškai. 'Python statistics.py help' - naudojimo instrukcija")
    
    path_for_analysis = sys.argv[1] #nuoroda iki norimo aplanko analizei
    path_for_results = sys.argv[2] #nuoroda iki norimo aplanko bei failo pavadinimas, kuriame bus išsaugotas rezultatas
    file_name = sys.argv[3] #failo pavadinimas

    if os.path.exists(path_for_analysis) and os.path.exists(path_for_results):
        return(path_for_analysis, path_for_results, file_name)
    else:
        sys.exit("Klaida: nėra tokio katalogo, kurį norima ištirti ar įrašyti rezultatų failą.")

def create_results_file(path_for_results, file_name): #sukuriamas arba atidaromas rezultatų failas
    try: 
        f = open(path_for_results + file_name, "w")
    except IOerror:
        sys.exit("Klaida: neįmanoma sukurti rezultatų failo.")
    return f    

def get_files_list(path_for_analysis):
    list_of_names = [f for f in os.listdir(path_for_analysis) if os.path.isfile(os.path.join(path_for_analysis,f))]
    return list_of_names

def open_files(list_of_names, frez): #nuskaitomi failai direktorijoje
    tot_list_of_symbols = {}
    tot_list_of_words = {}
    for x in xrange(0, len(list_of_names)):
        try:
            f = open(path_for_analysis + list_of_names[x], "r")
            print_string_to_file("\n\n Failas:" + path_for_analysis + list_of_names[x], frez) 
        except IOerror:
            sys.exit("Klaida: Nepavyko nuskaityti failo esančio direktorijoje")

        file_text = f.read()
        tot_list_of_symbols = analyse_file_symbols(file_text, frez, tot_list_of_symbols)
        tot_list_of_words = analyse_file_words(file_text, frez, tot_list_of_words)
        f.close()

    print_string_to_file("\n\n Visame kataloge simbolių dažnis: \n\n", frez) 
    print_string_to_file(str(tot_list_of_symbols), frez)

    print_string_to_file("\n\n Visame kataloge žodžių dažnis: \n\n", frez) 
    print_string_to_file(str(tot_list_of_words), frez)

def analyse_file_words(file_text, frez, tot_list_of_words):
    list_of_words = {}

    words = re.split('\W+', file_text)
    i = 0
    while i < len(words):
        if words[i] in list_of_words:
            number = list_of_words[words[i]] + 1
            list_of_words[words[i]] = number
        else:
            list_of_words[words[i]] = 1
        i = i + 1

    print_string_to_file('\n\n Žodžiai faile: \n\n', frez)
    print_string_to_file(str(list_of_words), frez)

    for word in list_of_words:
        tot_list_of_words[word] = tot_list_of_words.get(word, 0) + list_of_words[word]

    return tot_list_of_words

def analyse_file_symbols(file_text, frez, tot_list_of_symbols):
    list_of_symbols = {}

    i = 0
    while i < len(file_text):
        if file_text[i] in list_of_symbols:
            number = list_of_symbols[file_text[i]] + 1
            list_of_symbols[file_text[i]] = number
        else:
            list_of_symbols[file_text[i]] = 1
        i = i + 1

    print_string_to_file('\n\n Simboliai faile: \n\n', frez)
    print_string_to_file(str(list_of_symbols), frez)

    for symbol in list_of_symbols:
        tot_list_of_symbols[symbol] = tot_list_of_symbols.get(symbol, 0) + list_of_symbols[symbol]

    return tot_list_of_symbols

def print_string_to_file(string_line, f):
    f.write(string_line)

#metodų iškvietimai:
path_for_analysis, path_for_results, file_name = get_arguments()
f = create_results_file(path_for_results, file_name)
list_of_names = get_files_list(path_for_analysis)
open_files(list_of_names, f)