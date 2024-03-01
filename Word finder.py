#! Python3
import os, json, bs4
from collections import Counter

DIRECTORY = os.path.dirname(__file__)
INPUT_FILE = DIRECTORY+'/Letter_to_Herodotus_Bailey_Bilingual (master).html'
OUTPUT_FILE = DIRECTORY+'/Words.txt'
DICTIONARY_FILE = DIRECTORY+'/Greek_English_Dictionary.json'

with open(INPUT_FILE, 'r', encoding='utf8') as F:
    PARSED_HTML = bs4.BeautifulSoup(F, 'html.parser')
    
TABLE_CELLS = PARSED_HTML.find_all('td')
CLEANED_TEXT = ''
for cell in TABLE_CELLS:
    if TABLE_CELLS.index(cell) % 2 == 0:
        cleaned_text = str(cell).replace('<td>', '').replace('</td>', '').strip()
        CLEANED_TEXT += cleaned_text + ' '

with open(DICTIONARY_FILE, 'r', encoding='utf8') as F:
	DICTIONARY_DICT = json.load(F)

INPUT_WORDS = CLEANED_TEXT.split()
COUNTER = Counter(INPUT_WORDS)

# Uncomment to find most common words

# MOST_COMMON = COUNTER.most_common(3200)
# with open(OUTPUT_FILE, 'w', encoding='utf-8') as G:
# 	for item in MOST_COMMON:
# 		G.write(str(item)+'\n')
		
# Uncomment to find all words not in dictionary

SET_OF_WORDS = set(INPUT_WORDS)

with open(OUTPUT_FILE, 'w', encoding='utf-8') as G: 
	for word in sorted(SET_OF_WORDS):
		word = word.lstrip('(')
		word = word.lstrip('&lt;')
		word = word.rstrip(')')
		word = word.rstrip('.')
		word = word.rstrip(',')
		word = word.rstrip('·')
		word = word.rstrip('&gt;')
		word = word.rstrip(')')
		if word not in DICTIONARY_DICT.keys():
			G.write(word+'\n')
