import codecs
import sys
from vkservices.vk import *

word_find = input('Enter the Word : ')
print (" 0 - synset, 1 - avayavi(holo), 2- avayava(mero), 3-para(hyper), 4 -apara(hypo), 5-janya, 6-janak, 7-pati,\
 8-patni, 9-sevaka, 10-swamy, 11-dharmi, 12-dharma, 13-guna, 14-guni, 15-sambada, 16-upajeevyah, 17-upajeevkah, 18-avatara, 19-ontology")
rel_No = input("Enter relation Number : ")

print('The given word is : ' + word_find)
print('The Rel No is : ' + rel_No)

rel_jsonstr = ""

if (rel_No == "0"):
	print("The synonyms")    # Col 8 Synset 1
	rel_vkArrayOutput = get_synonyms(word_find, "null", 0)
	print("")
	rel_jsonstr = printJsonOutput(rel_vkArrayOutput)
	print("Json String is")
	print(rel_jsonstr)
else:
	rel_vkArrayOutput = get_relations(rel_No, word_find)
	rel_jsonstr = printJsonOutput(rel_vkArrayOutput)
	print("Json String is")
	print(rel_jsonstr)
#print("This is a" + rel_name + "function")
