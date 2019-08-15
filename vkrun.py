import codecs
import sys
from vkservices.vk import *

word_find = input('Enter the Word : ')
rel_word = raw_input("Enter relation word : ")

'''
word_find = input('Enter the Word : ')
rel_word = input("Enter relation word : ")'''
print('The given word is : ' + word_find)
print('The Rel word is : ' + rel_word)

rel_jsonstr = ""

if (rel_word == "1"):
	print("The synonyms")    # Col 8 Synset 1
	rel_vkArrayOutput = get_synonyms(word_find, "null")
	print("")
	rel_jsonstr = printJsonOutput(rel_vkArrayOutput)
	print("Json String is")
	print(rel_jsonstr)
elif (rel_word == "2"):
	print("The Hypernyms")    # Col 10 parapara - Hypernym 2
	rel_vkArrayOutput = get_hypernyms(word_find)
	rel_jsonstr = printJsonOutput(rel_vkArrayOutput)
	print("Json String is")
	print(rel_jsonstr)
	print("This is hypernym function")
elif (rel_word == "3"):
	print("The Holonyms")     # Col 9  Holonym - avyaya 3
	rel_vkArrayOutput = get_holonyms(word_find)
	rel_jsonstr = printJsonOutput(rel_vkArrayOutput)
	print("Json String is")
	print(rel_jsonstr)
	print("This is holonym function")
elif (rel_word == "4"): #  Meronym 4
	print("The Meronyms")
	rel_vkArrayOutput = get_meronyms(word_find)
	rel_jsonstr = printJsonOutput(rel_vkArrayOutput)
	print("Json String is")
	print(rel_jsonstr)
	print("This is meronym function")
elif (rel_word == "5"): # Hyponym 5
	print("The Hyponyms")
	rel_vkArrayOutput = get_hyponyms(word_find)
	rel_jsonstr = printJsonOutput(rel_vkArrayOutput)
	print("Json String is")
	print(rel_jsonstr)
	print("This is hyponym function")
else:
	print("Enter a valid Relation")
	#exit()

'''print("Json String is")
print(rel_jsonstr)
print("This is hyponym function")'''