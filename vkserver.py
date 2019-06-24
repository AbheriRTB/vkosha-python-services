# Program extracting first colum

import xlrd
import os
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

#------------------------ DON'T EDIT ABOVE THIS LINE --------------------
# Program extracting first colum

cols = 50
rows = 5
numSets = 0
m = 0
n = 0
sizeArray = [0,0,0,0,0]

class vkProp:
	def __init__(self, isheadword, padam, pratam, nigama, linga, adhyaya, kanda, synset, avyaya, parapara, janyajanaka,\
	             patipatni, swaswamy, vaishistyam, anya, ajivika, avatara, jathi, upadhi):
		# swaswamy, vaishistya,anya,ajiviak,avatara, patipatni, upadhi):
		self.isheadword = isheadword
		self.padam = padam
		self.pratam = pratam
		self.nigama = nigama
		self.linga = linga
		self.adhyaya = adhyaya
		self.kanda = kanda
		self.synset = synset
		self.avyaya = avyaya
		self.parapara = parapara
		self.janyajanaka = janyajanaka
		self.patipatni = patipatni
		self.swaswamy = swaswamy
		self.vaishistyam = vaishistyam
		self.anya = anya
		self.ajivika = ajivika
		self.avatara = avatara
		self.jathi = jathi
		self.upadhi = upadhi



def printClassVk(className):
	print('Headword : ' +className.synset)
	print('Synset ' + className.synset)
	print('Jathi ' + className.jathi)
	print('Adhyaya ' + className.adhyaya)
	print('Linga ' + className.linga)
	print('Ref ' + className.nigama)
	print('Kanda ' + className.kanda)

def printJsonOutput1(className):
	jsonStr = '{' + os.linesep
	jsonStr += '"synset": "' + className.synset + '",' + os.linesep
	jsonStr += '"jathi": "' + className.jathi + '",' + os.linesep
	jsonStr += '"adhyaya": "' + className.adhyaya + '",' + os.linesep
	jsonStr += '"linga": "' + className.linga + '",' + os.linesep
	jsonStr += '"nigama": "' + className.nigama + '",' + os.linesep
	jsonStr += '"kanda": "' + className.kanda  + '",' + os.linesep
	jsonStr += '}'
	return jsonStr

def printJsonOutput2(classArray):
	#jsonStr = '['
	jsonStr = ''
	for j in range(0, len(classArray)):  # print all the synonyms, corresponding items
		jsonStr += '[{' + os.linesep
		jsonStr += '"isheadword": "' + classArray[j].isheadword + '",' + os.linesep
		jsonStr += '"padam": "' + classArray[j].padam + '",' + os.linesep
		jsonStr += '"headword": "' + classArray[j].synset + '",' + os.linesep
		jsonStr += '"jathi": "' + classArray[j].jathi + '",' + os.linesep
		jsonStr += '"adhyaya": "' + classArray[j].adhyaya + '",' + os.linesep
		jsonStr += '"linga": "' + classArray[j].linga + '",' + os.linesep
		jsonStr += '"nigama": "' + classArray[j].nigama + '",' + os.linesep
		jsonStr += '"kanda": "' + classArray[j].kanda + '",' + os.linesep
		jsonStr += '},'
		if j < len(classArray):
			jsonStr += ','
	#jsonStr += ']'
	return jsonStr

def printJsonOutput(classArray):
	maxRowid = 0
	#Calculate how many rows out of max 5 has data
	for i in range(0, len(sizeArray)):
		if sizeArray[i] > 0:
			maxRowid += 1
	rowid = 0
	jsonStr = '['
	for vkRow in classArray:  # print all the synonyms, corresponding items
		if rowid < maxRowid:
			jsonStr += '['
		for j in range(0, sizeArray[rowid]):
			jsonStr += '{' + os.linesep
			jsonStr += '"isheadword": "' + vkRow[j].isheadword + '",' + os.linesep
			jsonStr += '"padam": "' + vkRow[j].padam + '",' + os.linesep
			jsonStr += '"headword": "' + vkRow[j].synset + '",' + os.linesep
			jsonStr += '"jathi": "' + vkRow[j].jathi + '",' + os.linesep
			jsonStr += '"adhyaya": "' + vkRow[j].adhyaya + '",' + os.linesep
			jsonStr += '"linga": "' + vkRow[j].linga + '",' + os.linesep
			jsonStr += '"nigama": "' + vkRow[j].nigama + '",' + os.linesep
			jsonStr += '"kanda": "' + vkRow[j].kanda + '"' + os.linesep
			jsonStr += '}'
			if j < sizeArray[rowid]-1:
				jsonStr += ','  #Add comma only until the last element is printed
		rowid = rowid + 1
		if rowid < maxRowid:
			jsonStr += '],'    #Add ] and comma to separate the array of elements
	jsonStr += ']]'
	return jsonStr

