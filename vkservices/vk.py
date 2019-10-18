# Program extracting first colum

import xlrd
import os

cols = 500
rows = 30
numSets = 0

maxRows = 2462
jathi_maxRows = 78
upadhi_maxRows = 25
m = 0
n = 0
sizeArray = [0, 0, 0, 0, 0,
			 0, 0, 0, 0, 0,
			 0, 0, 0, 0, 0,
			 0, 0, 0, 0, 0,
			 0, 0, 0, 0, 0,
			 0, 0, 0, 0, 0]


class vkProp:
	def __init__(self, isheadword, padam, pratam, nigama, linga, adhyaya, kanda, eng_meaning, sans_meaning,
				 meaning_source, synset, avyaya,
				 parapara, janyajanaka, patipatni, swaswamy, dharma, guna, anya, upajivika, avatara, jathi, upadhi,
				 wx_padam, wx_artha, onto_words):
		# swaswamy, vaishistya,anya,ajiviak,avatara, patipatni, upadhi):
		self.isheadword = isheadword
		self.padam = padam
		self.pratam = pratam
		self.nigama = nigama
		self.linga = linga
		self.adhyaya = adhyaya
		self.kanda = kanda
		self.eng_meaning = eng_meaning
		self.sans_meaning = sans_meaning
		self.meaning_source = meaning_source
		self.synset = synset
		self.avyaya = avyaya
		self.parapara = parapara
		self.janyajanaka = janyajanaka
		self.patipatni = patipatni
		self.swaswamy = swaswamy
		self.dharma = dharma
		self.guna = guna
		self.anya = anya
		self.upajivika = upajivika
		self.avatara = avatara
		self.jathi = jathi
		self.upadhi = upadhi
		self.wx_padam = wx_padam
		self.wx_artha = wx_artha
		self.onto_words = onto_words


def printJsonOutput(classArray):
	maxRowid = 0
	# Calculate how many rows out of max 5 has data
	for i in range(0, len(sizeArray)):
		if sizeArray[i] > 0:
			maxRowid += 1
	print("Max Row Id : ", maxRowid)
	rowid = 0
	jsonStr = '['
	for vkRow in classArray:  # print all the synonyms, corresponding items
		if rowid < maxRowid:
			jsonStr += '['
			for j in range(0, sizeArray[rowid]):
				jsonStr += '{' + os.linesep
				jsonStr += '"isheadword": "' + vkRow[j].isheadword + '",' + os.linesep
				jsonStr += '"padam": "' + vkRow[j].padam + '",' + os.linesep

				jsonStr += '"nigama": "' + vkRow[j].nigama + '",' + os.linesep
				jsonStr += '"linga": "' + vkRow[j].linga + '",' + os.linesep
				jsonStr += '"adhyaya": "' + vkRow[j].adhyaya + '",' + os.linesep
				jsonStr += '"kanda": "' + vkRow[j].kanda + '",' + os.linesep

				# Making changes here......
				jsonStr += '"eng_meaning": "' + vkRow[j].eng_meaning + '",' + os.linesep
				jsonStr += '"sans_meaning": "' + vkRow[j].sans_meaning + '",' + os.linesep
				# jsonStr += '"headword": "' + vkRow[j].isheadword + '",' + os.linesep
				# headword will come
				jsonStr += '"avyaya": "' + vkRow[j].avyaya + '",' + os.linesep
				jsonStr += '"parapara": "' + vkRow[j].parapara + '",' + os.linesep
				jsonStr += '"janyajanaka": "' + vkRow[j].janyajanaka + '",' + os.linesep
				jsonStr += '"patipatni": "' + vkRow[j].patipatni + '",' + os.linesep
				jsonStr += '"swaswamy": "' + vkRow[j].swaswamy + '",' + os.linesep
				jsonStr += '"dharma": "' + vkRow[j].dharma + '",' + os.linesep
				jsonStr += '"guna": "' + vkRow[j].guna + '",' + os.linesep
				jsonStr += '"anya": "' + vkRow[j].anya + '",' + os.linesep
				jsonStr += '"upajivika": "' + vkRow[j].upajivika + '",' + os.linesep
				jsonStr += '"avatara": "' + vkRow[j].avatara + '",' + os.linesep
				jsonStr += '"jathi": "' + vkRow[j].jathi + '",' + os.linesep
				jsonStr += '"upadhi": "' + vkRow[j].upadhi + '",' + os.linesep
				jsonStr += '"wx_padam": "' + vkRow[j].wx_padam + '",' + os.linesep
				jsonStr += '"wx_artha": "' + vkRow[j].wx_artha + '",' + os.linesep
				jsonStr += '"onto_word": "' + vkRow[j].onto_words + '",' + os.linesep

				jsonStr += '"headword": "' + vkRow[j].synset + '"' + os.linesep

				jsonStr += '}'
				if j < sizeArray[rowid] - 1:
					jsonStr += ','  # Add comma only until the last element is printed
		rowid = rowid + 1
		if rowid < maxRowid:
			jsonStr += '],'  # Add ] and comma to separate the array of elements
	jsonStr += ']]'
	return jsonStr


