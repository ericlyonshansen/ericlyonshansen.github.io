#! Python3

import os, json

DIRECTORY = os.path.dirname(__file__)
INPUT_FILE = DIRECTORY+'/Part A - Section II (master).html'
OUTPUT_FILE = DIRECTORY+'/output.html'
CONCORDANCE_FILE = DIRECTORY+'/Part A - Section II (concordance).txt'
CONCORDANCE_DICT = dict()

with open(INPUT_FILE, 'r', encoding='utf8') as F:
	INPUT_TEXT = F.read()

with open(CONCORDANCE_FILE, 'r', encoding='utf8') as F:
	CONCORDANCE_TEXT = F.read()

SECTION_SPLIT = CONCORDANCE_TEXT.split('\n\n')
for section in SECTION_SPLIT:
	line_split = section.split('\n')
	CONCORDANCE_DICT[line_split[0]] = line_split[1]
	
#print(CONCORDANCE_DICT)

for k, v in CONCORDANCE_DICT.items():
	if k in INPUT_TEXT:
		INPUT_TEXT = INPUT_TEXT.replace(k, '<span class="highlight-span"><span title="'+v+'">'+k.replace('\n', '')+'</span></span>')
		

with open(OUTPUT_FILE, 'w', encoding='utf8') as G:
	G.write(INPUT_TEXT)
	


#add method to deal with capitalized words; python lower() might be able to do it

# for word, definition in DICT_DICT.items():
# 	replacement_text = '<span title="'+definition+'">'+word+'</span>'
# 	INPUT_TEXT = INPUT_TEXT.replace(' '+word+' ', ' '+replacement_text+' ')
# 	INPUT_TEXT = INPUT_TEXT.replace(' '+word+',', ' '+replacement_text+',')
# 	INPUT_TEXT = INPUT_TEXT.replace(' '+word+'.', ' '+replacement_text+'.')
	