def get_synonyms(word_find):
	#loc = "/home/abheri/vkserver/vk.xlsx"
	loc = "/Users/Maha/Documents/Samskrit/PGDSCL/Vaijayanthi Kosha/vk.xlsx"

	wb = xlrd.open_workbook(loc)
	sheet = wb.sheet_by_index(0)
	sheet.cell_value(0, 0)

	sheet = wb.sheet_by_index(0)
	sheet.cell_value(0, 0)

	myVK = [[vkProp for i in range(cols)] for j in range(rows)]




	padam_word =[]           #col 0
	pratam_singular = []     #col 1
	nigama_reference = []     #col 2
	linga_gender = []        #col 3
	adhyaya_chapter = []     #col 4
	kanda_section = []       #col 5, no 6 n 7
	synset_headwd = []       #col 8
	avyaya_partof = []       #col 9  holonym
	para_kindof = []         #col 10 hypernym
	janyajanaka_cp = []      #col 11
	patipatni_hw = []        #col 12
	swaswamy_mp = []         #col 13
	vaishistyam_pec = []     #col 14
	anya_connection = []     #col 15
	ajivika_profession = []  #col 16
	avatara_incarnation = [] #col 17
	jathi_class = []         #col 18  jathi
	upadhi_attr = []         #col 19  upadhi

	synonyms = []
	synset_word = ''
	jathi_words = []

	padamArray = []

	p1 = vkProp("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")

	m = 0
	for i in range(5):
		sizeArray[i] = 0

	##Getting all the values of xl in an array
	for i in range(1,200):
		padam_word.append(sheet.cell_value(i,0))
		nigama_reference.append(sheet.cell_value(i,2))
		kanda_section.append(sheet.cell_value(i,5))
		linga_gender.append(sheet.cell_value(i,3))
		#avyaya_partof = sheet.cell_value(i,0))
		adhyaya_chapter.append(sheet.cell_value(i,4))
		jathi_class.append(sheet.cell_value(9,18))
		synset_headwd.append(sheet.cell_value(i,8))

	for i in range(0,199):
		#print(padam_word[i])
		if (padam_word[i] == word_find ): # if word matches put headword it in class obj of vkprop
			p1.padam = padam_word[i]
			p1.nigama = nigama_reference[i]
			p1.linga = linga_gender[i]
			p1.adhyaya = adhyaya_chapter[i]
			p1.synset = synset_headwd[i]
			p1.jathi = jathi_class[i]
			p1.kanda = kanda_section[i]
			p1.isheadword = "true"

			print('Word :' +padam_word[i])
			print('Headword for word :' +synset_headwd[i])
			print('Refence No of synset : ' +nigama_reference[i])
			print('Gender of synset: ' +linga_gender[i])
			print('Adhyaya of synset: ' +adhyaya_chapter[i])
			print('Jathi for synset :' + jathi_class[i])
			print('Kanda for synset :' + kanda_section[i])

			synset_word = synset_headwd[i]
			n = 0

			#myVK.append(p1)
			synonyms.clear()

			for j in range(0,199):
				#print('Test '+synset_headwd[i])
				if(synset_headwd[j] == synset_word):      # if its a synset word, get the other details

					synonyms.append(padam_word[j])
					jathi_words.append(jathi_class[j])
					linga_gender.append(linga_gender[j])
					nigama_reference.append(nigama_reference[j])

					p2 = vkProp("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
					p2.jathi = jathi_class[j]
					p2.nigama = nigama_reference[j]
					p2.linga = linga_gender[j]
					p2.padam = padam_word[j]
					p2.synset = synset_word
					p2.isheadword = "false"

					#myVK[m][n].append(p1)
					myVK[m][n] = p2
					n=n+1

			print (m,n)
			sizeArray[m]=n #This is to keep track of which row in the array has valid data and which are blank
			m = m + 1
			for j in range (0, len(synonyms)): #print all the synonyms, corresponding items
				'''print(synonyms[j], end=',')
				print(jathi_words[j],end=',')
				print(nigama_reference[j],end=',')
				print(linga_gender[j])

				print("ishead:" + myVK[j+1].isheadword)
				print("synonym:" + myVK[j + 1].padam)
				print("linga:" + myVK[j + 1].linga)
				print("nigama:" + myVK[j + 1].nigama)
				print("kanda:" + myVK[j + 1].kanda)
				print("adhyaya:" + myVK[j + 1].adhyaya)'''

			print()

			tmpstr = ","

			#p1.synset = tmpstr.join(synonyms)
			print('Head word is '+synset_word)
			print(p1.synset)
			print('*********************')

			print('------------')

	return myVK

#--------------- DON'T EDIT BELOW THIS LINE --------------------

@app.route('/vkosha/findwordold/<wordtofind>',methods=['GET'])
def findwordold(wordtofind):
	retstring = ", "
	print('The given word is : ' + wordtofind)
	vkObj = get_synonyms(wordtofind)
	retstring = vkObj.synset
	return retstring

@app.route('/vkosha/findwordold2/<wordtofind>',methods=['GET'])
def findwordold2(wordtofind):
	retstring = ", "
	print('The given word is : ' + wordtofind)
	vkObj = get_synonyms(wordtofind)
	retstring = printJsonOutput(vkObj)
	return retstring

@app.route('/vkosha/findword/<wordtofind>',methods=['GET'])
def findword(wordtofind):
	retstring = ", "
	print('The given word is : ' + wordtofind)
	vkArrayOutput = get_synonyms(wordtofind)
	retstring = printJsonOutput(vkArrayOutput)
	return retstring

@app.route('/vkosha/helloworld',methods=['GET'])
def vkHello():
	return "Hello World!"

if __name__ == '__main__':
	app.run()