def get_synonyms(word_to_find, rel_word, relnostr):
	myVK = [[vkProp for i in range(cols)] for j in range(rows)]
	global m
	compare_word = ""

	for k in range(0, len(sizeArray)):
		sizeArray[k] = 0
	# myVK = [[vkProp for i in range(cols)] for j in range(rows)]
	m = 0
	for i in range(0, maxRows - 1):
		synset_word = None
		if (rel_word != "null"):
			synset_word = rel_word
			n = 0
		elif ((padam_word[i] == word_to_find) or (
				wx_padam[i] == word_to_find)):  # if word matches put other attributes it in class obj of vkprop
			synset_word = synset_headwd[i]
			n = 0
			'''synonyms.clear()'''
		relno = int(relnostr)

		if (synset_word != None):
			for j in range(0, maxRows - 1):
				if (relno == 0): #synset
					compare_word = synset_headwd[j]
				elif (relno == 1): #avayavi direct
					compare_word = synset_headwd[j]
				elif (relno == 2): #avayavah
					compare_word = avyaya_partof[j]
				elif (relno == 3): # parajati direct
					compare_word = synset_headwd[j]
				elif (relno == 4): #aparajati
					compare_word = para_kindof[j]
				elif (relno == 5): #janya
					compare_word = janyajanaka_cp[j]
				elif (relno == 6): # janaka direct
					compare_word = synset_headwd[j]
				elif (relno == 7): # pati direct
					compare_word = synset_headwd[j]
				elif (relno == 8): #patni
					compare_word = patipatni_hw[j]
				elif (relno == 9): #sevaka
					compare_word = swaswamy_mp[j]
				elif (relno == 10): #swamy direct
					compare_word =  synset_headwd[j]
				elif (relno == 11): #dharmi direct
					compare_word = synset_headwd[j]
				elif (relno == 12): #dharma
					compare_word = dharma_pos[j]
				elif (relno == 13): # guni direct
					compare_word = synset_headwd[j]
				elif (relno == 14): # guna
					compare_word = guna_nature[j]
				elif (relno == 15): # sambadda
					compare_word = synset_headwd[j]
				elif (relno == 16): #upajivyah direct
					compare_word = 	synset_headwd[j]
				elif (relno == 17): #upajiakah
					compare_word = upajivika_profession[j]
				elif (relno == 18): # avatarah
					compare_word = synset_headwd[j]
				elif (relno == 19): #ontology
					compare_word = jathi_class[j]

				if (compare_word == synset_word):  # if its a synset word, get the other details

					p2 = vkProp("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16",
								"17", \
								"19", "20", "21", "22", "23", "24", "25", "26", "27")
					p2.padam = padam_word[j]
					p2.nigama = nigama_reference[j]
					p2.adhyaya = adhyaya_chapter[j]
					p2.linga = linga_gender[j]
					p2.kanda = kanda_section[j]
					p2.eng_meaning = eng_meaning[j]
					p2.sans_meaning = sans_meaning[j]
					p2.synset = synset_word
					p2.avyaya = avyaya_partof[j]
					p2.parapara = para_kindof[j]
					p2.janyajanaka = janyajanaka_cp[j]
					p2.patipatni = patipatni_hw[j]
					p2.swaswamy = swaswamy_mp[j]
					p2.dharma = dharma_pos[j]
					p2.guna = guna_nature[j]
					p2.anya = anya_connection[j]
					p2.upajivika = upajivika_profession[j]
					p2.avatara = avatara_incarnation[j]
					p2.onto_word = ""

					p2.upadhi = upadhi_attr[j]
					p2.wx_padam = wx_padam[j]
					p2.wx_artha = wx_artha[j]

					myVK[m][n] = p2
					n = n + 1

			print (m, n)
			'''increment the index only if there are elements in the array'''
			if (n > 0):
				sizeArray[m] = n  # This is to keep track of which row in the array has valid data and which are blank
				m = m + 1
			if (rel_word != "null"):  # If rel_word is passed, break the loops after one run
				break

	return myVK


