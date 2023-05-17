#! Python3
import os, json
from collections import Counter

DIRECTORY = os.path.dirname(__file__)
INPUT_FILE = DIRECTORY+'/Letter to Herodotus Usener.txt'
OUTPUT_FILE = INPUT_FILE.replace('.txt', ' - Words.txt')
DICTIONARY_FILE = DIRECTORY+'/Greek_English_Dictionary.json'

with open(INPUT_FILE, 'r', encoding='utf-8') as F:
	INPUT_TEXT = F.read()
INPUT_TEXT = INPUT_TEXT.replace('.', '').replace(',', '').replace("'", "").replace('(', '').replace(')', '').replace('<', '').replace('>', '').replace('[', '').replace(']', '')

with open(DICTIONARY_FILE, 'r', encoding='utf8') as F:
	DICTIONARY_DICT = json.load(F)

INPUT_WORDS = INPUT_TEXT.split()
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
		if word not in DICTIONARY_DICT.keys():
			G.write(word+'\n')
