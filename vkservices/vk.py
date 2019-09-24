# Program extracting first colum

import xlrd
import os

cols = 500
rows = 5
numSets = 0

maxRows = 2000
m = 0
n = 0
sizeArray = [0,0,0,0,0]

class vkProp:
	def __init__(self, isheadword, padam, pratam, nigama, linga, adhyaya, kanda, eng_meaning, sans_meaning, synset, avyaya, \
	             parapara, janyajanaka, patipatni, swaswamy, dharma, guna, anya, upajivika, avatara, jathi, upadhi,wx_padam,wx_artha):
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


def printJsonOutput(classArray):
	maxRowid = 0
	#Calculate how many rows out of max 5 has data
	for i in range(0, len(sizeArray)):
		if sizeArray[i] > 0:
			maxRowid += 1
	print("Max Row Id : ",maxRowid)
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

#Making changes here......
				jsonStr += '"eng_meaning": "' + vkRow[j].eng_meaning + '",' + os.linesep
				jsonStr += '"sans_meaning": "' + vkRow[j].sans_meaning + '",' + os.linesep
				#jsonStr += '"headword": "' + vkRow[j].isheadword + '",' + os.linesep
				#headword will come
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

				jsonStr += '"headword": "' + vkRow[j].synset + '"' + os.linesep

				jsonStr += '}'
				if j < sizeArray[rowid]-1:
					jsonStr += ','  #Add comma only until the last element is printed
		rowid = rowid + 1
		if rowid < maxRowid:
			jsonStr += '],'    #Add ] and comma to separate the array of elements
	jsonStr += ']]'
	return jsonStr




def get_synonyms(word_to_find, rel_word):

	myVK = [[vkProp for i in range(cols)] for j in range(rows)]
	global m

	for k in range(0, len(sizeArray)):
		sizeArray[k] = 0
	#myVK = [[vkProp for i in range(cols)] for j in range(rows)]
	m=0
	for i in range(0,maxRows-1):
		synset_word = None
		if (rel_word != "null"):
			synset_word = rel_word
			n = 0
		elif ((padam_word[i] == word_to_find) or (wx_padam[i] == word_to_find)): # if word matches put other attributes it in class obj of vkprop
			synset_word = synset_headwd[i]
			n = 0
			'''synonyms.clear()'''
		if(synset_word != None):
			for j in range(0,maxRows-1):
				if(synset_headwd[j] == synset_word):      # if its a synset word, get the other details

					p2 = vkProp("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17",\
					            "19", "20", "21", "22","23","24","25")
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
					p2.upadhi = upadhi_attr[j]
					p2.wx_padam = wx_padam[j]
					p2.wx_artha = wx_artha[j]


					myVK[m][n] = p2
					n=n+1

			print (m,n)
			sizeArray[m]=n #This is to keep track of which row in the array has valid data and which are blank
			m = m + 1
			if (rel_word != "null"):     #If rel_word is passed, break the loops after one run
				break

	return myVK
#####************************##################
def get_relations(relNo,word_to_find):
	print("Inside get relations" + relNo + ' ' + word_to_find)

	rel_myVK = [[vkProp for i in range(cols)] for j in range(rows)]
	tmpSizeArray = [0,0,0,0,0]
	idx=0

	for i in range(0, maxRows - 1):
		if ((padam_word[i] == word_to_find) or (wx_padam[i] == word_to_find)):  # if word matches put other attributes it in class obj of vkprop
			if (relNo == '1'): ### Holonym
				rel_name = "Holonym"
				rel_word = avyaya_partof[i]
			elif (relNo == '2'):  ##Meronym
				rel_name = "Meronym"
				rel_word = avyaya_partof[i]
			elif (relNo == '3'): # para hypernym
				rel_name = "Hypernym"
				rel_word = para_kindof[i]
			elif (relNo == '4'): #### hyponym
				rel_name = "Hyponym"
				rel_word = para_kindof[i]
			elif (relNo == '5' or relNo == '6' ): #### janya janaka
				rel_name = "Janya Janaka"
				rel_word = janyajanaka_cp[i]
			elif (relNo == '7' or relNo == '8'): ### Pati patni
				rel_name = "Pati Patni"
				rel_word = patipatni_hw[i]
			elif (relNo == '9' or relNo == '10'): ### swamy
				rel_name = "Swamy "
				rel_word = swaswamy_mp[i]
			elif (relNo == '11'):   ####\ sambandhitah
				rel_name = "Anya Sambandhitah"
				rel_word = anya_connection[i]
			elif (relNo == '12'):    #####vrutti
				rel_name = "Vrutti"
				rel_word = upajivika_profession[i]
			elif (relNo == '13'): #### avatara
				rel_name = "Avatara"
				rel_word = avatara_incarnation[i]

			print("Relation word :", rel_word)
			print("Relation used : ", rel_name)

			test = get_synonyms("null", rel_word)
			for i in range(0, cols):
				rel_myVK[idx][i]=test[0][i]
			tmpSizeArray[idx] = sizeArray[0]
			idx = idx+1
	for k in range(0, len(sizeArray)):
		sizeArray[k] = tmpSizeArray[k]
	return rel_myVK