#####************************##################
def get_relations(relNo, word_to_find):
	print("Inside get relations" + relNo + ' ' + word_to_find)

	rel_myVK = [[vkProp for i in range(cols)] for j in range(rows)]
	tmpSizeArray = [0, 0, 0, 0, 0,
					0, 0, 0, 0, 0,
					0, 0, 0, 0, 0,
					0, 0, 0, 0, 0,
					0, 0, 0, 0, 0,
					0, 0, 0, 0, 0]
	idx = 0

	for i in range(0, maxRows - 1):
		if ((padam_word[i] == word_to_find) or (
				wx_padam[i] == word_to_find)):  # if word matches put other attributes it in class obj of vkprop
			if (relNo == '1'):  ### Holonym
				rel_name = "Holonym"
				rel_word = avyaya_partof[i]
			elif (relNo == '2'):  ##Meronym
				rel_name = "Meronym"
				rel_word = synset_headwd[i]
			elif (relNo == '3'):  # para hypernym direct
				rel_name = "Hypernym"
				rel_word = para_kindof[i]
			elif (relNo == '4'):  #### hyponym
				rel_name = "Hyponym"
				rel_word = synset_headwd[i]
			elif (relNo == '5'):  #### janya
				rel_name = "Janya"
				rel_word = synset_headwd[i]
			elif (relNo == '6'):  ## janaka direct
				rel_name = "Janaka"
				rel_word = janyajanaka_cp[i]
			elif (relNo == '7'):  ### Pati direct
				rel_name = "Pati "
				rel_word = patipatni_hw[i]
			elif (relNo == '8'):  # Patni
				rel_name = "Patni"
				rel_word = synset_headwd[i]
			elif (relNo == '9'):  ### sevaka
				rel_name = "Sevaka "
				rel_word = synset_headwd[i]
			elif (relNo == '10'):  # swamy direct
				rel_name = "Swamy"
				rel_word =   swaswamy_mp[i]
			elif (relNo == '11'):  ### Dharmi direct
				rel_name = "Dharmi "
				rel_word = dharma_pos[i]
			elif (relNo == '12'):  # Dharma
				rel_name = "dharma"
				rel_word = synset_headwd[i]
			elif (relNo == '13'):  ### guni direct
				rel_name = "guna "
				rel_word = guna_nature[i]
			elif (relNo == '14'):  # guna
				rel_name = "guni"
				rel_word = synset_headwd[i]
			elif (relNo == '15'):  ####\ sambandhitah
				rel_name = "Anya Sambandhitah"
				rel_word = anya_connection[i]
			elif (relNo == '16'):  #####upajeevyah direct
				rel_name = "Upajeevyah"
				rel_word = upajivika_profession[i]
			elif (relNo == '17'):  #####upajeevikah
				rel_name = "Upajeevakah"
				rel_word = synset_headwd[i]
			elif (relNo == '18'):  #### avatara
				rel_name = "Avatara"
				rel_word = avatara_incarnation[i]
			elif (relNo == '19'):
				rel_name = 'Ontology'
				rel_word = jathi_class[i]
				upadhi_word = upadhi_attr[i]

			print("Relation word :", rel_word)
			print("Relation used : ", rel_name)

			if (relNo != "19"):
				test = get_synonyms("null", rel_word, relNo)
			else:
				test = get_ontology(rel_word, upadhi_word)
			for i in range(0, cols):
				rel_myVK[idx][i] = test[0][i]
			tmpSizeArray[idx] = sizeArray[0]
			'''Increment the index only if there are elements'''
			if (sizeArray[0] > 0):
				idx = idx + 1
	for k in range(0, len(sizeArray)):
		sizeArray[k] = tmpSizeArray[k]
	return rel_myVK


def get_ontology(onto_word, upadi_word):  # Col 18 Jathi/ Upadhi
	jathi_words.append(onto_word)
	upadhi_words.append(upadi_word)
	print("This is Ontology function, onto word is", onto_word)
	# for i in range(0,sheet2_maxRows-1):
	# print (i,col1[i],col2[i])
	# print (jathi1[46],jathi2[46])
	print("============>")
	myVK = [[vkProp for i in range(cols)] for j in range(rows)]

	for k in range(0, len(sizeArray)):
		sizeArray[k] = 0

	n = 0
	onto_word_check = onto_word
	upadi_word_check = upadi_word

	p3 = vkProp("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16",
				"17", "19", "20", "21", "22", "23", "24", "25", "26", "27")
	p3.onto_words = onto_word
	myVK[0][n] = p3
	n = n+1

	for ixno in range(jathi_maxRows - 1, 0, -1):
		#print (ixno, jathi1[ixno], jathi2[ixno])
		if (jathi1[ixno] == onto_word_check):
			p3 = vkProp("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16",
						"17", "19", "20", "21", "22", "23", "24", "25", "26", "27")
			jathi_words.append(jathi2[ixno])
			p3.onto_words = jathi2[ixno]
			myVK[0][n] = p3
			n = n + 1
			onto_word_check = jathi2[ixno]

	for ixno in range(upadhi_maxRows - 1, 0, -1):
		if (upadhi1[ixno] == upadi_word_check):
			p3 = vkProp("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16",
						"17", "19", "20", "21", "22", "23", "24", "25", "26", "27")
			jathi_words.append(upadhi1[ixno] + '_up')
			p3.onto_words = upadhi1[ixno] + '_up'
			myVK[0][n] = p3
			n = n + 1
			upadi_word_check = upadhi2[ixno]
		'''increment the index only if there are elements in the array'''
	print ('n=' , n)
	if (n > 0):
		sizeArray[0] = n  # This is to keep track of which row in the array has valid data and which are blank

	for w in jathi_words:
		print ('===>', w)
	return myVK


