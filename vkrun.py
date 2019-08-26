import codecs
import sys
from vkservices.vk import *

word_find = input('Enter the Word : ')
rel_No = input("Enter relation Number : ")

print('The given word is : ' + word_find)
print('The Rel word is : ' + rel_No)

rel_jsonstr = ""

if (rel_No == "1"):
	print("The synonyms")    # Col 8 Synset 1
	rel_vkArrayOutput = get_synonyms(word_find, "null")
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

'''
elif (rel_No == "2"):
	print("The Hypernyms")    # Col 10 parapara - Hypernym 2 ( & 5 same)
	rel_vkArrayOutput = get_hypernyms(word_find)
	rel_jsonstr = printJsonOutput(rel_vkArrayOutput)
	print("Json String is")
	print(rel_jsonstr)
	print("This is hypernym function")
elif (rel_No == "3"):
	print("The Holonyms")     # Col 9  Holonym - avyaya 3 (& 4 same)
	rel_vkArrayOutput = get_holonyms(word_find)
	rel_jsonstr = printJsonOutput(rel_vkArrayOutput)
	print("Json String is")
	print(rel_jsonstr)
	print("This is holonym function")
elif (rel_No == "4"): #  Meronym 4 (& 3 same)
	print("The Meronyms")
	rel_vkArrayOutput = get_meronyms(word_find)
	rel_jsonstr = printJsonOutput(rel_vkArrayOutput)
	print("Json String is")
	print(rel_jsonstr)
	print("This is meronym function")
elif (rel_No == "5"): # Hyponym 5 (& 2 same)
	print("The Hyponyms")
	rel_vkArrayOutput = get_hyponyms(word_find)
	rel_jsonstr = printJsonOutput(rel_vkArrayOutput)
	print("Json String is")
	print(rel_jsonstr)
	print("This is hyponym function")
else:
	print("Enter a valid Relation")
	#exit()'''

'''print("Json String is")
print(rel_jsonstr)
print("This is hyponym function")'''