'''
def get_holonyms(holo_word):    #   Col 9 Avayavi - *** Not sure
	print("This is holonym function")
	holo_myVK = [[vkProp for i in range(cols)] for j in range(rows)]

	for i in range(0, maxRows - 1):
		if (padam_word[i] == holo_word):  # if word matches put other attributes it in class obj of vkprop
			holonym_word = avyaya_partof[i]
			print("Holonym word :", holonym_word)
			holo_myVK = get_synonyms("null", holonym_word)
	return holo_myVK


def get_meronyms(mero_word):  # Col 9 avayava ** same as above??
	print("This is Meronym function")
	mero_myVK = [[vkProp for i in range(cols)] for j in range(rows)]

	for i in range(0, maxRows - 1):
		if (padam_word[i] == mero_word):  # if word matches put other attributes it in class obj of vkprop
			meronym_word = avyaya_partof[i]
			print("Meronym word :", meronym_word)
			mero_myVK = get_synonyms("null", meronym_word)
	return mero_myVK


def get_hypernyms(hyper_word):  #   Col 10 Parajathi

	hyper_myVK = [[vkProp for i in range(cols)] for j in range(rows)]

	for i in range(0,maxRows-1):
		if (padam_word[i] == hyper_word):  # if word matches put other attributes it in class obj of vkprop
			hypernym_word = para_kindof[i]
			print("Hypernym word :", hypernym_word)
			hyper_myVK = get_synonyms("null",hypernym_word)
	return hyper_myVK


def get_hyponyms(hypo_word): #Col 10  Aparajathi
	print("This is hyponym function")


def get_janyajanaka(jj_word): # Col 11
	print("This is Janya Janaka function")


def get_patipatni(pp_word):   # Col 12
	print("This is pati patni sambhandha function")

def get_swaswamy(ss_word): # Col 13
	print("This is Swami Sevaka function")

def get_vaishishtyam(vai_word): # Col 14
	print("This is Vaishishtyam function")

def get_sambandha(samb_word): # Col 15
	print("This is Sambhandhita function")

def get_ajivika(ajivika_word): # Col 16 vritti
	print("This is Ajivika/ Vritti function")

def get_avatara(avatara_word): # Col 17
	print("This is Avatara function")

def get_ontology(onto_word): # Col 18 Jathi/ Upadhi
	print("This is Ontology function")

'''
#######*********Fuctions over***********

#loc = "/Users/Maha/Documents/Samskrit/PGDSCL/Vaijayanthi Kosha/vk.xlsx"
loc = "vk.xlsx"

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
numSets = m

padam_word =[]           #col 0
pratam_singular = []     #col 1
nigama_reference = []    #col 2
linga_gender = []        #col 3
adhyaya_chapter = []     #col 4
kanda_section = []       #col 5
eng_meaning = []         #col 6
sans_meaning = []        #col 7
synset_headwd = []       #col 8
avyaya_partof = []       #col 9  holonym
para_kindof = []         #col 10 hypernym
janyajanaka_cp = []      #col 11
patipatni_hw = []        #col 12
swaswamy_mp = []         #col 13
dharma_pos = []          #col 14
guna_nature = []         #col 15
anya_connection = []     #col 16
upajivika_profession = []  #col 17
avatara_incarnation = []   #col 18
jathi_class = []           #col 19  jathi
upadhi_attr = []           #col 20  upadhi
wx_padam = []              #col 21 wx_notation
wx_artha = []              #col 22 wx_artha

synonyms = []
synset_word = ''
jathi_words = []

padamArray = []

p1 = vkProp("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "19", "20", "21", "22","23","24","25")

#m = 0
##Getting all the values of xl in an array
for i in range(1, maxRows):
	padam_word.append(sheet.cell_value(i,0))
	pratam_singular.append(sheet.cell_value(i,1))
	nigama_reference.append(sheet.cell_value(i,2))
	linga_gender.append(sheet.cell_value(i,3))
	adhyaya_chapter.append(sheet.cell_value(i,4))
	kanda_section.append(sheet.cell_value(i,5))
	eng_meaning.append(sheet.cell_value(i,6))
	sans_meaning.append(sheet.cell_value(i,7))
	synset_headwd.append(sheet.cell_value(i,8))
	avyaya_partof.append(sheet.cell_value(i,9))
	para_kindof.append(sheet.cell_value(i,10))
	janyajanaka_cp.append(sheet.cell_value(i,11))
	patipatni_hw.append(sheet.cell_value(i,12))
	swaswamy_mp.append(sheet.cell_value(i,13))
	dharma_pos.append(sheet.cell_value(i,14))
	guna_nature.append(sheet.cell_value(i,15))
	anya_connection.append(sheet.cell_value(i,16))
	upajivika_profession.append(sheet.cell_value(i,17))
	avatara_incarnation.append(sheet.cell_value(i,18))
	jathi_class.append(sheet.cell_value(i,19))
	upadhi_attr.append(sheet.cell_value(i,20))
	wx_padam.append(sheet.cell_value(i,21))
	wx_artha.append(sheet.cell_value(i,22))