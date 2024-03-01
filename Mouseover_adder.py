#! Python3

import os, json

DIRECTORY = os.path.dirname(__file__)
INPUT_FILE = DIRECTORY+'/Letter_to_Herodotus_Bailey_Bilingual (master).html'
OUTPUT_FILE = DIRECTORY+'/Output.html'
DICT_FILE = DIRECTORY+'/Greek_English_Dictionary.json'

with open(DICT_FILE, 'r', encoding='utf8') as F:
	DICT_DICT = json.load(F)
with open(INPUT_FILE, 'r', encoding='utf8') as F:
	INPUT_TEXT = F.read()

INPUT_WORD_LIST = INPUT_TEXT.split(' ')
OUTPUT_WORD_LIST = list()

for word in INPUT_WORD_LIST:
	cleaned_word = word.lstrip('(').lstrip('&lt;').rstrip('\n').rstrip(')').rstrip('.').rstrip(',').rstrip('·').rstrip('&gt;')
	cleaned_word = cleaned_word.lstrip('(').lstrip('&lt;').rstrip(')').rstrip('.').rstrip(',').rstrip('·').rstrip('&gt;')
	if cleaned_word in DICT_DICT.keys():
		definition = DICT_DICT[cleaned_word]
		replacement_text = '<span title="'+definition+'">'+word.replace('\n', '')+'</span>'
		OUTPUT_WORD_LIST.append(replacement_text)
	else:
		OUTPUT_WORD_LIST.append(word)
		
OUTPUT_TEXT = ''
for word in OUTPUT_WORD_LIST:
	OUTPUT_TEXT += word+' '
	
		

#add method to deal with capitalized words; python lower() might be able to do it

# for word, definition in DICT_DICT.items():
# 	replacement_text = '<span title="'+definition+'">'+word+'</span>'
# 	INPUT_TEXT = INPUT_TEXT.replace(' '+word+' ', ' '+replacement_text+' ')
# 	INPUT_TEXT = INPUT_TEXT.replace(' '+word+',', ' '+replacement_text+',')
# 	INPUT_TEXT = INPUT_TEXT.replace(' '+word+'.', ' '+replacement_text+'.')
	

with open(OUTPUT_FILE, 'w', encoding='utf8') as G:
	G.write(OUTPUT_TEXT)