#######*********Fuctions over***********

# loc = "/Users/Maha/Documents/Samskrit/PGDSCL/Vaijayanthi Kosha/vk.xlsx"
loc = "vk.xlsx"

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
numSets = m

padam_word = []  # col 0
pratam_singular = []  # col 1
nigama_reference = []  # col 2
linga_gender = []  # col 3
adhyaya_chapter = []  # col 4
kanda_section = []  # col 5
eng_meaning = []  # col 6
sans_meaning = []  # col 7
meaning_source = []  # col 8
synset_headwd = []  # col 9
avyaya_partof = []  # col 10  holonym
para_kindof = []  # col 11 hypernym
janyajanaka_cp = []  # col 12
patipatni_hw = []  # col 13
swaswamy_mp = []  # col 14
dharma_pos = []  # col 15
guna_nature = []  # col 16
anya_connection = []  # col 17
upajivika_profession = []  # col 18
avatara_incarnation = []  # col 19
jathi_class = []  # col 20  jathi
upadhi_attr = []  # col 21  upadhi
wx_padam = []  # col 22 wx_notation
wx_artha = []  # col 23 wx_artha
onto_words = []  # For ontology

synonyms = []
synset_word = ''
jathi_words = []
upadhi_words = []

padamArray = []

# ***** For Ontology**********
sheet2 = wb.sheet_by_index(1)
sheet2.cell_value(0, 0)

jathi1 = []
jathi2 = []
upadhi1 = []
upadhi2 = []

p1 = vkProp("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "19", "20",
			"21", "22", \
			"23", "24", "25", "26", "27")

# m = 0
##Getting all the values of xl in an array

'''upadhi1.append(sheet2.cell_value(1,2))
 jathi1.append(sheet2.cell_value(1,0)) 
print (upadhi1[0], jathi1[0]) '''
for k in range(1, jathi_maxRows + 1):
	jathi1.append(sheet2.cell_value(k, 0))
	jathi2.append(sheet2.cell_value(k, 1))
	if (k <= upadhi_maxRows):
		upadhi1.append(sheet2.cell_value(k, 2))
		upadhi2.append(sheet2.cell_value(k, 3))

for i in range(1, maxRows):
	padam_word.append(sheet.cell_value(i, 0))
	pratam_singular.append(sheet.cell_value(i, 1))
	nigama_reference.append(sheet.cell_value(i, 2))
	linga_gender.append(sheet.cell_value(i, 3))
	adhyaya_chapter.append(sheet.cell_value(i, 4))
	kanda_section.append(sheet.cell_value(i, 5))
	eng_meaning.append(sheet.cell_value(i, 6))
	sans_meaning.append(sheet.cell_value(i, 7))
	meaning_source.append(sheet.cell_value(i, 8))
	synset_headwd.append(sheet.cell_value(i, 9))
	avyaya_partof.append(sheet.cell_value(i, 10))
	para_kindof.append(sheet.cell_value(i, 11))
	janyajanaka_cp.append(sheet.cell_value(i, 12))
	patipatni_hw.append(sheet.cell_value(i, 13))
	swaswamy_mp.append(sheet.cell_value(i, 14))
	dharma_pos.append(sheet.cell_value(i, 15))
	guna_nature.append(sheet.cell_value(i, 16))
	anya_connection.append(sheet.cell_value(i, 17))
	upajivika_profession.append(sheet.cell_value(i, 18))
	avatara_incarnation.append(sheet.cell_value(i, 19))
	jathi_class.append(sheet.cell_value(i, 20))
	upadhi_attr.append(sheet.cell_value(i, 21))
	wx_padam.append(sheet.cell_value(i, 22))
	wx_artha.append(sheet.cell_value(i, 23))
	onto_words.append("")
