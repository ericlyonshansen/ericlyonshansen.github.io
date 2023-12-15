#! Python3

import os, json

DIRECTORY = os.path.dirname(__file__)
INPUT_FILE = DIRECTORY+'/Input.html'
OUTPUT_FILE = DIRECTORY+'/Output.html'
DICT_FILE = DIRECTORY+'/Greek_English_Dictionary.json'

with open(DICT_FILE, 'r', encoding='utf8') as F:
	DICT_DICT = json.load(F)
with open(INPUT_FILE, 'r', encoding='utf8') as F:
	INPUT_TEXT = F.read()

INPUT_WORD_LIST = INPUT_TEXT.split()
OUTPUT_WORD_LIST = list()

for word in INPUT_WORD_LIST:
	if word in DICT_DICT.keys():
		definition = DICT_DICT[word]
		replacement_text = '<span title="'+definition+'">'+word+'</span>'
		OUTPUT_WORD_LIST.append(replacement_text)
	elif word.rstrip('.') in DICT_DICT.keys():
		definition = DICT_DICT[word.rstrip('.')]
		replacement_text = '<span title="'+definition+'">'+word+'</span>'
		OUTPUT_WORD_LIST.append(replacement_text)
	elif word.rstrip(',') in DICT_DICT.keys():
		definition = DICT_DICT[word.rstrip(',')]
		replacement_text = '<span title="'+definition+'">'+word+'</span>'
		OUTPUT_WORD_LIST.append(replacement_text)
	else:
		OUTPUT_WORD_LIST.append(word)
		
OUTPUT_TEXT = ''
for word in OUTPUT_WORD_LIST:
	if '.<' in word:
		OUTPUT_TEXT += word+'\n<p>\n<p>'
	else:
		OUTPUT_TEXT += word+' '
	
		

#add method to deal with capitalized words; python lower() might be able to do it

# for word, definition in DICT_DICT.items():
# 	replacement_text = '<span title="'+definition+'">'+word+'</span>'
# 	INPUT_TEXT = INPUT_TEXT.replace(' '+word+' ', ' '+replacement_text+' ')
# 	INPUT_TEXT = INPUT_TEXT.replace(' '+word+',', ' '+replacement_text+',')
# 	INPUT_TEXT = INPUT_TEXT.replace(' '+word+'.', ' '+replacement_text+'.')
	

with open(OUTPUT_FILE, 'w', encoding='utf8') as G:
	G.write(OUTPUT_TEXT)