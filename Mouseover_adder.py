#! Python3

import os, json

DIRECTORY = os.path.dirname(__file__)
INPUT_FILE = DIRECTORY+'/Letter_to_Herodotus_GR_EN.html'
OUTPUT_FILE = DIRECTORY+'/Output.html'
DICT_FILE = DIRECTORY+'/Greek_English_Dictionary.json'

with open(DICT_FILE, 'r', encoding='utf8') as F:
	DICT_DICT = json.load(F)
with open(INPUT_FILE, 'r', encoding='utf8') as F:
	INPUT_TEXT = F.read()

#add method to deal with capitalized words; python lower() might be able to do it

for word, definition in DICT_DICT.items():
	replacement_text = '<span title="'+definition+'">'+word+'</span>'
	INPUT_TEXT = INPUT_TEXT.replace(' '+word+' ', ' '+replacement_text+' ')

with open(OUTPUT_FILE, 'w', encoding='utf8') as G:
	G.write(INPUT_TEXT)